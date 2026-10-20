# Agent execution architecture checklist

Fill one copy per agent. Every item comes from the post's architecture; leave a note where a
choice is still open.

## 1. Brain vs. hands
- [ ] Harness runs outside the sandbox — where: ______
- [ ] Session state stored on durable infrastructure outside the sandbox — where: ______
- [ ] Credentials never placed in the sandbox — how they are injected/used: ______
- [ ] The sandbox is used only as an execution tool

## 2. Untrusted inputs reaching the sandbox
- [ ] Cloned repos
- [ ] Websites read
- [ ] Tool output parsed
- [ ] Packages installed
- [ ] Other: ______

## 3. Execution location
- [ ] Self-hosted sandbox on own infrastructure, or
- [ ] Managed sandbox provider: ______
- [ ] Code execution, sensitive files, packages, services, and data stay inside the perimeter
- [ ] Isolation unit (container / microVM / other): ______

## 4. Policy runtime (e.g., NVIDIA OpenShell)
- [ ] Default deny — everything blocked unless a rule allows it
- [ ] Rules for each tool the agent may use
- [ ] File rules
- [ ] Network connection rules
- [ ] Data access rules
- [ ] Rules enforced outside the agent
- [ ] Every allow/block decision logged — log location: ______

## 5. Tightening loop
- [ ] Initial rule set is narrow
- [ ] Log review cadence: ______
- [ ] Rule changes drafted with Claude and reviewed by: ______
- [ ] Policy prover run after each rule change; last result: ______
