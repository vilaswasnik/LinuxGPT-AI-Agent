#!/usr/bin/env python3
"""
Linux Command Agent - Natural Language to Linux Command System

This agent converts natural language queries into appropriate Linux commands,
executes them, and returns the results. It uses an LLM for reasoning and 
command generation based on a Linux commands database.
"""

import os
import subprocess
import json
import sys
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass

# Load environment variables from .env file
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # python-dotenv not installed, will use system env vars


@dataclass
class CommandResult:
    """Result of command execution"""
    success: bool
    output: str
    error: str
    command: str


class LinuxCommandDatabase:
    """Database of Linux commands with descriptions and examples"""
    
    def __init__(self, db_file: str = "linux_commands_db.json"):
        self.db_file = db_file
        self.comprehensive_db = "linux_commands_db_comprehensive.json"
        self.commands = self._load_database()
        self.combinations = self.commands.get('command_combinations', {})
    
    def _load_database(self) -> Dict:
        """Load the commands database from JSON file"""
        # Try comprehensive database first
        if os.path.exists(self.comprehensive_db):
            with open(self.comprehensive_db, 'r') as f:
                return json.load(f)
        # Fallback to simple database
        elif os.path.exists(self.db_file):
            with open(self.db_file, 'r') as f:
                return json.load(f)
        return {}
    
    def search(self, query: str) -> List[Dict]:
        """Search for relevant commands based on query keywords"""
        query_lower = query.lower()
        relevant = []
        
        # Skip metadata
        commands_dict = {k: v for k, v in self.commands.items() 
                        if k not in ['_meta', 'command_combinations']}
        
        for cmd, info in commands_dict.items():
            if isinstance(info, dict):
                if (query_lower in cmd.lower() or 
                    query_lower in info.get('description', '').lower() or
                    any(query_lower in str(tag).lower() for tag in info.get('tags', []))):
                    relevant.append({
                        'command': cmd,
                        'description': info.get('description', ''),
                        'usage': info.get('usage', ''),
                        'examples': info.get('examples', []),
                        'tips': info.get('tips', []),
                        'category': info.get('category', '')
                    })
        
        return relevant
    
    def get_combination(self, query: str) -> Optional[Dict]:
        """Search for relevant command combinations"""
        query_lower = query.lower()
        for combo_name, combo_info in self.combinations.items():
            if (query_lower in combo_info.get('description', '').lower() or
                any(query_lower in str(tag).lower() for tag in combo_info.get('tags', []))):
                return combo_info
        return None
    
    def get_command_details(self, command: str) -> Optional[Dict]:
        """Get detailed information about a specific command"""
        return self.commands.get(command, None)
    
    def get_context(self) -> str:
        """Get formatted context for LLM"""
        context = "Linux Commands Database:\n\n"
        commands_dict = {k: v for k, v in self.commands.items() 
                        if k not in ['_meta', 'command_combinations']}
        
        for cmd, info in list(commands_dict.items())[:30]:  # Limit to avoid token overflow
            if isinstance(info, dict):
                context += f"Command: {cmd}\n"
                context += f"Description: {info.get('description', '')}\n"
                if info.get('usage'):
                    context += f"Usage: {info.get('usage', '')}\n"
                if info.get('examples'):
                    examples = info.get('examples', [])
                    if examples and isinstance(examples[0], dict):
                        context += f"Example: {examples[0].get('command', '')}\n"
                    elif examples:
                        context += f"Examples: {', '.join(examples[:2])}\n"
                context += "\n"
        return context


