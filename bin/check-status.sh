#!/bin/bash
# QUANTUM SUPERSYSTEM - CHECK STATUS
# Owner: Dang Viet Quang

echo "╔════════════════════════════════════════════════════════════════╗"
echo "║  🔍 QUANTUM SUPERSYSTEM STATUS - Dang Viet Quang              ║"
echo "╠════════════════════════════════════════════════════════════════╣"

# Kiểm tra daemon
if pgrep -f "quantum-daemon.sh" > /dev/null; then
    echo "║  ✅ 24/7 DAEMON: ĐANG CHẠY (PID: $(pgrep -f quantum-daemon.sh))"
    DAEMON_RUNNING=true
else
    echo "║  ❌ 24/7 DAEMON: KHÔNG CHẠY"
    DAEMON_RUNNING=false
fi

# Kiểm tra launchd service
if launchctl list | grep -q "com.quantum.supersystem"; then
    echo "║  ✅ LAUNCHD SERVICE: ĐÃ CÀI ĐẶT"
else
    echo "║  ❌ LAUNCHD SERVICE: CHƯA CÀI ĐẶT"
fi

# Kiểm tra GitHub repos
REPO_COUNT=$(ls -1 ~/quantum-supersystem/repos/ 2>/dev/null | wc -l)
echo "║  📊 GITHUB REPOS: $REPO_COUNT/7"

# Kiểm tra logs
if [ -f ~/quantum-supersystem/logs/daemon.log ]; then
    LAST_LOG=$(tail -1 ~/quantum-supersystem/logs/daemon.log 2>/dev/null)
    echo "║  📋 LOG GẦN NHẤT: $LAST_LOG"
else
    echo "║  📋 LOG: Chưa có"
fi

# Kiểm tra kết nối mạng
echo "╠════════════════════════════════════════════════════════════════╣"
echo "║  🌐 KIỂM TRA KẾT NỐI:"
for domain in apple.com microsoft.com kernel.org ibm.com bloomberg.com swift.com; do
    if curl -s --connect-timeout 2 "https://$domain" -o /dev/null 2>/dev/null; then
        echo "║     ✅ $domain"
    else
        echo "║     ⚠️ $domain"
    fi
done

echo "╚════════════════════════════════════════════════════════════════╝"

# Hướng dẫn
if [ "$DAEMON_RUNNING" = false ]; then
    echo ""
    echo "📋 ĐỂ KÍCH HOẠT 24/7, CHẠY:"
    echo "   launchctl load ~/Library/LaunchAgents/com.quantum.supersystem.plist"
    echo "   ~/quantum-supersystem/bin/quantum-daemon.sh"
fi
