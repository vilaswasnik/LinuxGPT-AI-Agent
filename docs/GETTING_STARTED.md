# Getting Started with Sample.AI

This guide will help you get started with Sample.AI framework for building AI agents.

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Install from Source

```bash
# Clone the repository
git clone https://github.com/vilaswasnik/sample.ai.git
cd sample.ai

# Install in development mode
pip install -e .
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Your First Agent

### 1. Chat Agent Example

Create a simple conversational agent:

```python
from sample_ai import ChatAgent
from sample_ai.core.agent import AgentConfig

# Configure your agent
config = AgentConfig(
    name="MyAssistant",
    description="A helpful assistant",
    system_prompt="You are a friendly AI assistant.",
    temperature=0.7
)

# Create the agent
agent = ChatAgent(config)

# Start chatting
response = agent.process("Hello! How are you?")
print(response)
```

### 2. Task Agent Example

Create an agent for specific tasks:

```python
from sample_ai import TaskAgent
from sample_ai.core.agent import AgentConfig

# Configure the agent
config = AgentConfig(
    name="TaskBot",
    description="Task execution agent"
)

# Create the agent
agent = TaskAgent(config)

# Execute a task
text = "Your long text to summarize..."
summary = agent.execute_summarization(text)
print(summary)
```

### 3. Design Agent Example

Create an agent for AI system design:

```python
from sample_ai import DesignAgent
from sample_ai.core.agent import AgentConfig

# Configure the agent
config = AgentConfig(
    name="Architect",
    description="AI system designer"
)

# Create the agent
agent = DesignAgent(config)

# Design a system
requirements = {
    "name": "my_app",
    "purpose": "Customer support",
    "features": ["chat", "ticketing"]
}

design = agent.design_architecture(requirements)
print(design)
```

## Creating Custom Agents

Extend the `BaseAgent` class to create specialized agents:

```python
from sample_ai.core.agent import BaseAgent, AgentConfig
from typing import Any

class MyCustomAgent(BaseAgent):
    """My specialized agent."""
    
    def process(self, input_data: Any, **kwargs) -> Any:
        """Process input data."""
        # Your custom logic here
        result = f"Processed: {input_data}"
        
        # Track in history
        self.add_to_history({
            "input": input_data,
            "output": result
        })
        
        return result

# Use your custom agent
config = AgentConfig(name="CustomAgent")
agent = MyCustomAgent(config)
output = agent.process("test input")
```

## Integrating AI Models

### Using Mock Models (for testing)

The framework includes a `MockModel` for development:

```python
from sample_ai.core.model import MockModel, ModelConfig

model = MockModel(ModelConfig(model_name="test-model"))
response = model.generate("Hello")
print(response)
```

### Creating Custom Models

Integrate any AI API by extending `AIModel`:

```python
from sample_ai.core.model import AIModel, ModelConfig
from typing import List, Dict

class MyCustomModel(AIModel):
    """Custom model integration."""
    
    def generate(self, prompt: str, **kwargs) -> str:
        """Generate text."""
        # Call your AI API here
        # For example: response = api.complete(prompt)
        return "Generated response"
    
    def chat(self, messages: List[Dict[str, str]], **kwargs) -> str:
        """Generate chat response."""
        # Call your AI API here
        # For example: response = api.chat(messages)
        return "Chat response"

# Use with agents
from sample_ai import ChatAgent

config = AgentConfig(name="Agent")
model = MyCustomModel(ModelConfig(model_name="my-model"))
agent = ChatAgent(config, model=model)
```

## Configuration Files

### Using YAML Configuration

Create a `config.yaml` file:

```yaml
name: "MyAgent"
description: "Production agent"
temperature: 0.7
max_tokens: 2048
system_prompt: "You are a helpful assistant."
metadata:
  version: "1.0"
  environment: "production"
```

Load and use:

```python
from sample_ai.utils import load_config
from sample_ai.core.agent import AgentConfig
from sample_ai import ChatAgent

# Load configuration
config_dict = load_config("config.yaml")
config = AgentConfig(**config_dict)

# Create agent
agent = ChatAgent(config)
```

## Agent Features

### History Tracking

All agents track their interactions:

```python
# Get history
history = agent.get_history()
print(f"Total interactions: {len(history)}")

# Clear history
agent.clear_history()
```

### Configuration Updates

Update agent configuration dynamically:

```python
agent.update_config(temperature=0.9, max_tokens=4096)
```

### Conversation Management (ChatAgent)

```python
# Get conversation
conversation = agent.get_conversation()

# Clear conversation
agent.clear_conversation()

# Set system prompt
agent.set_system_prompt("New system prompt")
```

## Running Examples

The repository includes several examples:

```bash
# Chat agent example
python examples/chat_example.py

# Task agent example
python examples/task_example.py

# Design agent example
python examples/design_example.py

# Custom agent example
python examples/custom_agent_example.py
```

## Next Steps

1. **Explore Examples**: Run the examples to see agents in action
2. **Read Architecture**: Understand the framework design in `docs/ARCHITECTURE.md`
3. **Build Your Agent**: Create custom agents for your use case
4. **Integrate Models**: Connect real AI models to your agents
5. **Build Applications**: Use agents to build complete AI applications

## Common Patterns

### Multi-Step Processing

```python
# Use multiple agents in sequence
chat_agent = ChatAgent(config)
task_agent = TaskAgent(config)

# Get user input
user_input = chat_agent.process("Explain AI")

# Process response
summary = task_agent.execute_summarization(user_input)
```

### Agent Composition

```python
class CompositeAgent(BaseAgent):
    """Agent that uses multiple sub-agents."""
    
    def __init__(self, config):
        super().__init__(config)
        self.chat = ChatAgent(config)
        self.task = TaskAgent(config)
    
    def process(self, input_data, **kwargs):
        # Use both agents
        response = self.chat.process(input_data)
        summary = self.task.execute_summarization(response)
        return summary
```

## Troubleshooting

### Import Errors

Make sure the package is installed:
```bash
pip install -e .
```

### Configuration Errors

Validate your configuration:
```python
config = AgentConfig(
    name="MyAgent",  # Required
    description=""   # Optional
)
```

## Getting Help

- Check the examples in `examples/`
- Read the architecture documentation
- Open an issue on GitHub

## What's Next?

- Integrate with OpenAI, Anthropic, or other AI APIs
- Build multi-agent systems
- Create specialized agents for your domain
- Contribute back to the project!
