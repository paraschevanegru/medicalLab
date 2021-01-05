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
        for r in range(6):
            self.title_frame.rowconfigure(r, weight=1)
        for c in range(5):
            self.title_frame.columnconfigure(c, weight=1)

        logo = Image.open(Path(__file__).parent / "logo.png")
        logo = logo.resize((25, 25), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(logo)
        img = tk.Label(self, image=render, bd=0)
        tk.Label(
            master=title_frame, text="Medical Laboratory", font=self.title_font, fg="#4380FA", bg=title_frame["bg"]
        ).grid(row=0, column=0, ipadx=42, ipady=10, sticky="nw")
        img.image = render
        img.place(x=10, y=10)

    # def init(self):
    #     self.bg_color = "white"
    #     self.btn_fg = "white"
    #     self.button_font = tkfont.Font(family="Helvetica", size=10)

    #     self.main_frame_welcome_label_var = tk.StringVar()

    #     main_frame = tk.Frame(master=self, bg=self.bg_color)
    #     main_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    #     main_frame.grid_rowconfigure(1, weight=1)
    #     # main_frame.grid_columnconfigure(0, weight=0)
    #     main_frame.grid_columnconfigure(0, weight=1)

    #     welcome_label_frame = tk.LabelFrame(main_frame, bg="white", bd=0)
    #     welcome_label_frame.grid(row=0, column=2)

    #     tk.Label(
    #         welcome_label_frame,
    #         textvariable=self.main_frame_welcome_label_var,
    #         font=self.title_font,
    #         bg=self.bg_color,
    #         fg="#99CCFF",
    #     ).grid(row=0, column=2, padx=5, pady=10)
    #     tk.Button(
    #         welcome_label_frame,
    #         text="Logout",
    #         font=self.button_font,
    #         command=self.on_logout,
    #         bg="#4380FA",
    #         fg=self.btn_fg,
    #     ).grid(row=1, column=2, padx=10, pady=5, sticky="e")

    # def on_logout(self):
    #     from tkinter import messagebox

    #     if messagebox.askokcancel("Logout", "Are you sure you want to logout?"):
    #         self.controller.render_frame("LoginFrame")