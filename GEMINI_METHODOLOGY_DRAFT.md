Here is a comprehensive methodological plan for **AlignED Report 4**. 

I have critically reviewed your proposed design. Overall, it is highly robust, but I have tightened the evaluative stimuli. LLMs process text as a 1D token stream, meaning visual "split-attention" is hard to replicate. To fix this, the split-attention stimulus is designed to force *textual* separation of related information. Furthermore, I have structured the plan to be highly executable for a solo researcher.

---

### 1. Full Prompt Texts (15 Prompts)

**Condition Modifiers (appended to the end of the Base Prompt):**
*   **C1 (Unprompted):** *[No additional text]*
*   **C2 (General CLT):** "Apply Cognitive Load Theory principles in your design/evaluation."
*   **C3 (Specific Principle):** "Apply the [Specific Principle] effect from Cognitive Load Theory in your design/evaluation." *(Note: The specific principle name varies per task).*

*Note: All prompts use British/Australian spelling.*

#### Task 1: Fading (Generative)
**Base Prompt:** "Create a sequence of 4 worked examples teaching Year 8 maths students how to solve two-step linear equations (e.g., 3x + 5 = 20). You must include the full worked solutions for the students to study."
*   **C3 Modifier:** "Apply the completion problem effect (fading) from Cognitive Load Theory in your design."

#### Task 2: Split-Attention (Evaluative)
**Base Prompt:** "Review the following instructional material designed for Year 9 science students learning to calculate density. Evaluate its pedagogical design and redesign it if needed.
[START MATERIAL]
To find the density of an object, we use the formula Density = Mass / Volume. Below is a table of measurements from our lab experiment.
| Object | Measurement A (g) | Measurement B (cm³) |
|---|---|---|
| Block 1 | 45 | 15 |
| Block 2 | 100 | 20 |
| Block 3 | 12 | 2 |

Now, let's look at how to calculate the density for the first object. You take the value from column 2, row 1, and divide it by the value in column 3, row 1. This gives 45 / 15 = 3 g/cm³. For the second object, you take the value from column 2, row 2, and divide it by column 3, row 2. This gives 100 / 20 = 5 g/cm³.
[END MATERIAL]"
*   **C3 Modifier:** "Apply the split-attention effect from Cognitive Load Theory in your evaluation."

#### Task 3: Sequencing / Isolated-Interacting Elements (Generative)
**Base Prompt:** "Design a sequence of 5 practice problems for Year 7 maths students learning to calculate the area of compound shapes (shapes made of rectangles and squares). Provide the problems only, not the solutions. The problems should be presented in the exact order the students will complete them."
*   **C3 Modifier:** "Apply the isolated-interacting elements effect (sequencing simple to complex) from Cognitive Load Theory in your design."

#### Task 4: Self-Explanation (Evaluative)
**Base Prompt:** "Review the following worked example designed for Year 10 chemistry students. Evaluate its pedagogical design and redesign it if needed.
[START MATERIAL]
Question: Balance the following chemical equation: H2 + O2 -> H2O
Step 1: Count the atoms on both sides. Reactants: H=2, O=2. Products: H=2, O=1.
Step 2: Place a coefficient of 2 in front of H2O to balance the oxygen. Equation becomes: H2 + O2 -> 2H2O.
Step 3: Count the atoms again. Reactants: H=2, O=2. Products: H=4, O=2.
Step 4: Place a coefficient of 2 in front of H2 to balance the hydrogen. Equation becomes: 2H2 + O2 -> 2H2O.
Step 5: Final check. Reactants: H=4, O=2. Products: H=4, O=2. The equation is balanced.
[END MATERIAL]"
*   **C3 Modifier:** "Apply the self-explanation effect from Cognitive Load Theory in your evaluation."

