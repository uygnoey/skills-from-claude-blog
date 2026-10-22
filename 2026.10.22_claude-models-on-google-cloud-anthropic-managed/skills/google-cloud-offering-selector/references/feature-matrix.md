# Feature matrix - Claude on Google Cloud

Source: "Claude Platform is now available on Google Cloud" (October 22, 2026). For the authoritative,
current list see the official documentation:
https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed

## Two offerings

| | Anthropic managed | Google managed |
|---|---|---|
| Status | Generally available (Oct 22, 2026) | Remains available |
| Operator / data processor | Anthropic | Google Cloud |
| Feature access | Full Claude Platform parity; new features and betas same day as native platform | See Google Cloud docs |
| Best for | Day-zero access to all beta and GA features via Google Cloud | Google as processor, strict regional residency, native integrations (Model Armor, Agent Engine) |
| Access | Existing Google Cloud IAM credentials | Google Cloud |
| Billing | Single Google Cloud invoice; draws down Google Cloud commitment | Google Cloud |
| Endpoints | US and Global (currently) | See Google Cloud docs |
| Console | Claude Console included | - |

## Included in Anthropic managed

### Build and deploy agents
| Feature | What it does | Docs |
|---|---|---|
| Claude Managed Agents (beta) | Long-running agents without managing infrastructure | https://platform.claude.com/docs/en/managed-agents/overview |
| Code execution | Run Python, create visualizations, analyze data within an API call | https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool |
| Computer use | Let Claude operate a browser or desktop | https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool |
| Agent skills | Teach repeatable workflows for consistent results | https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview |
| Advisor strategy (beta) | Agents consult an advisor model | https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool |

### Connect to systems and knowledge
| Feature | What it does | Docs |
|---|---|---|
| Files API | Upload and reference documents across conversations | https://platform.claude.com/docs/en/build-with-claude/files |
| Citations | Ground responses in source documents | https://platform.claude.com/docs/en/build-with-claude/citations |
| Web search / web fetch | Current real-world data from the web | https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool , https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool |
| MCP connector (beta) | Connect to other tools without writing client code | https://platform.claude.com/docs/en/agents-and-tools/mcp-connector |

### Manage cost and performance
| Feature | What it does | Docs |
|---|---|---|
| Prompt caching | Lower cost and latency on repeated context | https://platform.claude.com/docs/en/build-with-claude/prompt-caching |
| Batch processing | High-volume asynchronous workloads | https://platform.claude.com/docs/en/build-with-claude/batch-processing |

### Fast Mode on Claude Opus 5.5 (GA on this offering)
- Up to 2.5x faster output token generation.
- For rapid iteration, live debugging, interactive agents.
- Pricing: $8 per million input tokens, $40 per million output tokens.

### Claude Console
Write prompts and configure agents, run them on hosted environments, monitor usage and costs, manage
access and security per workspace.

### Models
Claude Fable 5.1, Opus 5.5, Sonnet 5.5, Haiku 5.5; new models ship on the offering as they launch.

## Commercial note
Existing discounts: contact the Anthropic or Google Cloud account executive before starting. Discounts
cannot be applied retroactively.
