## 🏗️ Model Context Protocol (MCP) — Architect in Action

```text
+------------------------+      1. Request (intent)
|     LLM / AI Agent     |  -----------------------------▶
|  (e.g., Claude, GPT)   |
+------------------------+

          ▲                                ▼
          |                         2. Secure Routing
          |                         3. Permission Checks
          |                         4. Prompt Assembly
+------------------------+  ◀──────────────────────────────
|         HOST           |      (MCP Coordinator)
| - Executes MCP logic   |
| - Manages session,     |
|   access, and prompts  |
+------------------------+
        ▲           ▲
        |           |
        |           |          5. Tool call (POST-like)
        |           +--------------------------+
        |                                      |
        |                            +--------------------+
        |                            |      Tool Server    |
        |                            | (APIs, DBs, Actions)|
        |                            +--------------------+
        |
        |           6. Resource read (GET-like, no action)
        +--------------------------+
                                   |
                         +----------------------+
                         |   Resource Server     |
                         |  (logs, docs, config) |
                         +----------------------+

Final Step:
HOST sends structured **response or context** → LLM → Generates output based on Tools + Resources + Prompts
