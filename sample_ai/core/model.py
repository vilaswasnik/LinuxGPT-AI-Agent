"""AI Model abstraction layer for the framework."""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field


class ModelConfig(BaseModel):
    """Configuration for an AI model."""
    
    model_name: str = Field(..., description="Name/identifier of the model")
    provider: str = Field("custom", description="Model provider (e.g., openai, anthropic, custom)")
    api_key: Optional[str] = Field(None, description="API key for the model provider")
    endpoint: Optional[str] = Field(None, description="API endpoint URL")
    parameters: Dict[str, Any] = Field(default_factory=dict, description="Model-specific parameters")


class AIModel(ABC):
    """
    Abstract base class for AI models.
    
    This class provides a common interface for different AI model implementations,
    allowing easy swapping and integration of various AI backends.
    """
    
    def __init__(self, config: ModelConfig):
        """
        Initialize the AI model.
        
        Args:
            config: Configuration for the model
        """
        self.config = config
        self._client = None
    
    @abstractmethod
    def generate(self, prompt: str, **kwargs) -> str:
        """
        Generate text based on the given prompt.
        
        Args:
            prompt: Input prompt for generation
            **kwargs: Additional generation parameters
            
        Returns:
            Generated text
        """
        pass
    
    @abstractmethod
    def chat(self, messages: List[Dict[str, str]], **kwargs) -> str:
        """
        Generate a response based on a conversation history.
        
        Args:
            messages: List of message dictionaries with 'role' and 'content'
            **kwargs: Additional generation parameters
            
        Returns:
            Generated response
        """
        pass
    
    def get_config(self) -> ModelConfig:
        """
        Get the model's configuration.
        
        Returns:
            Model configuration
        """
        return self.config
    
    def __repr__(self) -> str:
        """String representation of the model."""
        return f"{self.__class__.__name__}(model='{self.config.model_name}')"


class MockModel(AIModel):
    """
    Mock model implementation for testing and development.
    
    This model returns predefined responses without calling any external APIs.
    """
    
    def generate(self, prompt: str, **kwargs) -> str:
        """
        Generate a mock response.
        
        Args:
            prompt: Input prompt
            **kwargs: Additional parameters (ignored)
            
        Returns:
            Mock generated text
        """
        return f"[Mock Response] Processed prompt: '{prompt[:50]}...'"
    
    def chat(self, messages: List[Dict[str, str]], **kwargs) -> str:
        """
        Generate a mock chat response.
        
        Args:
            messages: Conversation history
            **kwargs: Additional parameters (ignored)
            
        Returns:
            Mock chat response
        """
        last_message = messages[-1] if messages else {"content": ""}
        return f"[Mock Chat Response] Reply to: '{last_message.get('content', '')[:50]}...'"
