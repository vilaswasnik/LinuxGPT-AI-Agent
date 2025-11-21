# LinuxGPT

A natural language interface for Linux commands powered by LLMs. This system converts natural language queries into appropriate Linux commands, executes them safely, and returns the results.

## System Architecture

```
┌─────────────┐
│   Query     │  User asks in natural language
│  (Natural   │  e.g., "help me show list of files in directory"
│  Language)  │
└──────┬──────┘
       │
       v
┌─────────────────────────────────────────────────┐
│                    Agent                        │
│                                                 │
│  ┌─────────────────────────────────────────┐  │
│  │  1. Query Processing                    │  │
│  │     - Parse natural language            │  │
│  │     - Search commands database          │  │
│  └─────────────────────────────────────────┘  │
│                                                 │
│  ┌─────────────────────────────────────────┐  │
│  │  2. LLM Reasoning                       │  │
│  │     - Convert query to command          │  │
│  │     - Use database context              │  │
│  │     - Apply safety checks               │  │
│  └─────────────────────────────────────────┘  │
│                                                 │
│  ┌─────────────────────────────────────────┐  │
│  │  3. Command Execution                   │  │
│  │     - Execute Linux command             │  │
│  │     - Capture output                    │  │
│  │     - Handle errors                     │  │
│  └─────────────────────────────────────────┘  │
│                                                 │
│  ┌─────────────────────────────────────────┐  │
│  │  Linux Commands Database                │  │
│  │  (60+ commands with descriptions)       │  │
│  └─────────────────────────────────────────┘  │
└─────────────────────────────────────────────────┘
       │
       v
┌──────────────┐
│   Response   │  Command output or error message
└──────────────┘
```

## Features

- 🗣️ **Natural Language Interface**: Ask questions in plain English
- 🤖 **LLM-Powered**: Uses OpenAI GPT-4 for intelligent command generation
- 📚 **Comprehensive Knowledge Base**: 60+ Linux commands with detailed documentation
- 🎓 **Educational Mode**: Learn with explanations, tips, and examples
- 🔗 **Command Combinations**: 30+ real-world command pipelines
- 🛡️ **Safety First**: Built-in checks prevent dangerous commands
- 📝 **Command History**: Track all executed commands
- 🎯 **Mock Mode**: Works without API key for testing
- ⚡ **Interactive & CLI Modes**: Use interactively or as single commands
- 💡 **Interactive Help**: Explain any command with detailed options and tips

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/sample.ai.git
   cd sample.ai
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up API key** (optional for full functionality):
   ```bash
   cp .env.example .env
   # Edit .env and add your OpenAI API key
   export OPENAI_API_KEY='your-api-key-here'
   ```

## Usage

### Interactive Mode

Run the agent in interactive mode for continuous queries:

```bash
python agent.py
```

Example session:
```
Query> help me show list of files in directory
Command: ls -la
------------------------------------------------------------
total 48
drwxr-xr-x  6 user user 4096 Nov 21 10:30 .
drwxr-xr-x  3 user user 4096 Nov 21 10:00 ..
-rw-r--r--  1 user user  123 Nov 21 10:30 agent.py
...

Query> what's my current directory?
Command: pwd
------------------------------------------------------------
/workspaces/sample.ai

Query> show me running processes
Command: ps aux
------------------------------------------------------------
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.1  18236  3456 ?        Ss   10:00   0:00 /sbin/init
...
```

### Command Line Mode

Execute a single query:

```bash
python agent.py "show me disk space usage"
```

Output:
```
Query: show me disk space usage
Command: df -h

Output:
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1        50G   20G   28G  42% /
...
```

### Special Commands

- `history` - View command history
- `quit` or `exit` - Exit interactive mode

## Example Queries

| Natural Language Query | Generated Command |
|------------------------|-------------------|
| "show list of files in directory" | `ls -la` |
| "what's my current directory?" | `pwd` |
| "show disk space usage" | `df -h` |
| "show running processes" | `ps aux` |
| "show memory usage" | `free -h` |
| "find all text files" | `find . -name '*.txt'` |
| "find large files" | `find . -type f -size +100M -exec ls -lh {} \;` |
| "list by size" | `ls -lhS` |
| "list by date" | `ls -lht` |
| "show network connections" | `netstat -tuln` |
| "show system information" | `uname -a` |

## 🎓 Educational Features

The system includes powerful learning features:

### Explain Commands
```bash
Query> explain grep
📚 GREP - Search text using patterns
Usage: grep [OPTIONS] PATTERN [FILE]...
Common Options:
  -r: Recursive search
  -i: Case-insensitive
  -n: Show line numbers
Examples with explanations...
💡 Tips and best practices...
```

### View Command Combinations
```bash
Query> combinations
🔗 30+ Common Command Combinations:
- Find and delete patterns
- Text processing pipelines
- System monitoring
- And more...
```

### Learn as You Go
Every command executed shows educational info automatically:
- What the command does
- Common options explained
- Pro tips and best practices

**See [EDUCATIONAL_FEATURES.md](EDUCATIONAL_FEATURES.md) for complete learning guide!**

## Configuration

Edit `config.json` to customize:

```json
{
  "llm": {
    "provider": "openai",
    "model": "gpt-4",
    "temperature": 0.3
  },
  "security": {
    "enable_dangerous_command_check": true,
    "command_timeout_seconds": 30
  }
}
```

## Linux Commands Database

The system includes a comprehensive database of 60+ Linux commands:

- **File Operations**: ls, cd, pwd, cat, find, grep
- **System Info**: ps, top, free, df, du, uname
- **Network**: netstat, ping, curl, wget, ifconfig
- **Package Management**: apt, yum
- **Service Control**: systemctl, service
- **And many more...**

## Safety Features

The agent includes built-in safety checks:

- ❌ Blocks dangerous patterns (e.g., `rm -rf /`, `mkfs`)
- ⏱️ 30-second timeout for command execution
- 🔒 Runs with user permissions (no automatic sudo)
- 📋 Command validation before execution

## Mock Mode

Without an API key, the agent runs in mock mode using pattern matching:

```bash
python agent.py
⚠️  No OPENAI_API_KEY found. Using mock LLM mode.
```

This is useful for:
- Testing the system without API costs
- Demonstrating basic functionality
- Development and debugging

## Project Structure

```
sample.ai/
├── agent.py                    # Main agent program
├── linux_commands_db.json      # Commands database
├── config.json                 # Configuration file
├── requirements.txt            # Python dependencies
├── .env.example               # Environment variables template
├── .gitignore                 # Git ignore rules
└── README.md                  # This file
```

## Requirements

- Python 3.7+
- OpenAI API key (optional, for full LLM functionality)
- Linux/Unix environment

## Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Add commands to the database in `linux_commands_db.json`
4. Submit a pull request

## License

MIT License - Feel free to use this project for learning and development.

## Troubleshooting

**Q: Commands not executing?**
- Check file permissions: `chmod +x agent.py`
- Verify Python version: `python --version` (need 3.7+)

**Q: "No OPENAI_API_KEY" warning?**
- This is normal - the system will use mock mode
- For full functionality, set the environment variable

**Q: Command blocked for safety?**
- The system blocks potentially dangerous commands
- Review the command and run manually if intended

## Future Enhancements

- 🔄 Support for command chaining and pipes
- 📊 Better output formatting and visualization
- 🌐 Support for multiple LLM providers (Claude, Llama)
- 🔍 Enhanced command search and suggestions
- 💾 Persistent command history
- 🎨 Syntax highlighting for output

## Contact

For questions or feedback, please open an issue on GitHub.

---

**Note**: Always review generated commands before execution, especially in production environments.