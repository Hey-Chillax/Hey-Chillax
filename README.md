<picture>
  <source media="(max-width: 600px)" srcset="assets/banner-narrow.svg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg">
  <img alt="Yi Zhang. M.S. student at Nanjing University, Class of 2028. Multimodal LLMs, post-training (SFT → RL → OPD), agentic RL, efficient inference." src="assets/banner-light.svg" width="100%">
</picture>

### 🟢 Open to LLM algorithm internships

Available now · 5+ days a week · up to 9 consecutive months

🏠&nbsp;[Homepage](https://hey-chillax.github.io) &nbsp;·&nbsp; 📄&nbsp;[CV&nbsp;(PDF,&nbsp;Chinese)](https://hey-chillax.github.io/files/Yi_Zhang_CV_zh.pdf) &nbsp;·&nbsp; 🎓&nbsp;[Google&nbsp;Scholar](https://scholar.google.com/citations?user=SpbemaUAAAAJ)<br>
✉️&nbsp;[yizhang200304@gmail.com](mailto:yizhang200304@gmail.com) &nbsp;·&nbsp; [yizhang@smail.nju.edu.cn](mailto:yizhang@smail.nju.edu.cn)

### 🔬 Projects

**[Scaffold-OPD](https://github.com/Hey-Chillax/scaffold-opd)** · SFT → OPD → RL post-training for long chain-of-thought math<br>
A 4B teacher steps into the 1.7B student's rollout only where the student would miss a reflection or the conclusion; the whole relayed answer is then distilled token by token.<br>
**25.4 → 46.9** average on MATH-500 and AIME 2024–26 in 40 steps, **+6.2** over standard OPD · [report](https://hey-chillax.github.io/projects/scaffold-opd.html)

**[StepCredit-RL](https://github.com/Hey-Chillax/stepcredit-rl)** · SFT → agentic RL for long-horizon, multi-turn tool-calling agents<br>
Steps that start from the same environment state in different rollouts are compared by the return that followed, so every step gets its own credit, with no critic and no extra rollouts.<br>
ALFWorld **98.6% / 94.0%** (seen / unseen) after SFT and 100 RL steps; **82.9% vs 70.7%** against GRPO from the base model · [report](https://hey-chillax.github.io/projects/stepcredit-rl.html)

<sub>Single-seed results. Each report cites the original papers the methods are adapted from.</sub>

### 📚 Publications & honors

Four SCI journal papers and one EI conference paper as first author · B.Eng. ranked 1st of 541 in the major · National Scholarship · Xiaomi Special Scholarship

### 🛠️ Toolbox

PyTorch · FSDP2 · veRL · vLLM · Slurm, 16,000+ H100 GPU-hours · also [openreview-paper-digest](https://github.com/Hey-Chillax/openreview-paper-digest), which filters OpenReview papers by keywords and review scores and reads each one with an LLM
