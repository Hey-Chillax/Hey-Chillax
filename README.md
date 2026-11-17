<picture>
  <source media="(max-width: 600px)" srcset="assets/banner-narrow.svg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg">
  <img alt="Yi Zhang. M.S. student at Nanjing University, Class of 2028. Multimodal LLMs, post-training (SFT → RL → OPD), agentic RL, efficient inference." src="assets/banner-light.svg" width="100%">
</picture>

### 🟢 Open to LLM algorithm internships

![Available now](https://img.shields.io/badge/Available_now-2ea44f?style=flat) ![5+ days a week](https://img.shields.io/badge/5%2B_days_a_week-2d5a96?style=flat) ![Up to 9 consecutive months](https://img.shields.io/badge/Up_to_9_consecutive_months-2d5a96?style=flat)

🏠&nbsp;[Homepage](https://hey-chillax.github.io) &nbsp;·&nbsp; 📄&nbsp;[CV&nbsp;(PDF,&nbsp;Chinese)](https://hey-chillax.github.io/files/Yi_Zhang_CV_zh.pdf) &nbsp;·&nbsp; 🎓&nbsp;[Google&nbsp;Scholar](https://scholar.google.com/citations?user=SpbemaUAAAAJ) &nbsp;·&nbsp; ✉️&nbsp;[yizhang@smail.nju.edu.cn](mailto:yizhang@smail.nju.edu.cn)

### 🔬 Projects

**[Scaffold-OPD](https://github.com/Hey-Chillax/scaffold-opd)** · SFT → OPD → RL post-training for long chain-of-thought math<br>
A 4B teacher steps into the 1.7B student's rollout only where the student would miss a reflection or the conclusion; the whole relayed answer is then distilled token by token.<br>
**25.4 → 46.9** average on MATH-500 and AIME 2024–26 in 40 steps, **+6.2** over standard OPD · [report](https://hey-chillax.github.io/projects/scaffold-opd.html)

**[StepCredit-RL](https://github.com/Hey-Chillax/stepcredit-rl)** · SFT → agentic RL for long-horizon, multi-turn tool-calling agents<br>
Steps that start from the same environment state in different rollouts are compared by the return that followed, so every step gets its own credit, with no critic and no extra rollouts.<br>
ALFWorld **98.6% / 94.0%** (seen / unseen) after SFT and 100 RL steps; **82.9% vs 70.7%** against GRPO from the base model · [report](https://hey-chillax.github.io/projects/stepcredit-rl.html)

### 🛠️ Toolbox

**Post-training** · SFT, on-policy distillation, RL with PPO / DPO / GRPO / DAPO / GSPO, reward design, data synthesis and filtering<br>
**Agents** · agentic RL with step-level credit assignment; ReAct, context engineering, agent memory, MCP<br>
**Models** · MLLM architecture changes, ViT (SigLIP, DINO, SAM), MRoPE; Qwen3-VL, Qwen3.5 (Gated DeltaNet), DeepSeek-V3.2 (MLA, DSA), Mamba-3, MoE<br>
**Systems** · FSDP2, veRL, vLLM, FlashAttention, speculative decoding (MTP), KV-cache compression; Slurm clusters, 16,000+ H100 GPU-hours

### 📚 Publications & honors

**Publications** · four SCI journal papers and one EI conference paper as first author (IEEE Photonics Journal, JOSA B, Applied Physics B, Applied Sciences, Proc. SPIE)<br>
**Honors** · ranked 1st of 541 in the B.Eng. major · National Scholarship · Xiaomi Special Scholarship (5 recipients university-wide) · National First Prize, “Challenge Cup” · Honorable Mention, MCM