class LLMInterface:
    """Interface for LLM interaction (OpenAI API compatible)"""
    
    def __init__(self, api_key: Optional[str] = None, model: str = "gpt-4"):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.model = model
        self.use_mock = not self.api_key  # Use mock if no API key
    
    def query(self, prompt: str, system_prompt: str) -> str:
        """Query the LLM with a prompt"""
        if self.use_mock:
            return self._mock_llm_response(prompt)
        
        try:
            import openai
            client = openai.OpenAI(api_key=self.api_key)
            
            response = client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
                max_tokens=500
            )
            
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"LLM API Error: {e}", file=sys.stderr)
            return self._mock_llm_response(prompt)
    
    def _mock_llm_response(self, prompt: str) -> str:
        """Mock LLM response for testing without API key"""
        prompt_lower = prompt.lower()
        
        # Extract the actual query from the prompt
        if "user query:" in prompt_lower:
            query_start = prompt.lower().find("user query:") + len("user query:")
            # Find the end of the line (first newline after query)
            query_part = prompt[query_start:]
            newline_pos = query_part.find("\n")
            if newline_pos > 0:
                actual_query = query_part[:newline_pos].strip().lower()
            else:
                actual_query = query_part.strip().lower()
        else:
            actual_query = prompt_lower.strip()
        
        # Check natural language patterns first (before direct command check)
        # Pattern matching for natural language queries  
        if "large" in actual_query and "file" in actual_query:
            return "find . -type f -size +100M -exec ls -lh {} \\;"
        elif ("list" in actual_query or "show" in actual_query) and "size" in actual_query:
            return "ls -lhS"
        elif ("list" in actual_query or "show" in actual_query) and ("date" in actual_query or "time" in actual_query):
            return "ls -lht"
        elif "disk usage" in actual_query and "sort" in actual_query:
            return "du -sh * | sort -rh"
        elif "recent" in actual_query and ("file" in actual_query or "modified" in actual_query):
            return "find . -type f -mtime -1"
        elif ("partition" in actual_query or "block" in actual_query or "lsblk" in actual_query) and not "format" in actual_query:
            return "lsblk -f"
        elif "fdisk" in actual_query or ("disk" in actual_query and "partition" in actual_query):
            return "sudo fdisk -l"
        elif "iostat" in actual_query or ("io" in actual_query and "stat" in actual_query):
            return "iostat -x 1 5"
        elif "var" in actual_query and "log" in actual_query:
            return "ls -lht /var/log/ | head -20"
        elif ("error" in actual_query or "errors" in actual_query) and "log" in actual_query:
            return "grep -i error /var/log/syslog | tail -20"
        elif "latest" in actual_query and "log" in actual_query:
            return "tail -f /var/log/syslog"
        
        # If user typed a direct command, return it as-is
        direct_commands = ['ls', 'pwd', 'cd', 'cat', 'grep', 'find', 'ps', 'top', 'df', 'du', 
                          'free', 'uptime', 'uname', 'whoami', 'date', 'cal', 'history',
                          'netstat', 'ss', 'ip', 'ifconfig', 'ping', 'curl', 'wget', 'lsblk',
                          'fdisk', 'iostat', 'vmstat', 'lsof', 'dmesg', 'journalctl', 'dir']
        first_word = actual_query.split()[0] if actual_query.split() else ''
        
        # Handle dir command (alias for ls)
        if first_word == 'dir':
            return actual_query.replace('dir', 'ls', 1)
        
        if first_word in direct_commands:
            return actual_query
        
        # More natural language patterns
        if ("list" in actual_query or "show" in actual_query) and "file" in actual_query:
            return "ls -la"
        elif "list" in actual_query and ("command" in actual_query or "available" in actual_query):
            return "compgen -c | head -50"
        elif "get" in actual_query and "file" in actual_query:
            return "ls -la"
        elif "current directory" in actual_query or "working directory" in actual_query or actual_query == "pwd":
            return "pwd"
        elif "change directory" in actual_query or "go to" in actual_query:
            return "cd /"
        elif "disk" in actual_query and ("space" in actual_query or "usage" in actual_query):
            return "df -h"
        elif ("process" in actual_query or "running" in actual_query) and not "stop" in actual_query:
            return "ps aux"
        elif "network" in actual_query and "connection" in actual_query:
            return "netstat -tuln"
        elif "network" in actual_query and "interface" in actual_query:
            return "ip addr show"
        elif "memory" in actual_query or "ram" in actual_query:
            return "free -h"
        elif "system" in actual_query and ("info" in actual_query or "information" in actual_query):
            return "uname -a"
        elif "uptime" in actual_query:
            return "uptime"
        elif "find" in actual_query and ("file" in actual_query or "python" in actual_query):
            return "find . -type f -name '*.py'"
        elif "search" in actual_query or "grep" in actual_query:
            return "grep -r 'pattern' ."
        elif "cpu" in actual_query:
            return "top -bn1 | head -20"
        elif "who" in actual_query and "logged" in actual_query:
            return "who"
        elif "user" in actual_query:
            return "whoami"
        elif "help" in actual_query and "memory" in actual_query:
            return "free -h"
        elif "monitor" in actual_query and "log" in actual_query:
            return "tail -f /var/log/syslog"
        elif "port" in actual_query and ("using" in actual_query or "listen" in actual_query):
            return "netstat -tuln | grep LISTEN"
        elif "archive" in actual_query or ("compress" in actual_query and "directory" in actual_query):
            return "tar -czf archive.tar.gz directory/"
        elif "extract" in actual_query:
            return "tar -xzf archive.tar.gz"
        elif "count" in actual_query and "line" in actual_query:
            return "wc -l file.txt"
        elif "empty" in actual_query and "file" in actual_query:
            return "find . -empty"
        elif "watch" in actual_query:
            return "watch -n 2 'command'"
        elif "help" in actual_query or "how" in actual_query or "command" in actual_query:
            return "echo 'Available: ls (files), df (disk), free (memory), ps (processes), pwd (directory), uname (system)'"
        elif "hi" == actual_query or "hello" == actual_query or "hey" == actual_query:
            return "echo 'Hello! I can help you with Linux commands. Try: show files, disk space, list processes, etc.'"
        else:
            # Better fallback - try to be helpful
            return "echo 'Query not recognized. Try: show files, disk space, memory, processes, find large files, etc.'"


