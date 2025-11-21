# LinuxGPT Command Database Expansion Plan

## Current Status
- **Current Commands**: 110+
- **Target**: 200-250 high-value commands
- **Strategy**: Add most commonly used and educational commands

## Priority Commands to Add

### Phase 1: Text Editors & Processing (20 commands)
- vim, nano, emacs, vi
- sed (expanded with more examples)
- awk (expanded with more examples)  
- cut, paste, join, tr, expand, unexpand
- diff, patch, cmp, comm
- column, pr, fmt, fold

### Phase 2: Compression & Archives (15 commands)
- gzip, gunzip, zcat, zless, zgrep
- bzip2, bunzip2, bzcat
- xz, unxz, xzcat
- zip, unzip (expanded)
- rar, unrar

### Phase 3: Advanced Networking (25 commands)
- nmap, tcpdump, wireshark, tshark
- iptables, firewall-cmd, ufw
- nc (netcat), telnet
- ftp, sftp, scp, rsync
- nslookup, dig, host, whois
- route, arp, arping
- mtr, iftop, nethogs, bmon

### Phase 4: System Monitoring & Debugging (20 commands)
- strace, ltrace, gdb
- perf, ftrace, systemd-analyze
- ldd, nm, objdump, readelf
- hexdump, od, xxd
- smartctl, sensors, acpi
- uptime, w, last, lastlog

### Phase 5: Shell & Scripting (25 commands)
- bash, sh, dash, zsh
- export, source, alias, unalias
- type, which, whereis, command
- echo, printf, read, test
- expr, bc, dc
- env, printenv, set, unset
- exec, eval, shift, getopts

### Phase 6: Security & Permissions (20 commands)
- sudo (expanded), visudo
- chroot, setfacl, getfacl
- chattr, lsattr
- umask, sg, newgrp, gpasswd
- groupadd, groupdel, groupmod
- pwck, grpck, vipw, vigr
- ssh-keygen, ssh-copy-id, ssh-agent

### Phase 7: Scheduling & Automation (12 commands)
- at, batch, atq, atrm
- crontab (expanded), anacron
- watch (expanded), timeout
- nice, renice, ionice, taskset

### Phase 8: Process & Resource Management (15 commands)
- kill (expanded), killall, pkill, pgrep
- nohup, disown, bg, fg, jobs (expanded)
- ulimit, prlimit
- cpulimit, cgexec, cgcreate

### Phase 9: File System & Storage (15 commands)
- sync, fsync
- fuser, lsof (expanded)
- mount (expanded), umount, mountpoint
- e2label, tune2fs (expanded), debugfs
- xfs_info, xfs_repair, xfs_admin
- badblocks, smartctl

### Phase 10: Miscellaneous Essential (13 commands)
- screen, tmux, byobu
- tee, xargs (expanded)
- basename, dirname, realpath
- seq, shuf, factor
- yes, sleep, true, false

## Implementation Strategy

1. **Batch Addition**: Add 20-30 commands at a time
2. **Full Documentation**: Each command includes:
   - Description
   - Usage pattern
   - Common options (3-5)
   - Examples (3-5 with explanations)
   - Tips & best practices (2-3)
   - Category and tags

3. **Testing**: Test agent with new commands after each batch
4. **Git Commits**: Commit in logical batches

## Expected Outcome
- **Total Commands**: 210-250
- **Total Examples**: 700-800
- **Categories**: 15+
- **Comprehensive coverage** of essential Linux administration, development, and daily use commands
