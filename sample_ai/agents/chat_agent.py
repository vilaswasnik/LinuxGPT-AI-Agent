"""Chat agent implementation for conversational AI applications."""

from typing import Any, Dict, List, Optional
from sample_ai.core.agent import BaseAgent, AgentConfig
from sample_ai.core.model import AIModel, MockModel, ModelConfig


class ChatAgent(BaseAgent):
    """
    Chat agent for building conversational AI applications.
    
    This agent maintains conversation context and can generate responses
    based on chat history.
    """
    
    def __init__(
        self,
        config: AgentConfig,
        model: Optional[AIModel] = None
    ):
        """
        Initialize the chat agent.
        
        Args:
            config: Agent configuration
            model: AI model to use for generation (defaults to MockModel)
        """
        super().__init__(config)
        self.model = model or MockModel(ModelConfig(model_name="mock-chat"))
        self.conversation: List[Dict[str, str]] = []
        
        # Add system prompt to conversation if provided
        if config.system_prompt:
            self.conversation.append({
                "role": "system",
                "content": config.system_prompt
            })
    
    def process(self, input_data: str, **kwargs) -> str:
        """
        Process a chat message and generate a response.
        
        Args:
            input_data: User message
            **kwargs: Additional parameters for generation
            
        Returns:
            Agent's response
        """
        # Add user message to conversation
        self.conversation.append({
            "role": "user",
            "content": input_data
        })
        
        # Generate response using the model
        response = self.model.chat(self.conversation, **kwargs)
        
        # Add assistant response to conversation
        self.conversation.append({
            "role": "assistant",
            "content": response
        })
        
        # Add to history
        self.add_to_history({
            "type": "chat",
            "user_message": input_data,
            "assistant_response": response
        })
        
        return response
    
    def get_conversation(self) -> List[Dict[str, str]]:
        """
        Get the full conversation history.
        
        Returns:
            List of conversation messages
        """
        return self.conversation.copy()
    
    def clear_conversation(self) -> None:
        """Clear the conversation history, keeping only the system prompt if present."""
        system_messages = [msg for msg in self.conversation if msg.get("role") == "system"]
        self.conversation = system_messages
        self.clear_history()
    
    def set_system_prompt(self, prompt: str) -> None:
        """
        Set or update the system prompt.
        
        Args:
            prompt: New system prompt
        """
        # Remove existing system prompts
        self.conversation = [msg for msg in self.conversation if msg.get("role") != "system"]
        
        # Add new system prompt at the beginning
        self.conversation.insert(0, {
            "role": "system",
            "content": prompt
        })
        
        self.config.system_prompt = prompt
