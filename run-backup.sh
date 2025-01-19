#!/bin/bash

# Set the paths for the source directories and the repository
TEST_DIR="/home/vinay/delete"
BOOT_DIR="/boot"
HOME_DIR="/home"
ROOT_DIR="/"
TMP_DIR="/tmp"
VAR_DIR="/var"
REPO="/media/vinay/My Passport/Ubuntu-PC-Backup"

# Run BorgBackup to create a backup
sudo borg create --stats --progress "$REPO::full-system_$(date +%Y-%m-%d)" \
    $TEST_DIR $BOOT_DIR $HOME_DIR $ROOT_DIR $TMP_DIR $VAR_DIR \
    --exclude "/mnt/*" \
    --exclude "/media/vinay/*" \
    --exclude "/home/vinay/data/*" \
    --exclude "/mnt/*" \
    --exclude "/media/vinay/*" \
    --exclude "/home/vinay/data/*" \
    --exclude "/dev" \
    --exclude "/proc" \
    --exclude "/sys" \
    --exclude "/var/run" \
    --exclude "/run" \
    --exclude "/lost+found" \
    --exclude "/mnt" \
    --exclude "/var/lib/lxcfs" \
    --exclude "/FULL_BACKUP" \
    --exclude "/swapfile" \
    --exclude "/tmp" \
    --exclude "/var/cache" \
    --exclude "/root/.cache" \
    # --one-file-system


