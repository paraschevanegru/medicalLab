from tkinter import messagebox
from medical_lab.frames.table_frame import TableFrame
import tkinter as tk
from tkinter import font as tkfont, ttk
from tkinter.constants import NW
from .base_frame import TitleFrame


class LaborantFrame(TitleFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.init()

    def init(self):
        self.bg_color = "white"
        self.btn_fg = "white"
        self.button_font = tkfont.Font(family="Helvetica", size=10)

        self.main_frame_welcome_label_var = tk.StringVar()

        laborant_frame = tk.Frame(master=self, bg=self.bg_color)
        laborant_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        laborant_frame.grid_rowconfigure(1, weight=1)
        laborant_frame.grid_columnconfigure(0, weight=1)
        laborant_frame.grid_columnconfigure(1, weight=1)

        welcome_label_frame = tk.LabelFrame(laborant_frame, bg="red", bd=0)
        welcome_label_frame.grid(column=2, row=0, columnspan=2, ipadx=430, ipady=0, sticky="NSEW")

        query = list(map("".join, self.controller.get_columns_name("Laboranti")))
        self.table = TableFrame(laborant_frame, query)
        self.table.grid(row=1, column=1, sticky="nsew")
        # self.populate_the_table_with_all_values()
        self.table.tree.bind("<<TreeviewSelect>>")
        self.init_dashboard(laborant_frame)

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
        ).grid(row=0, column=1, padx=10, pady=15, sticky="e")

    def init_dashboard(self, parent):

        self.dashboard_frame = tk.LabelFrame(parent, bg="gray97", bd=0)
        self.dashboard_frame.grid(row=1, column=0, columnspan=1, sticky="w")
        self.dashboard_frame.place(x=0, y=0, anchor="nw", width=225, height=650)

        Bulletin_button_frame = tk.LabelFrame(self.dashboard_frame, bg="gray97", bd=0)
        Bulletin_button_frame.grid(row=1, column=0, pady=10)
        tk.Label(
            Bulletin_button_frame,
            text="Dashboard",
            font=self.title_font,
            bg="gray97",
            fg="#99CCFF",
        ).grid(row=0, column=0, padx=35, pady=10)
        tk.Button(
            Bulletin_button_frame,
            text="Add test bulletin",
            font=self.button_font,
            bg="gray97",
            fg="#4380FA",
            relief="flat",
            width=20,
            #height=2,
            command=lambda: self.AddBulletinTest(),
        ).grid(row=1, column=0, padx=35, pady=5, sticky="w")

        tk.Button(
            Bulletin_button_frame,
            text="Remove test bulletin",
            font=self.button_font,
            bg="gray97",
            fg="#4380FA",
            relief="flat",
            width=20,
            #height=2,
            command=lambda: self.NewPage("Remove test bulletin"),
        ).grid(row=2, column=0, padx=35, pady=5, sticky="w")

        tk.Button(
            Bulletin_button_frame,
            text="Update test bulletin",
            font=self.button_font,
            bg="gray97",
            fg="#4380FA",
            relief="flat",
            width=20,
            command=lambda: self.NewPage("Update test bulletin"),
        ).grid(row=3, column=0, padx=35, pady=5, sticky="w")
        Admin_button_frame = tk.LabelFrame(self.dashboard_frame, bg="gray97", bd=0)
        Admin_button_frame.grid(row=2, column=0, pady=10)
        tk.Button(
            Admin_button_frame,
            text="Add administrated test",
            font=self.button_font,
            bg="gray97",
            fg="#4380FA",
            relief="flat",
            width=20,
            command=lambda: self.NewPage("add administrated test"),
        ).grid(row=4, column=0, padx=35, pady=5, sticky="w")
        tk.Button(
            Admin_button_frame,
            text="Remove administrated test",
            font=self.button_font,
            bg="gray97",
            fg="#4380FA",
            relief="flat",
            width=20,
            command=lambda: self.NewPage("Remove administrated test"),
        ).grid(row=5, column=0, padx=35, pady=5, sticky="w")
        tk.Button(
            Admin_button_frame,
            text="Update administrated test",
            font=self.button_font,
            bg="gray97",
            fg="#4380FA",
            relief="flat",
            width=20,
            command=lambda: self.NewPage("Update administrated test"),
        ).grid(row=6, column=0, padx=35, pady=5, sticky="w")

    def on_logout(self):
        from tkinter import messagebox

        if messagebox.askokcancel("Logout", "Are you sure you want to logout?"):
            self.controller.render_frame("LoginFrame")

    def NewPage(self,title_name):
        print("New Page")
        self.win2 = tk.Toplevel()
        self.win2.title(title_name)
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
    def AddBulletinTest(self):
            print("New Page")
            self.win2 = tk.Toplevel()
            self.win2.title("Add Bulletin Test")
            self.win2.geometry("500x500")
            self.win2.resizable(0, 0)
            self.win2.config(bg="gray97")
            width_label = 18

            cod_programare_insert_frame = tk.LabelFrame(self.win2, bg="gray94")
            cod_programare_insert_frame.grid(row=0, column=0, pady=20, padx=80, sticky="w")
            tk.Label(
                cod_programare_insert_frame,
                text="ceva text nu stiu ce vine aici ",
                bg=cod_programare_insert_frame["bg"],
                fg="#4380FA",
                width=width_label,
            ).grid(row=0, column=0)
            self.cod_programare_insert = tk.Entry(cod_programare_insert_frame)
            self.cod_programare_insert.grid(row=0, column=1, padx=5, pady=10)

            data_insert_frame = tk.LabelFrame(self.win2, bg="gray94")
            data_insert_frame.grid(row=1, column=0, pady=20, padx=80, sticky="w")
            tk.Label(
                data_insert_frame, text="Appointment Date ", bg=data_insert_frame["bg"], fg="#4380FA", width=width_label
            ).grid(row=0, column=0)
            self.data_prog_insert = tk.Entry(data_insert_frame)
            self.data_prog_insert.grid(row=0, column=1, padx=5, pady=10)

            nume_pacient_insert_frame = tk.LabelFrame(self.win2, bg="gray94")
            nume_pacient_insert_frame.grid(row=2, column=0, pady=20, padx=80, sticky="w")
            tk.Label(
                nume_pacient_insert_frame,
                text="Pacient Name ",
                bg=nume_pacient_insert_frame["bg"],
                fg="#4380FA",
                width=width_label,
            ).grid(row=0, column=0)
            self.nume_pacient_insert = tk.Entry(nume_pacient_insert_frame)
            self.nume_pacient_insert.grid(row=0, column=1, padx=5, pady=10)

            cnp_insert_frame = tk.LabelFrame(self.win2, bg="gray94")
            cnp_insert_frame.grid(row=3, column=0, pady=20, padx=80, sticky="w")
            tk.Label(
                cnp_insert_frame, text="Pacient CNP ", bg=cnp_insert_frame["bg"], fg="#4380FA", width=width_label
            ).grid(row=0, column=0)
            self.cnp_insert = tk.Entry(cnp_insert_frame)
            self.cnp_insert.grid(row=0, column=1, padx=5, pady=10)

            tk.Button(
                self.win2,
                text="Insert",
                font=("Helvetica", 10),
                bg="gray97",
                fg="#4380FA",
                relief="flat",
                width=15,
                height=2,
                command=self.Quit,
            ).place(x=80, y=450)
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
            a2.place(x=270, y=450)
            self.win2.mainloop()
