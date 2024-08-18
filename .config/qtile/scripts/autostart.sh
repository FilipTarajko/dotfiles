#!/bin/bash 

# Kill if already running
killall -9 picom xfce4-power-manager ksuperkey dunst sxhkd eww

# setup screen layout
xrandr --output DP-0 --off --output DP-1 --off --output HDMI-0 --mode 2560x1440 --pos 0x460 --rotate normal --output DP-2 --off --output DP-3 --off --output DP-4 --mode 2560x1440 --pos 2560x0 --rotate left --output DP-5 --off --output None-1-1 --off

# Set background scaled
# feh --no-fehbg --bg-scale "$HOME/.config/qtile/icons/wallpaper.jpg"

# Set background filling each screen
feh --no-fehbg --bg-fill "$HOME/.config/qtile/icons/wallpaper.jpg"

# Set background filling each screen, with different screens centered on different parts of the image
# feh --no-fehbg --bg-fill \
#     --geometry +0+0 \
#     "$HOME/.config/qtile/icons/wallpaper.jpg" \
#     --geometry +1920+0 \
#     "$HOME/.config/qtile/icons/wallpaper.jpg"

#lxsession &

# start hotkey daemon
sxhkd &

# start picom
picom &

# start volumeicon
volumeicon &

# start nm-applet
nm-applet &

# start flameshot
flameshot &

# start bluetooth
bluetooth &

# wal -R &
# nitrogen --restore &
#discord &
#caprine &
#firefox &
#discord &

# start redshift
redshift &