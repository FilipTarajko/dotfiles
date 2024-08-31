import os
from libqtile import bar
from libqtile.config import Screen
from .widgets import init_widgets_list

size = 25
opacity = 0.9
margin = [2, 2, -1, 2]

primary_screen_number = 0

def init_screens():
    connected_monitors = len(os.popen(
        "xrandr --listmonitors | grep '+' | awk {'print $4'}").read().splitlines())

    screens = []

    for i in range(0, connected_monitors):
        screens.append(
            Screen(
                top=bar.Bar(
                    widgets=init_widgets_list(i == primary_screen_number),
                    size=size,
                    opacity=opacity,
                    margin=margin
                )
            )
        )

    return screens


screens = init_screens()
