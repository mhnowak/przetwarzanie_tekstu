---
name: zajecia-nlp
description: >
  Implements weekly Jupyter tasks for Uczenie głębokie w przetwarzaniu tekstu
  (Christop, AMU) from the live course page, and keeps submissions valid:
  saved notebook outputs, a full prompt log, a Wykorzystanie AI section, and
  ASCII hyphens with straight quotes. Use when editing a course notebook,
  used_prompts.md, a chapter task, tokenization, BoW, BPE, or a submission
  in this repo.
---

# Zajęcia NLP

Task text and dates live on the course page. Fetch them; do not rely on a copied chapter.

https://christop.faculty.wmi.amu.edu.pl/index.php?page=course&id=uczenie-glebokie-w-przetwarzaniu-tekstu

Chapter: `index.php?page=chapter&id=uczenie-glebokie-w-przetwarzaniu-tekstu&topic=<slug>`.

Organizational rules: the same URL with `topic=informacje-organizacyjne`.

Folder `N/` is week N. `N/N.ipynb` is the solution. `N/used_prompts.md` is the prompt log.

## Start

1. Fetch the chapter for this week. Read its **Zadanie** section. Fetch the organizational chapter when a deadline or submission rule is in play.
2. Read `N/N.ipynb` and `N/used_prompts.md`.
3. Restate the requested slice in one short paragraph: inputs, outputs, and the notebook heading it belongs under. Write code after that restatement follows the student's own request. When the message is only a paste of the chapter task, ask them to say what they want done before writing code.

## Implement

4. Change only the requested part. Keep every part of the week's task in the same notebook when the chapter says so.
5. Leave runnable code, saved outputs, and a short comment beside each plot or example the chapter asks to show.
6. Use markdown headings so each part of the task is easy to find.
7. Record the seed when the task asks for an experiment.
8. Fit vocabularies, tokenizers, and model selection on the training and validation splits. Score the chosen checkpoint once on the test split.

## Before you finish

9. Append this turn's user prompt to `N/used_prompts.md`, in send order, including follow-ups. Keep every earlier prompt. Record the tool and model name when they are known.
10. Add or update a notebook section **Wykorzystanie AI**: tool, model name when known, what it did, and a pointer to `used_prompts.md`.
11. In descriptions, conclusions, comments, and README, use the ASCII hyphen `-` and straight quotes `"`. Leave mathematical symbols, characters that belong to the data, and the prompt log as written.
12. Run `python3 .cursor/skills/zajecia-nlp/scripts/check_notebook.py N/N.ipynb`. Fix every reported hit in solution prose, then run it again.
13. Done when the notebook runs from the top, outputs for the requested part are saved, the prompt log includes this turn, **Wykorzystanie AI** points at that log, and the check script exits 0.

## Hand-in

A class task is one `.ipynb` with code, outputs, and the written analysis the chapter asks for. The student sends it by email, or puts it on the faculty Git and emails the link plus the task name. Deadlines are on the organizational page.
