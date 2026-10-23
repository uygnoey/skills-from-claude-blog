# Benchmark results quoted in the source

## Effort sweeps
| Benchmark | Model | Low effort | Max effort | Takeaway |
|---|---|---|---|---|
| FrontierCode Diamond (hardest 50) | Fable 5 | 11.5% at $5.35/task | 30.9% at $19.00/task | ~2.7x score (+19 pts) for ~3.5x cost: effort pays off |
| Humanity's Last Exam (no tools) | Fable 5.1 | ~53% at ~$0.30/question | ~61% at ~$2.23 | Final step added ~0.5 pt for 46% more cost, within noise |
| CursorBench 3.2 | Fable 5.1 vs Fable 5 | Fable 5.1 low matched Fable 5 high | - | ~1/3 the cost; ~40% cheaper even at Fable 5 prices |

Fable 5.1 cache reads: $0.25 per million tokens vs $1.00 for Fable 5 (as stated in the source).

## Customer support hillclimb
- Baseline: Opus 4.8 at high effort.
- Opus 5 at low effort + prompt-audit: 98.9% train accuracy, 2.6 cents/ticket.
- Sonnet 5 at low effort: 1 cent/ticket but 88.9%; added routing rules and a refund-cap cross-reference
  restored 98.9% at the same cost.
- 14 held-out tickets: final config 90.5% vs 78.6% original, at about one fifth the cost.

## cost-optimize on public benchmarks (vs Opus 5.5 baseline)
| Benchmark | Cost reduction | Levers | Quality |
|---|---|---|---|
| LegalBench | ~67% | Partial prompt caching, low effort, Batch API | Thinking tokens -84%, accuracy change < 1 pt |
| tau2-bench retail | ~73% | ~93% of prompt cacheable | No change in pass rate |
| OfficeQA Pro | ~72% | Batch API + trimming documents to relevant sections | No significant change |
| SWE-bench Verified | ~24% | Medium effort, concise output constraints (caching already applied) | - |
