# Contributing to Sample.AI

Thank you for your interest in contributing to Sample.AI! This document provides guidelines for contributing to the project.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/sample.ai.git`
3. Create a new branch: `git checkout -b feature/your-feature-name`
4. Install dependencies: `pip install -e .`

## Development Setup

### Prerequisites

- Python 3.8 or higher
- pip

### Installation

```bash
pip install -e .
pip install -r requirements.txt
```

## Making Changes

### Code Style

- Follow PEP 8 Python style guidelines
- Use type hints for function parameters and return values
- Write docstrings for all public classes and methods
- Keep functions focused and modular

### Testing

Run tests before submitting:

```bash
python tests/test_agents.py
```

Or with pytest if available:

```bash
pytest tests/
```

### Adding New Features

1. Create a new branch for your feature
2. Implement the feature with appropriate tests
3. Update documentation
4. Ensure all tests pass
5. Submit a pull request

## Types of Contributions

### Bug Fixes

- Check if the bug is already reported in Issues
- Create a new issue if needed
- Submit a PR with the fix and test case

### New Features

- Discuss the feature in an issue first
- Implement the feature
- Add tests and documentation
- Submit a PR

### Documentation

- Fix typos or clarify existing documentation
- Add examples
- Improve code comments

### Examples

- Add new usage examples
- Improve existing examples
- Add real-world use cases

## Pull Request Process

1. Update README.md with details of changes if applicable
2. Update examples if your changes affect usage
3. Add tests for new functionality
4. Ensure all tests pass
5. Update version numbers if applicable
6. Submit the PR with a clear description

## Code Review Process

- PRs require review before merging
- Address review comments
- Keep PRs focused and atomic

## Community Guidelines

- Be respectful and constructive
- Help others learn and grow
- Follow the code of conduct

## Questions?

Feel free to open an issue for questions or discussions.

Thank you for contributing!