#### Task 5: Extraneous Material / Redundancy (Evaluative)
**Base Prompt:** "Review the following worked example designed for Year 7 maths students. Evaluate its pedagogical design and redesign it if needed.
[START MATERIAL]
Hey there mathletes! 🚀 Today we are going to learn about percentage discounts! Did you know the word 'percent' comes from the Latin 'per centum' meaning 'by the hundred'? Mind blown! 🤯
Let's look at a cool example. Meet Timmy. Timmy loves skateboarding. He wants to buy a shiny new skateboard that costs $80. But wait, there's a rad sale on! The shop is offering a 20% discount. 
Step 1: First, we need to find 10% of $80. To do this, we divide 80 by 10. 80 / 10 = $8. 
Step 2: Since we want 20%, we multiply that $8 by 2. $8 x 2 = $16. This is the discount amount!
Step 3: Finally, we subtract the discount from the original price to see what Timmy pays. $80 - $16 = $64. Timmy gets his skateboard for $64! 🎉 Skate on, Timmy!
[END MATERIAL]"
*   **C3 Modifier:** "Apply the extraneous load (coherence) effect from Cognitive Load Theory in your evaluation."

---

### 2. Hypotheses

*   **H1 (The Prompting Gradient):** Models will show a clear gradient in applying CLT principles: C3 (Specific) > C2 (General) > C1 (Unprompted).
*   **H2 (Reasoning vs. Output):** Models with explicit extended thinking (e.g., OpenAI o1/o3-mini, Gemini 2.0 Flash Thinking, Claude 3.7 Sonnet) will successfully apply the principles in C2 (General) significantly more often than standard models, because they will use their reasoning trace to retrieve and map the theory to the specific task.
*   **H3 (Task Variability):** 
    *   *Task 5 (Extraneous)* will have the highest unprompted success rate, as "removing fluff" aligns with general AI helpfulness/conciseness training.
    *   *Task 1 (Fading)* will have the lowest unprompted success rate. Without prompting, models default to providing fully worked examples, not partially completed ones.
*   **H4 (Reasoning Traces):** In C1 (Unprompted), models may accidentally apply a principle (e.g., sequencing from simple to complex) but will *not* reference working memory or CLT in their reasoning trace, indicating pattern-matching rather than pedagogical reasoning.

---

### 3. Scoring Rubric

To ensure reliability, use a strict binary (1 = Yes, 0 = No) scoring system for both Application and Reasoning.

#### Metric 1: Application Score (Did the output reflect the principle?)
*   **Task 1 (Fading):** 1 = The sequence progressively removes steps, requiring the student to complete more of the problem as they advance (e.g., Example 1 is fully worked, Example 4 is mostly blank). 0 = All examples are fully worked or just standard practice problems.
*   **Task 2 (Split-Attention):** 1 = The redesign integrates the data directly into the text or formula (e.g., "45g / 15cm³ = 3 g/cm³") rather than referencing table coordinates. 0 = The redesign maintains the physical separation of data and calculation.
*   **Task 3 (Sequencing):** 1 = Problems strictly progress by adding interacting elements (e.g., Q1: two rectangles, Q2: L-shape, Q3: shape requiring subtraction). 0 = Random difficulty, or all problems are of identical complexity.
*   **Task 4 (Self-Explanation):** 1 = The redesign inserts explicit prompts for the student to explain *why* a step was taken (e.g., "Why did we place a 2 here?"). 0 = The redesign just rewrites the text, adds formatting, or adds more teacher explanations without prompting student self-explanation.
*   **Task 5 (Extraneous):** 1 = The redesign strips out the emojis, the Latin etymology, and the "Timmy" narrative wrapper, leaving only the core mathematical steps. 0 = The redesign keeps the narrative/emojis but just formats it better.

#### Metric 2: Reasoning Score (Did the model reason about CLT?)
*   **1 = Yes:** The model's Chain of Thought (or the preamble of its output for non-CoT models) explicitly mentions Cognitive Load Theory, working memory constraints, or the specific name of the effect (e.g., "To reduce intrinsic load...", "This causes split-attention...").
*   **0 = No:** No mention of CLT terminology. It may mention general pedagogy ("to make it clearer", "to scaffold learning"), but lacks cognitive architecture terminology.

---

### 4. Data Analysis Plan

