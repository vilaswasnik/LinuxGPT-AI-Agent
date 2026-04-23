#!/bin/bash
###############################################################################
# LinuxGPT Service Control Script
# Controls starting, stopping, and monitoring the LinuxGPT agent
###############################################################################

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PID_FILE="${SCRIPT_DIR}/.linuxgpt.pid"
LOG_FILE="${SCRIPT_DIR}/linuxgpt.log"
LAUNCHER="${SCRIPT_DIR}/linuxgpt_launcher.py"
AGENT="${SCRIPT_DIR}/agent.py"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

###############################################################################
# Helper Functions
###############################################################################

print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if process is running
is_running() {
    if [ -f "$PID_FILE" ]; then
        PID=$(cat "$PID_FILE")
        if ps -p "$PID" > /dev/null 2>&1; then
            return 0  # Running
        else
            # Stale PID file
            rm -f "$PID_FILE"
            return 1  # Not running
        fi
    fi
    return 1  # Not running
}

# Get process info
get_process_info() {
    if [ -f "$PID_FILE" ]; then
        PID=$(cat "$PID_FILE")
        if ps -p "$PID" > /dev/null 2>&1; then
            echo "PID: $PID"
            ps -p "$PID" -o pid,ppid,cmd,%mem,%cpu,etime
        fi
    fi
}

###############################################################################
# Service Control Functions
###############################################################################

start_service() {
    print_status "Starting LinuxGPT agent..."
    
    # Check if already running
    if is_running; then
        PID=$(cat "$PID_FILE")
        print_warning "LinuxGPT agent is already running (PID: $PID)"
        return 1
    fi
    
    # Check if launcher exists
    if [ ! -f "$LAUNCHER" ]; then
        print_error "Launcher not found: $LAUNCHER"
        return 1
    fi
    
    # Start the service in background
    nohup python3 "$LAUNCHER" > "$LOG_FILE" 2>&1 &
    PID=$!
    
    # Save PID
    echo "$PID" > "$PID_FILE"
    
    # Wait a moment and check if it's still running
    sleep 2
    if is_running; then
        print_success "LinuxGPT agent started successfully (PID: $PID)"
        print_status "Log file: $LOG_FILE"
        return 0
    else
        print_error "LinuxGPT agent failed to start. Check log file: $LOG_FILE"
        rm -f "$PID_FILE"
        return 1
    fi
}

stop_service() {
    print_status "Stopping LinuxGPT agent..."
    
    if ! is_running; then
        print_warning "LinuxGPT agent is not running"
        return 1
    fi
    
    PID=$(cat "$PID_FILE")
    
    # Try graceful shutdown first
    print_status "Sending SIGTERM to process $PID..."
    kill -TERM "$PID" 2>/dev/null
    
    # Wait for process to stop (max 10 seconds)
    for i in {1..10}; do
        if ! ps -p "$PID" > /dev/null 2>&1; then
            rm -f "$PID_FILE"
            print_success "LinuxGPT agent stopped successfully"
            return 0
        fi
        sleep 1
    done
    
    # Force kill if still running
    print_warning "Process did not stop gracefully, forcing shutdown..."
    kill -KILL "$PID" 2>/dev/null
    sleep 1
    
    if ! ps -p "$PID" > /dev/null 2>&1; then
        rm -f "$PID_FILE"
        print_success "LinuxGPT agent stopped (forced)"
        return 0
    else
        print_error "Failed to stop LinuxGPT agent"
        return 1
    fi
}

restart_service() {
    print_status "Restarting LinuxGPT agent..."
    stop_service
    sleep 2
    start_service
}

status_service() {
    echo "=========================================="
    echo "LinuxGPT Agent Status"
    echo "=========================================="
    
    if is_running; then
        PID=$(cat "$PID_FILE")
        echo -e "${GREEN}Status: RUNNING${NC}"
        echo ""
        get_process_info
        echo ""
        echo "Log file: $LOG_FILE"
        echo "PID file: $PID_FILE"
    else
        echo -e "${RED}Status: STOPPED${NC}"
        echo ""
        if [ -f "$LOG_FILE" ]; then
            echo "Last 10 lines of log:"
            echo "----------------------------------------"
            tail -n 10 "$LOG_FILE"
        fi
    fi
    echo "=========================================="
}

view_logs() {
    if [ ! -f "$LOG_FILE" ]; then
        print_warning "Log file not found: $LOG_FILE"
        return 1
    fi
    
    if [ "$1" == "--follow" ] || [ "$1" == "-f" ]; then
        print_status "Following log file (Ctrl+C to stop)..."
        tail -f "$LOG_FILE"
    else
        print_status "Displaying last 50 lines of log file..."
        tail -n 50 "$LOG_FILE"
    fi
}

clear_logs() {
    if [ -f "$LOG_FILE" ]; then
        > "$LOG_FILE"
        print_success "Log file cleared"
    else
        print_warning "No log file to clear"
    fi
}

###############################################################################
# Main Script
###############################################################################

show_usage() {
    cat << EOF
Usage: $0 {start|stop|restart|status|logs|clear-logs|help}

Commands:
    start       - Start the LinuxGPT agent service
    stop        - Stop the LinuxGPT agent service
    restart     - Restart the LinuxGPT agent service
    status      - Show current status and process information
    logs        - Display recent logs (use -f to follow)
    clear-logs  - Clear the log file
    help        - Show this help message

Examples:
    $0 start              # Start the service
    $0 stop               # Stop the service
    $0 restart            # Restart the service
    $0 status             # Check if running
    $0 logs               # View logs
    $0 logs -f            # Follow logs in real-time

Files:
    PID file: $PID_FILE
    Log file: $LOG_FILE
    Launcher: $LAUNCHER

EOF
}

# Main command handler
case "$1" in
    start)
        start_service
        ;;
    stop)
        stop_service
        ;;
    restart)
        restart_service
        ;;
    status)
        status_service
        ;;
    logs)
        view_logs "$2"
        ;;
    clear-logs)
        clear_logs
        ;;
    help|--help|-h)
        show_usage
        ;;
    *)
        print_error "Invalid command: $1"
        echo ""
        show_usage
        exit 1
        ;;
esac

exit $?
