#!/bin/bash
# Create portable distribution package for LinuxGPT

VERSION="2.0"
DIST_NAME="linuxgpt-v${VERSION}-linux"
DIST_DIR="dist/$DIST_NAME"

echo "📦 Creating LinuxGPT Distribution Package v$VERSION"
echo ""

# Clean old dist
rm -rf dist
mkdir -p "$DIST_DIR"

echo "📋 Copying files..."
cp agent.py "$DIST_DIR/"
cp linux_commands_db_comprehensive.json "$DIST_DIR/"
cp linuxgpt_launcher.py "$DIST_DIR/"
cp install.sh "$DIST_DIR/"
cp README.md "$DIST_DIR/" 2>/dev/null || true
cp CHANGELOG.md "$DIST_DIR/" 2>/dev/null || true

# Create .env template
cat > "$DIST_DIR/.env.example" << 'EOF'
# OpenAI API Configuration (optional - works in mock mode without this)
OPENAI_API_KEY=your-api-key-here
OPENAI_MODEL=gpt-4
EOF

# Create standalone executable wrapper
cat > "$DIST_DIR/linuxgpt" << 'EOF'
#!/bin/bash
# LinuxGPT Standalone Runner
# No installation required - run directly from this directory

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR" && python3 linuxgpt_launcher.py "$@"
EOF
chmod +x "$DIST_DIR/linuxgpt"

# Create README for distribution
cat > "$DIST_DIR/INSTALL.txt" << 'EOF'
╔════════════════════════════════════════════════════════════╗
║           LinuxGPT - Installation Guide                   ║
║     Natural Language → Linux Command Converter             ║
╚════════════════════════════════════════════════════════════╝

QUICK START (No installation needed):
═══════════════════════════════════════════════════════════

  ./linuxgpt "show disk space"
  ./linuxgpt "find large files"
  ./linuxgpt                      # Interactive mode


INSTALLATION (Optional):
═══════════════════════════════════════════════════════════

Option 1: System-wide installation
  sudo ./install.sh
  
Option 2: User installation (recommended)
  ./install.sh
  
After installation, use 'linuxgpt' from anywhere!


CONFIGURATION:
═══════════════════════════════════════════════════════════

OpenAI API (Optional - works without it):
  1. Copy .env.example to .env
  2. Add your OpenAI API key
  3. Mock mode works automatically without API key


REQUIREMENTS:
═══════════════════════════════════════════════════════════

  • Python 3.7+
  • pip (for automatic dependency installation)
  • Internet connection (for first run to install deps)


FEATURES:
═══════════════════════════════════════════════════════════

  ✓ 144 Linux commands with full documentation
  ✓ 425+ examples with explanations
  ✓ Natural language query processing
  ✓ Educational mode with tips
  ✓ Works offline (mock mode)
  ✓ Safe command execution with validation


EXAMPLES:
═══════════════════════════════════════════════════════════

  ./linuxgpt "how to find files larger than 100MB"
  ./linuxgpt "show running processes"
  ./linuxgpt "compress a file"
  ./linuxgpt "explain rsync"


SUPPORT:
═══════════════════════════════════════════════════════════

  GitHub: https://github.com/vilaswasnik/sample.ai
  Version: 2.0
  Commands: 144
  License: MIT

EOF

echo "📦 Creating tarball..."
cd dist
tar -czf "${DIST_NAME}.tar.gz" "$DIST_NAME"

echo "📦 Creating zip archive..."
zip -rq "${DIST_NAME}.zip" "$DIST_NAME"

cd ..

echo ""
echo "✅ Distribution packages created:"
echo "   • dist/${DIST_NAME}.tar.gz"
echo "   • dist/${DIST_NAME}.zip"
echo ""
echo "📊 Package contents:"
ls -lh "dist/${DIST_NAME}/"
echo ""
echo "🚀 To test:"
echo "   cd dist/${DIST_NAME}"
echo "   ./linuxgpt 'list files'"
