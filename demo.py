#!/usr/bin/env python3
"""
Test script to demonstrate the Linux Command Agent functionality
"""

import sys
import os

# Add current directory to path to import agent
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from agent import LinuxCommandAgent


def print_section(title):
    """Print a formatted section header"""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)


def run_test_query(agent, query):
    """Run a test query and display results"""
    print(f"\n📝 Query: {query}")
    print("-" * 70)
    
    command, result = agent.process_query(query)
    
    print(f"🔧 Command: {command}")
    print("-" * 70)
    
    if result.success:
        print("✅ Success!")
        if result.output:
            # Limit output to first 10 lines for demo
            lines = result.output.strip().split('\n')
            if len(lines) > 10:
                print('\n'.join(lines[:10]))
                print(f"... ({len(lines) - 10} more lines)")
            else:
                print(result.output)
        else:
            print("(No output)")
    else:
        print(f"❌ Error: {result.error}")
    
    print()


def main():
    print_section("Linux Command Agent - Demo Script")
    
    print("\n🤖 Initializing agent...")
    
    # Check for API key
    if not os.getenv("OPENAI_API_KEY"):
        print("⚠️  Running in MOCK MODE (no OPENAI_API_KEY set)")
        print("   Results will use pattern matching instead of AI")
    else:
        print("✓ OpenAI API key detected - using full LLM mode")
    
    agent = LinuxCommandAgent()
    
    # Test queries covering different categories
    test_queries = [
        "show me list of files in directory",
        "what's my current directory?",
        "show disk space usage",
        "show memory usage",
        "show running processes",
        "what's the system information?",
        "find text files in current directory"
    ]
    
    print_section("Running Test Queries")
    
    for i, query in enumerate(test_queries, 1):
        print(f"\n[Test {i}/{len(test_queries)}]")
        run_test_query(agent, query)
        
        # Small pause between tests for readability
        if i < len(test_queries):
            input("Press Enter to continue to next test...")
    
    # Show history
    print_section("Command History")
    print("\n📚 Commands executed during this session:\n")
    
    for i, entry in enumerate(agent.get_history(), 1):
        status = "✓" if entry['success'] else "✗"
        print(f"{i}. [{status}] {entry['query']}")
        print(f"   → {entry['command']}")
        print()
    
    # Summary
    print_section("Demo Complete")
    history = agent.get_history()
    successful = sum(1 for entry in history if entry['success'])
    total = len(history)
    
    print(f"\n📊 Summary:")
    print(f"   Total queries: {total}")
    print(f"   Successful: {successful}")
    print(f"   Failed: {total - successful}")
    print(f"   Success rate: {(successful/total*100):.1f}%")
    
    print("\n✨ To run the agent interactively, use:")
    print("   python agent.py")
    print("\n✨ To run a single command, use:")
    print("   python agent.py \"your query here\"")
    print()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Demo interrupted. Goodbye!")
    except Exception as e:
        print(f"\n❌ Error during demo: {e}")
        import traceback
        traceback.print_exc()
