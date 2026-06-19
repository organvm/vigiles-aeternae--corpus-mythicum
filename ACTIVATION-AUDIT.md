# Activation Audit

> Tracks the **activation state** of this repository — whether it ships a live,
> installable, or runnable artifact, distinct from the maturity of its research
> content. Maintained per the system-wide Activation Audit sweep.

## Current Verdict: `park`

| Field | Value |
|-------|-------|
| **Audit cursor** | `EV-2026-06-11-200202` |
| **Sweep** | `EV-2026-06-11` |
| **Identity** | Mythological research corpus and policy source material |
| **Frozen state** | `docs-only-shell` |
| **Evidence level** | `inspected-only` |
| **Verdict** | **`park`** |
| **Tracking issue** | [organvm-i-theoria/vigiles-aeternae--corpus-mythicum#4](https://github.com/organvm-i-theoria/vigiles-aeternae--corpus-mythicum/issues/4) |

### Shipped-artifact test

The audit checks for any concrete, externally-reachable activation path. None is
documented for this repository:

| Probe | Result |
|-------|--------|
| Live URL | not documented |
| Installable package | not documented |
| Runnable release | not documented |
| Documented execution path | not documented |

## What `park` means

`park` is **not** archival and **not** a defect. It records that this repository
is a **documentation-and-research shell**: it carries substantive corpus content
(tradition syntheses, the metaLAWs codex, comparative taxonomy, regime drafts)
but exposes **no code, no tests, and no shippable or runnable artifact**. There
is therefore nothing to "activate" as a product at this time.

The corpus remains **active as source material** — it produces creative source
material and regime specifications for downstream organs (see `seed.yaml`). The
`park` verdict applies strictly to the *product activation* axis, not to the
liveness of the research itself.

### Exit conditions

This verdict should be revisited when any of the following becomes true, at which
point a fresh audit cursor supersedes the one above:

- A runnable artifact is added (CLI, service, or generator over the corpus).
- A published package or release exposes the corpus programmatically.
- A live URL serves the corpus or a derived product.
- Downstream activation in another organ creates a documented execution path
  rooted in this repository.

Until then the repository is **parked**: preserved and inspectable, with no
activation work scheduled.
