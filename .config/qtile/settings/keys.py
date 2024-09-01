from libqtile.config import Key
from libqtile.lazy import lazy


# Sets mod key to SUPER/WINDOWS
mod = "mod4"

keys = [
    # MINE - Toggle widgetbox
    Key([mod, "shift"], "w", lazy.widget["widgetbox"].toggle()),

    # MINE - Switch between screens
    Key([mod, "shift", "control"], "Up", lazy.next_screen()),
    Key([mod, "shift", "control"], "Right", lazy.next_screen()),
    Key([mod, "shift", "control"], "Down", lazy.prev_screen()),
    Key([mod, "shift", "control"], "Left", lazy.prev_screen()),

    # MINE - Switch between screens - VIM
    Key([mod, "shift", "control"], "k", lazy.next_screen()),
    Key([mod, "shift", "control"], "l", lazy.next_screen()),
    Key([mod, "shift", "control"], "j", lazy.prev_screen()),
    Key([mod, "shift", "control"], "h", lazy.prev_screen()),

    # Most of our keybindings are in sxhkd file - except these

    # SUPER + FUNCTION KEYS
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod], "q", lazy.window.kill()),

    # SUPER + SHIFT KEYS
    Key([mod, "shift"], "q", lazy.window.kill()),
    Key([mod, "shift"], "r", lazy.restart()),

    # QTILE LAYOUT KEYS
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "space", lazy.next_layout()),

    # CHANGE FOCUS
    Key([mod], "Up", lazy.layout.up()),
    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),

    # RESIZE UP, DOWN, LEFT, RIGHT
    Key([mod, "control"], "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),
    Key([mod, "control"], "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),

    # FLIP LAYOUT FOR MONADTALL/MONADWIDE
    Key([mod, "shift"], "f", lazy.layout.flip()),

    # FLIP LAYOUT FOR BSP
    Key([mod, "mod1"], "k", lazy.layout.flip_up()),
    Key([mod, "mod1"], "j", lazy.layout.flip_down()),
    Key([mod, "mod1"], "l", lazy.layout.flip_right()),
    Key([mod, "mod1"], "h", lazy.layout.flip_left()),
    Key([mod, "mod1"], "Up", lazy.layout.flip_up()),
    Key([mod, "mod1"], "Down", lazy.layout.flip_down()),
    Key([mod, "mod1"], "Right", lazy.layout.flip_right()),
    Key([mod, "mod1"], "Left", lazy.layout.flip_left()),


    # MOVE WINDOWS UP OR DOWN BSP LAYOUT
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),

    # MOVE WINDOWS UP OR DOWN MONADTALL/MONADWIDE LAYOUT
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "Left", lazy.layout.swap_left()),
    Key([mod, "shift"], "Right", lazy.layout.swap_right()),

    # MY ADDITION FOR COLUMNS
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right()),

    # TOGGLE FLOATING LAYOUT
    Key([mod, "shift"], "space", lazy.window.toggle_floating()),

    # COLUMNS KEYS
    # Key([mod], "j", lazy.layout.down()),
    # Key([mod], "k", lazy.layout.up()),
    # Key([mod], "h", lazy.layout.left()),
    # Key([mod], "l", lazy.layout.right()),
    # Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    # Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    # Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    # Key([mod, "shift"], "l", lazy.layout.shuffle_right()),
    # Key([mod, "control"], "j", lazy.layout.grow_down()),
    # Key([mod, "control"], "k", lazy.layout.grow_up()),
    # Key([mod, "control"], "h", lazy.layout.grow_left()),
    # Key([mod, "control"], "l", lazy.layout.grow_right()),
    # Key([mod, "shift", "control"], "h", lazy.layout.swap_column_left()),
    # Key([mod, "shift", "control"], "l", lazy.layout.swap_column_right()),
    # Key([mod], "Return", lazy.layout.toggle_split()),
    # Key([mod], "n", lazy.layout.normalize()),
]
