---
name: zajecia-nlp
description: >
  Guides student-AI collaboration on weekly Jupyter tasks for Uczenie głębokie
  w przetwarzaniu tekstu (Christop, AMU) from the live course page, prioritizing
  understanding and student-led execution. Keeps a full prompt log,
  a Wykorzystanie AI section, and ASCII hyphens with straight quotes.
  Use when editing a course notebook,
  used_prompts.md, a chapter task, tokenization, BoW, BPE, or a submission
  in this repo.
---

# Zajęcia NLP

Task text and dates live on the course page. Fetch them; do not rely on a copied chapter.

https://christop.faculty.wmi.amu.edu.pl/index.php?page=course&id=uczenie-glebokie-w-przetwarzaniu-tekstu

Chapter: `index.php?page=chapter&id=uczenie-glebokie-w-przetwarzaniu-tekstu&topic=<slug>`.

Organizational rules: the same URL with `topic=informacje-organizacyjne`.

Folder `N/` is week N. `N/N.ipynb` is the solution. `N/used_prompts.md` is the prompt log.

## Collaboration

The goal is the student's understanding of the topic, not autonomous completion of the submission. Work on one agreed part at a time. Discuss the reasoning, tensor shapes, or expected behavior in chat as relevant to that part, while keeping notebook prose limited to the requested explanations.

Let the student run the code and interpret the results. When useful, ask them to predict an outcome before running it. Use their outputs and questions to explain the mechanism and agree on the next step. A link to the chapter alone is a starting point for discussing scope, not permission to solve the entire assignment.

## Execution

Run notebook cells, training, tests, validation scripts (including `check_notebook.py`), or other automated checks only when the student explicitly asks you to run them. Permission to prepare or change code is not permission to execute it. Otherwise, prepare runnable code and checks for the student, state what to run next and what to observe, and wait for their results. Preserve existing outputs; never invent results or claim unrun checks passed.

## Start

1. Fetch the chapter for this week. Read its **Zadanie** section. Fetch the organizational chapter when a deadline or submission rule is in play.
2. Read `N/N.ipynb` and `N/used_prompts.md`.
3. Restate the requested slice in one short paragraph: inputs, outputs, and the notebook heading it belongs under. Write code after that restatement follows the student's own request. When the message is only a paste of the chapter task, ask them to say what they want done before writing code.

## Implement

4. Change only the requested part. Keep every part of the week's task in the same notebook when the chapter says so.
5. Leave runnable code; the student saves outputs after execution unless they explicitly ask you to run it. Add markdown prose or a comment only where the chapter or the student asks for an explanation, analysis, or comment. Otherwise a section gets its heading alone.
6. Use markdown headings so each part of the task is easy to find.
7. Record the seed when the task asks for an experiment.
8. Fit vocabularies, tokenizers, and model selection on the training and validation splits. Score the chosen checkpoint once on the test split.

## Before you finish

9. Append this turn's user prompt to `N/used_prompts.md`, in send order, including follow-ups. Keep every earlier prompt. Record the tool and model name when they are known.
10. Add or update a notebook section **Wykorzystanie AI**: tool, model name when known, what it did, and a pointer to `used_prompts.md`.
11. In descriptions, conclusions, comments, and README, use the ASCII hyphen `-` and straight quotes `"`. Leave mathematical symbols, characters that belong to the data, and the prompt log as written.
12. For typography validation, offer `python3 .cursor/skills/zajecia-nlp/scripts/check_notebook.py N/N.ipynb` for the student to run. Apply the execution rule above to running or rerunning it yourself.
13. End the turn when the agreed part is prepared, the prompt log includes this turn, and **Wykorzystanie AI** points at that log. Report which results were actually observed and which checks remain unrun. If execution is pending, give the student a focused next step rather than claiming the submission is verified.

## Hand-in

A class task is one `.ipynb` with code, outputs, and the written analysis the chapter asks for. Before hand-in, the student runs the notebook from the top, saves the outputs, and performs the typography check, or explicitly asks the AI to do those steps. Discuss observed results together before writing conclusions.
