# Performance triage questions (template)

Copy/paste and fill in:

1. What is the slow operation (endpoint/job/UI)?
2. What are the symptoms (timeouts, high p95, CPU spikes, memory growth)?
3. What changed recently (deploy, config, dependencies, data volume)?
4. What is the input size / typical dataset size?
5. What is the target metric (latency/throughput/memory) and current baseline?
6. What measurements do you already have (profiling, logs, traces)?
7. Constraints: must preserve behavior, APIs, ordering, determinism, etc.
