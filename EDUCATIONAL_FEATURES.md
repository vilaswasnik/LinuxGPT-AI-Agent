# 🎓 LinuxGPT - Educational Features

## Overview

LinuxGPT now includes **comprehensive educational features** with:
- **100+ Linux commands** with detailed explanations
- **30+ command combinations** showing real-world usage
- **Interactive learning mode** with tips and examples
- **Pattern recognition** for natural language queries

---

## 📚 What's New

### 1. Comprehensive Command Database

**linux_commands_db_comprehensive.json** includes:

✅ **60+ core commands** with:
- Detailed descriptions
- Common options explained
- Multiple examples with explanations
- Pro tips and best practices
- Category classification

✅ **30+ command combinations** including:
- Find and delete patterns
- Text processing pipelines
- System monitoring commands
- File management workflows
- Network diagnostics

### 2. Educational Mode Features

#### Explain Command
```bash
# Get detailed information about any command
python agent.py
Query> explain grep

📚 GREP - Search text using patterns
======================================================================
Usage: grep [OPTIONS] PATTERN [FILE]...

Common Options:
  -r: Recursive search in directories
  -i: Case-insensitive search
  -n: Show line numbers
  ...

Examples:
  $ grep 'error' logfile.txt
    → Find lines containing 'error'
  ...

💡 Tips:
  • Use grep -P for Perl-compatible regex
  • Combine with other commands: ps aux | grep nginx
```

#### View Combinations
```bash
Query> combinations

🔗 Common Command Combinations:
======================================================================

Find and delete files matching a pattern:
  $ find . -name '*.tmp' -type f -delete
  → Searches current directory for .tmp files and deletes them

Show disk usage sorted by size:
  $ du -sh * | sort -rh
  → du shows disk usage, sort -rh sorts reverse human-readable numbers
...
```

---

## 🎯 Usage Examples

### Basic Queries

| Query | Command | Educational Output |
|-------|---------|-------------------|
| `show disk space` | `df -h` | Shows df options and tips |
| `find large files` | `find . -type f -size +100M -exec ls -lh {} \;` | Explains find patterns |
| `list by size` | `ls -lhS` | Shows ls sorting options |
| `list by date` | `ls -lht` | Explains time sorting |

### Learning Commands

```bash
# Learn about a specific command
explain tar
explain grep
explain find
explain awk

# See common combinations
combinations

# View command history
history
```

### Natural Language Support

The agent now recognizes these patterns:

**File Operations:**
- "find large files" → `find . -type f -size +100M`
- "list by size" → `ls -lhS`
- "list by date" → `ls -lht`
- "show recent files" → `find . -type f -mtime -1`
- "find empty files" → `find . -empty`

**System Monitoring:**
- "show disk space" → `df -h`
- "disk usage sorted" → `du -sh * | sort -rh`
- "show memory" → `free -h`
- "show processes" → `ps aux`
- "monitor log" → `tail -f /var/log/syslog`

**Network:**
- "show listening ports" → `netstat -tuln | grep LISTEN`
- "test connectivity" → `ping google.com`
- "show network interfaces" → `ip addr show`

**Archives:**
- "compress directory" → `tar -czf archive.tar.gz directory/`
- "extract archive" → `tar -xzf archive.tar.gz`

---

## 📖 Command Categories

### File Operations (25+ commands)
`ls`, `cd`, `pwd`, `cat`, `cp`, `mv`, `rm`, `mkdir`, `touch`, `ln`, `find`, `locate`, `which`, `whereis`, `basename`, `dirname`, `readlink`, `realpath`, `stat`, `file`

### Text Processing (15+ commands)
`grep`, `awk`, `sed`, `cut`, `sort`, `uniq`, `tr`, `paste`, `join`, `split`, `wc`, `head`, `tail`, `tee`, `comm`

### System Information (20+ commands)
`ps`, `top`, `htop`, `free`, `df`, `du`, `uname`, `uptime`, `hostname`, `date`, `cal`, `who`, `w`, `last`, `id`, `groups`, `vmstat`, `iostat`, `lsblk`, `blkid`

### Process Management (10+ commands)
`kill`, `killall`, `pkill`, `pgrep`, `pidof`, `nice`, `renice`, `nohup`, `bg`, `fg`, `jobs`

### Network (15+ commands)
`netstat`, `ss`, `ping`, `traceroute`, `curl`, `wget`, `nc`, `nslookup`, `dig`, `host`, `whois`, `route`, `arp`, `ip`, `ifconfig`

### Compression (10+ commands)
`tar`, `gzip`, `gunzip`, `zip`, `unzip`, `bzip2`, `bunzip2`, `xz`, `unxz`, `zcat`

### Permissions (5+ commands)
`chmod`, `chown`, `chgrp`, `umask`, `setfacl`, `getfacl`

### System Management (10+ commands)
`systemctl`, `service`, `journalctl`, `cron`, `at`, `mount`, `umount`, `sudo`, `su`, `systemctl`

---

## 🎓 Learning Features

### 1. Command Options Explained

Every command includes common options with plain-English explanations:

