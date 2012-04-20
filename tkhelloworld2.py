#!/usr/bin/env python

from Tkinter import Tk, Frame, Button, LEFT

class HelloApp(object):

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT)

    def say_hi(self):
        print "Welcome to the world of tomorrow!"

root = Tk()

app = HelloApp(root)

root.mainloop()