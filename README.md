# 🤖 AI Liaison Microservice

A dedicated Python service built to act as an intermediary between the core `FileIntake` application and various external AI providers (e.g., Gemini, OpenAI, etc.). This architecture centralizes API key management, isolates the main application from third-party dependencies, and allows for easy swapping of AI models.

## 🚀 Features

* **Centralized AI Access:** Single HTTP endpoint for all AI interaction logic.

* **Security:** Uses environment variables (`GENERIC_AI_API_KEY`) to securely manage provider API keys.

* **Decoupling:** Protects the main `FileIntake` application from changes in AI SDKs or API versions.

* **Provider Agnostic:** Designed with a placeholder function (`call_ai_api`) that can be easily updated to communicate with any LLM platform.