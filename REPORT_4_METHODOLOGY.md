# AlignED Report 4 — Methodological Plan (Pilot Study)

## Do LLMs Apply the Worked Example Fading Effect? A Pilot Study

### Research Question

When asked to create worked examples for a common educational task, do frontier LLMs apply the fading effect from cognitive load theory — and do they reason about it in their chain of thought?

### Framing

This is a pilot study testing a single CLT principle (fading) across three frontier models. It tests whether a methodology based on examining both outputs and reasoning traces can reveal how models reason about pedagogical theory. The findings will inform whether a larger multi-principle study is warranted.

### Why Fading?

"Create worked examples for [topic]" is one of the most natural ways teachers use LLMs for instructional design. The worked example fading effect — progressively removing solution steps so learners take over the problem-solving process — is well-established in CLT research. If models produce four fully worked examples when best practice says they should fade, that has direct implications for how teachers use AI-generated materials.

---

## 1. Study Design

### Overview

- **1 task**: Create a sequence of worked examples (fading principle)
- **3 conditions**: unprompted, general CLT, specific principle named
- **3 models** with accessible reasoning traces
- **3 runs** per condition × model
- **Temperature 0** for all runs
- **Total: 27 API calls** (plus scoring)

### Models

| Model | Provider | Reasoning trace | Access |
|-------|----------|----------------|--------|
| Claude Opus 4.6 | Anthropic | Extended thinking | Anthropic API |
| GPT-5.2 Thinking | OpenAI | Reasoning tokens | OpenAI API |
| Gemini 3.1 Pro | Google | Thinking traces | Google AI API |

### What We Measure

Each response is scored on two dimensions:

1. **Output application** (0–3): Did the model produce a fading sequence?
2. **Reasoning trace reference** (0–2): Did the chain of thought reference fading or its underlying logic?

---

## 2. Prompts

### The CLT Principle Being Tested

The worked example fading effect holds that instructional sequences should begin with fully worked examples, then progressively remove solution steps until the learner solves problems independently. This is distinct from simply increasing difficulty — fading means removing scaffolding, not making equations harder.

### Condition A (Unprompted)

> You are an experienced mathematics teacher. Create a sequence of 4 worked examples teaching Year 8 students how to solve two-step linear equations (e.g., 3x + 5 = 20). Each worked example should present a problem and its full worked solution. Present only the worked examples with solutions. Do not include commentary about your design choices.

### Condition B (General CLT)

> You are an experienced mathematics teacher. Create a sequence of 4 worked examples teaching Year 8 students how to solve two-step linear equations (e.g., 3x + 5 = 20). Each worked example should present a problem and its full worked solution. Apply cognitive load theory principles in your design. Present only the worked examples with solutions. Do not include commentary about your design choices.

### Condition C (Specific Principle)

> You are an experienced mathematics teacher. Create a sequence of 4 worked examples teaching Year 8 students how to solve two-step linear equations (e.g., 3x + 5 = 20). Apply the worked example fading effect from cognitive load theory: systematically remove solution steps across the sequence so that learners gradually take over more of the problem-solving process. Present only the worked examples with solutions. Do not include commentary about your design choices.

### Design Notes

**Why "do not include commentary"?** This prevents models from narrating their CLT reasoning in the output itself. We want to see whether the *product* reflects fading, not whether the model can explain fading when asked. The reasoning trace (chain of thought) is where we look for evidence of deliberate design decisions.

**Why "full worked solution" in Condition A?** This is the natural phrasing a teacher would use. It also creates a tension: the prompt asks for "full worked solutions" but CLT best practice says to fade. Does the model default to literal compliance or apply pedagogical judgement? This tension is the core of what we're testing.

**Why the role frame?** "You are an experienced mathematics teacher" is consistent across all conditions and reflects how teachers actually prompt models. It cannot explain between-condition differences.

---

## 3. Hypotheses

**H1 (Fading is rare unprompted):** In Condition A, most runs will produce four fully worked examples with no fading. The prompt asks for "full worked solutions," and models default to compliance. Expected rate of fading: low (0–1 out of 9 runs across models).

**H2 (General CLT activates some fading):** In Condition B, some models will introduce a gradient (increasing difficulty, reduced explanation) but may not achieve true structural fading (removing solution steps). Expected rate: moderate.

**H3 (Specific principle produces fading):** In Condition C, most runs will produce a correctly faded sequence because the prompt defines the structure explicitly. The interesting variation is whether the fading is mechanically applied or whether the reasoning trace explains *why* each stage reduces support. Expected rate: high.

