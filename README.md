# ChallengeHub Starter Codebase

ChallengeHub is the course project for CPE106L-4 Software Design Laboratory.

This repository contains the supplied Python prototype and sample data used throughout the course. Begin by running the system, inspecting its data and responsibilities, and tracing its observable behavior against the ChallengeHub Project Guide.

## Repository structure

```text
ChallengeHub/
├── challengehub/
├── data/
├── tests/
├── notebooks/
├── outputs/
│   ├── M2LA2/
│   ├── PO4/
│   ├── M2CW/
│   └── Final_Project/
├── docs/
├── pyproject.toml
└── requirements.txt
```

## Google Colab setup

Keep the complete `ChallengeHub` folder directly inside **My Drive**:

```text
My Drive/
└── ChallengeHub/
```

Course notebooks use `/content/drive/MyDrive/ChallengeHub` as the project root after Google Drive is mounted. Run the **Connect Course Project** cell whenever a new Colab runtime is connected.

See `COLAB_SETUP.md` for the one-time setup and normal weekly workflow.

## Local quick start

From the repository root:

```bash
python -m pytest -q
python -m challengehub.cli
```

## Working with the codebase

- Run the existing tests before making changes.
- Inspect the source and data before revising the design.
- Keep course-project terminology consistent across requirements, UML, code, and verification evidence.
- Preserve working behavior unless a documented project decision requires a change.
