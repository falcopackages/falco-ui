# List all available commands
_default:
    @just --list

@install:
    hatch run python --version

# Install dependencies
@bootstrap:
    uv sync

@clean:
    rm -rf .venv

# Run all formatters
@fmt:
    just --fmt --unstable
    uvx ruff --formatter
    uvx pyproject-fmt pyproject.toml
    # hatch run pre-commit run reorder-python-imports -a

@run-demo:
    cd demo && uv run python manage.py work

@run-dj *ARGS:
    cd demo && uv run python manage.py {{ ARGS }}