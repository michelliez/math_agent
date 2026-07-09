# Math Agent
## Architecture
                    User Question
                          │
                          ▼
                ┌──────────────────┐
                │   Planner LLM    │
                └──────────────────┘
                          │
          ┌───────────────┴────────────────┐
          │                                │
     Multi-step                       Single-step
          │                                │
          ▼                                ▼
 Execute Math Plan                  Extraction LLM
          │                                │
          ▼                            use_tool?
   Tool → Tool → Tool                /          \
          │                         no          yes
          ▼                         │            │
 Explanation LLM              Direct Answer   Tool Router
          │                                 │
          └────────────────┬────────────────┘
                           ▼
                      Final Answer