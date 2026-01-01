#!/bin/bash
#Declaring Paths
repo_dir="/home/glstation/BackupFromPi/Documents/GNSSTimerConfiguration"
update_file="$repo_dir/override.conf"

target_dir="/etc/systemd/system/GNSSScript.timer.d"
target_file="$target_dir/override.conf"

#Commands to git pull and check for latest updates
cd $repo_dir
git pull origin main

if ! diff -qwb "$target_file" "$update_file" ; then
        sudo cp "$update_file" "$target_dir"
        echo "Copied"
else
        echo "No changes found, exiting"
        exit 0
fi

sudo systemctl daemon-reload
sudo systemctl restart GNSSScript.timer

echo "Restarted Daemon and service, exiting"