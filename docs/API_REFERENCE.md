# API Reference

Complete API reference for Sample.AI framework.

## Core Classes

### BaseAgent

Abstract base class for all agents.

```python
class BaseAgent(ABC):
    def __init__(self, config: AgentConfig)
    def initialize(self) -> None
    def process(self, input_data: Any, **kwargs) -> Any  # Abstract
    def add_to_history(self, entry: Dict[str, Any]) -> None
    def get_history(self) -> List[Dict[str, Any]]
    def clear_history(self) -> None
    def get_config(self) -> AgentConfig
    def update_config(self, **kwargs) -> None
```

**Parameters:**
- `config`: AgentConfig object with agent settings

**Methods:**
- `initialize()`: Initialize the agent before first use
- `process()`: Main processing method (must be implemented by subclasses)
- `add_to_history()`: Add entry to agent's history
- `get_history()`: Retrieve all history entries
- `clear_history()`: Clear the history
- `get_config()`: Get current configuration
- `update_config()`: Update configuration parameters

### AgentConfig

Configuration model for agents.

```python
class AgentConfig(BaseModel):
    name: str
    description: str = ""
    model_name: Optional[str] = None
    temperature: float = 0.7
    max_tokens: int = 2048
    system_prompt: Optional[str] = None
    metadata: Dict[str, Any] = {}
```

**Fields:**
- `name`: Agent name (required)
- `description`: Agent description
- `model_name`: Name of AI model to use
- `temperature`: Generation temperature (0.0-2.0)
- `max_tokens`: Maximum tokens to generate
- `system_prompt`: System prompt for the agent
- `metadata`: Additional metadata dictionary

### AIModel

Abstract base class for AI model integration.

```python
class AIModel(ABC):
    def __init__(self, config: ModelConfig)
    def generate(self, prompt: str, **kwargs) -> str  # Abstract
    def chat(self, messages: List[Dict[str, str]], **kwargs) -> str  # Abstract
    def get_config(self) -> ModelConfig
```

**Methods:**
- `generate()`: Generate text from prompt
- `chat()`: Generate response from conversation
- `get_config()`: Get model configuration

### ModelConfig

Configuration model for AI models.

```python
class ModelConfig(BaseModel):
    model_name: str
    provider: str = "custom"
    api_key: Optional[str] = None
    endpoint: Optional[str] = None
    parameters: Dict[str, Any] = {}
```

**Fields:**
- `model_name`: Model identifier (required)
- `provider`: Model provider (openai, anthropic, custom, etc.)
- `api_key`: API key for the provider
- `endpoint`: Custom API endpoint URL
- `parameters`: Additional model-specific parameters

## Agent Implementations

### ChatAgent

Conversational agent with context management.

```python
class ChatAgent(BaseAgent):
    def __init__(self, config: AgentConfig, model: Optional[AIModel] = None)
    def process(self, input_data: str, **kwargs) -> str
    def get_conversation(self) -> List[Dict[str, str]]
    def clear_conversation(self) -> None
    def set_system_prompt(self, prompt: str) -> None
```

**Constructor:**
- `config`: Agent configuration
- `model`: AI model instance (defaults to MockModel)

**Methods:**
- `process()`: Process user message and return response
- `get_conversation()`: Get full conversation history
- `clear_conversation()`: Clear conversation (keeps system prompt)
- `set_system_prompt()`: Update system prompt

**Example:**
```python
config = AgentConfig(name="Assistant")
agent = ChatAgent(config)
response = agent.process("Hello!")
```

### TaskAgent

Agent for executing specific tasks.

```python
class TaskAgent(BaseAgent):
    def __init__(self, config: AgentConfig, model: Optional[AIModel] = None)
    def process(self, input_data: Any, task_type: str = "general", **kwargs) -> Dict[str, Any]
    def execute_summarization(self, text: str, **kwargs) -> str
    def execute_extraction(self, text: str, **kwargs) -> str
    def execute_classification(self, text: str, **kwargs) -> str
```

**Constructor:**
- `config`: Agent configuration
- `model`: AI model instance (defaults to MockModel)

**Methods:**
- `process()`: Execute a task with specified type
- `execute_summarization()`: Summarize text
- `execute_extraction()`: Extract information from text
- `execute_classification()`: Classify text

