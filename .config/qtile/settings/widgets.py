from libqtile import widget, qtile, bar
from .theme import colors
from .path import home_dir
from scripts import storage
import subprocess
import socket
import os
from .spotify import Spotify

myTerm = "alacritty"        # My terminal of choice
myBrowser = "firefox"       # My browser of choice

def generate_current_screen_indicator():
    return widget.CurrentScreen(
            active_color=colors[10],
            inactive_color=colors[1],
            active_text="||||||||||||||",
            inactive_text="   ",
            background=colors[1],
            fontsize=20
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

def init_widgets_list(screen_number):
    widgets_list = [
        init_edge_spacer(),
        # widget.Image(
        #     filename="~/.config/qtile/icons/python.png",
        #     background=colors[1],
        #     margin=3,
        #     mouse_callbacks={
        #         'Button1': lambda: qtile.cmd_spawn(
        #             'j4-dmenu'
        #         ),
        #         'Button3': lambda: qtile.cmd_spawn(
        #             f'{myTerm} -e vim {home_dir}/.config/qtile/config.py'
        #         )
        #     }
        # ),

        # nerd_icon(
        #     "﬙",
        #     colors[3]
        # ),
        # widget.CPU(
        #     format="{load_percent}%",
        #     foreground=colors[2],
        #     background=colors[1],
        #     update_interval=60,
        #     mouse_callbacks={
        #         'Button1': lambda: qtile.cmd_spawn(f"{myTerm} -e btop")
        #     }
        # ),
        # nerd_icon(
        #     "",
        #     colors[4]
        # ),
        # widget.Memory(
        #     measure_mem='G',
        #     format="{MemUsed:.0f}{mm}",
        #     foreground=colors[2],
        #     background=colors[1],
        #     update_interval=60,
        #     mouse_callbacks={
        #         'Button1': lambda: qtile.cmd_spawn(f"{myTerm} -e btop")
        #     }
        # ),
        # nerd_icon(
        #     "",
        #     colors[6]
        # ),
        # widget.GenPollText(
        #     foreground=colors[2],
        #     background=colors[1],
        #     update_interval=5,
        #     func=lambda: storage.diskspace('FreeSpace'),
        #     mouse_callbacks={
        #         'Button1': lambda: qtile.cmd_spawn(f"{myTerm} -e btop")
        #     }
        # ),
        # init_separator(),
        # nerd_icon(
        #     "",
        #     colors[4]
        # ),
        # widget.Net(
        #     format="{down} ↓↑ {up}",
        #     foreground=colors[2],
        #     background=colors[1],
        #     update_interval=30,
        #     mouse_callbacks={
        #         'Button1': lambda: qtile.cmd_spawn("def-nmdmenu")
        #     }
        # ),
        # init_separator(),
        # nerd_icon(
        #     "",
        #     colors[4]
        # ),
        # widget.GenPollText(
        #     foreground=colors[2],
        #     background=colors[1],
        #     update_interval=5,
        #     func=lambda: subprocess.check_output(
        #         f"{home_dir}/.config/qtile/scripts/num-installed-pkgs").decode("utf-8"),
        #     mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(
        #         myTerm + ' -e sudo pacman -Syu')},
        # ),
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
            text_closed = "",
            name=(f"widgetbox{screen_number}")
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
        # widget.CurrentLayoutIcon(),
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
        *maybe_show_systray(screen_number>0),
        # Center bar
        # Left Side of the bar
        generate_current_screen_indicator(),
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
        # init_separator(),
        # nerd_icon(
        #     "",
        #     colors[8]
        # ),
        init_edge_spacer()
    ]
    return widgets_list


def init_primary_widgets(screen_number):
    return init_widgets_list(screen_number)


def init_secondary_widgets(screen_number):
    return init_widgets_list(screen_number)
