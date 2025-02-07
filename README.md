# My Python Project

This is a demo project showing how to use Codegen to automatically add documentation to Python functions.

## Features

- Automatic docstring generation for Python functions
- Example functions demonstrating price calculation and input validation
- Integration with Codegen for code automation

## Project Structure

- `example.py`: Contains example Python functions with auto-generated documentation
- `.codegen/`: Contains Codegen configuration and custom code transformations

## Getting Started

1. Install the required tools:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv tool install codegen
```

2. Initialize Codegen in your project:
```bash
codegen init
```

3. Run the docstring generation:
```bash
codegen run add-docstrings
```
