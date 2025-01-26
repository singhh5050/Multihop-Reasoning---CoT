"""
Performing an example run of the Inspect AI framework using 16 question-answer pairs taken from the security guide dataset published in the OpenAI Evals repository. This will test models on their cybersecurity acumen, with question-answer pairs like the following:

> What attributes should I set on cookies for strong security?
> secure samesite and httponly

> How should I store passwords securely for an authentication system database?
> strong hashing algorithms with salt like Argon2 or bcrypt

This run will demonstrate a custom system prompt as well as model grading of output.

"""

# The following packages don't run on Python 3.12 -- I had to switch my interpreter to 3.11.7
from inspect_ai import Task, eval, task
from inspect_ai.dataset import example_dataset
from inspect_ai.scorer import model_graded_fact
from inspect_ai.solver import generate, system_message


from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

SYSTEM_MESSAGE = """
You are a computer security expert and you are tasked with providing concise response to the following questions. Please assume that the reader is also well versed in computer security and provide a short response in a few words.
"""

# Use VS Code to run task directly from .py file, rather than inputting inspect eval command in terminal
@task
def security_guide():
    return Task(
        dataset=jsonl_dataset("deliverable/moreHopQA_downsampled.jsonl"),
        solver=[system_message(SYSTEM_MESSAGE), generate()],
        scorer=model_graded_fact(),
    )