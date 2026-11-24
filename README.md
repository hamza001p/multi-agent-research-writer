# Multi-Agent Research Writer

A multi-step AI workflow built using LangChain and Groq LLM. It uses three components: a Researcher Agent, Writer Chain, and Reviewer Chain to generate and review topic-based articles.

## Features

- Researcher Agent gathers relevant facts using custom tools.
- Writer Chain generates structured articles.
- Reviewer Chain reviews generated content.
- Sequential multi-step workflow.
- Prompt engineering with LangChain.
- Groq LLM integration.

## Workflow

1. **Researcher:** Collects facts about the given topic.
2. **Writer:** Uses the research to write an article.
3. **Reviewer:** Reviews the generated article and provides feedback.

## Technologies Used

- Python
- LangChain
- Groq LLM
- ChatPromptTemplate
- Python Dotenv

## Installation

1. Clone the repository:

```bash
git clone https://github.com/hamza001p/multi-agent-research-writer.git
```

2. Navigate to the project:

```bash
cd multi-agent-research-writer
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

5. Run the project:

```bash
python agent_team.py
```

## Note

This project demonstrates a sequential multi-agent-style workflow using LangChain chains and agents. It does not use LangGraph StateGraph.

## Author

Hamza Asif