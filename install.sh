#!/bin/bash
# LinuxGPT Installer Script
# Installs LinuxGPT system-wide or locally

set -e

VERSION="2.0"
INSTALL_DIR="${INSTALL_DIR:-$HOME/.local/linuxgpt}"
BIN_DIR="${BIN_DIR:-$HOME/.local/bin}"

echo "╔════════════════════════════════════════════════════════════╗"
echo "║           LinuxGPT Installer v$VERSION                        ║"
echo "║     Natural Language → Linux Command Converter             ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

# Check for Python 3
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is required but not installed."
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1,2)
echo "✓ Found Python $PYTHON_VERSION"

# Ask for installation type
echo ""
echo "Installation options:"
echo "1) User installation (recommended) - $INSTALL_DIR"
echo "2) System-wide installation - /opt/linuxgpt (requires sudo)"
read -p "Choose option [1]: " INSTALL_TYPE
INSTALL_TYPE=${INSTALL_TYPE:-1}

if [ "$INSTALL_TYPE" = "2" ]; then
    INSTALL_DIR="/opt/linuxgpt"
    BIN_DIR="/usr/local/bin"
    SUDO="sudo"
else
    SUDO=""
fi

echo ""
echo "📦 Creating installation directory..."
$SUDO mkdir -p "$INSTALL_DIR"
$SUDO mkdir -p "$BIN_DIR"

echo "📋 Copying files..."
$SUDO cp agent.py "$INSTALL_DIR/"
$SUDO cp linux_commands_db_comprehensive.json "$INSTALL_DIR/"
$SUDO cp linuxgpt_launcher.py "$INSTALL_DIR/"

# Copy .env if it exists
if [ -f .env ]; then
    echo "🔑 Copying API key configuration..."
    $SUDO cp .env "$INSTALL_DIR/"
fi

echo "🔧 Creating executable..."
cat > /tmp/linuxgpt << 'EOF'
#!/bin/bash
# LinuxGPT wrapper script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [ "$SCRIPT_DIR" = "/usr/local/bin" ] || [ "$SCRIPT_DIR" = "$HOME/.local/bin" ]; then
    # Running from system bin, find actual installation
    if [ -d "/opt/linuxgpt" ]; then
        INSTALL_DIR="/opt/linuxgpt"
    else
        INSTALL_DIR="$HOME/.local/linuxgpt"
    fi
else
    INSTALL_DIR="$SCRIPT_DIR"
fi

cd "$INSTALL_DIR" && python3 linuxgpt_launcher.py "$@"
EOF

$SUDO cp /tmp/linuxgpt "$BIN_DIR/linuxgpt"
$SUDO chmod +x "$BIN_DIR/linuxgpt"

echo ""
echo "✅ Installation complete!"
echo ""
echo "Installation details:"
echo "  • Program files: $INSTALL_DIR"
echo "  • Executable: $BIN_DIR/linuxgpt"
echo "  • Commands: 144"
echo "  • Examples: 425+"
echo ""
echo "Usage:"
echo "  linuxgpt 'show disk space'"
echo "  linuxgpt 'find large files'"
echo "  linuxgpt                     (interactive mode)"
echo ""

# Check if BIN_DIR is in PATH
if [[ ":$PATH:" != *":$BIN_DIR:"* ]]; then
    echo "⚠️  Note: $BIN_DIR is not in your PATH"
    echo "   Add to ~/.bashrc or ~/.zshrc:"
    echo "   export PATH=\"\$PATH:$BIN_DIR\""
    echo ""
fi

# Setup API key if not configured
if [ ! -f "$INSTALL_DIR/.env" ]; then
    echo "🔑 OpenAI API Key Setup:"
    echo "   To use GPT-4 mode, create: $INSTALL_DIR/.env"
    echo "   Contents: OPENAI_API_KEY=your-api-key-here"
    echo "   (Mock mode works without API key)"
    echo ""
fi

echo "🚀 Ready to use! Try: linuxgpt 'list files'"
