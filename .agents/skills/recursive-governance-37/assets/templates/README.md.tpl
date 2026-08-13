# Agent governance

This directory indexes the repository's recursive self-governance configuration.

It is not intended to duplicate product, architecture, security, or operational sources of truth. Use `manifest.json` to point to canonical artifacts wherever they already exist.

## Operating rule

The repository uses the 37-factor engineering model as an audit and control framework:

- Operational kernel: 四念処・四正断・四神足
- Capability: 五根
- Robustness: 五力
- Adaptive meta-control: 七覚支
- Integrated governance: 八正道

See the installed `$recursive-governance-37` skill for the authoritative factor registry and runtime protocol.

## Local decisions

Record repository-specific policy in `constitution.md`, evidence/source pointers in `manifest.json`, and factor-specific overrides in `factor-overrides.json`.
