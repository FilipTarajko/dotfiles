from libqtile import widget, qtile, bar
from .theme import colors
from .path import home_dir
from scripts import storage
import subprocess
import socket
import os
from .spotify import Spotify

def generate_current_screen_indicator(is_on_left=False):
    active_text = "\\\\\\\\\\"
    inactive_text = "/////"
    if is_on_left:
        [active_text, inactive_text] = [inactive_text, active_text]
    return widget.CurrentScreen(
            active_color=colors[4],
            inactive_color=colors[3],
            active_text=active_text,
            inactive_text=inactive_text,
            background=colors[1],
            fontsize=20,
            padding=12,
        )

def init_widgets_defaults():
    return dict(
        font='Source Code Pro Medium',
        fontsize=12,
        padding=5)


def init_separator():
    return widget.Sep(
        size_percent=90,
        padding=12,
        linewidth=3,
        background=colors[1],
        foreground="#444444"
    )


def nerd_icon(nerdfont_icon, fg_color):
    return widget.TextBox(
        font="Iosevka Nerd Font",
        fontsize=15,
        padding=8,
        text=nerdfont_icon,
        foreground=fg_color,
        background=colors[1])


def init_edge_spacer():
    return widget.Spacer(
        length=5,
        background=colors[1])


widget_defaults = init_widgets_defaults()
extension_defaults = widget_defaults.copy()


def maybe_show_systray(should_show):
    if should_show:
        return [
            init_separator(),
            widget.Systray(
                background=colors[1],
                padding=8
            )
        ]
    return []


def init_widgets_list(is_primary):
    widgets_list = [
        init_edge_spacer(),
        Spotify(),
        widget.WidgetBox(
            background=colors[1],
            widgets=[
                init_separator(),
                widget.WindowName(
                    background=colors[1],
                    foreground=colors[2],
                    fontsize=14,
                    for_current_screen=True,
                ),
            ],
            fontsize=14,
            text_open = "",
            text_closed = ""
        ),
        widget.Spacer(
            length=bar.STRETCH,
            background=colors[1]
        ),
        generate_current_screen_indicator(),
        widget.GroupBox(
            font="Font Awesome",
            fontsize=15,
            foreground=colors[2],
            background=colors[1],
            borderwidth=4,
            highlight_method="block",
            this_current_screen_border=colors[10],
            active=colors[4],
            inactive=colors[2]
        ),
        init_separator(),
        nerd_icon(
            "",
            colors[7]
        ),
        widget.CurrentLayout(
            foreground=colors[2],
            background=colors[1]
        ),
        init_separator(),
        nerd_icon(
            "墳",
            colors[7]
        ),
        widget.Volume(
            foreground=colors[2],
            background=colors[1]
        ),
        *maybe_show_systray(is_primary),
        generate_current_screen_indicator(True),
        widget.Spacer(
            length=bar.STRETCH,
            background=colors[1]
        ),
        widget.Battery(
            background=colors[1],
            foreground=colors[2],
            notify_below=0.9,
            low_percentage=0.9,
        ),
        init_separator(),
        nerd_icon(
            "",
            colors[7]
        ),
        widget.Clock(
            format='%Y-%m-%d   %H:%M',
            foreground=colors[2],
            background=colors[1],
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn("vivaldi \"https://calendar.google.com/calendar/\""),
                "Button2": lambda: qtile.cmd_spawn("vivaldi --new-window \"https://calendar.google.com/calendar/\""),
                "Button3": lambda: qtile.cmd_spawn("vivaldi --new-window \"https://calendar.google.com/calendar/\""),
            }
        ),
        init_edge_spacer()
    ]
    return widgets_list
