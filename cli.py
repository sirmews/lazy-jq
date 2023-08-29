import os

import openai
from dotenv import load_dotenv
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from typer import Argument, Typer

load_dotenv()

app = Typer()


@app.command()
def generate_script(text: str = Argument(..., help="The text used to generate the bash script.")):
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
    print(chain.run(text))

if __name__ == "__main__":
    app()
