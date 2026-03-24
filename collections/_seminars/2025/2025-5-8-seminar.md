---
layout: post
speaker: "Yi Wu"
title: "SELP: Generating Safe and Efficient Task Plans for Robot Agents with Large Language Models"
time: 12p EST
location: "LWSN 3102A/B"
category: seminar
invited: false
link_abstract: true
bio: "Yi Wu is a fourth-year Ph.D. student in Computer Science at Purdue University, advised by Professor Lin Tan. Her research lies at the intersection of artificial intelligence and software engineering. She focuses on (1) advancing the reasoning and planning capabilities of LLMs for AI agents, and (2) improving LLMs for software development tasks such as code generation and bug repair."
---
Despite significant advancements in large language models (LLMs) that enhance robot agents' understanding and execution of natural language (NL) commands, ensuring the agents adhere to user-specified constraints remains challenging, particularly for complex commands and long-horizon tasks. To address this challenge, we present three key insights, equivalence voting, constrained decoding, and domain-specific finetuning, which significantly enhance LLM planners' capability in handling complex tasks. Equivalence voting ensures consistency by generating and sampling multiple Linear Temporal Logic (LTL) formulas from NL commands, grouping equivalent LTL formulas, and selecting the majority group of formulas as the final LTL formula. Constrained decoding then uses the generated LTL formula to enforce the autoregressive inference of plans, ensuring the generated plans conform to the LTL. Domain-specific fine-tuning customizes LLMs to produce safe and efficient plans within specific task domains. Our approach, Safe Efficient LLM Planner (SELP), combines these insights to create LLM planners to generate plans adhering to user commands with high confidence. We demonstrate the effectiveness and generalizability of SELP across different robot agents and tasks, including drone navigation and robot manipulation. For drone navigation tasks, SELP outperforms state-of-the-art planners by 10.8% in safety rate (i.e., finishing tasks conforming to NL commands) and by 19.8% in plan efficiency. For robot manipulation tasks, SELP achieves 20.4% improvement in safety rate.
