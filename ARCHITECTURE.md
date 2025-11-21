# System Architecture

## Component Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                         USER INTERFACE                          │
│                                                                 │
│  • Natural Language Query Input                                │
│  • Interactive Mode (REPL)                                     │
│  • Command Line Mode (Single Query)                           │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         v
┌─────────────────────────────────────────────────────────────────┐
│                         LINUXGPT                                │
│                      (agent.py)                                 │
│                                                                 │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │              1. QUERY PROCESSING                          │ │
│  │  • Parse natural language input                           │ │
│  │  • Extract keywords and intent                            │ │
│  │  • Search commands database                               │ │
│  └───────────────────────────────────────────────────────────┘ │
│                         │                                       │
│                         v                                       │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │              2. LLM REASONING                             │ │
│  │  ┌─────────────────────────────────────────────────────┐ │ │
│  │  │  LLMInterface                                       │ │ │
│  │  │  • OpenAI API Integration (gpt-4)                  │ │ │
│  │  │  • Mock Mode (pattern matching fallback)           │ │ │
│  │  │  • Context building from database                  │ │ │
│  │  │  • Command generation                              │ │ │
│  │  └─────────────────────────────────────────────────────┘ │ │
│  │                                                             │ │
│  │  Input: User query + database context                      │ │
│  │  Output: Linux command string                              │ │
│  └───────────────────────────────────────────────────────────┘ │
│                         │                                       │
│                         v                                       │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │              3. SAFETY CHECKS                             │ │
│  │  • Dangerous command pattern detection                    │ │
│  │  • Command validation                                     │ │
│  │  • Timeout enforcement                                    │ │
│  └───────────────────────────────────────────────────────────┘ │
│                         │                                       │
│                         v                                       │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │              4. COMMAND EXECUTION                         │ │
│  │  • subprocess.run() with shell=True                       │ │
│  │  • stdout/stderr capture                                  │ │
│  │  • Error handling                                         │ │
│  │  • 30-second timeout                                      │ │
│  └───────────────────────────────────────────────────────────┘ │
│                         │                                       │
│                         v                                       │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │              5. RESULT PROCESSING                         │ │
│  │  • Format output                                          │ │
│  │  • Store in history                                       │ │
│  │  • Return to user                                         │ │
│  └───────────────────────────────────────────────────────────┘ │
│                                                                 │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         v
┌─────────────────────────────────────────────────────────────────┐
│                    SUPPORTING COMPONENTS                        │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │  LINUX COMMANDS DATABASE                                 │ │
│  │  (linux_commands_db.json)                                │ │
│  │                                                           │ │
│  │  • 60+ Linux commands                                    │ │
│  │  • Descriptions and usage                                │ │
│  │  • Examples                                              │ │
│  │  • Tags for searching                                    │ │
│  │                                                           │ │
│  │  Structure:                                              │ │
│  │  {                                                       │ │
│  │    "command": {                                          │ │
│  │      "description": "...",                               │ │
│  │      "usage": "...",                                     │ │
│  │      "tags": [...],                                      │ │
│  │      "examples": [...]                                   │ │
│  │    }                                                     │ │
│  │  }                                                       │ │
│  └──────────────────────────────────────────────────────────┘ │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │  CONFIGURATION                                           │ │
│  │  (config.json)                                           │ │
│  │                                                           │ │
│  │  • LLM settings (model, temperature)                     │ │
│  │  • Security settings                                     │ │
│  │  • Timeout configuration                                 │ │
│  └──────────────────────────────────────────────────────────┘ │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │  COMMAND HISTORY                                         │ │
│  │  (in-memory)                                             │ │
│  │                                                           │ │
│  │  • Query → Command mapping                               │ │
│  │  • Success/failure status                                │ │
│  │  • Session tracking                                      │ │
│  └──────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
                         │
                         v
┌─────────────────────────────────────────────────────────────────┐
│                      LINUX SYSTEM                               │
│                                                                 │
│  • File system operations                                      │
│  • Process management                                          │
│  • Network operations                                          │
│  • System information                                          │
└─────────────────────────────────────────────────────────────────┘
```

## Data Flow

```
User Query
    ↓
[Query Processing]
    ↓
[Database Search] → Relevant Commands Context
    ↓
[LLM Interface] → Command Generation
    ↓
[Safety Checks] → Validation
    ↓
[Command Execution] → Linux System
    ↓
[Result Processing] → stdout/stderr
    ↓
[Response Formatting]
    ↓
User Output
```

## Key Classes

### LinuxGPT
- Main orchestrator
- Manages query → command → execution flow
- Maintains command history

### LinuxCommandDatabase
- Loads and searches command database
- Provides context for LLM
- Tag-based command discovery

### LLMInterface
- OpenAI API wrapper
- Mock mode for testing
- Context-aware prompt engineering

### CommandResult
- Data class for execution results
- Contains: success, output, error, command

## Operating Modes

### 1. Full LLM Mode (with API key)
```
Query → Database Context → LLM API → Command → Execute → Result
```

### 2. Mock Mode (without API key)
```
Query → Pattern Matching → Command → Execute → Result
```

### 3. Interactive Mode
```
Loop:
  User Input → Process → Display Result → Wait for Next Input
```

### 4. CLI Mode
```
Single Query → Process → Display Result → Exit
```

## Security Layers

1. **Input Validation**
   - Query sanitization
   - Length limits

2. **Command Generation**
   - LLM safety instructions
   - Context-aware generation

3. **Pre-Execution Checks**
   - Dangerous pattern detection
   - Blacklist verification

4. **Execution Constraints**
   - Timeout enforcement (30s)
   - User-level permissions only

5. **Post-Execution**
   - Error handling
   - Output sanitization

## Extension Points

- **New LLM Providers**: Add to LLMInterface
- **More Commands**: Update linux_commands_db.json
- **Custom Safety Rules**: Modify config.json
- **Output Formatters**: Extend result processing
- **History Persistence**: Add database integration
