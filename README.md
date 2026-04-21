# AI-Powered SEO Content Production Research

![Banner](research/other/banner.svg)

A structured research repository documenting how AI is reshaping SEO content production — from keyword-based ranking to generative engine optimization (GEO).

Built as part of a growth marketing research project, this repo collects and organizes content from 10 practitioners who actively build AI-driven SEO systems, not just write about them.

---

## Topic

**AI-powered SEO content production** — how AI tools and workflows are changing the way content is created, structured, and optimized for both traditional search engines and AI-driven discovery systems like ChatGPT, Perplexity, and Gemini.

---

## Repository Structure

```
research/
│
├── linkedin-posts/
│   ├── eric-siu.md
│   ├── koray-tugberk-gubur.md
│   ├── mike-king.md
│   ├── neil-patel.md
│   └── tom-niezgoda.md
│
├── other/
│   ├── eric-siu.png
│   ├── tom-niezgoda.jpg
│   └── sources.md
│
└── youtube-transcripts/
    ├── gael-breton.md
    ├── julian-goldie-link-building.md
    ├── mark-webster.md
    ├── matt-diggity-ai-seo.md
    └── nathan-gotch-new-playbook.md
```

Full source list with links and annotations: [`research/sources.md`](research/sources.md)

---

## The 10 Experts

These were selected based on one criterion: they build and ship real AI-SEO systems, not just commentary. Each has a documented track record of sharing case studies, workflows, or tools — not theory.

| # | Expert | Focus | Why Selected |
|---|--------|-------|--------------|
| 1 | [Matt Diggity](https://www.linkedin.com/in/mattdiggityseo/) | SEO testing, AI workflows | Data-driven experiments with real ranking case studies |
| 2 | [Julian Goldie](https://www.linkedin.com/in/juliangoldieseo/) | AI SEO automation, link building | Practical tutorials on scaling content production with AI |
| 3 | [Nathan Gotch](https://www.linkedin.com/in/nathangotch/) | SEO fundamentals, AI-assisted content | Bridges strong SEO foundations with modern AI workflows |
| 4 | [Gael Breton](https://www.linkedin.com/in/gael-breton/) | Authority sites, AI content systems | Builds structured, scalable AI-driven content systems |
| 5 | [Mark Webster](https://www.linkedin.com/in/markwebster1/) | SEO systems, content scaling | Focuses on repeatable systems for scaling SEO content |
| 6 | [Mike King](https://www.linkedin.com/in/michaelkingphilly/) | Technical SEO, semantic search, AI search | Connects SEO with embeddings, information retrieval, and how AI actually interprets content |
| 7 | [Koray Tugberk GUBUR](https://www.linkedin.com/in/koray-tugberk-gubur/) | Semantic SEO, topical authority | Advanced content structure and search intent optimization |
| 8 | [Tomasz Niezgoda](https://www.linkedin.com/in/niezgoda-tomasz/) | AI content optimization, on-page SEO | Builds AI-powered SEO tools at Surfer SEO, shares practical optimization insights |
| 9 | [Eric Siu](https://www.linkedin.com/in/ericosiu/) | B2B marketing, AI-driven growth | Strategic view on scaling marketing and content using AI and automation |
| 10 | [Neil Patel](https://www.linkedin.com/in/neilkpatel/) | SEO, content marketing, AI tools | High-volume practitioner frequently documenting AI's role in content production |

---

## Data Collection

**YouTube transcripts** were collected via the [Supadata API](https://supadata.ai), using their transcript endpoint with `text=True` to return clean plain text output. Example:

```python
from supadata import Supadata

supadata = Supadata(api_key="...")
transcript = supadata.transcript(
    url="https://www.youtube.com/watch?v=...",
    lang="en",
    text=True,
    mode="auto"
)
```

**LinkedIn posts** were collected manually — copied directly from each expert's profile, preserving original formatting and dates.

---

## Key Research Themes

### 1. GEO (Generative Engine Optimization)
- AI search prioritizes **answers over links**
- Goal shifts from *ranking* → to *being cited*

### 2. Chunking & Retrieval
- Optimal content blocks: **100–300 tokens**
- Improves passage-level retrieval, semantic matching, and AI citation likelihood

### 3. Freshness Over Structure
- Recent data heavily influences AI outputs
- Updating content increases visibility and citation probability

### 4. Brand Mentions in Blogs
- Third-party blog mentions strongly correlate with AI recommendation ranking
- Digital PR is becoming a core SEO lever

### 5. AI Agent Ecosystems
- Shift toward autonomous agents and machine-readable content (JSON, Markdown)
- Maintenance and monitoring are emerging challenges

---

## Why This Matters

Search is undergoing a fundamental shift:

| Traditional SEO | AI Search (GEO)    |
|-----------------|--------------------|
| Keywords        | Intent + reasoning |
| Rankings        | Recommendations    |
| Pages           | Passages           |
| Traffic         | Conversions        |

---

## Future Work

- Build structured datasets for AI retrieval testing
- Create GEO optimization frameworks
- Analyze citation patterns across LLMs
- Develop prompt-based content testing systems

---

## Author

**Erian Hadi**  
Information Systems Student — focused on AI, SEO, and digital systems

---

> The future of SEO is not about being found.  
> It's about being *chosen by AI*.
