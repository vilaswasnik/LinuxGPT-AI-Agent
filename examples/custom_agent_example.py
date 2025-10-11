"""Example: Creating a custom agent by extending BaseAgent."""

from typing import Any, Dict
from sample_ai.core.agent import BaseAgent, AgentConfig
from sample_ai.core.model import MockModel, ModelConfig


class CodeReviewAgent(BaseAgent):
    """Custom agent for code review tasks."""
    
    def __init__(self, config: AgentConfig):
        super().__init__(config)
        self.model = MockModel(ModelConfig(model_name="code-reviewer"))
        self.reviews: list = []
    
    def process(self, input_data: Dict[str, Any], **kwargs) -> Dict[str, Any]:
        """
        Review code and provide feedback.
        
        Args:
            input_data: Dictionary with 'code' and 'language' keys
            **kwargs: Additional parameters
            
        Returns:
            Review results
        """
        code = input_data.get("code", "")
        language = input_data.get("language", "unknown")
        
        # Build review prompt
        prompt = f"Review the following {language} code:\n\n{code}"
        
        # Generate review using model
        review = self.model.generate(prompt, **kwargs)
        
        # Prepare review result
        result = {
            "language": language,
            "code_length": len(code),
            "review": review,
            "issues_found": kwargs.get("issues_found", 0)
        }
        
        self.reviews.append(result)
        self.add_to_history(result)
        
        return result
    
    def get_reviews(self) -> list:
        """Get all reviews."""
        return self.reviews.copy()


def main():
    """Demonstrate custom agent creation."""
    
    # Create configuration for the custom agent
    config = AgentConfig(
        name="CodeReviewer",
        description="A specialized agent for code review",
        system_prompt="You are an expert code reviewer. Analyze code for bugs, performance, and best practices.",
        temperature=0.3
    )
    
    # Initialize the custom agent
    agent = CodeReviewAgent(config)
    
    print("=== Custom Agent Example: CodeReviewAgent ===")
    print(f"Agent: {agent}\n")
    
    # Example code to review
    code_snippet = """
def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total
    """
    
    # Perform code review
    print("=== Code Review ===")
    review_result = agent.process({
        "code": code_snippet,
        "language": "Python"
    }, issues_found=1)
    
    print(f"Language: {review_result['language']}")
    print(f"Code Length: {review_result['code_length']} characters")
    print(f"Review: {review_result['review']}")
    print(f"Issues Found: {review_result['issues_found']}\n")
    
    # Review another piece of code
    js_code = """
function greet(name) {
    console.log("Hello, " + name);
}
    """
    
    print("=== Another Code Review ===")
    review_result2 = agent.process({
        "code": js_code,
        "language": "JavaScript"
    })
    
    print(f"Language: {review_result2['language']}")
    print(f"Review: {review_result2['review']}\n")
    
    # Display all reviews
    print("=== All Reviews ===")
    for i, review in enumerate(agent.get_reviews(), 1):
        print(f"Review {i}: {review['language']} ({review['code_length']} chars)")


if __name__ == "__main__":
    main()
