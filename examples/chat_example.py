"""Example: Using ChatAgent for conversational AI."""

from sample_ai import ChatAgent
from sample_ai.core.agent import AgentConfig


def main():
    """Demonstrate ChatAgent usage."""
    
    # Create a chat agent configuration
    config = AgentConfig(
        name="Assistant",
        description="A helpful AI assistant",
        system_prompt="You are a helpful AI assistant. Be concise and friendly.",
        temperature=0.7,
        max_tokens=1024
    )
    
    # Initialize the chat agent
    agent = ChatAgent(config)
    
    print("=== ChatAgent Example ===")
    print(f"Agent: {agent}")
    print(f"System Prompt: {config.system_prompt}\n")
    
    # Simulate a conversation
    messages = [
        "Hello! What can you help me with?",
        "Can you explain what you are?",
        "Thank you!"
    ]
    
    for user_message in messages:
        print(f"User: {user_message}")
        response = agent.process(user_message)
        print(f"Agent: {response}\n")
    
    # Display conversation history
    print("=== Conversation History ===")
    for i, msg in enumerate(agent.get_conversation(), 1):
        print(f"{i}. [{msg['role']}]: {msg['content']}")
    
    # Clear conversation
    print("\n=== Clearing Conversation ===")
    agent.clear_conversation()
    print(f"Conversation length after clear: {len(agent.get_conversation())}")


if __name__ == "__main__":
    main()