class LinuxCommandAgent:
    """Main agent that processes queries and executes commands"""
    
    def __init__(self, db_file: str = "linux_commands_db.json", educational_mode: bool = True):
        self.db = LinuxCommandDatabase(db_file)
        self.llm = LLMInterface()
        self.command_history = []
        self.educational_mode = educational_mode
    
    def explain_command(self, command: str) -> Optional[str]:
        """Provide educational explanation for a command"""
        cmd_name = command.split()[0] if command else ""
        details = self.db.get_command_details(cmd_name)
        
        if details and isinstance(details, dict):
            explanation = f"\n📚 Educational Info about '{cmd_name}':\n"
            explanation += f"   {details.get('description', '')}\n"
            
            if details.get('common_options'):
                explanation += "\n   Common Options:\n"
                for opt, desc in list(details.get('common_options', {}).items())[:3]:
                    explanation += f"   {opt}: {desc}\n"
            
            if details.get('tips'):
                tips = details.get('tips', [])
                if tips:
                    explanation += f"\n   💡 Tip: {tips[0]}\n"
            
            return explanation
        return None
    
    def process_query(self, query: str) -> Tuple[str, CommandResult]:
        """Process natural language query and return command + result"""
        
        # Step 1: Search relevant commands in database
        relevant_commands = self.db.search(query)
        
        # Step 2: Build context for LLM
        system_prompt = """You are a Linux command expert assistant. Your job is to convert 
natural language queries into appropriate Linux commands. Return ONLY the command itself, 
without any explanation or markdown formatting. The command should be safe to execute.

Guidelines:
- Return only the command, nothing else
- Use common, safe Linux commands
- Avoid destructive operations unless explicitly requested
- Use appropriate flags for human-readable output (e.g., -h for human-readable sizes)
- If query is ambiguous, choose the most common interpretation"""

        context = ""
        if relevant_commands:
            context = "\n\nRelevant commands from database:\n"
            for cmd in relevant_commands[:5]:
                context += f"- {cmd['command']}: {cmd['description']}\n"
                if cmd['usage']:
                    context += f"  Usage: {cmd['usage']}\n"
        
        prompt = f"User query: {query}{context}\n\nLinux command:"
        
        # Step 3: Get command from LLM
        command = self.llm.query(prompt, system_prompt)
        command = command.strip().strip('`').strip()
        
        # Remove any markdown code block formatting if present
        if command.startswith('bash\n') or command.startswith('sh\n'):
            command = '\n'.join(command.split('\n')[1:])
        
        # Clean up mock response artifacts
        if command.startswith('# Mock response:'):
            # Extract just the command part after the comment
            lines = command.split('\n')
            if len(lines) > 1:
                command = lines[-1].strip()
            else:
                command = "echo 'Unable to determine command'"
        
        # Detect conversational responses (not actual commands)
        # Check if the response looks like a sentence rather than a command
        conversational_starters = ['the user', 'i cannot', 'please', 'sorry', 'could you', 
                                   'unable to', 'does not', 'is not', 'are not', 'cannot',
                                   'hello', 'hi there', 'greetings', 'your query', 'this query',
                                   'you are', 'i am', 'provide more']
        command_lower = command.lower()
        
        # Check if starts with conversational text OR contains question words
        is_conversational = (any(command_lower.startswith(starter) for starter in conversational_starters) or
                           any(word in command_lower[:30] for word in ['query is', 'more details', 'more information']))
        
        if is_conversational:
            # Handle greetings
            if any(word in query.lower() for word in ['hi', 'hello', 'hey', 'greetings']):
                command = "echo '👋 Hello! I can help you with Linux commands. Try: show files, disk space, list processes, etc.'"
            # Handle questions about previous output
            elif any(word in query.lower() for word in ['which', 'what', 'where', 'from which', 'this is']):
                if self.command_history:
                    last_cmd = self.command_history[-1]['command']
                    command = f"echo 'Previous command was: {last_cmd}'"
                else:
                    command = "echo 'No previous command to reference'"
            else:
                command = "echo 'Query not clear. Try specific commands like: show disk space, list files, find large files, check memory'"
        
        # Step 4: Execute the command
        result = self._execute_command(command)
        
        # Step 5: Store in history
        self.command_history.append({
            'query': query,
            'command': command,
            'success': result.success
        })
        
        return command, result
    
    def _execute_command(self, command: str) -> CommandResult:
        """Execute a Linux command safely"""
        try:
            # Check if it's a cd command (won't persist)
            if command.strip().startswith('cd '):
                # Note: cd doesn't persist across commands since each runs in new shell
                path = command.strip()[3:].strip()
                if os.path.exists(path) and os.path.isdir(path):
                    return CommandResult(
                        success=True,
                        output=f"Note: 'cd' command executed, but directory change doesn't persist.\nTo work in {path}, use commands like: ls {path}, cat {path}/file.txt",
                        error="",
                        command=command
                    )
                else:
                    return CommandResult(
                        success=False,
                        output="",
                        error=f"Directory not found: {path}",
                        command=command
                    )
            
            # Security check: prevent obviously dangerous commands
            dangerous_patterns = ['rm -rf /', 'mkfs', ':(){ :|:& };:', 'dd if=/dev/']
            for pattern in dangerous_patterns:
                if pattern in command:
                    return CommandResult(
                        success=False,
                        output="",
                        error=f"Command blocked for safety: contains dangerous pattern '{pattern}'",
                        command=command
                    )
            
            # Execute command
            process = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=30
            )
            
            return CommandResult(
                success=process.returncode == 0,
                output=process.stdout,
                error=process.stderr,
                command=command
            )
            
        except subprocess.TimeoutExpired:
            return CommandResult(
                success=False,
                output="",
                error="Command execution timed out (30s limit)",
                command=command
            )
        except Exception as e:
            return CommandResult(
                success=False,
                output="",
                error=str(e),
                command=command
            )
    
    def get_history(self) -> List[Dict]:
        """Get command history"""
        return self.command_history


