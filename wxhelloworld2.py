#!/usr/bin/env python

import wx

app = wx.App(False)  # Create a new app, don't redirect stdout/stderr to a window.
frame = wx.Frame(None, wx.ID_ANY, "Hello World") # A Frame is a top-level window.

button = wx.Button(frame, -1, "Print Hello")
def on_button_click(event):
    print "Hello!"

#frame.Add(button, 0, wx.EXPAND)
frame.Bind(wx.EVT_BUTTON, on_button_click, button)

frame.Show(True)     # Show the frame.
app.MainLoop()

