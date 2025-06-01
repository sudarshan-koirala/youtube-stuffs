# LiteLLM Integration Examples

This project demonstrates how to integrate various LLM providers (OpenAI, Groq, Ollama) using LiteLLM as a unified interface. It includes examples of direct API calls and using the LiteLLM proxy.

## Prerequisites

- Python 3.8+
- [uv](https://github.com/astral-sh/uv) - Fast Python package installer and resolver
- Ollama (for local LLM support)
- Required API keys from:
  - OpenAI
  - Groq
  - LangSmith (optional, for observability)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd litellm-crash-course
```

2. Install dependencies using uv:

```bash
uv sync # Creates virtual env and install all the packages
```

Or if you want to install the packages yourself, follow these steps.

```bash
# Create and activate virtual environment
uv venv
source .venv/bin/activate  # On Unix/macOS
.venv\Scripts\activate     # On Windows

# For adding new packages
uv add package_name    # Adds a single package
```

Note: `uv sync` ensures reproducible installations by using exact package versions, which is recommended for consistent development environments.

3. Set up environment variables:
```bash
cp env.example .env
```
Edit `.env` file and add your API keys:
```
OPENAI_API_KEY="your-openai-key"
GROQ_API_KEY="your-groq-key"
LANGSMITH_API_KEY="your-langsmith-key"  # Optional
```

## Features

- OpenAI API integration
- Groq API integration
- Ollama local LLM integration
- LiteLLM proxy setup and usage
- LangSmith integration for observability

## Usage

1. Open repo in vscode or your desired IDE

2. Open `different_llm_test.ipynb`

The notebook contains examples for:
- Using OpenAI's API
- Using Groq's API
- Using Ollama locally
- Using LiteLLM as a unified interface
- Setting up and using LiteLLM proxy
- Integrating with LangSmith for monitoring