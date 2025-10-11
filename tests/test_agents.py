"""Tests for agent implementations."""

from sample_ai import ChatAgent, TaskAgent, DesignAgent
from sample_ai.core.agent import AgentConfig


def test_chat_agent_initialization():
    """Test ChatAgent initialization."""
    config = AgentConfig(
        name="TestAgent",
        description="Test chat agent"
    )
    agent = ChatAgent(config)
    assert agent.config.name == "TestAgent"
    assert isinstance(agent.conversation, list)


def test_chat_agent_process():
    """Test ChatAgent message processing."""
    config = AgentConfig(name="TestAgent")
    agent = ChatAgent(config)
    
    response = agent.process("Hello")
    assert isinstance(response, str)
    assert len(agent.conversation) == 2  # User + assistant
    assert agent.conversation[0]["role"] == "user"
    assert agent.conversation[1]["role"] == "assistant"


def test_chat_agent_conversation_history():
    """Test ChatAgent conversation history."""
    config = AgentConfig(name="TestAgent")
    agent = ChatAgent(config)
    
    agent.process("Message 1")
    agent.process("Message 2")
    
    conversation = agent.get_conversation()
    assert len(conversation) == 4  # 2 user + 2 assistant
    
    agent.clear_conversation()
    assert len(agent.get_conversation()) == 0


def test_task_agent_initialization():
    """Test TaskAgent initialization."""
    config = AgentConfig(name="TaskAgent")
    agent = TaskAgent(config)
    assert agent.config.name == "TaskAgent"


def test_task_agent_process():
    """Test TaskAgent task processing."""
    config = AgentConfig(name="TaskAgent")
    agent = TaskAgent(config)
    
    result = agent.process("Test data", task_type="summarize")
    assert isinstance(result, dict)
    assert result["task_type"] == "summarize"
    assert "result" in result


def test_task_agent_specialized_methods():
    """Test TaskAgent specialized task methods."""
    config = AgentConfig(name="TaskAgent")
    agent = TaskAgent(config)
    
    summary = agent.execute_summarization("Long text here")
    assert isinstance(summary, str)
    
    extracted = agent.execute_extraction("Data to extract")
    assert isinstance(extracted, str)
    
    classification = agent.execute_classification("Text to classify")
    assert isinstance(classification, str)


def test_design_agent_initialization():
    """Test DesignAgent initialization."""
    config = AgentConfig(name="DesignAgent")
    agent = DesignAgent(config)
    assert agent.config.name == "DesignAgent"
    assert isinstance(agent.designs, dict)


def test_design_agent_process():
    """Test DesignAgent design generation."""
    config = AgentConfig(name="DesignAgent")
    agent = DesignAgent(config)
    
    requirements = {
        "name": "test_design",
        "purpose": "Testing"
    }
    
    design = agent.process(requirements, design_type="architecture")
    assert isinstance(design, dict)
    assert design["design_type"] == "architecture"
    assert "output" in design


def test_design_agent_storage():
    """Test DesignAgent design storage and retrieval."""
    config = AgentConfig(name="DesignAgent")
    agent = DesignAgent(config)
    
    requirements = {
        "name": "stored_design",
        "purpose": "Test storage"
    }
    
    agent.design_architecture(requirements)
    
    assert "stored_design" in agent.list_designs()
    retrieved = agent.get_design("stored_design")
    assert retrieved is not None
    assert retrieved["requirements"]["name"] == "stored_design"


def test_agent_history():
    """Test agent history tracking."""
    config = AgentConfig(name="TestAgent")
    agent = TaskAgent(config)
    
    agent.process("Test 1", task_type="summarize")
    agent.process("Test 2", task_type="extract")
    
    history = agent.get_history()
    assert len(history) == 2
    assert history[0]["task_type"] == "summarize"
    assert history[1]["task_type"] == "extract"
    
    agent.clear_history()
    assert len(agent.get_history()) == 0


if __name__ == "__main__":
    # Run tests manually
    test_chat_agent_initialization()
    test_chat_agent_process()
    test_chat_agent_conversation_history()
    test_task_agent_initialization()
    test_task_agent_process()
    test_task_agent_specialized_methods()
    test_design_agent_initialization()
    test_design_agent_process()
    test_design_agent_storage()
    test_agent_history()
    print("All tests passed!")