def main():
    """Main entry point for the agent"""
    print("=" * 60)
    print("Linux Command Agent - Natural Language Interface")
    print("=" * 60)
    print()
    
    # Check for API key
    if not os.getenv("OPENAI_API_KEY"):
        print("⚠️  No OPENAI_API_KEY found. Using mock LLM mode.")
        print("   Set OPENAI_API_KEY environment variable for full functionality.")
        print()
    
    agent = LinuxCommandAgent()
    
    # Interactive mode
    if len(sys.argv) > 1:
        # Command line mode
        query = ' '.join(sys.argv[1:])
        command, result = agent.process_query(query)
        
        print(f"Query: {query}")
        print(f"Command: {command}")
        print()
        
        if result.success:
            print("Output:")
            print(result.output)
        else:
            print("Error:")
            print(result.error)
    else:
        # Interactive mode
        print("Enter your queries in natural language.")
        print("\n📚 Special Commands:")
        print("  • 'explain <command>' - Get detailed info about a command")
        print("  • 'combinations' - See common command combinations")
        print("  • 'history' - View command history")
        print("  • 'quit' or 'exit' - Stop the agent")
        print("\n💡 Try queries like: 'show disk space', 'find large files', 'list by size'")
        print()
        
        while True:
            try:
                query = input("Query> ").strip()
                
                if not query:
                    continue
                
                if query.lower() in ['quit', 'exit', 'q']:
                    print("\nGoodbye!")
                    break
                
                if query.lower() == 'history':
                    print("\nCommand History:")
                    for i, entry in enumerate(agent.get_history(), 1):
                        status = "✓" if entry['success'] else "✗"
                        print(f"{i}. [{status}] {entry['query']} → {entry['command']}")
                    print()
                    continue
                
                # Check for explain command
                if query.lower().startswith('explain '):
                    cmd_to_explain = query[8:].strip()
                    details = agent.db.get_command_details(cmd_to_explain)
                    if details and isinstance(details, dict):
                        print(f"\n📚 {cmd_to_explain.upper()} - {details.get('description', '')}")
                        print("=" * 70)
                        if details.get('usage'):
                            print(f"\nUsage: {details.get('usage', '')}")
                        if details.get('common_options'):
                            print("\nCommon Options:")
                            for opt, desc in details.get('common_options', {}).items():
                                print(f"  {opt}: {desc}")
                        if details.get('examples'):
                            print("\nExamples:")
                            examples = details.get('examples', [])
                            for ex in examples[:5]:
                                if isinstance(ex, dict):
                                    print(f"  $ {ex.get('command', '')}")
                                    print(f"    → {ex.get('explanation', '')}")
                                else:
                                    print(f"  $ {ex}")
                        if details.get('tips'):
                            print("\n💡 Tips:")
                            for tip in details.get('tips', []):
                                print(f"  • {tip}")
                        print()
                    else:
                        print(f"\n⚠️  No detailed information available for '{cmd_to_explain}'")
                    print()
                    continue
                
                # Check for combinations
                if query.lower() == 'combinations' or query.lower() == 'combos':
                    print("\n🔗 Common Command Combinations:")
                    print("=" * 70)
                    for name, combo in list(agent.db.combinations.items())[:10]:
                        print(f"\n{combo.get('description', '')}:")
                        print(f"  $ {combo.get('command', '')}")
                        if combo.get('explanation'):
                            print(f"  → {combo.get('explanation', '')}")
                    print("\n💡 Try these combinations or ask in natural language!")
                    print()
                    continue
                
                print()
                command, result = agent.process_query(query)
                
                # Show educational info if enabled
                if agent.educational_mode and command:
                    explanation = agent.explain_command(command)
                    if explanation:
                        print(explanation)
                
                print(f"Command: {command}")
                print("-" * 60)
                
                if result.success:
                    if result.output:
                        print(result.output)
                    else:
                        print("(Command executed successfully with no output)")
                else:
                    print(f"Error: {result.error}")
                
                print()
                
            except KeyboardInterrupt:
                print("\n\nGoodbye!")
                break
            except Exception as e:
                print(f"Error: {e}")
                print()


if __name__ == "__main__":
    main()
