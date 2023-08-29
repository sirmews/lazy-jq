import os

import openai
from dotenv import load_dotenv
from langchain import PromptTemplate
from langchain.callbacks import get_openai_callback
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from typer import Argument, Option, Typer

load_dotenv()

app = Typer()

def count_tokens(chain, query, show_tokens: bool):
    with get_openai_callback() as cb:
        result = chain.run(query)
        if show_tokens:
            print(f'Spent a total of {cb.total_tokens} tokens')
    return result

@app.command()
def generate_script(text: str = Argument(..., help="The text used to generate the bash script."),
                     show_tokens: bool = Option(False, help="Display the number of tokens used.")):
    template = """
    You are a general purpose tool that parses input and generates output that can be 
    piped into command line tools, such as awk, sed, grep, etc.
    The question is: {question}.
    Return a response suitable for stdout.
    """
    # Initialize OpenAI API key from environment variable
    api_key = os.getenv("OPEN_AI_KEY")
    if not api_key:
        print("Error: OpenAI API key not found in environment variables.")
        return

    prompt = PromptTemplate(template=template, input_variables=["question"])

    # Initialize OpenAI LLM
    llm = OpenAI(openai_api_key=api_key, temperature=0)

    chain = LLMChain(prompt=prompt, llm=llm, verbose=False)
    response = count_tokens(chain, {'question': text}, show_tokens)
    print(response)

if __name__ == "__main__":
    app()
