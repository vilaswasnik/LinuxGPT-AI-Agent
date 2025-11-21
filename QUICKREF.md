# Quick Reference Guide

## Getting Started

### First Time Setup
```bash
# Run the quickstart script
./quickstart.sh

# Or manually:
pip install -r requirements.txt
python agent.py
```

### Set API Key (Optional)
```bash
# For full LLM functionality
export OPENAI_API_KEY='sk-...'

# Or create .env file
cp .env.example .env
# Edit .env and add your key
```

## Usage Examples

### Interactive Mode
```bash
python agent.py
```

**Sample Session:**
```
Query> show me list of files in directory
Command: ls -la
[output displayed]

Query> what's my current directory?
Command: pwd
/workspaces/sample.ai

Query> history
Command History:
1. [✓] show me list of files in directory → ls -la
2. [✓] what's my current directory? → pwd

Query> quit
```

### Command Line Mode
```bash
# Single queries
python agent.py "show disk space usage"
python agent.py "show running processes"
python agent.py "find all python files"
```

### Demo Mode
```bash
python demo.py
# Runs through multiple test queries automatically
```

## Common Queries

### File Operations
| Query | Expected Command |
|-------|------------------|
| "show files in directory" | `ls -la` |
| "show current directory" | `pwd` |
| "find text files" | `find . -name '*.txt'` |
| "search for word in files" | `grep -r 'word' .` |
| "show file contents" | `cat file.txt` |
| "show first 10 lines" | `head file.txt` |
| "show last 10 lines" | `tail file.txt` |

### System Information
| Query | Expected Command |
|-------|------------------|
| "show disk space" | `df -h` |
| "show memory usage" | `free -h` |
| "show running processes" | `ps aux` |
| "show system info" | `uname -a` |
| "show network interfaces" | `ip addr show` |
| "show system uptime" | `uptime` |

### Network Operations
| Query | Expected Command |
|-------|------------------|
| "show network connections" | `netstat -tuln` |
| "test connectivity to google" | `ping google.com` |
| "check website status" | `curl -I https://example.com` |
| "show open ports" | `lsof -i` |

### Process Management
| Query | Expected Command |
|-------|------------------|
| "show running processes" | `ps aux` |
| "show process tree" | `ps auxf` |
| "find nginx processes" | `ps aux | grep nginx` |
| "show cpu usage" | `top` |

### File Search
| Query | Expected Command |
|-------|------------------|
| "find python files" | `find . -name '*.py'` |
| "find large files" | `find . -size +10M` |
| "find recent files" | `find . -mtime -7` |
| "search for text" | `grep -r 'pattern' .` |

## Advanced Usage

### Chaining with Shell
```bash
# Use agent output in scripts
DISK_CMD=$(python agent.py "show disk usage command")
eval $DISK_CMD

# Save command for later
python agent.py "list all logs" > /tmp/log_command.sh
bash /tmp/log_command.sh
```

### Custom Configuration
Edit `config.json`:
```json
{
  "llm": {
    "model": "gpt-3.5-turbo",  // Use cheaper model
    "temperature": 0.1          // More deterministic
  },
  "security": {
    "command_timeout_seconds": 60  // Longer timeout
  }
}
```

### Adding New Commands to Database
Edit `linux_commands_db.json`:
```json
{
  "your_command": {
    "description": "What it does",
    "usage": "command [options]",
    "tags": ["keyword1", "keyword2"],
    "examples": ["example1", "example2"]
  }
}
```

## Troubleshooting

### Agent Not Responding
```bash
# Check if script is executable
chmod +x agent.py

# Check Python version
python --version  # Should be 3.7+

# Check dependencies
pip install -r requirements.txt
```

### Commands Not Working as Expected
```bash
# The agent runs in mock mode without API key
# Set OPENAI_API_KEY for better results
export OPENAI_API_KEY='your-key'

# Or check the mock responses in agent.py
# Edit _mock_llm_response() to add patterns
```

### Permission Errors
```bash
# Agent runs with user permissions
# For privileged commands, use sudo manually:
python agent.py "show system logs"
# Then run: sudo [command]
```

### Timeout Errors
```bash
# Increase timeout in config.json
# Or run long commands manually
```

## Tips & Best Practices

1. **Be Specific**: "show disk space in human readable format" vs "disk"
2. **Use Keywords**: Include command-related words (list, show, find, etc.)
3. **Review Commands**: Always check generated commands before trusting them
4. **History**: Use `history` command to track what you've done
5. **Mock Mode**: Test queries in mock mode before using API credits
6. **Safety**: The agent blocks dangerous commands, but always be careful

## Quick Commands Reference

```bash
# Show help
python agent.py --help   # (not implemented, just shows usage)

# Interactive
python agent.py

# Single query
python agent.py "your query"

# Demo
python demo.py

# Quick start
./quickstart.sh
```

## Environment Variables

| Variable | Purpose | Default |
|----------|---------|---------|
| `OPENAI_API_KEY` | OpenAI API authentication | None (mock mode) |
| `OPENAI_MODEL` | Model to use | gpt-4 |

## Files Overview

| File | Purpose |
|------|---------|
| `agent.py` | Main agent program |
| `demo.py` | Interactive demo script |
| `quickstart.sh` | Setup and run script |
| `linux_commands_db.json` | Commands knowledge base |
| `config.json` | Configuration settings |
| `requirements.txt` | Python dependencies |
| `.env.example` | Environment template |
| `README.md` | Full documentation |
| `ARCHITECTURE.md` | System design docs |

## Support

For issues or questions:
1. Check `README.md` for detailed documentation
2. Review `ARCHITECTURE.md` for system design
3. Run `demo.py` to see working examples
4. Open an issue on GitHub

## Next Steps

1. ✅ Run `./quickstart.sh` to get started
2. ✅ Try demo mode: `python demo.py`
3. ✅ Test in interactive mode: `python agent.py`
4. ✅ Add your API key for full functionality
5. ✅ Customize `linux_commands_db.json` for your needs
6. ✅ Build integrations with your workflows

---

**Happy commanding! 🚀**