```json
"ls": {
  "common_options": {
    "-l": "Long format with permissions, owner, size, date",
    "-a": "Show all files including hidden (starting with .)",
    "-h": "Human-readable sizes (KB, MB, GB)",
    "-t": "Sort by modification time, newest first",
    "-S": "Sort by file size, largest first"
  }
}
```

### 2. Real Examples with Explanations

Each command has multiple examples showing real-world usage:

```json
"examples": [
  {
    "command": "grep -rn 'TODO' .",
    "explanation": "Recursively search for 'TODO' with line numbers"
  },
  {
    "command": "grep -E 'error|warning|critical' app.log",
    "explanation": "Search for multiple patterns (OR logic)"
  }
]
```

### 3. Pro Tips

Learn best practices and advanced techniques:

```json
"tips": [
  "Use grep -P for Perl-compatible regex",
  "Combine with other commands: ps aux | grep nginx",
  "Use grep -c to count occurrences instead of piping to wc -l"
]
```

### 4. Command Combinations

Learn how to chain commands for powerful workflows:

```bash
# Find files and count by extension
find . -type f | sed 's/.*\.//' | sort | uniq -c | sort -rn

# Show top 10 memory-consuming processes
ps aux --sort=-%mem | head -11

# Monitor disk usage in real-time
watch -n 2 'df -h'
```

---

## 🚀 How to Use

### Interactive Mode (Recommended for Learning)

```bash
python agent.py

📚 Special Commands:
  • 'explain <command>' - Get detailed info about a command
  • 'combinations' - See common command combinations
  • 'history' - View command history
  • 'quit' or 'exit' - Stop the agent

Query> explain tar
[Detailed explanation shown]

Query> combinations
[30+ combinations displayed]

Query> find large files
Command: find . -type f -size +100M -exec ls -lh {} \;
📚 Educational Info about 'find':
   Search for files and directories in hierarchy
   Common Options:
   -name: Search by filename (case-sensitive)
   -type f: Find files only
   -size +10M: Files larger than 10MB
   💡 Tip: Use -maxdepth N to limit search depth
```

### Command Line Mode

```bash
# Quick queries
python agent.py "show disk space"
python agent.py "find python files"
python agent.py "list by size"
```

### Learning Path

1. **Start with basics:**
   ```
   explain ls
   explain cd
   explain pwd
   ```

2. **Learn text processing:**
   ```
   explain grep
   explain awk
   explain sed
   ```

3. **Explore combinations:**
   ```
   combinations
   find large files
   list by size
   ```

4. **Practice with queries:**
   ```
   show disk usage sorted
   find recent files
   monitor log files
   ```

---

## 📊 Database Statistics

- **Total Commands**: 60+ with detailed documentation
- **Command Combinations**: 30+ real-world examples
- **Total Examples**: 200+ with explanations
- **Categories**: 8 major categories
- **Options Documented**: 300+ command options explained
- **Pro Tips**: 150+ best practices and tips

---

## 🔧 Configuration

The agent automatically loads the comprehensive database if available:

```python
# Priority order:
1. linux_commands_db_comprehensive.json (detailed)
2. linux_commands_db.json (basic fallback)
```

Enable/disable educational mode:

```python
agent = LinuxGPT(educational_mode=True)  # Default
```

---

## 💡 Advanced Features

### Pattern Recognition

The mock LLM now recognizes 25+ query patterns:
- File operations (list, find, show)
- System monitoring (disk, memory, processes)
- Network commands (ports, connections)
- Text processing (search, count, sort)
- Archives (compress, extract)

### Contextual Help

Commands show relevant context automatically:
- Options used in the command
- Related commands
- Common pitfalls
- Best practices

### Safety Information

Some combinations include safer alternatives:

```json
"find_and_delete": {
  "command": "find . -name '*.tmp' -type f -delete",
  "safer_alternative": "find . -name '*.tmp' -type f -exec rm -i {} \\;"
}
```

---

## 🎯 Use Cases

### 1. Learning Linux
- Explore commands interactively
- See real examples with explanations
- Learn best practices and tips

### 2. Quick Reference
- Fast lookup of command options
- Find command combinations
- Get syntax reminders

### 3. System Administration
- Monitor system resources
- Troubleshoot issues
- Automate tasks

### 4. Development
- Find files quickly
- Process logs
- Manage processes

---

## 📚 Next Steps

1. **Try the explain command** for any Linux command you want to learn
2. **Explore combinations** to see how commands work together
3. **Practice with natural language** queries to build intuition
4. **Review command history** to track what you've learned

---

## 🤝 Contributing

To add more commands or combinations, edit:
- `linux_commands_db_comprehensive.json`

Format:
```json
"command_name": {
  "description": "What it does",
  "usage": "command [options]",
  "category": "category_name",
  "tags": ["tag1", "tag2"],
  "common_options": {
    "-option": "What it does"
  },
  "examples": [
    {
      "command": "example command",
      "explanation": "What this does"
    }
  ],
  "tips": ["Helpful tip"]
}
```

---

**The system is now a comprehensive Linux learning platform! 🚀📚**
