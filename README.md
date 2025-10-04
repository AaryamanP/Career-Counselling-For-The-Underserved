# Career Counseling for Underserved

Small project that looks like a Streamlit app using OpenAI.

## What this repo contains
- `main.py` — app entry (existing)
- `Counseling.ipynb` — notebook
- `requirements.txt` — runtime dependencies

## Quick start
1. Create a virtual environment and activate it:

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Run the Streamlit app:

```powershell
streamlit run main.py
```

## Notes
- Add your OpenAI API key as an environment variable before running (example below).

```powershell
# Set your API key in the current PowerShell session (do NOT commit secrets)
$env:OPENAI_API_KEY = "<your-openai-key-here>"
```

## Security

- The code (both `main.py` and `Counseling.ipynb`) now reads the API key from the `OPENAI_API_KEY` environment variable. Do not hard-code API keys in source files.
- If a key was accidentally committed or exposed, rotate (revoke and create a new) the key immediately via your provider dashboard and remove it from git history if it was pushed to a public repo.

## How to publish to GitHub (short)
1. Create a new empty repo on GitHub (no README/license).
2. In this folder run the git commands below (example provided in the repo root `GIT_PUSH.md`).

## Next steps
- Add a `LICENSE` (MIT suggested).
- Add a simple GitHub Actions workflow for tests/linting.
- Add a short `README` section documenting `main.py` inputs/outputs and any expected files.
