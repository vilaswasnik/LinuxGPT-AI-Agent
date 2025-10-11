"""Base agent class for all AI agents in the framework."""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field


class AgentConfig(BaseModel):
    """Configuration for an AI agent."""
    
    name: str = Field(..., description="Name of the agent")
    description: str = Field("", description="Description of the agent's purpose")
    model_name: Optional[str] = Field(None, description="Name of the AI model to use")
    temperature: float = Field(0.7, ge=0.0, le=2.0, description="Temperature for generation")
    max_tokens: int = Field(2048, gt=0, description="Maximum tokens to generate")
    system_prompt: Optional[str] = Field(None, description="System prompt for the agent")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional metadata")


class BaseAgent(ABC):
    """
    Base class for all AI agents.
    
    This abstract class provides the foundation for building different types of AI agents.
    Subclasses must implement the `process` method to define their specific behavior.
    """
    
    def __init__(self, config: AgentConfig):
        """
        Initialize the base agent.
        
        Args:
            config: Configuration for the agent
        """
        self.config = config
        self.history: List[Dict[str, Any]] = []
        self._initialized = False
    
    def initialize(self) -> None:
        """Initialize the agent. Called before first use."""
        if not self._initialized:
            self._setup()
            self._initialized = True
    
    def _setup(self) -> None:
        """Internal setup method. Override in subclasses if needed."""
        pass
    
    @abstractmethod
    def process(self, input_data: Any, **kwargs) -> Any:
        """
        Process input data and return output.
        
        Args:
            input_data: Input data to process
            **kwargs: Additional keyword arguments
            
        Returns:
            Processed output
        """
        pass
    
    def add_to_history(self, entry: Dict[str, Any]) -> None:
        """
        Add an entry to the agent's history.
        
        Args:
            entry: Dictionary containing the history entry
        """
        self.history.append(entry)
    
    def get_history(self) -> List[Dict[str, Any]]:
        """
        Get the agent's history.
        
        Returns:
            List of history entries
        """
        return self.history.copy()
    
    def clear_history(self) -> None:
        """Clear the agent's history."""
        self.history.clear()
    
    def get_config(self) -> AgentConfig:
        """
        Get the agent's configuration.
        
        Returns:
            Agent configuration
        """
        return self.config
    
    def update_config(self, **kwargs) -> None:
        """
        Update agent configuration.
        
        Args:
            **kwargs: Configuration parameters to update
        """
        for key, value in kwargs.items():
            if hasattr(self.config, key):
                setattr(self.config, key, value)
    
    def __repr__(self) -> str:
        """String representation of the agent."""
        return f"{self.__class__.__name__}(name='{self.config.name}')"
