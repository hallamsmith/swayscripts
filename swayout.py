#!/usr/bin/env python

import i3ipc

sway = i3ipc.Connection()

while True:
    focused = sway.get_tree().find_focused()
    x = focused.window_rect.width
    y = focused.window_rect.height
    if (x > y):
        largest = 'x'
    else:
        largest = 'y'
    if (largest == 'x'):
        focused.command("split h")
    else:
        focused.command("split v")
        
    while True:
        focused2 = sway.get_tree().find_focused()
        if (focused != focused2):
            break
