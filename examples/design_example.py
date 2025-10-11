"""Example: Using DesignAgent for AI application design."""

from sample_ai import DesignAgent
from sample_ai.core.agent import AgentConfig


def main():
    """Demonstrate DesignAgent usage."""
    
    # Create a design agent configuration
    config = AgentConfig(
        name="AIArchitect",
        description="An AI agent for designing AI applications and architectures",
        system_prompt="You are an expert AI architect specializing in system design.",
        temperature=0.7,
        max_tokens=3072
    )
    
    # Initialize the design agent
    agent = DesignAgent(config)
    
    print("=== DesignAgent Example ===")
    print(f"Agent: {agent}\n")
    
    # Example 1: Design an AI chatbot architecture
    print("=== Design 1: AI Chatbot Architecture ===")
    chatbot_requirements = {
        "name": "customer_support_chatbot",
        "purpose": "Customer support automation",
        "features": ["FAQ answering", "ticket creation", "sentiment analysis"],
        "scale": "10,000 users/day",
        "integration": ["Slack", "Email", "Web"]
    }
    
    architecture = agent.design_architecture(chatbot_requirements)
    print(f"Design Type: {architecture['design_type']}")
    print(f"Output: {architecture['output']}\n")
    
    # Example 2: Design a multi-agent workflow
    print("=== Design 2: Multi-Agent Content Creation System ===")
    workflow_requirements = {
        "name": "content_creation_workflow",
        "goal": "Automated content generation and review",
        "agents": ["research_agent", "writer_agent", "editor_agent", "publisher_agent"],
        "workflow": "Sequential processing with feedback loops"
    }
    
    workflow = agent.design_workflow(workflow_requirements)
    print(f"Design Type: {workflow['design_type']}")
    print(f"Output: {workflow['output']}\n")
    
    # Example 3: Design a multi-agent system
    print("=== Design 3: Multi-Agent Data Processing System ===")
    system_requirements = {
        "name": "data_processing_system",
        "purpose": "Real-time data ingestion and analysis",
        "components": ["ingestion", "validation", "transformation", "storage", "analysis"],
        "data_volume": "1TB/day",
        "latency": "< 100ms"
    }
    
    system = agent.design_multi_agent_system(system_requirements)
    print(f"Design Type: {system['design_type']}")
    print(f"Output: {system['output']}\n")
    
    # List all stored designs
    print("=== Stored Designs ===")
    for design_name in agent.list_designs():
        print(f"- {design_name}")
    
    # Retrieve a specific design
    print("\n=== Retrieving Specific Design ===")
    retrieved = agent.get_design("customer_support_chatbot")
    if retrieved:
        print(f"Retrieved: {retrieved['requirements']['name']}")
        print(f"Purpose: {retrieved['requirements']['purpose']}")


if __name__ == "__main__":
    main()
