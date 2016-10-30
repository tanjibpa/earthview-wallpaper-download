#!/bin/bash
PID=$(pgrep gnome-session)
export DBUS_SESSION_BUS_ADDRESS=$(grep -z DBUS_SESSION_BUS_ADDRESS /proc/$PID/environ|cut -d= -f2-)
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd ${DIR}
# cd /home/tanjib/.earthview_download
if [ ! -d 'venv' ]; then
    virtualenv -p python3 venv
    pip install -r requirements.txt
fi
source venv/bin/activate
if [ ! -d $HOME'/Pictures/earthview-wallpaper' ]; then
    mkdir $HOME'/Pictures/earthview-wallpaper'
fi
OUTPUT="$(python change_wallpaper.py)"
gsettings set org.gnome.desktop.background picture-uri file://$HOME/Pictures/earthview-wallpaper/"${OUTPUT}"

