# Model × effort benchmark grid

Treat every (model, effort) pair as its own candidate. Fill one grid per use case, then publish a
single default recommendation.

**Use case:** <e.g. "per-file migration edits with tests">
**Quality metric:** <e.g. tests pass + reviewer acceptance rate>
**Cost metric:** <e.g. tokens or spend per completed task>

| Model | low | medium | high | xhigh |
|---|---|---|---|---|
| <frontier model> | q= / c= | q= / c= | q= / c= | q= / c= |
| <mid model> | q= / c= | q= / c= | q= / c= | q= / c= |
| <small model> | q= / c= | q= / c= | q= / c= | q= / c= |

**Default:** "Use <model> on <effort> for this kind of task."
**Escalate to:** <model/effort> when <condition>.
**Notes:** a model on a low effort level can beat a different model on xhigh — don't assume.
