import os
from libqtile import bar
from libqtile.config import Screen
from .widgets import init_primary_widgets
from .widgets import init_secondary_widgets

size = 25
opacity = 0.9
margin = [2, 2, -1, 2]

def init_screens():
    screens = [
        Screen(
            top=bar.Bar(
                widgets=init_primary_widgets(0),
                size=size,
                opacity=opacity,
                margin=margin
            )
        )
    ]

    connected_monitors = len(os.popen(
        "xrandr --listmonitors | grep '+' | awk {'print $4'}").read().splitlines())

    if connected_monitors == 1:
        return screens

    for i in range(1, connected_monitors):
        screens.append(
            Screen(
                top=bar.Bar(
                    widgets=init_secondary_widgets(i),
                    size=size,
                    opacity=opacity,
                    margin=margin
                )
            )
        )

    return screens


screens = init_screens()
