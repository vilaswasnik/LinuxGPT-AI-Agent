#!/usr/bin/env python3
"""
LinuxGPT Launcher
Portable launcher that includes all dependencies
"""

import sys
import os
import subprocess

def check_dependencies():
    """Check and install required dependencies"""
    required = ['openai', 'python-dotenv']
    missing = []
    
    for package in required:
        try:
            __import__(package.replace('-', '_'))
        except ImportError:
            missing.append(package)
    
    if missing:
        print(f"📦 Installing missing dependencies: {', '.join(missing)}")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--user'] + missing)
        print("✅ Dependencies installed!\n")

def main():
    # Check dependencies first
    check_dependencies()
    
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Import and run the agent
    sys.path.insert(0, script_dir)
    
    # Import agent module
    import agent
    
    # Run main
    if len(sys.argv) > 1:
        query = ' '.join(sys.argv[1:])
        linux_agent = agent.LinuxGPT()
        result = linux_agent.process_query(query)
        print(result)
    else:
        # Interactive mode
        from agent import main as agent_main
        agent_main()

if __name__ == '__main__':
    main()
