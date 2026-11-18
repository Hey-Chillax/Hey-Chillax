<picture>
  <source media="(max-width: 600px)" srcset="assets/banner-narrow.svg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg">
  <img alt="Yi Zhang. M.S. student at Nanjing University, Class of 2028. Multimodal LLMs, post-training (SFT → RL → OPD), agentic RL, efficient inference." src="assets/banner-light.svg" width="100%">
</picture>

<picture>
  <source media="(max-width: 600px)" srcset="assets/status-narrow.svg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/status-dark.svg">
  <img alt="Open to LLM algorithm internships: available now, 5+ days a week, 6+ consecutive months." src="assets/status-light.svg" width="100%">
</picture>

🏠&nbsp;[Homepage](https://hey-chillax.github.io) &nbsp;·&nbsp; 📄&nbsp;[CV&nbsp;(PDF,&nbsp;Chinese)](https://hey-chillax.github.io/files/Yi_Zhang_CV_zh.pdf) &nbsp;·&nbsp; 🎓&nbsp;[Google&nbsp;Scholar](https://scholar.google.com/citations?user=SpbemaUAAAAJ) &nbsp;·&nbsp; ✉️&nbsp;[yizhang@smail.nju.edu.cn](mailto:yizhang@smail.nju.edu.cn)

### 🔬 Projects

**[Scaffold-OPD](https://github.com/Hey-Chillax/scaffold-opd)** · SFT → OPD → RL post-training for long chain-of-thought math<br>
A 4B teacher steps into the 1.7B student's rollout only where the student would miss a reflection or the conclusion; the whole relayed answer is then distilled token by token.<br>
**25.4 → 46.9** average on MATH-500 and AIME 2024–26 in 40 steps, **+6.2** over standard OPD · [report](https://hey-chillax.github.io/projects/scaffold-opd.html)

**[StepCredit-RL](https://github.com/Hey-Chillax/stepcredit-rl)** · SFT → agentic RL for long-horizon, multi-turn tool-calling agents<br>
Steps that start from the same environment state in different rollouts are compared by the return that followed, so every step gets its own credit, with no critic and no extra rollouts.<br>
ALFWorld **98.6% / 94.0%** (seen / unseen) after SFT and 100 RL steps; **82.9% vs 70.7%** against GRPO from the base model · [report](https://hey-chillax.github.io/projects/stepcredit-rl.html)

### 🛠️ Toolbox

**Models & architectures** · Qwen3-VL, Qwen3.5 (Gated DeltaNet), Qwen3.8-Flash-Next (QSA, gated residual), DeepSeek-V3.2 (MLA, DSA), DeepSeek-V4 (mHC, CSA / HCA), Mamba-3; MoE, DiT, TTT, Loop Transformer<br>
**Multimodal** · MLLM architecture changes, ViT (SigLIP, DINO, SAM), MRoPE; modality alignment and multi-stage training, data mixing and cleaning<br>
**Agent** · Agentic RL (credit assignment); ReAct, context engineering, agent memory, agent harness; MCP, Skills<br>
**Post-training** · Data synthesis, data filtering, SFT, LoRA; PPO, DPO, GRPO, DAPO, GSPO, OPD; reward design<br>
**Training systems** · Multi-GPU distributed training, FSDP2, veRL, mixed precision; experienced with Slurm clusters, 16,000+ H100 GPU-hours in total<br>
**Inference** · vLLM, FlashAttention, speculative decoding (MTP, DFlash), KV cache (pruning, low-rank, PagedAttention)

### 📚 Publications & honors

**Publications** · four SCI journal papers and one EI conference paper as first author (IEEE Photonics Journal, JOSA B, Applied Physics B, Applied Sciences, Proc. SPIE)<br>
**Honors** · ranked 1st of 541 in the B.Eng. major · National Scholarship · Xiaomi Special Scholarship (5 recipients university-wide) · National First Prize, “Challenge Cup” · Honorable Mention, MCM
