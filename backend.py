from langchain_community.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from config import OPENROUTER_API_KEY, SYSTEM_PROMPT

def load_chain():
    llm = ChatOpenAI(
        temperature=0.5,
        openai_api_key=OPENROUTER_API_KEY,
        openai_api_base="https://openrouter.ai/api/v1",
        model="qwen/qwen3-235b-a22b-2507:free",
    )

    prompt = PromptTemplate(
        input_variables=["chat_history", "user_input"],
        template="""
{system_prompt}

### Recent History ###
{chat_history}

### Patient Input ###
{user_input}

### MediBuddy's Response:
"""
    )

    return LLMChain(
        llm=llm,
        prompt=prompt.partial(system_prompt=SYSTEM_PROMPT),
        verbose=False,
    )
