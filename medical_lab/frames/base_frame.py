import tkinter as tk
from tkinter import font as tkfont


class TitleFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=parent["bg"])
        self.controller = controller
        self.parent = parent
        self.title_font = tkfont.Font(family="Helvetica", size=20, weight="bold")
        self.init_title()

    def init_title(self):
        title_frame = tk.Frame(master=self, bg=self.parent["bg"])
        title_frame.pack(side=tk.TOP, fill=tk.X)
        for i in range(2):
            title_frame.grid_columnconfigure(i, weight=1)

        tk.Label(master=title_frame, text="Medical", font=self.title_font, fg="#4380FA", bg=title_frame["bg"]).grid(
            row=0, column=0, sticky="e"
        )
        tk.Label(title_frame, text="Laboratory", font=self.title_font, fg="#4380FA", bg=title_frame["bg"]).grid(
            row=0, column=1, sticky="w"
        )
