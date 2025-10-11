# Sample.AI

An AI base agent model framework to build and design any AI application.

## Overview

Sample.AI provides a flexible and extensible framework for creating AI agents that can power various AI applications. Whether you're building chatbots, task automation systems, or complex multi-agent architectures, Sample.AI gives you the foundation you need.

## Features

- 🤖 **Base Agent Architecture**: Extensible base classes for creating custom AI agents
- 💬 **Pre-built Agents**: Ready-to-use agents for common use cases
  - `ChatAgent`: Conversational AI applications
  - `TaskAgent`: Specific task execution (summarization, extraction, classification, etc.)
  - `DesignAgent`: AI application architecture and design
- 🔌 **Model Abstraction**: Easy integration with any AI model or API
- 📝 **Configuration Management**: YAML/JSON-based configuration system
- 📊 **History Tracking**: Built-in conversation and task history
- 🎯 **Type Safety**: Full typing support with Pydantic models

## Installation

### From Source

```bash
git clone https://github.com/vilaswasnik/sample.ai.git
cd sample.ai
pip install -e .
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Quick Start

### Using ChatAgent

```python
from sample_ai import ChatAgent
from sample_ai.core.agent import AgentConfig

# Create configuration
config = AgentConfig(
    name="Assistant",
    description="A helpful AI assistant",
    system_prompt="You are a helpful AI assistant.",
    temperature=0.7
)

# Initialize agent
agent = ChatAgent(config)

# Chat with the agent
response = agent.process("Hello! How are you?")
print(response)
```

### Using TaskAgent

```python
from sample_ai import TaskAgent
from sample_ai.core.agent import AgentConfig

# Create configuration
config = AgentConfig(
    name="TaskExecutor",
    description="Task execution agent",
    temperature=0.5
)

# Initialize agent
agent = TaskAgent(config)

# Execute a summarization task
summary = agent.execute_summarization("Your long text here...")
print(summary)
```

### Using DesignAgent

```python
from sample_ai import DesignAgent
from sample_ai.core.agent import AgentConfig

# Create configuration
config = AgentConfig(
    name="AIArchitect",
    description="AI system designer"
)

# Initialize agent
agent = DesignAgent(config)

# Design an architecture
requirements = {
    "name": "chatbot_system",
    "purpose": "Customer support",
    "features": ["FAQ", "Ticketing"]
}

design = agent.design_architecture(requirements)
print(design)
```

## Creating Custom Agents

Extend the `BaseAgent` class to create your own specialized agents:

```python
from sample_ai.core.agent import BaseAgent, AgentConfig
from typing import Any

class MyCustomAgent(BaseAgent):
    def process(self, input_data: Any, **kwargs) -> Any:
        # Implement your custom logic
        result = f"Processed: {input_data}"
        self.add_to_history({"input": input_data, "result": result})
        return result

# Use your custom agent
config = AgentConfig(name="CustomAgent", description="My custom agent")
agent = MyCustomAgent(config)
output = agent.process("Hello")
```

## Examples

The `examples/` directory contains detailed examples:

- `chat_example.py`: ChatAgent usage
- `task_example.py`: TaskAgent usage
- `design_example.py`: DesignAgent usage
- `custom_agent_example.py`: Creating custom agents

Run an example:

```bash
python examples/chat_example.py
```

## Architecture

### Core Components

- **BaseAgent**: Abstract base class for all agents
- **AIModel**: Abstract base class for AI model integrations
- **AgentConfig**: Configuration model using Pydantic
- **ModelConfig**: Model configuration

### Agent Types

1. **ChatAgent**: Maintains conversation context and generates responses
2. **TaskAgent**: Executes specific tasks like summarization, extraction, classification
3. **DesignAgent**: Creates AI application designs and architectures

### Extending the Framework

You can extend Sample.AI in several ways:

1. **Custom Agents**: Inherit from `BaseAgent`
2. **Custom Models**: Inherit from `AIModel` to integrate any AI service
3. **Custom Configuration**: Use YAML/JSON for complex configurations

## Configuration

### Agent Configuration

```python
from sample_ai.core.agent import AgentConfig

config = AgentConfig(
    name="MyAgent",
    description="Agent description",
    model_name="gpt-4",  # Optional
    temperature=0.7,
    max_tokens=2048,
    system_prompt="Custom system prompt",
    metadata={"key": "value"}
)
```

### Using Configuration Files

```python
from sample_ai.utils import load_config

config_dict = load_config("config.yaml")
config = AgentConfig(**config_dict)
```

## Integrating AI Models

The framework supports any AI model through the `AIModel` abstraction:

```python
from sample_ai.core.model import AIModel, ModelConfig
from typing import List, Dict

class MyCustomModel(AIModel):
    def generate(self, prompt: str, **kwargs) -> str:
        # Implement generation logic
        return "Generated response"
    
    def chat(self, messages: List[Dict[str, str]], **kwargs) -> str:
        # Implement chat logic
        return "Chat response"

# Use with agents
agent = ChatAgent(config, model=MyCustomModel(ModelConfig(model_name="custom")))
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.

## Support

For issues and questions, please open an issue on GitHub.

## Roadmap

- [ ] Integration with popular AI APIs (OpenAI, Anthropic, etc.)
- [ ] Multi-agent orchestration
- [ ] Built-in prompt templates
- [ ] Performance monitoring and logging
- [ ] Web UI for agent management
- [ ] Vector database integration
- [ ] Tool/function calling support