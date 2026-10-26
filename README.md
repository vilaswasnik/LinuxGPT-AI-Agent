# LinuxGPT

**Ask your Linux machine questions in plain English.** LinuxGPT turns a natural-language request into a Linux command, checks it against a safety list, runs it, and shows you the output — and, in educational mode, explains what the command actually does.

<!-- TODO(author): add a terminal screenshot or asciinema link here before publishing. -->

```text
Query> show me disk space usage
Command: df -h

Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1        50G   20G   28G   42% /
```

## What it does

- **Natural language → command** — type "show running processes" and get `ps aux`; "what's my current directory?" gives `pwd`. A table of supported query patterns is below.
- **LLM reasoning with a local knowledge base** — queries are matched against a bundled Linux commands database before generation, so answers are grounded in documented commands, options, and examples, not just model memory.
- **Safety checks before anything runs** — dangerous patterns (e.g. `rm -rf /`, `mkfs`, fork bombs, `chmod -R 777 /`, from `config.json`) are blocked, execution times out after 30 seconds, and nothing runs with automatic sudo.
- **Educational mode** — `explain grep` walks through usage, common options, examples, and tips; `combinations` lists 30+ real-world command pipelines (see EDUCATIONAL_FEATURES.md).
- **Works with no API key** — without an `OPENAI_API_KEY`, LinuxGPT runs in mock mode using pattern matching, so you can try the full loop with zero setup cost.
- **Two ways to run** — interactive REPL for continuous questions, or one-shot CLI for a single query. Command history is tracked in-session (`history` command).

## Quickstart

Requirements: Python 3.7+, a Linux/Unix environment. An OpenAI API key is optional (mock mode works without one).

```bash
git clone https://github.com/vilaswasnik/LinuxGPT-AI-Agent.git
cd LinuxGPT-AI-Agent
pip install -r requirements.txt

# just try it (mock mode, no key needed)
python agent.py

# or a single question
python agent.py "show me disk space usage"
```

For full LLM generation, add your key:

```bash
cp .env.example .env   # then edit in your OPENAI_API_KEY
# or: export OPENAI_API_KEY='your-api-key-here'
python agent.py
```

Example queries:

| You type | It runs |
|---|---|
| "show list of files in directory" | `ls -la` |
| "what's my current directory?" | `pwd` |
| "show disk space usage" | `df -h` |
| "show running processes" | `ps aux` |
| "show memory usage" | `free -h` |
| "find all text files" | `find . -name '*.txt'` |
| "find large files" | `find . -type f -size +100M -exec ls -lh {} \;` |
| "show network connections" | `netstat -tuln` |
| "show system information" | `uname -a` |

## How it works

```text
Query (natural language)
   │
   ▼
1. Query processing ── parse input, search the commands database
   │
   ▼
2. LLM reasoning ───── OpenAI GPT-4 with database context (or mock pattern matching)
   │
   ▼
3. Safety checks ────── dangerous-pattern blocklist + 30s timeout (config.json)
   │
   ▼
4. Execution ────────── run command, capture output/errors, record history
```

See [ARCHITECTURE.md](ARCHITECTURE.md) for the full component breakdown.

Configuration lives in `config.json`: LLM provider/model/temperature, the dangerous-pattern list, the execution timeout, and the database path. The commands database ships in two files — `linux_commands_db.json` and the larger `linux_commands_db_comprehensive.json`, which `agent.py` loads first when present.

## Try it / run a POC

- **Five-minute trial:** clone, `pip install -r requirements.txt`, run `python agent.py` with no API key. Mock mode answers common queries and shows the safety/education behavior end to end.
- **Teaching POC:** run a lab session with `explain <command>` and `combinations` — students see usage, options, and worked pipelines, not just answers.
- **Safety POC:** try asking for something destructive ("delete everything in root") and watch it get blocked; then review the pattern list in `config.json` and add a pattern of your own.
- **Real-key POC:** set `OPENAI_API_KEY` (see `.env.example`) and compare generated commands against mock-mode answers on your own admin questions. Always review a generated command before letting it run — especially anywhere near production.

## Project structure

```text
agent.py                              # the agent (query processing, LLM, safety, execution)
demo.py                               # scripted demo
config.json                           # LLM + security configuration
linux_commands_db.json                # commands database
linux_commands_db_comprehensive.json  # extended database (loaded first if present)
requirements.txt                      # openai, python-dotenv
install.sh / quickstart.sh            # setup helpers
linuxgpt_service.sh                   # service start/stop/status wrapper
linuxgpt.spec                         # PyInstaller packaging spec
ARCHITECTURE.md                       # design notes
EDUCATIONAL_FEATURES.md               # learning-mode guide
CHANGELOG.md                          # change history
```

## Screenshots / demo

<!-- TODO(author): add terminal capture (interactive session + explain mode) here. -->

_Planned:_ interactive session · `explain` output · a blocked dangerous command.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) — the easiest high-value contributions are new entries in the commands database, tests for the safety checker, and documentation fixes. Please open an issue before large changes.

## Talk to the author

Using LinuxGPT for teaching, onboarding junior admins, or a lab? I'd like to hear how it holds up. Open a GitHub Issue, or a Discussion if enabled — command suggestions and failure reports (query + what it generated) are equally useful.

— Vilas Wasnik, Senior Linux & DevOps Engineer · GitHub [@vilaswasnik](https://github.com/vilaswasnik)

## License

MIT — see the LICENSE file. (Author note: if the LICENSE file is not yet in the repo, add it in the same commit as this README.)
