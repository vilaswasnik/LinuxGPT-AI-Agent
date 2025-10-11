"""Task agent implementation for executing specific AI tasks."""

from typing import Any, Dict, Optional
from sample_ai.core.agent import BaseAgent, AgentConfig
from sample_ai.core.model import AIModel, MockModel, ModelConfig


class TaskAgent(BaseAgent):
    """
    Task agent for executing specific AI tasks.
    
    This agent is designed to complete well-defined tasks such as:
    - Text summarization
    - Content generation
    - Data extraction
    - Classification
    - And more
    """
    
    def __init__(
        self,
        config: AgentConfig,
        model: Optional[AIModel] = None
    ):
        """
        Initialize the task agent.
        
        Args:
            config: Agent configuration
            model: AI model to use for task execution (defaults to MockModel)
        """
        super().__init__(config)
        self.model = model or MockModel(ModelConfig(model_name="mock-task"))
    
    def process(self, input_data: Any, task_type: str = "general", **kwargs) -> Dict[str, Any]:
        """
        Process input data according to the specified task type.
        
        Args:
            input_data: Input data for the task
            task_type: Type of task to perform
            **kwargs: Additional task-specific parameters
            
        Returns:
            Dictionary containing task results
        """
        # Build prompt based on task type and system prompt
        prompt = self._build_prompt(input_data, task_type)
        
        # Execute the task using the model
        result = self.model.generate(prompt, **kwargs)
        
        # Prepare output
        output = {
            "task_type": task_type,
            "input": input_data,
            "result": result,
            "metadata": kwargs
        }
        
        # Add to history
        self.add_to_history(output)
        
        return output
    
    def _build_prompt(self, input_data: Any, task_type: str) -> str:
        """
        Build a prompt for the task.
        
        Args:
            input_data: Input data
            task_type: Task type
            
        Returns:
            Formatted prompt
        """
        system_prompt = self.config.system_prompt or ""
        
        task_instructions = {
            "summarize": "Summarize the following text:",
            "extract": "Extract key information from the following:",
            "classify": "Classify the following content:",
            "generate": "Generate content based on the following:",
            "translate": "Translate the following:",
            "general": "Process the following:"
        }
        
        instruction = task_instructions.get(task_type, task_instructions["general"])
        
        prompt = f"{system_prompt}\n\n{instruction}\n\n{input_data}"
        return prompt.strip()
    
    def execute_summarization(self, text: str, **kwargs) -> str:
        """
        Execute a text summarization task.
        
        Args:
            text: Text to summarize
            **kwargs: Additional parameters
            
        Returns:
            Summary of the text
        """
        result = self.process(text, task_type="summarize", **kwargs)
        return result["result"]
    
    def execute_extraction(self, text: str, **kwargs) -> str:
        """
        Execute a data extraction task.
        
        Args:
            text: Text to extract data from
            **kwargs: Additional parameters
            
        Returns:
            Extracted data
        """
        result = self.process(text, task_type="extract", **kwargs)
        return result["result"]
    
    def execute_classification(self, text: str, **kwargs) -> str:
        """
        Execute a classification task.
        
        Args:
            text: Text to classify
            **kwargs: Additional parameters
            
        Returns:
            Classification result
        """
        result = self.process(text, task_type="classify", **kwargs)
        return result["result"]
