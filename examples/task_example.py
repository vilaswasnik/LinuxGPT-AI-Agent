"""Example: Using TaskAgent for specific AI tasks."""

from sample_ai import TaskAgent
from sample_ai.core.agent import AgentConfig


def main():
    """Demonstrate TaskAgent usage."""
    
    # Create a task agent configuration
    config = AgentConfig(
        name="TaskExecutor",
        description="An AI agent for executing specific tasks",
        system_prompt="You are an AI assistant specialized in processing and analyzing text.",
        temperature=0.5,
        max_tokens=2048
    )
    
    # Initialize the task agent
    agent = TaskAgent(config)
    
    print("=== TaskAgent Example ===")
    print(f"Agent: {agent}\n")
    
    # Example 1: Summarization
    text_to_summarize = """
    Artificial Intelligence (AI) has become an integral part of modern technology.
    It powers everything from search engines to autonomous vehicles. Machine learning,
    a subset of AI, enables systems to learn from data and improve over time without
    explicit programming. Deep learning, using neural networks, has achieved remarkable
    results in image recognition, natural language processing, and game playing.
    """
    
    print("=== Task 1: Text Summarization ===")
    summary = agent.execute_summarization(text_to_summarize)
    print(f"Summary: {summary}\n")
    
    # Example 2: Data Extraction
    text_with_data = """
    Contact: John Doe, Email: john.doe@example.com, Phone: +1-234-567-8900
    Address: 123 Main Street, Anytown, ST 12345
    """
    
    print("=== Task 2: Data Extraction ===")
    extracted = agent.execute_extraction(text_with_data)
    print(f"Extracted Data: {extracted}\n")
    
    # Example 3: Classification
    text_to_classify = "This product is amazing! I love it and would definitely recommend it."
    
    print("=== Task 3: Text Classification ===")
    classification = agent.execute_classification(text_to_classify)
    print(f"Classification: {classification}\n")
    
    # Display agent history
    print("=== Agent History ===")
    for i, entry in enumerate(agent.get_history(), 1):
        print(f"Task {i}: {entry['task_type']}")


if __name__ == "__main__":
    main()
