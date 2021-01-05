import tkinter as tk
from tkinter import font as tkfont
from PIL import Image, ImageTk
from pathlib import Path


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

        logo = Image.open(Path(__file__).parent / "logo.png")
        logo = logo.resize((25, 25), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(logo)
        img = tk.Label(self, image=render, bd=0)
        tk.Label(
            master=title_frame, text="Medical Laboratory", font=self.title_font, fg="#4380FA", bg=title_frame["bg"]
        ).grid(row=0, column=0, padx=42, pady=10, sticky="w")
        img.image = render
        img.place(x=10, y=10)
