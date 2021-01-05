from tkinter import messagebox
from medical_lab.frames.table_frame import TableFrame
import tkinter as tk
from tkinter import font as tkfont, ttk
from tkinter.constants import NW
from .base_frame import TitleFrame


class MainFrame(TitleFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.init()

    def init(self):
        self.bg_color = "white"
        self.btn_fg = "white"
        self.button_font = tkfont.Font(family="Helvetica", size=10)

        self.main_frame_welcome_label_var = tk.StringVar()

        main_frame = tk.Frame(master=self, bg=self.bg_color)
        main_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        main_frame.grid_rowconfigure(1, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)

        welcome_label_frame = tk.LabelFrame(main_frame, bg="red", bd=0)
        welcome_label_frame.grid(column=2, row=0, columnspan=2, ipadx=430, ipady=0, sticky="NSEW")

        query = list(map("".join, self.controller.get_columns_name("asistenti")))
        self.table = TableFrame(main_frame, query)
        self.table.grid(row=1, column=1, sticky="nsew")
        # self.populate_the_table_with_all_values()
        self.table.tree.bind("<<TreeviewSelect>>")
        self.init_dashboard(main_frame)

        tk.Label(
            welcome_label_frame,
            textvariable=self.main_frame_welcome_label_var,
            font=self.title_font,
            bg=self.bg_color,
            fg="#99CCFF",
        ).grid(row=0, column=2, padx=5, pady=10)
        tk.Button(
            welcome_label_frame,
            text="Logout",
            font=self.button_font,
            command=self.on_logout,
            bg="#4380FA",
            fg=self.btn_fg,
        ).grid(row=0, column=1, padx=10, pady=5, sticky="e")

    def init_dashboard(self, parent):

        self.dashboard_frame = tk.LabelFrame(parent, bg="gray97", bd=0)
        self.dashboard_frame.grid(row=1, column=0, columnspan=1, sticky="w")
        self.dashboard_frame.place(x=0, y=0, anchor="nw", width=225, height=650)

        tk.Label(
            self.dashboard_frame,
            text="Dashboard",
            font=self.title_font,
            bg="gray97",
            fg="#99CCFF",
        ).grid(row=0, column=0, padx=35, pady=10)
        tk.Button(
            self.dashboard_frame,
            text="Add payment",
            font=self.button_font,
            bg="gray97",
            fg="#4380FA",
            relief="flat",
            width=20,
            command=lambda: self.NewPage(),
        ).grid(row=1, column=0, padx=35, pady=15, sticky="w")

        tk.Button(
            self.dashboard_frame,
            text="Add appointment",
            font=self.button_font,
            bg="gray97",
            fg="#4380FA",
            relief="flat",
            width=20,
            command=lambda: self.NewPage(),
        ).grid(row=2, column=0, padx=35, pady=15, sticky="w")

        tk.Button(
            self.dashboard_frame,
            text="Add administered test",
            font=self.button_font,
            bg="gray97",
            fg="#4380FA",
            relief="flat",
            width=20,
            command=lambda: self.NewPage(),
        ).grid(row=3, column=0, padx=35, pady=15, sticky="w")

    def on_logout(self):
        from tkinter import messagebox

        if messagebox.askokcancel("Logout", "Are you sure you want to logout?"):
            self.controller.render_frame("LoginFrame")

    def NewPage(self):
        print("New Page")
        self.win2 = tk.Toplevel()
        self.win2.title("Add payment")
        self.win2.geometry("500x500")
        self.win2.resizable(0, 0)
        self.win2.config(bg="gray97")
        a2 = tk.Button(
            self.win2,
            text=("Exit"),
            font=("Helvetica", 10),
            bg="gray97",
            fg="#4380FA",
            relief="flat",
            width=15,
            height=2,
            command=self.Quit,
        )
        a2.place(x=190, y=450)
        self.win2.mainloop()

    def Quit(self):
        answer = messagebox.askokcancel("Quit", "      Are you sure?")
        if answer:
            self.win2.destroy()
