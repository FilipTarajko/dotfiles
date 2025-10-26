from libqtile.config import Group, Key
from libqtile.lazy import lazy
from .keys import mod, keys
from libqtile import hook


groups = []

group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

group_labels = ["", "", "", "", "", "", "", "", "9", "0"]

group_layouts = ["columns", "columns", "columns", "columns", "columns", "columns", "columns", "columns", "columns", "columns"]

                #  ["monadtall", "monadtall", "monadtall",
                #  "monadtall", "monadtall", "monadtall",
                #  "monadtall", "monadtall"]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        )
    )

for i in groups:
    keys.extend([

        # CHANGE WORKSPACES
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        Key([mod], "Tab", lazy.screen.next_group()),
        Key([mod, "shift"], "Tab", lazy.screen.prev_group()),
        Key(["mod1"], "Tab", lazy.screen.next_group()),
        Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),

        # MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
        # MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND FOLLOW MOVED WINDOW TO WORKSPACE
        Key([mod, "control"], i.name, lazy.window.togroup(
            i.name), lazy.group[i.name].toscreen()),
    ])


# assign apps to groups/workspace
@hook.subscribe.client_new
def assign_app_group(client):
    d = {}

    # browsers
    d[group_names[0]] = ["Navigator", "Firefox", "Vivaldi-stable", "Vivaldi-snapshot", "Chromium", "Google-chrome", "Brave", "Brave-browser", "navigator", "firefox", "vivaldi-stable", "vivaldi-snapshot", "chromium", "google-chrome", "brave", "brave-browser"]
    # code editors
    d[group_names[1]] = [ "Atom", "Subl", "Geany", "Brackets", "Code-oss", "Code", "TelegramDesktop", "Discord", "atom", "subl", "geany", "brackets", "code-oss", "code", "nvim", "vim", "vscodium" ]
    # anki
    # d[group_names[2]] = ['anki']
    # notes (obsidian)
    d[group_names[3]] = ['obsidian']
    # music
    d[group_names[4]] = ['spotify']
    # video
    d[group_names[5]] = ['vlc', 'obs', 'mpv', 'mplayer', 'lxmusic']
    # files/thunar
    d[group_names[6]] = ['thunar']

    wm_class = client.window.get_wm_class()[0]
    for i in range(len(d)):
        if wm_class in list(d.values())[i]:
            group = list(d.keys())[i]
            client.togroup(group)
            client.group.cmd_toscreen(toggle=False)
