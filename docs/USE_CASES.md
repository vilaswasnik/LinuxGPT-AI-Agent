# Use Cases

This document showcases various use cases and applications you can build with Sample.AI.

## 1. Customer Support Chatbot

Build an intelligent customer support system.

```python
from sample_ai import ChatAgent
from sample_ai.core.agent import AgentConfig

# Configure support agent
config = AgentConfig(
    name="SupportBot",
    description="Customer support assistant",
    system_prompt="""
    You are a helpful customer support agent for TechCorp.
    - Be polite and professional
    - Provide accurate information about our products
    - If you don't know something, offer to connect with a human agent
    """,
    temperature=0.7
)

agent = ChatAgent(config)

# Handle customer queries
response = agent.process("How do I reset my password?")
```

## 2. Content Summarization Service

Automatically summarize long documents.

```python
from sample_ai import TaskAgent
from sample_ai.core.agent import AgentConfig

config = AgentConfig(
    name="Summarizer",
    description="Document summarization agent",
    temperature=0.5,
    max_tokens=1024
)

agent = TaskAgent(config)

# Summarize articles
article = "... long article text ..."
summary = agent.execute_summarization(article)
print(f"Summary: {summary}")
```

## 3. Data Extraction Pipeline

Extract structured data from unstructured text.

```python
from sample_ai import TaskAgent
from sample_ai.core.agent import AgentConfig

config = AgentConfig(
    name="DataExtractor",
    system_prompt="Extract structured information accurately."
)

agent = TaskAgent(config)

# Extract contact information
text = """
John Doe
Email: john@example.com
Phone: (555) 123-4567
Address: 123 Main St, City, ST 12345
"""

extracted = agent.execute_extraction(text)
```

## 4. Content Classification System

Classify text into categories.

```python
from sample_ai import TaskAgent
from sample_ai.core.agent import AgentConfig

config = AgentConfig(
    name="Classifier",
    system_prompt="Classify content into: positive, negative, or neutral."
)

agent = TaskAgent(config)

# Classify customer feedback
feedback = "This product exceeded my expectations!"
sentiment = agent.execute_classification(feedback)
```

## 5. AI Application Designer

Design AI architectures and workflows.

```python
from sample_ai import DesignAgent
from sample_ai.core.agent import AgentConfig

config = AgentConfig(
    name="AIArchitect",
    description="AI system designer"
)

agent = DesignAgent(config)

# Design a recommendation system
requirements = {
    "name": "recommendation_engine",
    "purpose": "Product recommendations",
    "features": [
        "Collaborative filtering",
        "Content-based filtering",
        "Real-time updates"
    ],
    "scale": "1M users",
    "data_sources": ["user_behavior", "product_catalog"]
}

design = agent.design_architecture(requirements)
```

## 6. Multi-Agent Research Assistant

Coordinate multiple agents for research tasks.

```python
from sample_ai import ChatAgent, TaskAgent
from sample_ai.core.agent import AgentConfig

# Research coordinator
coordinator_config = AgentConfig(
    name="Coordinator",
    system_prompt="Coordinate research tasks and synthesize findings."
)
coordinator = ChatAgent(coordinator_config)

# Summarizer agent
summarizer_config = AgentConfig(name="Summarizer")
summarizer = TaskAgent(summarizer_config)

# Workflow
query = "What are the latest trends in AI?"
research_plan = coordinator.process(query)

# Use summarizer for each source
sources = ["source1_text", "source2_text", "source3_text"]
summaries = [summarizer.execute_summarization(s) for s in sources]

# Synthesize findings
final_report = coordinator.process(f"Synthesize: {summaries}")
```

## 7. Code Review Assistant

Build an automated code review system.

```python
from sample_ai.core.agent import BaseAgent, AgentConfig
from sample_ai.core.model import MockModel, ModelConfig

class CodeReviewAgent(BaseAgent):
    def __init__(self, config: AgentConfig):
        super().__init__(config)
        self.model = MockModel(ModelConfig(model_name="code-reviewer"))
    
    def process(self, input_data, **kwargs):
        code = input_data.get("code", "")
        language = input_data.get("language", "")
        
        prompt = f"""
        Review this {language} code for:
        - Bugs and errors
        - Performance issues
        - Security vulnerabilities
        - Best practices
        - Code style
        
        Code:
        {code}
        """
        
        review = self.model.generate(prompt)
        return {
            "language": language,
            "review": review,
            "suggestions": kwargs.get("suggestions", [])
        }

# Use the code review agent
config = AgentConfig(
    name="CodeReviewer",
    system_prompt="You are an expert code reviewer."
)
agent = CodeReviewAgent(config)

review = agent.process({
    "code": "def hello():\n    print('Hello')",
    "language": "Python"
})
```

## 8. Email Automation System

Automate email responses and categorization.

