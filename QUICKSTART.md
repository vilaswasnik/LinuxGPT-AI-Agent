# Quick Start Guide

Get started with Sample.AI in 5 minutes!

## Installation

```bash
git clone https://github.com/vilaswasnik/sample.ai.git
cd sample.ai
pip install -e .
```

## Example 1: Chat Agent (30 seconds)

```python
from sample_ai import ChatAgent
from sample_ai.core.agent import AgentConfig

# Create and use a chat agent
config = AgentConfig(name="Assistant", description="Helpful AI")
agent = ChatAgent(config)

response = agent.process("Hello!")
print(response)
```

## Example 2: Task Agent (30 seconds)

```python
from sample_ai import TaskAgent
from sample_ai.core.agent import AgentConfig

# Create a task agent
config = AgentConfig(name="TaskBot")
agent = TaskAgent(config)

# Summarize text
summary = agent.execute_summarization("Your long text here...")
print(summary)
```

## Example 3: Design Agent (30 seconds)

```python
from sample_ai import DesignAgent
from sample_ai.core.agent import AgentConfig

# Create a design agent
config = AgentConfig(name="Architect")
agent = DesignAgent(config)

# Design an architecture
design = agent.design_architecture({
    "name": "my_app",
    "purpose": "Customer support"
})
print(design)
```

## Example 4: Custom Agent (2 minutes)

```python
from sample_ai.core.agent import BaseAgent, AgentConfig

class MyAgent(BaseAgent):
    def process(self, input_data, **kwargs):
        result = f"Processed: {input_data}"
        self.add_to_history({"input": input_data, "result": result})
        return result

# Use your custom agent
config = AgentConfig(name="CustomAgent")
agent = MyAgent(config)
output = agent.process("test")
print(output)
```

## Run Pre-built Examples

```bash
python examples/chat_example.py
python examples/task_example.py
python examples/design_example.py
python examples/custom_agent_example.py
```

## Next Steps

1. Read the full [README.md](README.md) for detailed features
2. Check [docs/GETTING_STARTED.md](docs/GETTING_STARTED.md) for comprehensive guide
3. Review [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) to understand the framework
4. Explore the `examples/` directory for more examples
5. Build your own AI application!

## Key Features

✅ Multiple agent types (Chat, Task, Design)  
✅ Easy to extend with custom agents  
✅ Model-agnostic (integrate any AI API)  
✅ Type-safe with Pydantic  
✅ Configuration via YAML/JSON  
✅ Built-in history tracking  

## Need Help?

- Check the [GETTING_STARTED.md](docs/GETTING_STARTED.md) guide
- Review examples in `examples/` directory
- Open an issue on GitHub

Happy building! 🚀
