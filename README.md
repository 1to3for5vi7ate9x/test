# test

## Project Type: basic

## Setup Instructions

### 1. Activate the Environment

This project uses Poetry for dependency management.

To activate the Poetry shell (virtual environment):
```bash
poetry shell
```

Alternatively, you can run commands within the Poetry environment:
```bash
poetry run python src/main.py
poetry run pytest
```

On Windows, you can also use:
```powershell
poetry run python src\main.py
poetry run pytest
```

To deactivate the Poetry shell:
```bash
exit
```

### 2. Install Dependencies

Poetry manages dependencies automatically. To install all dependencies:
```bash
poetry install
```

To add new dependencies:
```bash
# Add a runtime dependency
poetry add package-name

# Add a development dependency
poetry add --group dev package-name
```

### 3. Project Structure

```
test/
├── src/              # Source code
│   ├── __init__.py
│   └── main.py
├── tests/            # Test files
│   └── __init__.py
├── data/             # Data files (gitignored)
├── notebooks/        # Jupyter notebooks
├── pyproject.toml    # Project configuration and dependencies
├── README.md         # This file
└── .gitignore       # Git ignore rules
```

### 4. Running the Project

```bash
python src/main.py
```

### 5. Development

To run tests:
```bash
pytest tests/
```

To format code:
```bash
black src/ tests/
```

To check code style:
```bash
flake8 src/ tests/
```

To check types:
```bash
mypy src/
```

### 6. Managing Dependencies with Poetry

```bash
# Show all installed packages
poetry show

# Show dependency tree
poetry show --tree

# Update dependencies
poetry update

# Export dependencies to requirements.txt (if needed)
poetry export -f requirements.txt -o requirements.txt

# Build the project
poetry build

# Publish to PyPI (for library projects)
poetry publish
```

### 7. Poetry Virtual Environment

```bash
# Show info about the virtual environment
poetry env info

# List all virtual environments
poetry env list

# Remove the virtual environment
poetry env remove python3.11
```
