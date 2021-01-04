import tkinter as tk
from tkinter import font as tkfont, ttk
from tkinter.constants import NW
from .base_frame import TitleFrame


class MainFrame(TitleFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.init()

    def init(self):
        bg_color = "gray97"
        btn_fg = "white"
        button_font = tkfont.Font(family="Helvetica", size=10)

        self.main_frame_welcome_label_var = tk.StringVar()

        main_frame = tk.Frame(master=self, bg=bg_color)
        main_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        main_frame.grid_rowconfigure(1, weight=1)
        # main_frame.grid_columnconfigure(0, weight=0)
        main_frame.grid_columnconfigure(1, weight=1)
        tk.Label(
            main_frame, textvariable=self.main_frame_welcome_label_var, font=self.title_font, bg=bg_color, fg="black"
        ).grid(row=0, column=0, padx=35, pady=15, sticky="w")
        tk.Button(main_frame, text="Logout", font=button_font, command=self.on_logout, bg="#4380FA", fg=btn_fg).grid(
            row=0, column=2, padx=35, pady=15, sticky="w"
        )

    def on_logout(self):
        from tkinter import messagebox

        if messagebox.askokcancel("Logout", "Are you sure you want to logout?"):
            self.controller.render_frame("LoginFrame")
