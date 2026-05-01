# System Architecture

## Layers
1. **Brain Layer (Hermes)**
   - Planning: Decomposition of complex goals into actionable steps.
   - Memory: Integration of short-term context and long-term vector-based retrieval.
   - Reasoning: Logic processing powered by advanced LLMs.

2. **Execution Layer (OpenClaw)**
   - Task execution across various environments.
   - Tool usage: Browser automation, Terminal access, and API integrations.

3. **Model Layer**
   - Local LLMs: Optimized via Ollama for privacy and speed.
   - Remote APIs: Integration with OpenAI (GPT-4), Anthropic (Claude), and DeepSeek.

## Logical Flow
User Input → Hermes (Planning) → Task Decomposition → OpenClaw (Execution) → Feedback Loop → Final Result
