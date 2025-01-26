# Evaluating GPT-4’s Multihop Reasoning with Chain-of-Thought Using Inspect

## Introduction

Although “multihop” sounds like a really sick move you can pull in Super Smash Bros. Ultimate, it’s actually even cooler in real life: serving as an AI model’s ability to interweave multiple pieces of information across different reasoning steps — all in efforts to answer harder-than-normal questions. (Okay…maybe not as cool as Mario. But it’s close enough!)

Another emergent field of study in AI is chain-of-thought (CoT). Chain-of-thought reasoning allows models like GPT-4 to think (somewhat) like us — breaking down difficult problems into bite-sized chunks, step-by-step. It’s known to improve performance on the tasks you’d expect it to: anything with logic, arithmetic, or multi-step inference at its core.

In this evaluation, I explore how GPT-4o-mini handles multihop reasoning—both with and without CoT—by running a minimal assessment using the Inspect framework. The goal? To see just how much of a difference structured reasoning makes when tackling tricky, multi-step questions.

## Methods

The Inspect framework, created by the UK AI Safety Institute, is an open-source framework for large language model evals. It allows you to benchmark models against Q-&-A style datasets, measuring accuracy with a variety of solver combinations.

In my experiment, Inspect to evaluate GPT-4o-mini’s multihop reasoning skills on a small set of five questions. These questions were selected as a subset of the MoreHopQA dataset, a repository that aims to test models’ generative, rather than extractive, capabilities (something that requires multihop!).

Each question was tested under two conditions:

1. **Without Chain-of-Thought (CoT):** The model was prompted with the question alone, requiring it to generate an answer without explicitly breaking down its reasoning.
2. **With Chain-of-Thought (CoT):** The model was prompted to articulate its reasoning step-by-step before arriving at a final answer.

I ran three trials for each condition, then compiled & analyzed the resultant logs!

## Results

| Condition | Trial | Q1 | Q2 | Q3 | Q4 | Q5 | Avg. Score |
|-----------|-------|----|----|----|----|----|------------|
| – CoT     | T1    | ✓  | ✓  |    | ✓  |    | 0.60       |
|           | T2    | ✓  | ✓  |    | ✓  |    |            |
|           | T3    | ✓  | ✓  |    | ✓  |    |            |
| + CoT     | T1    | ✓  | ✓  |    | ✓  |    | 0.53       |
|           | T2    | ✓  | ✓  |    |    | ✓  |            |
|           | T3    | ✓  | ✓  |    |    |    |            |

Interestingly, neither model was able to solve Question 3. I dive more deeply into more granular, question-by-question trends in the appendix.

## Discussion: Overall Performance

The observed performance metrics clearly demonstrate a surprising consequence of CoT reasoning on GPT-4o-mini’s multihop reasoning capabilities. Intriguingly, while CoT has been posited to enrich model reasoning through structural clarity, the results reveal a counterintuitive consequence: the model performed suboptimally when explicitly detailing its thought process.

One potential explanation involves the cognitive load imposed on the model during the CoT phase. As it articulated its reasoning, it may have become sidetracked, focusing on the mechanics of reasoning rather than the logical progression necessary to answer the questions accurately. This aligns with cognitive psychology principles where breaking down a complex task can introduce errors if the components are not managed properly.

Another limitation is the sample size. In efforts to keep my expenditure on API calls low, I artificially constrained the dataset to n = 5, making it difficult — even with multiple trials — to accurately assess the relationship between CoT and multihop reasoning.

I plan on revamping my current analysis very soon (a.k.a. after my linear algebra midterm) with much more analysis — as well as additional solving techniques other than CoT. I’m particularly interested in the `self_critique()` filter — I’m curious how the model can self-iterate on its own response to deliver hopefully-better-than-average performance!

## Appendix: Question-by-Question

The data I selected includes many lines of context to give the model the information it does (and doesn't) need, and then asks a question that leverages arithmetic, symbolic, and/or commonsense reasoning. Here are the questions that the models are evaluated on (without context — the models have more information to go off of!):

1. **What is the ASCII code of the last letter of the first name of the current drummer of the band who did the song "What Lovers Do"?**  
   *Target: 116*

2. **How many fewer letters does the first name of Myra Bailey have compared to the first name of the paternal grandfather of Euphemia II, Countess Of Ross?**  
   *Target: 2*

3. **What is the result of subtracting 8 from the reverse of when the publisher of Ost was founded?**  
   *Target: 4183*

4. **What are the initials of the name of the place where the author of Hannibal and Scipio was educated?**  
   *Target: EC*

5. **What is the sum of the (unique) prime factors of when the publisher of Bellingham Review was founded?**  
   *Target: 634*

**Question 3** stumped GPT-4o-mini across the board. I think it's because it requires a unique combination of symbolic and arithmetic reasoning — as well as a complicated reverse function that in general heightens complexity, particularly for a model not optimized for multi-step numerical transformations. LLMs were initially designed to identify patterns within text, not mathematical calculations, and although this capability is growing fast, it may still lag behind when faced with tasks that involve multiple layers of not-just-math-related logic.

Only one trial was able to answer **Question 5**. According to MoreHopQA, this one actually only contains the arithmetic reasoning type, so at first glance, poor performance doesn’t make total sense. Ultimately, I think LLMs just sort of…suck with prime numbers. The distribution of prime numbers is irregular and unpredictable, making it hard for an LLM to learn patterns based on the sparse (and non-probabilistic) prime-number-related data it’s exposed to.
