import tkinter as tk
from tkinter import font as tkfont, ttk
from .base_frame import TitleFrame


class AsistentFrame(TitleFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.init()

    def init(self):
        self.bg_color = "white"
        self.btn_fg = "white"

        text_font = tkfont.Font(family="Helvetica", size=13)
        self.button_font = tkfont.Font(family="Helvetica", size=10)

        asistent_frame = tk.LabelFrame(master=self, bg="gray97")
        asistent_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        asistent_frame.grid_rowconfigure(2, weight=1)
        asistent_frame.grid_columnconfigure(0, weight=1)

    #     self.init_dashboard(asistent_frame)

    # def init_dashboard(self, parent):
    #     print("ajutor")
    #     self.dashboard_frame = tk.LabelFrame(parent, bg="red")
    #     self.dashboard_frame.grid(row=2, column=0, rowspan=3, columnspan=2, sticky="w")

    #     self.dashboard_insert_frame = tk.LabelFrame(self.dashboard_frame, bg="gray94")
    #     self.dashboard_insert_frame.grid(row=0, column=0, pady=5, padx=5, sticky="w")
    #     tk.Label(
    #         self.dashboard_insert_frame,
    #         textvariable="Dashborad",
    #         font=self.title_font,
    #         bg=self.bg_color,
    #         fg="#99CCFF",
    #     ).grid(row=0, column=0, padx=5, pady=10)
    #     tk.Button(
    #         self.dashboard_insert_frame,
    #         text="HELP",
    #         font=self.button_font,
    #         bg="#4380FA",
    #         fg=self.btn_fg,
    #     ).grid(row=1, column=0, padx=10, pady=5, sticky="e")