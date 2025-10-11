"""Configuration loading and saving utilities."""

import json
import yaml
from pathlib import Path
from typing import Any, Dict, Union


def load_config(filepath: Union[str, Path]) -> Dict[str, Any]:
    """
    Load configuration from a file.
    
    Supports JSON and YAML formats based on file extension.
    
    Args:
        filepath: Path to the configuration file
        
    Returns:
        Configuration dictionary
        
    Raises:
        ValueError: If file format is not supported
        FileNotFoundError: If file doesn't exist
    """
    filepath = Path(filepath)
    
    if not filepath.exists():
        raise FileNotFoundError(f"Configuration file not found: {filepath}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        if filepath.suffix in ['.yaml', '.yml']:
            return yaml.safe_load(f)
        elif filepath.suffix == '.json':
            return json.load(f)
        else:
            raise ValueError(f"Unsupported file format: {filepath.suffix}")


def save_config(config: Dict[str, Any], filepath: Union[str, Path]) -> None:
    """
    Save configuration to a file.
    
    Supports JSON and YAML formats based on file extension.
    
    Args:
        config: Configuration dictionary to save
        filepath: Path where to save the configuration
        
    Raises:
        ValueError: If file format is not supported
    """
    filepath = Path(filepath)
    
    # Create parent directories if they don't exist
    filepath.parent.mkdir(parents=True, exist_ok=True)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        if filepath.suffix in ['.yaml', '.yml']:
            yaml.safe_dump(config, f, default_flow_style=False, sort_keys=False)
        elif filepath.suffix == '.json':
            json.dump(config, f, indent=2)
        else:
            raise ValueError(f"Unsupported file format: {filepath.suffix}")