**Task Types:**
- `summarize`: Text summarization
- `extract`: Data extraction
- `classify`: Classification
- `generate`: Content generation
- `translate`: Translation
- `general`: General processing

**Example:**
```python
config = AgentConfig(name="TaskBot")
agent = TaskAgent(config)
summary = agent.execute_summarization("Long text...")
```

### DesignAgent

Agent for AI application design.

```python
class DesignAgent(BaseAgent):
    def __init__(self, config: AgentConfig, model: Optional[AIModel] = None)
    def process(self, input_data: Dict[str, Any], design_type: str = "architecture", **kwargs) -> Dict[str, Any]
    def design_architecture(self, requirements: Dict[str, Any], **kwargs) -> Dict[str, Any]
    def design_workflow(self, requirements: Dict[str, Any], **kwargs) -> Dict[str, Any]
    def design_multi_agent_system(self, requirements: Dict[str, Any], **kwargs) -> Dict[str, Any]
    def get_design(self, name: str) -> Optional[Dict[str, Any]]
    def list_designs(self) -> List[str]
```

**Constructor:**
- `config`: Agent configuration
- `model`: AI model instance (defaults to MockModel)

**Methods:**
- `process()`: Generate a design with specified type
- `design_architecture()`: Design application architecture
- `design_workflow()`: Design agent workflow
- `design_multi_agent_system()`: Design multi-agent system
- `get_design()`: Retrieve stored design by name
- `list_designs()`: List all stored design names

**Design Types:**
- `architecture`: Application architecture
- `workflow`: Agent workflow
- `multi_agent`: Multi-agent system
- `component`: Component specification
- `api`: API structure

**Example:**
```python
config = AgentConfig(name="Architect")
agent = DesignAgent(config)
design = agent.design_architecture({
    "name": "my_app",
    "purpose": "Customer support"
})
```

## Utility Functions

### load_config

Load configuration from YAML or JSON file.

```python
def load_config(filepath: Union[str, Path]) -> Dict[str, Any]
```

**Parameters:**
- `filepath`: Path to configuration file (.yaml, .yml, or .json)

**Returns:**
- Dictionary with configuration data

**Example:**
```python
from sample_ai.utils import load_config
config_dict = load_config("config.yaml")
```

### save_config

Save configuration to YAML or JSON file.

```python
def save_config(config: Dict[str, Any], filepath: Union[str, Path]) -> None
```

**Parameters:**
- `config`: Configuration dictionary to save
- `filepath`: Path where to save (.yaml, .yml, or .json)

**Example:**
```python
from sample_ai.utils import save_config
save_config({"name": "Agent"}, "config.yaml")
```

## Mock Model

Testing model implementation.

```python
class MockModel(AIModel):
    def generate(self, prompt: str, **kwargs) -> str
    def chat(self, messages: List[Dict[str, str]], **kwargs) -> str
```

Returns mock responses for testing and development.

**Example:**
```python
from sample_ai.core.model import MockModel, ModelConfig
model = MockModel(ModelConfig(model_name="mock"))
response = model.generate("Hello")
```

## Type Definitions

### Message Format (Chat)

```python
{
    "role": str,      # "system", "user", or "assistant"
    "content": str    # Message content
}
```

### Task Result Format

```python
{
    "task_type": str,        # Type of task executed
    "input": Any,            # Input data
    "result": str,           # Task result
    "metadata": Dict[str, Any]  # Additional metadata
}
```

### Design Result Format

```python
{
    "design_type": str,              # Type of design
    "requirements": Dict[str, Any],  # Input requirements
    "output": str,                   # Design output
    "metadata": Dict[str, Any]       # Additional metadata
}
```

## Error Handling

All classes use standard Python exceptions:

- `ValueError`: Invalid configuration or parameters
- `FileNotFoundError`: Configuration file not found
- `NotImplementedError`: Abstract method not implemented

## Best Practices

1. **Always validate configuration:**
   ```python
   config = AgentConfig(name="MyAgent")  # Validates automatically
   ```

2. **Use type hints:**
   ```python
   def process(self, input_data: str, **kwargs) -> str:
       ...
   ```

3. **Track history for debugging:**
   ```python
   history = agent.get_history()
   ```

4. **Clear history to save memory:**
   ```python
   agent.clear_history()
   ```

5. **Use configuration files for production:**
   ```python
   config_dict = load_config("production.yaml")
   config = AgentConfig(**config_dict)
   ```
