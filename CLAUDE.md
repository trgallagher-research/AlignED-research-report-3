# AlignED Report 3 — Site Guidelines

## Project Overview

AlignED Report 3 analyses education-related AI usage patterns from the Anthropic Economic Index V4. It is a static HTML/CSS/JS site hosted on GitHub Pages. No build tools, no templating.

This report is a descriptive analysis of Claude.ai usage, not a study of "AI in education" broadly.

## File Structure

- Abstract/Cover: `index.html`
- Introduction: `introduction.html`
- Methods: `methods.html`
- Results: `results.html` (all charts rendered via `js/charts.js`)
- Discussion: `discussion.html`
- Appendices: `appendices.html`
- Shared styles: `css/style.css`
- Charts: `js/charts.js` (Chart.js, only renders on `data-page="results"`)
- Navigation: `js/main.js` (mobile toggle, active link)
- Data: `data/*.json` (7 JSON files derived from Anthropic Economic Index CSVs)

## Critical Writing Rules

### Scope precision
- Always say "Claude.ai" not "AI" when describing scope
- Always say "interaction pattern" not "learning behaviour" or "learning style"
- Never claim interaction patterns reveal learning intent
- Never claim these findings generalise to other platforms

### Epistemic precision
- Report what was measured. Let the reader draw the inference.
- Never claim "directive = not learning"
- Never claim geographic patterns reflect actual adoption rates
- Always acknowledge the one-week, one-platform limitation

### Tone
- British/Australian spelling (prioritise, recognise, organisation, behaviour)
- Short, confident sentences. Active voice.
- No AI slop phrases (see Report 1 CLAUDE.md for full blacklist)

## Design System

Identical to Reports 1 and 2:
- Background: `#F4F1EB`, Surface: `#FEFDFB`, Text: `#2D3748`
- Primary: `#3B6B9A`, Accent: `#B67D5C`
- Typography: Inter (headings) + Georgia (body)
- All styles in `css/style.css`. No inline styles.

## Footer Tagline

Use: "Benchmarking AI models for educational practice."
