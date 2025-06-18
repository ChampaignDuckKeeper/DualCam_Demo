#!/bin/bash
# update_check.sh - Complete repository synchronization script with local change handling

# Strict error handling
set -euo pipefail
cd "$(dirname "$0")" || exit 1

# Configuration
BRANCH="main"
REMOTE="origin"

# 1. Fetch latest changes
echo "[SYNC] Fetching repository updates..."
git fetch "$REMOTE" "$BRANCH"

# 2. Check repository state
LOCAL_HASH=$(git rev-parse HEAD)
REMOTE_HASH=$(git rev-parse "$REMOTE/$BRANCH")
UNCOMMITTED=$(git status --porcelain)

# 3. Decision logic
if [ "$LOCAL_HASH" != "$REMOTE_HASH" ]; then
    # Case 1: Need to update to new remote commits
    echo -e "\n[UPDATE] New commits available:"
    git log --pretty=format:"%h %s (%cr)" "$LOCAL_HASH".."$REMOTE/$BRANCH"
    
    if [ -n "$UNCOMMITTED" ]; then
        echo -e "\n[WARNING] Local changes will be lost:"
        git status --short
    fi
    
    read -r -p $'\nProceed with HARD RESET to remote? (all local changes will be lost) (y/n): ' RESPONSE
    if [[ "$RESPONSE" =~ ^[Yy] ]]; then
        echo -e "\n[RESET] Forcing repository synchronization..."
        git reset --hard "$REMOTE/$BRANCH"
        git clean -fd
        echo "[SUCCESS] Fully synchronized with $REMOTE/$BRANCH"
    else
        echo "[ABORT] Update cancelled by user"
    fi

elif [ -n "$UNCOMMITTED" ]; then
    # Case 2: Same commit but local modifications
    echo -e "\n[STATE] Repository is at same commit as remote but has local changes:"
    git status --short
    
    echo -e "\nAvailable actions:"
    echo "1. Keep local changes (default)"
    echo "2. Discard all local changes"
    echo "3. View change differences"
    
    read -r -p $'\nSelect action (1-3): ' ACTION
    case $ACTION in
        2)
            echo -e "\n[DISCARD] Resetting all local changes..."
            git reset --hard "$REMOTE/$BRANCH"
            git clean -fd
            echo "[SUCCESS] All local changes removed"
            ;;
        3)
            echo -e "\n[DIFF] Showing local modifications:"
            git diff
            ;;
        *)
            echo "[INFO] Keeping local changes"
            ;;
    esac
else
    # Case 3: Fully synchronized
    echo "[STATUS] Repository is fully synchronized with $REMOTE/$BRANCH"
fi