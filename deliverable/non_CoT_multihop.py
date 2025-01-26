"""
Performing an run of the Inspect AI framework using 5 question-answer pairs taken from the MoreHopQA: More Than Multi-hop Reasoning paper. This will test models on their ability to shift between arithmetic, symbolic, and commonsense reasoning.

The initial dataset is quite large, so in efforts to reduce API calls, I downsampled to 5 types of questions:
> Q1: Symbolic, Commonsense
> Q2: Commonsense, Arithmetic
> Q3: Symbolic, Arithmetic
> Q4: Purely Symbolic
> Q5: Purely Arithmetic

This run will demonstrate a custom system prompt as well as model grading of output. However, it DOES NOT include Chain of Thought reasoning. We have left out that solving process so that this can serve as a baseline.

"""

# don't forget: 
# pip install inspect-ai python-dotenv

# The following packages don't run on Python 3.12 -- I had to switch my interpreter to 3.11.7
from inspect_ai import Task, eval, task
from inspect_ai.scorer import model_graded_fact
from inspect_ai.solver import generate
from inspect_ai.dataset import json_dataset


from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Use VS Code to run task directly from .py file, rather than inputting inspect eval command in terminal
@task
def non_CoT_multihop():
    return Task(
        dataset=json_dataset("/Users/harshsingh/Desktop/Multihop Reasoning + CoT/deliverable/moreHopQA_downsampled.json"),
        solver=[generate()], # no CoT
        scorer=model_graded_fact(),
    )