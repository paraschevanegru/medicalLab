import tkinter as tk


class GUI:
    def __init__(self, window, config) -> None:
        self.window = window
        self.window.resizable(False, False)

        myButton = tk.Button(self.window, text="Click me!", command=self.myClick, fg="black", bg="#ffffff")
        myButton.pack()

    def myClick(self):
        myLabel = tk.Label(self.window, text="Hello World!")
        myLabel.pack()