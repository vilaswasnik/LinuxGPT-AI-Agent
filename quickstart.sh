#!/bin/bash
# Quick Start Script for LinuxGPT

echo "╔═════════════════════════════════════════════════════════════════╗"
echo "║                   LinuxGPT - Quick Start                       ║"
echo "╚═════════════════════════════════════════════════════════════════╝"
echo ""

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.7 or higher."
    exit 1
fi

echo "✓ Python 3 found: $(python3 --version)"
echo ""

# Check if pip is available
if ! command -v pip3 &> /dev/null && ! command -v pip &> /dev/null; then
    echo "❌ pip is not installed. Please install pip."
    exit 1
fi

echo "✓ pip found"
echo ""

# Install dependencies
echo "📦 Installing dependencies..."
pip3 install -q -r requirements.txt 2>/dev/null || pip install -q -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✓ Dependencies installed successfully"
else
    echo "⚠️  Some dependencies may not have installed correctly"
fi

echo ""
echo "════════════════════════════════════════════════════════════════"
echo ""

# Check for OpenAI API key
if [ -z "$OPENAI_API_KEY" ]; then
    echo "⚠️  OPENAI_API_KEY not set"
    echo ""
    echo "The agent will run in MOCK MODE using pattern matching."
    echo "For full LLM functionality, set your API key:"
    echo ""
    echo "  export OPENAI_API_KEY='your-api-key-here'"
    echo ""
    echo "Or create a .env file with:"
    echo "  cp .env.example .env"
    echo "  # Edit .env and add your key"
    echo ""
else
    echo "✓ OPENAI_API_KEY is set"
    echo ""
fi

echo "════════════════════════════════════════════════════════════════"
echo ""
echo "🚀 Ready to go! Choose an option:"
echo ""
echo "1. Run demo (recommended first time)"
echo "   python3 demo.py"
echo ""
echo "2. Interactive mode"
echo "   python3 agent.py"
echo ""
echo "3. Single command"
echo "   python3 agent.py \"your query here\""
echo ""
echo "════════════════════════════════════════════════════════════════"
echo ""

read -p "Press Enter to run demo, or Ctrl+C to exit..."
echo ""
python3 demo.py
