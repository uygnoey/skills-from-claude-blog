# What the model setting actually changes

The model setting swaps **which set of frozen weights** handles your request. Understanding what
that means makes both dials stop feeling like magic.

## 1. Everything becomes one request

When you press enter, Claude Code assembles your message together with the system prompt, tool
definitions, your `CLAUDE.md`, the conversation history, and any files in context. All of it is
sent as **one request** to the API.

## 2. Tokenization

The model never sees that as plain text. The first thing that happens on the server is
tokenization: the text is split into pieces, and each piece is mapped to an integer from a fixed
vocabulary the model was trained with. `const` might map to `1978`; `await` might map to `4293`.
From here on, your prompt is an array of integers.

## 3. Prediction

The model's job is to take that array and predict which token comes next. It computes a
probability for every token in its vocabulary and picks from the top. After `const x = await`, a
well-trained model puts high probability on `fetch` (very likely) and near-zero on `banana` (not
likely at all).

## 4. The weights

What turns your input tokens into those probabilities is the **weights** (also called
parameters): billions of numbers organized into large matrices. To predict one token, the model
runs your input through those matrices — a long chain of matrix multiplications — and reads the
probabilities at the end.

**The weights are where everything the model "knows" lives.** They are set during training, and
by the time you're sending requests they are read-only. Nothing in your prompt, your `CLAUDE.md`,
or your context changes them. (That is all the word *inference* means: using the model after
training is done, with the weights fixed.)

## 5. Steering is not teaching

Everything Claude knows about TypeScript, popular frameworks, idiomatic Go, or any other general
programming knowledge was encoded into those weights at training time.

Your prompt and context can still **steer** the prediction — putting your real code in front of
Claude is steering, and it works really well — but they don't add anything to the weights
themselves.

If a library didn't exist when the model was trained, it isn't in the weights. You can put the
docs in context and Claude will use them, but that's steering, not teaching: the response is
influenced for that request only, and the underlying model has not retained the information.

**This is also what a hallucination is.** When Claude confidently calls an API that doesn't
exist, that's the weights producing a token sequence that *looks plausible* from training
patterns — not a failed lookup.

## 6. One token at a time

The model doesn't generate a whole answer at once. It predicts one token, appends it to the
sequence, and runs the whole computation again to get the next one. **A 200-token response is 200
separate passes through the weights.** This loop is where most of your wait time and your output
cost come from.

## What this means for the two settings

- The **model setting** decides which weights handle your request, and what each output token
  costs.
- It does **not** decide how many tokens get generated. That number varies a lot for the same
  prompt, depending on how much work Claude decides to do.
- **How much work Claude decides to do is what the effort level controls.**

## Source

["Choosing a Claude model and effort level in Claude Code"](https://claude.com/blog/claude-model-and-effort-level-in-claude-code)