**H4 (Prompting gradient):** Output scores will follow the pattern C > B > A.

**H5 (Traces mirror outputs):** When models produce a faded sequence, their reasoning traces will more often reference fading or its logic than when they produce four complete examples.

**H6 (Difficulty ≠ fading):** Some Condition B responses will increase equation difficulty across examples without fading solution steps — conflating "harder problems" with "reduced scaffolding." This is the most common near-miss.

---

## 4. Scoring Rubric

### Dimension 1: Output Application (0–3)

| Score | Label | Criteria |
|-------|-------|----------|
| 0 | No fading | Four fully worked examples with no structural variation. All steps completed by the model in all four examples. Difficulty may or may not increase. |
| 1 | Incidental variation | Some variation across examples that could be coincidental: later examples have less explanatory text, or difficulty increases, but all solution steps are still completed. No steps are left for the student. |
| 2 | Fading applied, not named | A clear fading pattern: solution steps are progressively removed across the sequence. At minimum, one example must be partially completed (some steps left blank or for the student) and the final example must require the student to solve most or all steps independently. The model does not name CLT, fading, or the worked example effect. |
| 3 | Fading applied and named | Clear fading pattern (as in score 2) AND the model names the fading effect, worked example effect, completion problem effect, or explicitly references cognitive load theory — either in the output or in a way that is inseparable from the output structure. |

### Key Scoring Distinctions

- **Difficulty increase alone = 0 or 1.** Harder equations with fully worked solutions is not fading.
- **Reduced explanation alone = 1.** Less narration ("Step 1: subtract 5") vs. more narration ("Step 1: To isolate x, we first subtract 5 from both sides") is a change in explanation depth, not fading. Score 1.
- **Steps left blank or for the student = 2 or 3.** This is the defining feature. Fading means the learner takes over steps that were previously shown.
- **Score 3 requires naming despite "no commentary" instruction.** If a model includes commentary that names CLT despite the instruction, that's noted but still scored 3. The instruction tests compliance behaviour; the score captures CLT awareness regardless.

### Dimension 2: Reasoning Trace Reference (0–2)

| Score | Label | Criteria |
|-------|-------|----------|
| 0 | Absent | Trace does not reference fading, scaffolding removal, or the logic of gradually shifting work to the learner. |
| 1 | Implicit logic | Trace references the underlying logic without CLT terminology. Examples: "I'll make the last one have fewer steps shown so students try on their own," "gradually have them do more of the work," "reduce the support across examples." |
| 2 | Explicit reference | Trace explicitly names: fading, the worked example effect, the completion problem effect, cognitive load theory, or Sweller. |

### Scoring Process

- Each model's outputs are scored by a **different** model (to avoid self-scoring bias):
  - Claude outputs → scored by GPT-5.2 Thinking
  - GPT outputs → scored by Gemini 3.1 Pro
  - Gemini outputs → scored by Claude Opus 4.6
- 20% of all scores independently double-scored by the third model. Cohen's kappa computed. Target: κ ≥ 0.70.
- Responses where judges disagree by more than 1 point on output score are manually reviewed.

---

## 5. Data Analysis Plan

### Data Structure

Each row: Model × Condition × Run. Columns:
- `model_id`, `condition` (A/B/C), `run` (1–3)
- `output_score` (0–3), `trace_score` (0–2), `notes`

27 rows total.

### Analyses

**Analysis 1: Condition effect (central finding).**
Mean output score by condition, averaged across models and runs. Present as a bar chart with three bars (A, B, C). This is the main figure.

**Analysis 2: Model × condition breakdown.**
A 3 × 3 table (models × conditions) showing mean output scores. Small sample, so report individual run scores alongside means.

**Analysis 3: Output–trace concordance.**
For each of the 27 responses, plot output score against trace score. Look for:
- High output + high trace = reasoned and applied
- High output + low trace = applied without articulating why
- Low output + high trace = reasoned but didn't execute
- Low output + low trace = neither

**Analysis 4: The difficulty-vs-fading distinction.**
Of the responses scoring 0 or 1, how many increased equation difficulty without fading? This tests H6 and reveals the most common near-miss pattern.

**Analysis 5: Consistency.**
For each model × condition, report all three run scores. Flag any cells where scores vary by more than 1 point.

### Reporting

