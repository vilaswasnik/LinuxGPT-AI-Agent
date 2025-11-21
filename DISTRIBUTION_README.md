# LinuxGPT - Distribution Package

**Natural Language to Linux Command Converter**  
Version 2.0 | 144 Commands | 425+ Examples

---

## 🚀 Quick Start (Zero Installation)

Just extract and run:

```bash
# Extract the package
tar -xzf linuxgpt-v2.0-linux.tar.gz
cd linuxgpt-v2.0-linux

# Run directly (no installation needed!)
./linuxgpt "show disk space"
./linuxgpt "find large files"
./linuxgpt                      # Interactive mode
```

**First run** will automatically install required Python dependencies.

---

## 📦 Installation Options

### Option 1: Portable (Recommended for testing)
No installation needed - just run `./linuxgpt` from the extracted directory.

### Option 2: User Installation
Install to `~/.local/linuxgpt` for access from anywhere:

```bash
./install.sh
```

Then use from anywhere:
```bash
linuxgpt "list processes"
```

### Option 3: System-wide Installation
Install to `/opt/linuxgpt` (requires sudo):

```bash
sudo ./install.sh
```

---

## 🎯 Usage Examples

```bash
# Natural language queries
./linuxgpt "show disk usage"
./linuxgpt "find files modified today"
./linuxgpt "compress a directory"
./linuxgpt "check network connections"

# Get explanations
./linuxgpt "explain rsync"
./linuxgpt "what does strace do"

# Interactive mode
./linuxgpt
> show running processes
> how to use grep
> exit
```

---

## ⚙️ Configuration

### OpenAI API Key (Optional)

LinuxGPT works in **mock mode** without an API key, but you can enable GPT-4 for better results:

1. Copy the example file:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` and add your key:
   ```
   OPENAI_API_KEY=sk-your-key-here
   OPENAI_MODEL=gpt-4
   ```

**Mock mode** provides intelligent responses using pattern matching - perfect for learning and most use cases!

---

## 📋 Requirements

- **Python 3.7+** (most Linux systems have this)
- **pip** (for auto-installing dependencies)
- **Internet connection** (first run only, for dependencies)

Dependencies installed automatically:
- `openai` (if using API mode)
- `python-dotenv` (for configuration)

---

## ✨ Features

- ✅ **144 Linux commands** with comprehensive documentation
- ✅ **425+ examples** with step-by-step explanations
- ✅ **Natural language processing** - ask in plain English
- ✅ **Educational mode** - learn as you use
- ✅ **Safe execution** - validates dangerous commands
- ✅ **Works offline** - mock mode for learning
- ✅ **Command combinations** - real-world pipelines
- ✅ **Multi-category** - file ops, networking, processes, disk, text, security

---

## 📚 Command Categories

### Text Editors & Processing
`vim`, `nano`, `awk`, `sed`, `cut`, `paste`, `tr`, `grep`, `sort`, `uniq`

### Networking
`rsync`, `scp`, `ssh`, `nmap`, `nc`, `dig`, `host`, `curl`, `wget`, `iptables`, `ufw`

### System & Process
`ps`, `top`, `htop`, `kill`, `pkill`, `nice`, `strace`, `ltrace`, `lsof`

### File Operations
`ls`, `find`, `locate`, `stat`, `file`, `diff`, `split`, `tar`, `zip`

### Disk & Storage
`df`, `du`, `lsblk`, `fdisk`, `mount`, `rsync`, `dd`, `fsck`

### Compression
`gzip`, `bzip2`, `xz`, `tar`, `zip`, `unzip`, `zcat`

### Debugging & Analysis
`strace`, `ltrace`, `ldd`, `strings`, `hexdump`, `xxd`, `od`

### Session Management
`screen`, `tmux`, `nohup`

---

## 🔒 Security Features

- **Dangerous command detection** - blocks destructive operations
- **Timeout protection** - 30-second execution limit  
- **Safe defaults** - validates before execution
- **Educational warnings** - explains risks

---

## 🆘 Troubleshooting

### "Command not found" after installation
Add to your PATH in `~/.bashrc`:
```bash
export PATH="$PATH:$HOME/.local/bin"
```

### Missing Python dependencies
Install manually if auto-install fails:
```bash
pip3 install --user openai python-dotenv
```

### Permission errors
Make sure the script is executable:
```bash
chmod +x linuxgpt
```

---

## 📖 Documentation Files

- `INSTALL.txt` - Quick installation guide
- `CHANGELOG.md` - Version history and updates
- `README.md` - Comprehensive documentation

---

## 🌟 Example Session

```bash
$ ./linuxgpt "find large files in current directory"

Query: find large files in current directory
Command: find . -type f -size +100M -exec ls -lh {} \;

Explanation:
  • find . -type f: Search for files in current directory
  • -size +100M: Files larger than 100MB
  • -exec ls -lh {}: Show details in human-readable format

$ ./linuxgpt "explain rsync"

rsync - Fast, versatile file copying tool for remote and local

Usage: rsync [OPTIONS] SOURCE DEST

Common Options:
  -a    Archive mode (recursive, preserves)
  -v    Verbose output
  -z    Compress during transfer
  -P    Show progress
  --delete    Delete files not in source

Examples:
  1. rsync -avz /source/ /dest/
     Sync local directories

  2. rsync -avz -e ssh /local/ user@host:/remote/
     Sync to remote server

Tips:
  • Trailing slash on source matters!
  • Use -n (dry-run) first to test
  • Much faster than cp for large transfers
```

---

## 🔗 Links

- **GitHub**: https://github.com/vilaswasnik/sample.ai
- **Issues**: Report bugs and feature requests
- **Contribute**: Pull requests welcome!

---

## 📄 License

MIT License - Free to use, modify, and distribute

---

## 🎓 Learning Mode

LinuxGPT is designed to be educational. Every command comes with:
- Detailed explanations
- Multiple real-world examples
- Tips and best practices
- Common pitfalls to avoid
- Related commands

Perfect for:
- Linux beginners learning commands
- Experienced users discovering new tools
- Quick reference without man pages
- Teaching and training environments

---

## 💡 Tips

1. **Start simple**: Try basic queries like "list files" or "show disk space"
2. **Be specific**: More context = better results
3. **Use explain**: Ask "explain <command>" to learn
4. **Mock mode is smart**: Works great without API key
5. **Check history**: Review past commands for learning

---

## 🚀 Get Started Now!

```bash
./linuxgpt "show me what you can do"
```

Enjoy using LinuxGPT! 🐧✨
