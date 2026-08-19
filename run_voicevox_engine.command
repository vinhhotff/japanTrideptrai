#!/bin/bash
echo "=================================================="
echo "  🚀 KHỞI ĐỘNG VOICEVOX ENGINE (CORS: ALLOW ALL) "
echo "=================================================="
echo ""

echo "🔄 Đang giải phóng cổng 50021..."
lsof -ti :50021 | xargs kill -9 2>/dev/null
pkill -f "vv-engine/run" 2>/dev/null
sleep 1

echo "🟢 Đang mở VOICEVOX Engine với CORS mở khóa toàn bộ..."
echo "Địa chỉ: http://127.0.0.1:50021"
echo "--------------------------------------------------"
echo "👉 Hãy giữ cửa sổ Terminal này mở trong lúc học!"
echo "--------------------------------------------------"
echo ""

if [ -f "/Applications/VOICEVOX.app/Contents/Resources/vv-engine/run" ]; then
    "/Applications/VOICEVOX.app/Contents/Resources/vv-engine/run" --cors_policy_mode all --host 127.0.0.1 --port 50021
else
    echo "❌ Không tìm thấy VOICEVOX trong /Applications."
    read -p "Nhấn Enter để thoát..."
fi