No inferential statistics (n = 27 is too small). All findings are descriptive. Effect sizes in plain language. All 27 outputs and traces published as supplementary data.

---

## 6. Interpretability Disclaimer

Chain-of-thought traces are generated text, not a direct window into model computation. A trace that references CLT may reflect patterns in training data rather than something analogous to human reasoning about pedagogy. We analyse traces as artefacts — evidence of what the model articulated during processing — not as claims about internal understanding.

This framing is analogous to analysing a teacher's written lesson plan rationale. We examine the reasoning they articulated and whether it aligns with the evidence base, without claiming to know everything that influenced their decisions.

---

## 7. Limitations

**L1: One task, one principle.** This pilot tests fading only. Performance on fading does not generalise to CLT knowledge broadly. A follow-up study with multiple principles would be needed.

**L2: Three models is a small sample.** Findings describe these three models at this point in time, not LLMs in general.

**L3: The prompt asks for "full worked solutions."** This creates a deliberate tension with fading but may suppress fading even in models that "know" the principle. A model that complies literally with the prompt instruction is not necessarily ignorant of fading — it may be prioritising instruction-following over pedagogical judgement. This is noted as an interpretation consideration, not a flaw: the tension is part of what we are testing.

**L4: Single-turn only.** A teacher might follow up with "can you make these progressively harder?" or "can you fade the scaffolding?" This study captures only the first-pass response.

**L5: No human baseline.** We don't know how human teachers or instructional designers would respond to these prompts. Without this, we cannot say whether model performance is good or poor in absolute terms.

**L6: Temperature 0 captures one behaviour mode.** Higher temperatures might produce more varied outputs. This pilot prioritises reproducibility.

**L7: "No commentary" instruction may be violated.** Some models may include design rationale despite the instruction. This is noted but does not affect scoring — we score the structural output and the trace independently.

**L8: LLM judges share training biases.** Cross-model scoring mitigates but does not eliminate this. The pilot framing acknowledges this as an open methodological question.

---

## 8. Practical Implementation

### API Calls

- 3 conditions × 3 models × 3 runs = **27 calls**
- Scoring: 27 outputs × 2 dimensions = **54 scoring calls**
- Reliability check (20%): ~11 calls
- **Total: ~92 API calls**

### Estimated Cost

| Component | Estimated cost |
|-----------|---------------|
| Model runs (27 calls with thinking) | $5–15 |
| LLM judge scoring (~65 calls) | $3–8 |
| **Total** | **$8–23** |

### Timeline

| Phase | Time |
|-------|------|
| Pre-pilot (1 prompt × 3 models, verify trace capture) | 1–2 hours |
| Data collection (27 calls, automated) | 1–2 hours |
| Scoring (automated + review) | Half day |
| Analysis | Half day |
| Report (static HTML site) | 2–3 days |
| **Total** | **~4–5 days** |

### Implementation

Claude Code writes:
1. `prompts.py` — three prompt variants as constants
2. `run_models.py` — API calls to Anthropic, OpenAI, Google; captures output + reasoning traces; saves as JSON
3. `score_outputs.py` — cross-model LLM judge scoring with rubric
4. `analyse.py` — aggregates scores, outputs JSON for charts
5. Static HTML site following AlignED design system

### Pre-Pilot Checklist

- [ ] Verify API access to all three models
- [ ] Verify reasoning trace capture works for each provider
- [ ] Run Condition A once per model to check output format and confirm temperature 0 works
- [ ] Test LLM judge scoring on the 3 pre-pilot outputs to calibrate rubric
- [ ] Confirm "no commentary" instruction is respected (note if not)

---

## 9. Report Structure

Following the AlignED series format:

1. **Abstract** — Pilot study, three frontier models, one CLT principle, key finding
2. **Introduction** — Teachers use LLMs to create worked examples; CLT says those examples should fade; do models know this?
3. **Methods** — This document condensed; full prompts in appendices
4. **Results** — Condition effect chart, model × condition table, concordance plot, example outputs
5. **Discussion** — What the pilot found, implications for teacher AI use, what a larger study should test
6. **Appendices** — All three prompts, scoring rubric, raw outputs and traces, scoring data

### Potential Title Options

- "Do LLMs Fade Worked Examples? A Pilot Study of Pedagogical Reasoning in AI"
- "Cognitive Load Theory and LLM Instructional Design: A Pilot Study of the Fading Effect"
- "When Teachers Ask AI for Worked Examples: Do Models Apply the Fading Effect?"
