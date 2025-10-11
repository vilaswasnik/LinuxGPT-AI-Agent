"""Design agent implementation for AI application architecture and design."""

from typing import Any, Dict, List, Optional
from sample_ai.core.agent import BaseAgent, AgentConfig
from sample_ai.core.model import AIModel, MockModel, ModelConfig


class DesignAgent(BaseAgent):
    """
    Design agent for creating AI application architectures and designs.
    
    This agent helps in:
    - Designing AI application architectures
    - Creating agent workflows
    - Planning multi-agent systems
    - Generating component specifications
    """
    
    def __init__(
        self,
        config: AgentConfig,
        model: Optional[AIModel] = None
    ):
        """
        Initialize the design agent.
        
        Args:
            config: Agent configuration
            model: AI model to use for design tasks (defaults to MockModel)
        """
        super().__init__(config)
        self.model = model or MockModel(ModelConfig(model_name="mock-design"))
        self.designs: Dict[str, Any] = {}
    
    def process(self, input_data: Dict[str, Any], design_type: str = "architecture", **kwargs) -> Dict[str, Any]:
        """
        Process design requirements and generate a design.
        
        Args:
            input_data: Design requirements and specifications
            design_type: Type of design to create
            **kwargs: Additional design parameters
            
        Returns:
            Dictionary containing the design
        """
        # Build design prompt
        prompt = self._build_design_prompt(input_data, design_type)
        
        # Generate design using the model
        design_output = self.model.generate(prompt, **kwargs)
        
        # Create design document
        design = {
            "design_type": design_type,
            "requirements": input_data,
            "output": design_output,
            "metadata": kwargs
        }
        
        # Store design if it has a name
        if "name" in input_data:
            self.designs[input_data["name"]] = design
        
        # Add to history
        self.add_to_history(design)
        
        return design
    
    def _build_design_prompt(self, requirements: Dict[str, Any], design_type: str) -> str:
        """
        Build a prompt for design generation.
        
        Args:
            requirements: Design requirements
            design_type: Type of design
            
        Returns:
            Formatted design prompt
        """
        system_prompt = self.config.system_prompt or "You are an AI architect and designer."
        
        design_templates = {
            "architecture": "Design an AI application architecture based on these requirements:",
            "workflow": "Create an agent workflow for the following use case:",
            "multi_agent": "Design a multi-agent system with these specifications:",
            "component": "Specify components for the following application:",
            "api": "Design an API structure for:"
        }
        
        instruction = design_templates.get(design_type, design_templates["architecture"])
        
        # Format requirements
        req_text = "\n".join([f"- {k}: {v}" for k, v in requirements.items()])
        
        prompt = f"{system_prompt}\n\n{instruction}\n\n{req_text}"
        return prompt.strip()
    
    def design_architecture(self, requirements: Dict[str, Any], **kwargs) -> Dict[str, Any]:
        """
        Design an AI application architecture.
        
        Args:
            requirements: Architecture requirements
            **kwargs: Additional parameters
            
        Returns:
            Architecture design
        """
        return self.process(requirements, design_type="architecture", **kwargs)
    
    def design_workflow(self, requirements: Dict[str, Any], **kwargs) -> Dict[str, Any]:
        """
        Design an agent workflow.
        
        Args:
            requirements: Workflow requirements
            **kwargs: Additional parameters
            
        Returns:
            Workflow design
        """
        return self.process(requirements, design_type="workflow", **kwargs)
    
    def design_multi_agent_system(self, requirements: Dict[str, Any], **kwargs) -> Dict[str, Any]:
        """
        Design a multi-agent system.
        
        Args:
            requirements: System requirements
            **kwargs: Additional parameters
            
        Returns:
            Multi-agent system design
        """
        return self.process(requirements, design_type="multi_agent", **kwargs)
    
    def get_design(self, name: str) -> Optional[Dict[str, Any]]:
        """
        Retrieve a stored design by name.
        
        Args:
            name: Name of the design
            
        Returns:
            Design dictionary or None if not found
        """
        return self.designs.get(name)
    
    def list_designs(self) -> List[str]:
        """
        List all stored design names.
        
        Returns:
            List of design names
        """
        return list(self.designs.keys())