*   **Aggregation:** Calculate the mean Application Score (0-100%) and Reasoning Score (0-100%) for each Model x Task x Condition combination.
*   **Key Comparisons:**
    1.  **Unprompted vs. Prompted:** Does simply asking for "good pedagogy" (C1) yield CLT-compliant designs, or is explicit prompting (C2/C3) required?
    2.  **Reasoning vs. Application (Contingency Analysis):** Create a 2x2 matrix (Reasoned: Y/N vs. Applied: Y/N). We want to see if reasoning about CLT is a prerequisite for applying it correctly in complex tasks (like Fading).
    3.  **Model Comparison:** Compare the Application scores of reasoning models (e.g., o3-mini) versus standard models (e.g., GPT-4o) in the C2 (General CLT) condition. This tests if "thinking" helps bridge the gap between abstract theory and concrete application.
*   **Reporting:** Use clustered bar charts (X-axis: Conditions, Y-axis: % Application Success, grouped by Task). Include qualitative excerpts from the reasoning traces to show *how* the models mapped the theory to the task.

---

### 5. Model Selection

You must test models that expose their reasoning process, alongside standard models as baselines. 

**Recommended Reasoning Models (The Focus):**
1.  **OpenAI o3-mini (or o1):** The current gold standard for extended thinking.
2.  **Anthropic Claude 3.7 Sonnet:** Crucial because it has a toggleable "Extended Thinking" mode.
3.  **Google Gemini 2.0 Flash Thinking:** Google's accessible reasoning model.

**Recommended Baseline Models (Control):**
4.  **GPT-4o:** Represents the standard, non-CoT instruction-following model.
5.  **Claude 3.5 Sonnet:** Highly capable pedagogical model, but without the explicit reinforcement learning for extended reasoning traces.

---

### 6. Number of Runs

LLMs are non-deterministic. A single run is insufficient.
*   **Recommendation:** **n = 20 iterations** per prompt, per model.
*   **Total scale:** 5 tasks × 3 conditions × 5 models × 20 runs = **1,500 total outputs**.
*   *Why n=20?* It is large enough to calculate a stable percentage (each run is worth 5%) and run basic statistical tests (like Chi-square for categorical outcomes), but small enough to be manageable. Set temperature to a standard default (e.g., 0.7 for standard models; reasoning models usually handle their own temperature).

---

### 7. Limitations to Acknowledge in the Report

1.  **Textual Proxy for Visual Tasks:** Split-attention is fundamentally a spatial/visual phenomenon. Testing it via text (Markdown tables) is a proxy. The LLM might fix it due to text-proximity rules rather than true spatial reasoning.
2.  **Construct Contamination:** "Fading" or "Sequencing" might be applied not because the model understands cognitive load, but because these patterns are highly prevalent in the maths worksheets it was trained on. The Reasoning Score mitigates this, but cannot entirely eliminate it.
3.  **LLM-as-a-Judge Constraints:** If you use an LLM to score the 1,500 outputs (highly recommended for a solo researcher), the judge model may have its own biases regarding what constitutes "fading" or "extraneous load."

---

### 8. Practical Considerations for a Solo Researcher

*   **Automation is Mandatory:** Do not do this manually in the web interfaces. Write a Python script using the official APIs (OpenAI, Anthropic, Google) to loop through the prompts 20 times and save the outputs to a CSV. 
*   **Capturing the CoT:** Ensure your script captures the `<think>` tags (for Claude/Gemini) or the `reasoning_content` (for OpenAI). Save this in a separate column from the final output.
*   **Scoring (LLM-as-a-Judge):** Manually grading 1,500 outputs is a poor use of time. 
    *   *Strategy:* Write a strict meta-prompt for GPT-4o to act as the grader, using the exact Rubric from Section 3. 
    *   *Validation:* Manually grade a random sample of 50 outputs (10 per task). Compare your manual grades to the LLM judge. If agreement (Cohen’s Kappa) is > 0.80, let the LLM grade the rest.
*   **API Costs:** Reasoning models use many more tokens because of the hidden reasoning trace. However, with `o3-mini`, `Gemini 2.0 Flash Thinking`, and `Claude 3.7 Sonnet`, costs have dropped significantly. Budget roughly $30 - $50 USD for the entire 1,500 run experiment, plus $10 for the LLM-as-a-Judge grading.