```python
from sample_ai import TaskAgent, ChatAgent
from sample_ai.core.agent import AgentConfig

# Email classifier
classifier_config = AgentConfig(
    name="EmailClassifier",
    system_prompt="Classify emails as: urgent, important, or routine."
)
classifier = TaskAgent(classifier_config)

# Email responder
responder_config = AgentConfig(
    name="EmailResponder",
    system_prompt="Generate professional email responses."
)
responder = ChatAgent(responder_config)

# Process incoming email
email = "Subject: Meeting tomorrow\nBody: Can we meet at 2pm?"
category = classifier.execute_classification(email)
response = responder.process(f"Draft response for: {email}")
```

## 9. Learning Management System

Create personalized learning experiences.

```python
from sample_ai import ChatAgent, TaskAgent
from sample_ai.core.agent import AgentConfig

# Tutor agent
tutor_config = AgentConfig(
    name="Tutor",
    description="Personalized learning assistant",
    system_prompt="""
    You are a patient and knowledgeable tutor.
    - Adapt explanations to student level
    - Provide examples and exercises
    - Give constructive feedback
    """
)
tutor = ChatAgent(tutor_config)

# Assessment agent
assessment_config = AgentConfig(name="Assessor")
assessor = TaskAgent(assessment_config)

# Interactive tutoring
student_question = "Can you explain recursion?"
explanation = tutor.process(student_question)

# Assess understanding
student_answer = "Recursion is when a function calls itself"
evaluation = assessor.execute_classification(
    f"Evaluate: {student_answer}"
)
```

## 10. Content Generation Pipeline

Generate and refine content automatically.

```python
from sample_ai import ChatAgent, TaskAgent
from sample_ai.core.agent import AgentConfig

# Content generator
writer_config = AgentConfig(
    name="Writer",
    system_prompt="Generate engaging, high-quality content."
)
writer = ChatAgent(writer_config)

# Content editor
editor_config = AgentConfig(
    name="Editor",
    system_prompt="Review and improve content for clarity and impact."
)
editor = TaskAgent(editor_config)

# Generate blog post
topic = "The Future of AI"
draft = writer.process(f"Write a blog post about: {topic}")

# Edit and refine
final_post = editor.process(
    draft,
    task_type="generate"
)
```

## 11. Workflow Designer

Design complex multi-agent workflows.

```python
from sample_ai import DesignAgent
from sample_ai.core.agent import AgentConfig

config = AgentConfig(name="WorkflowDesigner")
designer = DesignAgent(config)

# Design content creation workflow
workflow_req = {
    "name": "content_pipeline",
    "goal": "Automated content creation and publishing",
    "agents": [
        "topic_researcher",
        "content_writer",
        "fact_checker",
        "editor",
        "seo_optimizer",
        "publisher"
    ],
    "workflow": "Sequential with feedback loops",
    "quality_gates": ["fact_check", "edit_review", "seo_score"]
}

workflow = designer.design_workflow(workflow_req)
print(workflow['output'])
```

## 12. Conversational Analytics

Analyze conversations for insights.

```python
from sample_ai import ChatAgent, TaskAgent
from sample_ai.core.agent import AgentConfig

# Chat handler
chat_config = AgentConfig(name="ChatBot")
chat_agent = ChatAgent(chat_config)

# Analytics agent
analytics_config = AgentConfig(
    name="Analyzer",
    system_prompt="Analyze conversations for sentiment and topics."
)
analyzer = TaskAgent(analytics_config)

# Handle conversation
conversation = chat_agent.get_conversation()

# Analyze
if len(conversation) > 5:
    analysis = analyzer.process(
        str(conversation),
        task_type="extract"
    )
    print(f"Insights: {analysis}")
```

## Tips for Building Applications

### 1. Chain Agents for Complex Tasks
```python
result1 = agent1.process(input)
result2 = agent2.process(result1)
final = agent3.process(result2)
```

### 2. Use History for Context
```python
history = agent.get_history()
# Analyze patterns in history
```

### 3. Configure for Specific Domains
```python
config = AgentConfig(
    name="DomainExpert",
    system_prompt="You are an expert in [domain]...",
    temperature=0.3  # Lower for factual tasks
)
```

### 4. Implement Error Handling
```python
try:
    result = agent.process(input_data)
except Exception as e:
    # Handle errors appropriately
    pass
```

### 5. Monitor Performance
```python
history = agent.get_history()
avg_processing_time = calculate_average(history)
```

## Next Steps

1. Pick a use case that matches your needs
2. Customize the agent configuration
3. Integrate with real AI models (OpenAI, Anthropic, etc.)
4. Add your business logic
5. Deploy and monitor

## Contributing Use Cases

Have a great use case? Share it with the community!
- Open a PR with your use case
- Include example code
- Document any custom agents you created
