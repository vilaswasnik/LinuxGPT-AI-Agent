# Contributing to LinuxGPT

Contributions are welcome — especially commands-database entries, safety-check tests, and docs fixes. LinuxGPT is a single-file Python agent (`agent.py`) plus JSON data files, so most contributions need no build step at all.

## Run it locally

Requirements: Python 3.7+, Linux/Unix environment. An OpenAI API key is optional — without one the agent runs in mock (pattern-matching) mode, which is enough for most development.

```bash
git clone https://github.com/vilaswasnik/LinuxGPT-AI-Agent.git
cd LinuxGPT-AI-Agent
pip install -r requirements.txt
python agent.py            # interactive mode
python agent.py "show me disk space usage"   # one-shot mode
```

Useful while developing:

- `demo.py` runs a scripted demonstration.
- `test_openai.py` checks your API key/connectivity when you do have a key (it is a manual script, not a test suite).
- Behavior knobs live in `config.json` (model, temperature, dangerous patterns, timeout).
- The agent loads `linux_commands_db_comprehensive.json` first if present, falling back to `linux_commands_db.json` (see `LinuxCommandDatabase._load_database` in `agent.py`) — know which file your change actually affects.

## Filing an issue

Open a GitHub Issue with:

- The exact query you typed, the command LinuxGPT generated, and what it should have generated (for command-quality bugs).
- Whether you were in mock mode or using an API key, your Python version, and your distro.
- For safety issues (a dangerous command that was **not** blocked, or a safe one that was): the query, the generated command, and your `config.json` security section. Safety reports get priority.

## PR process

1. Fork and branch from `main`.
2. Keep changes focused: code in `agent.py`, data in the JSON databases, docs in Markdown.
3. If you change command generation or safety logic, show before/after runs for a handful of queries in the PR description (mock mode output is fine and preferred — it's reproducible without a key).
4. For database additions, follow the existing entry shape (description, usage, examples, tags) exactly as neighboring entries do.
5. Maintainer review merges; expect questions on anything that loosens a safety check — those need a strong justification and a test case.

## Good first issues

Concrete starting points, each tied to something actually in the repo:

1. **Fix the README's clone URL and project name.** The current README's Installation step clones `https://github.com/yourusername/sample.ai.git` and its structure section is headed `sample.ai/` — leftovers from another project. Correct them to this repo. (This package's README draft already fixes it; the issue tracks applying that fix and sweeping the other root docs for the same leftover.)
2. **Add the missing LICENSE file.** The README declares MIT but there is no LICENSE file in the repository root. Add the standard MIT text so the declaration is real.
3. **Automated tests for the safety checker.** There is no test suite today — only the manual `test_openai.py`. The dangerous-pattern list in `config.json` (`rm -rf /`, `mkfs`, fork bomb, `chmod -R 777 /`, …) plus the timeout rule are pure, deterministic logic: a small pytest suite asserting each listed pattern is blocked and common safe commands pass would protect the project's most important feature.
4. **Document — or deduplicate — the two commands databases.** `agent.py` silently prefers `linux_commands_db_comprehensive.json` (136 KB) over `linux_commands_db.json` (15 KB), while the README describes a single "60+ commands" database. Either document which file is authoritative and how they relate, or merge them and update the loader.
5. **Tidy the repo root for developers.** The root mixes code with 10+ management/presentation files (MANAGEMENT_PRESENTATION.md, ROI_CALCULATOR.md, EXECUTIVE_SUMMARY.md, PRESENTATION_TALKING_POINTS.md, EXPANSION_PLAN.md, PROJECT_DIAGRAM.txt, PROJECT_VISUAL.txt). Moving them under a `docs/presentation/` folder (updating links) makes the developer entry points — `agent.py`, `ARCHITECTURE.md`, `QUICKREF.md` — findable at a glance.
