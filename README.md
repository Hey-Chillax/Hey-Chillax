🌐 [Homepage](https://hey-chillax.github.io) · 📚 [Google Scholar](https://scholar.google.com/citations?user=SpbemaUAAAAJ) · ✉️ yizhang [at] smail.nju.edu.cn

### Hi, I'm Yi Zhang (张益) 👋

M.S. student in Communication Engineering at **Nanjing University** (class of 2028), working on **LLM post-training** and **multimodal LLMs**.

🔎 **Looking for an LLM algorithm internship** — available now, 5+ days a week, up to 9 months.
正在寻找大模型算法实习，可立即到岗，每周至少 5 天，可连续实习 9 个月。

**What I work on**

- **Post-training:** SFT → RL → on-policy distillation (OPD) for long chain-of-thought reasoning in small models
- **Agentic RL:** long-horizon, multi-turn tool-calling agents and step-level credit assignment
- **Multimodal LLMs:** efficient long-video understanding

**Projects**

| Project | What it is | Result (single seed) |
|---|---|---|
| [Scaffold-OPD](https://github.com/Hey-Chillax/scaffold-opd) | SFT → OPD → RL pipeline: a Qwen3-4B teacher takes over the Qwen3-1.7B student's rollout where it misses a reflection | MATH-500 + AIME 2024–26 average **25.4 → 46.9** in 40 steps, +6.2 over standard OPD · [report](https://hey-chillax.github.io/projects/scaffold-opd.html) |
| [StepCredit-RL](https://github.com/Hey-Chillax/stepcredit-rl) | Expert SFT → agentic RL for multi-turn tool-calling agents (Qwen3-4B) | ALFWorld **98.6% / 94.0%** (seen / unseen); step-level advantage vs GRPO 82.9% vs 70.7% · [report](https://hey-chillax.github.io/projects/stepcredit-rl.html) |
| [openreview-paper-digest](https://github.com/Hey-Chillax/openreview-paper-digest) | Filters OpenReview papers by keywords and review scores, then reads each one with an LLM | — |

**Tools:** PyTorch · FSDP2 · veRL · vLLM · Slurm (16,000+ H100 GPU hours)
