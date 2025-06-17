#!/usr/bin/env bash
# ------------------------------------------
# Install a desktop shortcut for this project
# ------------------------------------------
set -e

PROJECT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
DESKTOP_FILE="$HOME/.local/share/applications/camera-module.desktop"

cat > "$DESKTOP_FILE" <<EOF
[Desktop Entry]
Type=Application
Name=Camera Module
Comment=Launch the camera-module demo
Exec='cd ${PROJECT_DIR} && env LD_LIBRARY_PATH=${PROJECT_DIR}/lib python main.py'
Path=$PROJECT_DIR
Icon=utilities-camera        # 可改为 $PROJECT_DIR/icon.png
Terminal=true                # 如不想看日志可设 false
EOF

chmod +x "$DESKTOP_FILE"
update-desktop-database "$HOME/.local/share/applications" &>/dev/null || true
echo "✔ shotcut created: $(basename "$DESKTOP_FILE")"
echo "   Search "Camera Module" in application menu, or drag the icon from the menu to the desktop."
