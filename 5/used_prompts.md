# Użyty skill (zajecia-nlp)

```markdown
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
```

# Prompty

```text
tool: OpenCode (OpenChamber)
model: GPT-6.1 Sol (github-copilot/gpt-6.1-sol)
/zajecia-nlp https://christop.faculty.wmi.amu.edu.pl/index.php?page=chapter&id=uczenie-glebokie-w-przetwarzaniu-tekstu&topic=architektura-transformer
```

```text
tool: OpenCode (OpenChamber)
model: GPT-6.1 Sol (github-copilot/gpt-6.1-sol)
ok
```

```text
tool: OpenCode (OpenChamber)
model: GPT-6.1 Sol (github-copilot/gpt-6.1-sol)
zmien skill aby nie uruchamial automatycznie testow, ma polegac on na wspolpracy miedzy studentem a AI i celem jest zrozumienie zagadnienia
```

```text
tool: OpenCode (OpenChamber)
model: GPT-6.1 Sol (github-copilot/gpt-6.1-sol)
ok wiec zresetuj teraz i dawaj
```

```text
tool: OpenCode (OpenChamber)
model: GPT-6.1 Sol (github-copilot/gpt-6.1-sol)
Odpowiedź na pytanie o zakres resetu: Notebook 5 od początku
```

```text
tool: OpenCode (OpenChamber)
model: GPT-6.1 Sol (github-copilot/gpt-6.1-sol)
nie mam pojcia, ale uruchomilem komorke
```

```text
tool: OpenCode (OpenChamber)
model: GPT-6.1 Sol (github-copilot/gpt-6.1-sol)
2x [x, x, x], gdzie x = [c, c, c, c]?
```

```text
tool: OpenCode (OpenChamber)
model: GPT-6.1 Sol (github-copilot/gpt-6.1-sol)
ok, co dalej?
```

```text
tool: OpenCode (OpenChamber)
model: GPT-6.1 Sol (github-copilot/gpt-6.1-sol)
ok
```

```text
tool: OpenCode (OpenChamber)
model: GPT-6.1 Sol (github-copilot/gpt-6.1-sol)
pierwszy?
```

```text
tool: OpenCode (OpenChamber)
model: GPT-6.1 Sol (github-copilot/gpt-6.1-sol)
Kształt K po transpozycji: (2, 2, 3)
Kształt dopasowań: (2, 3, 3)
Iloczyny skalarne dla pierwszej sekwencji:
 tensor([[17.2498,  4.6220, -3.3278],
        [ 0.3686,  0.6396, -0.0227],
        [-0.3457,  0.7831,  0.1452]])
Skalowane dopasowania dla pierwszej sekwencji:
 tensor([[12.1975,  3.2683, -2.3531],
        [ 0.2607,  0.4523, -0.0160],
        [-0.2444,  0.5538,  0.1026]])
Dopasowania zapytania pierwszego tokenu do trzech kluczy: tensor([12.1975,  3.2683, -2.3531])
Iloczyn q_0 i k_0 policzony osobno: tensor(17.2498)
```

```text
tool: OpenCode (OpenChamber)
model: GPT-6.1 Sol (github-copilot/gpt-6.1-sol)
Ok wygląda prawidłowego
```

```text
tool: OpenCode (OpenChamber)
model: GPT-6.1 Sol (github-copilot/gpt-6.1-sol)
ok
```

```text
tool: OpenCode (OpenChamber)
model: GPT-6.1 Sol (github-copilot/gpt-6.1-sol)
oki
```

```text
tool: OpenCode (OpenChamber)
model: GPT-6.1 Sol (github-copilot/gpt-6.1-sol)
dodaj used prompts do aktualnego pliku na koncu
```

```text
tool: OpenCode (OpenChamber)
model: GPT-6.1 Sol (github-copilot/gpt-6.1-sol)
oraz sprawdz notebook
```

```text
tool: OpenCode (OpenChamber)
model: GPT-6.1 Sol (github-copilot/gpt-6.1-sol)
chdozilo mi pythonem
```

```text
tool: OpenCode (OpenChamber)
model: GPT-6.1 Sol (github-copilot/gpt-6.1-sol)
w skillu jest tscrpt
```

```text
tool: Antigravity
model: Gemini 3.8 Flash
continue on 5 where we have finished
```

```text
tool: Antigravity
model: Gemini 3.8 Flash
i think we're overcomplicating the 2nd section. Should take way less code blocks. We already have 5 where most of the code is printing stuff. Please fall back to the notes and let's redo this part: Zaimplementuj skalowane iloczyny zapytań i kluczy, opcjonalną maskę dodawaną przed softmaxem, softmax po osi kluczy oraz mnożenie przez 
V
V. Możesz używać podstawowych operacji tensorowych i gotowego softmaxu. Zwracaj zarówno wyjście, jak i wagi atencji.
Wypisz kształty - 
Q
Q i 
K
K mają 
batch
×
n
×
d
k
batch×n×d 
k

 , 
V
V ma 
batch
×
n
×
d
v
batch×n×d 
v

 , wagi mają 
batch
×
n
×
n
batch×n×n, a wyjście 
batch
×
n
×
d
v
batch×n×d 
v

 . Transponuj w 
K
K tylko dwie ostatnie osie, pozostawiając batch na miejscu. Sprawdź także przypadek, w którym 
d
v
d 
v

  różni się od 
d
k
d 
k

 .
Odtwórz przykład z trzema pozycjami i jednostkowymi projekcjami. Porównaj otrzymane dopasowania, wagi i wyjście z przykładem w notatkach.
Dodaj maskę przyczynową. Sprawdź, czy wagi ponad przekątną są zerowe i czy wynik pierwszej pozycji jest równy jej wartości. Zmień ostatni wiersz wejścia - wyniki wcześniejszych pozycji jednej maskowanej głowy nie powinny się zmienić.
Dodaj maskę paddingu. Sprawdź zerowe wagi zamaskowanych kluczy oraz to, że zmiana wartości na tych pozycjach nie zmienia wyjść prawidłowych zapytań. Dla każdego prawidłowego wiersza suma wag powinna wynosić około 1. Nie podawaj do softmaxu wiersza bez ani jednego dozwolonego klucza.
```

```text
tool: Antigravity
model: Gemini 3.8 Flash
ok
```

```text
tool: Antigravity
model: Gemini 3.8 Flash
ok to teraz dodaj maske przyczynowa
```

```text
tool: Antigravity
model: Gemini 3.8 Flash
Wyczyscilem kod troche z niepotrzebnych printów, do czego służą te dwa? Co one mają pokazać? print("Wcześniejsze pozycje niezmienione po zmianie ostatniego wiersza:", torch.allclose(causal_output[:, :-1], causal_output_mod[:, :-1]))
print("Ostatnia pozycja zmieniona:", not torch.allclose(causal_output[:, -1], causal_output_mod[:, -1])). Btw. czy rozważyliśmy przypadek w którym Sprawdź także przypadek, w którym 
d
v
d 
v

  różni się od 
d
k
d 
k

 .
?
```

```text
tool: Antigravity
model: Gemini 3.8 Flash
1. w takim razie wyprintuj te zmienione wagi zamiast sprawdzać za mnie 2. ok
```

```text
tool: Antigravity
model: Gemini 3.8 Flash
zembeduj uzyty skill do zadania w sekcji used prompts
```
