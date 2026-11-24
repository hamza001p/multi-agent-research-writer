from dotenv import load_dotenv
load_dotenv()
import os
from langchain.agents import create_agent
from langchain.tools import tool
from langchain.chat_models import init_chat_model
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate




@tool
def get_facts(topic: str) -> str:
    """Provides facts about a given topic."""
    facts = {
        "solar energy": "Solar energy is renewable and can be harnessed using solar panels.",
        "artificial intelligence": "Artificial intelligence is the simulation of human intelligence in machines.",

        "climate change": "Climate change refers to long-term shifts in temperatures and weather patterns.",
        "electric cars": "Electric cars are vehicles that run on electricity instead of gasoline.",
        "quantum computing": "Quantum computing uses quantum bits to perform complex calculations faster than classical computers.",
    }
    return facts.get(topic.lower(), "No facts available for this topic.")

model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)

researcher = create_agent(
    model=model,
    tools=[get_facts],
    system_prompt="Tum aik madadgar researcher ho",)


writer_model = init_chat_model(
    model="openai/gpt-oss-120b",
    model_provider="groq",
)


writer_prompt = ChatPromptTemplate.from_template(
    "tum aik madadgar writer ho, tum aik {topic} par article likho."
    "article ki length (3-4 lines) honi chahiye, aur article ka tone {tone} hona chahiye:/n/n{facts}")

writer_chain = writer_prompt | writer_model

topic = "solar energy"
# step A
research_result = researcher.invoke({
    "messages": [{"role": "user", "content": f"mujhe {topic} ke bare mein facts chahiye.in roman urdu"}]},
    )
facts_text = research_result["messages"][-1].content

# step B
final_paragraph = writer_chain.invoke({"facts": facts_text, "topic": topic, "tone": "informative"})

print(final_paragraph.content)

reviewer_chain = ChatPromptTemplate.from_template(
    "is paragraph ko check karo aur agar koi galti ho to usko correct karo, aur agar koi improvement ho to usko improve karo" 

    "kya ye clear or dilchasb hai:\n\n{paragraph}")

reviewer_chain = reviewer_chain | writer_model

feedback = reviewer_chain.invoke({"paragraph": final_paragraph.content})
print(feedback.content)