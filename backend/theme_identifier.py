from langchain_groq import ChatGroq
from backend.config import GROQ_API_KEY

# Initialize the LLM
llm = ChatGroq(model="llama-3.3-70b-versatile", api_key=GROQ_API_KEY)

def identify_themes(responses):
    theme_prompt = """
    Based on the following answers, extract common themes and summarize each theme clearly with supporting examples.
    Answers:
    {}

    Provide the result in bullet points with short titles.
    """.format("\n\n".join(responses))
    return llm.invoke(theme_prompt)
