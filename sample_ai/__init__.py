"""
Sample.AI - An AI base agent model to build and design any AI app.

This package provides a flexible framework for creating and managing AI agents
that can be used to build various AI applications.
"""

from sample_ai.core.agent import BaseAgent
from sample_ai.core.model import AIModel
from sample_ai.agents.chat_agent import ChatAgent
from sample_ai.agents.task_agent import TaskAgent
from sample_ai.agents.design_agent import DesignAgent

__version__ = "0.1.0"
__all__ = [
    "BaseAgent",
    "AIModel",
    "ChatAgent",
    "TaskAgent",
    "DesignAgent",
]
