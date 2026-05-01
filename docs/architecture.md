# System Architecture

## Overview
This system is designed as a modular AI agent framework combining reasoning and execution.

---

## Layers

### 1. Brain Layer (Hermes)
Responsible for intelligence and decision-making.

- Planning  
  Decomposition of complex goals into actionable steps

- Memory  
  Integration of short-term context and long-term vector-based retrieval

- Reasoning  
  Logic processing powered by advanced LLMs

---

### 2. Execution Layer (OpenClaw)
Handles real-world interactions.

- Task execution across various environments  
- Tool usage:
  - Browser automation  
  - Terminal access  
  - API integrations  

---

### 3. Model Layer

- **Local LLMs**
  - Optimized via Ollama
  - Focus on privacy and low latency

- **Remote APIs**
  - OpenAI (GPT-4)
  - Anthropic (Claude)
  - DeepSeek

---

## Logical Flow

User Input  
→ Hermes (Planning)  
→ Task Decomposition  
→ OpenClaw (Execution)  
→ Feedback Loop  
→ Final Result
