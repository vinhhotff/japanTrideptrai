#!/bin/bash
echo "=========================================================="
echo "  🚀 CÀI ĐẶT VOICEVOX CHẠY NGẦM TỰ ĐỘNG TRÊN MAC (24/7)  "
echo "=========================================================="
echo ""

PLIST_DIR="$HOME/Library/LaunchAgents"
PLIST_FILE="$PLIST_DIR/com.voicevox.engine.plist"

mkdir -p "$PLIST_DIR"

cat << 'EOF' > "$PLIST_FILE"
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.voicevox.engine</string>
    <key>ProgramArguments</key>
    <array>
        <string>/Applications/VOICEVOX.app/Contents/Resources/vv-engine/run</string>
        <string>--cors_policy_mode</string>
        <string>all</string>
        <string>--host</string>
        <string>127.0.0.1</string>
        <string>--port</string>
        <string>50021</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
    <key>StandardOutPath</key>
    <string>/tmp/voicevox_engine.log</string>
    <key>StandardErrorPath</key>
    <string>/tmp/voicevox_engine_err.log</string>
</dict>
</plist>
EOF

# Giải phóng cổng cũ và load service mới
lsof -ti :50021 | xargs kill -9 2>/dev/null
pkill -f "vv-engine/run" 2>/dev/null
launchctl unload "$PLIST_FILE" 2>/dev/null
launchctl load "$PLIST_FILE"

echo "✅ CÀI ĐẶT HOÀN TẤT THÀNH CÔNG 100%!"
echo "----------------------------------------------------------"
echo "👉 Từ bây giờ, VOICEVOX Engine sẽ TỰ ĐỘNG CHẠY NGẦM vĩnh viễn"
echo "   mỗi khi bạn mở máy Mac lên."
echo "👉 Bạn chỉ cần vào web là có giọng đọc Anime NGAY LẬP TỨC,"
echo "   KHÔNG BAO GIỜ cần phải mở file hay gõ lệnh gì nữa!"
echo "----------------------------------------------------------"
echo ""
read -p "Nhấn Enter để hoàn tất..."
