from tkinter import messagebox
from medical_lab.frames.table_frame import TableFrame
import tkinter as tk
from tkinter import font as tkfont, ttk
from tkinter.constants import NONE, NW
from .base_frame import TitleFrame


class AsistentFrame(TitleFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.init()

    def init(self):
        self.bg_color = "gray97"
        self.btn_fg = "white"
        self.button_font = tkfont.Font(family="Helvetica", size=10)

        self.main_frame_welcome_label_var = tk.StringVar()

        main_frame = tk.Frame(master=self, bg=self.bg_color)
        main_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        for r in range(10):
            main_frame.rowconfigure(r, weight=1)
        for c in range(7):
            main_frame.columnconfigure(c, weight=1)

        welcome_label_frame = tk.Frame(main_frame, bg="gray97", bd=0)
        welcome_label_frame.grid(column=1, row=0, columnspan=6, rowspan=3, sticky=tk.NSEW)

        self.init_dashboard(main_frame)

        tk.Label(
            welcome_label_frame,
            textvariable=self.main_frame_welcome_label_var,
            font=self.title_font,
            bg=self.bg_color,
            fg="#99CCFF",
        ).grid(row=0, column=1, padx=5, pady=15)
        tk.Button(
            welcome_label_frame,
            text="Logout",
            font=self.button_font,
            command=self.on_logout,
            bg="#4380FA",
            fg=self.btn_fg,
        ).grid(row=0, column=2, padx=5, pady=15, sticky="e")

        tk.Label(
            welcome_label_frame,
            text="Search",
            bg=welcome_label_frame["bg"],
            fg="#4380FA",
            width=18,
        ).grid(row=0, column=5, padx=5, pady=10)
        self.search_button = tk.Entry(welcome_label_frame)
        self.search_button.grid(row=0, column=6, padx=5, pady=10)
        self.base_frame = main_frame
        self.table = None
        self.populate_table_appointments()

    def init_dashboard(self, parent):

        self.dashboard_frame = tk.Frame(parent, bg="gray97", bd=0)
        self.dashboard_frame.grid(row=0, column=0, rowspan=10, sticky=tk.NSEW)
        # self.dashboard_frame.place(x=0, y=0, anchor="nw", width=225, height=650)

        tk.Label(
            self.dashboard_frame,
            text="Dashboard",
            font=self.title_font,
            bg="gray97",
            fg="#99CCFF",
        ).grid(row=0, column=0, padx=10, pady=15)

        tk.Button(
            self.dashboard_frame,
            text="View payments",
            font=self.button_font,
            bg="gray97",
            fg="#4380FA",
            relief="flat",
            width=20,
            command=lambda: self.populate_table_payments(),
        ).grid(row=1, column=0, padx=30, pady=(5, 5))
        tk.Button(
            self.dashboard_frame,
            text="Add payment",
            font=self.button_font,
            bg="gray97",
            fg="#4380FA",
            relief="flat",
            width=20,
            command=lambda: self.add_payment(),
        ).grid(row=2, column=0, padx=30)

        tk.Button(
            self.dashboard_frame,
            text="Remove payment",
            font=self.button_font,
            bg="gray97",
            fg="#4380FA",
            relief="flat",
            width=20,
            command=lambda: self.remove_payment(),
        ).grid(row=3, column=0, padx=30, pady=5)

        tk.Button(
            self.dashboard_frame,
            text="Update payment",
            font=self.button_font,
            bg="gray97",
            fg="#4380FA",
            relief="flat",
            width=20,
            command=lambda: self.update_payment(),
        ).grid(row=4, column=0, padx=30, pady=5)

        tk.Button(
            self.dashboard_frame,
            text="View appointments",
            font=self.button_font,
            bg="gray97",
            fg="#4380FA",
            relief="flat",
            width=20,
            command=lambda: self.populate_table_appointments(),
        ).grid(row=5, column=0, padx=35, pady=(30, 5))

        tk.Button(
            self.dashboard_frame,
            text="Add appointment",
            font=self.button_font,
            bg="gray97",
            fg="#4380FA",
            relief="flat",
            width=20,
            command=lambda: self.add_appointment(),
        ).grid(row=6, column=0, padx=35, pady=5)

        tk.Button(
            self.dashboard_frame,
            text="Remove appointment",
            font=self.button_font,
            bg="gray97",
            fg="#4380FA",
            relief="flat",
            width=20,
            command=lambda: self.remove_appointment(),
        ).grid(row=7, column=0, padx=35, pady=5)

        tk.Button(
            self.dashboard_frame,
            text="Update appointment",
            font=self.button_font,
            bg="gray97",
            fg="#4380FA",
            relief="flat",
            width=20,
            command=lambda: self.update_appointment(),
        ).grid(row=8, column=0, padx=35, pady=5)

        tk.Button(
            self.dashboard_frame,
            text="View administered tests",
            font=self.button_font,
            bg="gray97",
            fg="#4380FA",
            relief="flat",
            width=20,
            command=lambda: self.populate_table_administrated_tests(),
        ).grid(row=9, column=0, padx=35, pady=(30, 5))
        tk.Button(
            self.dashboard_frame,
            text="Add administered test",
            font=self.button_font,
            bg="gray97",
            fg="#4380FA",
            relief="flat",
            width=20,
            command=lambda: self.add_administeredTest(),
        ).grid(row=10, column=0, padx=35, pady=5)

        tk.Button(
            self.dashboard_frame,
            text="Remove administered test",
            font=self.button_font,
            bg="gray97",
            fg="#4380FA",
            relief="flat",
            width=20,
            command=lambda: self.remove_administeredTest(),
        ).grid(row=11, column=0, padx=35, pady=5)

        tk.Button(
            self.dashboard_frame,
            text="Update administered test",
            font=self.button_font,
            bg="gray97",
            fg="#4380FA",
            relief="flat",
            width=20,
            command=lambda: self.update_administeredTest(),
        ).grid(row=12, column=0, padx=35, pady=5)

    def on_logout(self):
        from tkinter import messagebox

        if messagebox.askokcancel("Logout", "Are you sure you want to logout?"):
            self.controller.render_frame("LoginFrame")

    def add_appointment(self):
        print("New Page")
        self.win2 = tk.Toplevel()
        self.win2.title("Add Appointment")
        self.win2.geometry("500x500")
        self.win2.resizable(0, 0)
        self.win2.config(bg="gray97")
        width_label = 18

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

    def update_appointment(self):
        print("New Page")
        self.win2 = tk.Toplevel()
        self.win2.title("Update Appointment")
        self.win2.geometry("500x500")
        self.win2.resizable(0, 0)
        self.win2.config(bg="gray97")
        width_label = 18

        cod_programare_insert_frame = tk.LabelFrame(self.win2, bg="gray94")
        cod_programare_insert_frame.grid(row=0, column=0, pady=20, padx=80, sticky="w")
        tk.Label(
            cod_programare_insert_frame,
            text="Appointment Code ",
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
            text="Update",
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

    def remove_appointment(self):
        print("New Page")
        self.win2 = tk.Toplevel()
        self.win2.title("Remove Appointment")
        self.win2.geometry("500x500")
        self.win2.resizable(0, 0)
        self.win2.config(bg="gray97")
        width_label = 18

        cod_programare_insert_frame = tk.LabelFrame(self.win2, bg="gray94")
        cod_programare_insert_frame.grid(row=0, column=0, pady=20, padx=80, sticky="w")
        tk.Label(
            cod_programare_insert_frame,
            text="Appointment Code ",
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
            text="Remove",
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

    def add_administeredTest(self):
        print("New Page")
        self.win2 = tk.Toplevel()
        self.win2.title("Add Administered Test")
        self.win2.geometry("500x500")
        self.win2.resizable(0, 0)
        self.win2.config(bg="gray97")
        width_label = 18

        cod_programare_insert_frame = tk.LabelFrame(self.win2, bg="gray94")
        cod_programare_insert_frame.grid(row=0, column=0, pady=20, padx=80, sticky="w")
        tk.Label(
            cod_programare_insert_frame,
            text="Appointment Code ",
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

    def update_administeredTest(self):
        print("New Page")
        self.win2 = tk.Toplevel()
        self.win2.title("Update Administered Test")
        self.win2.geometry("500x500")
        self.win2.resizable(0, 0)
        self.win2.config(bg="gray97")
        width_label = 18

        cod_programare_insert_frame = tk.LabelFrame(self.win2, bg="gray94")
        cod_programare_insert_frame.grid(row=0, column=0, pady=20, padx=80, sticky="w")
        tk.Label(
            cod_programare_insert_frame,
            text="Appointment Code ",
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
            text="Update",
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

    def remove_administeredTest(self):
        print("New Page")
        self.win2 = tk.Toplevel()
        self.win2.title("Remove Administered Test")
        self.win2.geometry("500x500")
        self.win2.resizable(0, 0)
        self.win2.config(bg="gray97")
        width_label = 18

        cod_programare_insert_frame = tk.LabelFrame(self.win2, bg="gray94")
        cod_programare_insert_frame.grid(row=0, column=0, pady=20, padx=80, sticky="w")
        tk.Label(
            cod_programare_insert_frame,
            text="Appointment Code ",
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
            text="Remove",
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

    def add_payment(self):
        print("New Page")
        self.win2 = tk.Toplevel()
        self.win2.title("Add Payment")
        self.win2.geometry("500x500")
        self.win2.resizable(0, 0)
        self.win2.config(bg="gray97")
        width_label = 18

        cod_programare_insert_frame = tk.LabelFrame(self.win2, bg="gray94")
        cod_programare_insert_frame.grid(row=0, column=0, pady=20, padx=80, sticky="w")
        tk.Label(
            cod_programare_insert_frame,
            text="Appointment Code ",
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

    def update_payment(self):
        print("New Page")
        self.win2 = tk.Toplevel()
        self.win2.title("Update Payment")
        self.win2.geometry("500x500")
        self.win2.resizable(0, 0)
        self.win2.config(bg="gray97")
        width_label = 18

        cod_programare_insert_frame = tk.LabelFrame(self.win2, bg="gray94")
        cod_programare_insert_frame.grid(row=0, column=0, pady=20, padx=80, sticky="w")
        tk.Label(
            cod_programare_insert_frame,
            text="Appointment Code ",
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
            text="Update",
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

    def remove_payment(self):
        print("New Page")
        self.win2 = tk.Toplevel()
        self.win2.title("Remove Payment")
        self.win2.geometry("500x500")
        self.win2.resizable(0, 0)
        self.win2.config(bg="gray97")
        width_label = 18

        cod_programare_insert_frame = tk.LabelFrame(self.win2, bg="gray94")
        cod_programare_insert_frame.grid(row=0, column=0, pady=20, padx=80, sticky="w")
        tk.Label(
            cod_programare_insert_frame,
            text="Appointment Code ",
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
            text="Remove",
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

    def Quit(self):
        answer = messagebox.askokcancel("Quit", "      Are you sure?")
        if answer:
            self.win2.destroy()

    def populate_table_appointments(self):
        if self.table:
            self.table.clear_table()
            self.table.destroy()
        query = list(map("".join, self.controller.get_columns_name("programari")))[:3]
        query.extend(list(map("".join, self.controller.get_columns_name("asistenti")))[1:2])
        query.extend(list(map("".join, self.controller.get_columns_name("pacienti")))[1:3])
        self.table = TableFrame(self.base_frame, query)
        self.table.grid(row=1, column=1, columnspan=6, rowspan=9, sticky=tk.NSEW)
        self.table.tree.bind("<<TreeviewSelect>>")
        query_select = self.controller.run_query(
            """select id_programare, cod_programare, data_programare, cod_asistent, nume_pacient,cnp 
               from programari p, asistenti a, pacienti pa 
               where p.id_pacient=pa.id_pacient and a.id_asistent=p.id_asistent"""
        )
        for row in query_select:
            self.table.insert("", "end", values=row)

    def populate_table_payments(self):
        if self.table:
            self.table.clear_table()
            self.table.destroy()
        query = list(map("".join, self.controller.get_columns_name("plati")))[:4]
        query.extend(list(map("".join, self.controller.get_columns_name("pacienti")))[1:3])

        self.table = TableFrame(self.base_frame, query)
        self.table.grid(row=1, column=1, columnspan=6, rowspan=9, sticky=tk.NSEW)
        self.table.tree.bind("<<TreeviewSelect>>")
        query_select = self.controller.run_query(
            """select id_plata, data_plata, total_plata,moneda, nume_pacient,cnp 
               from plati p, pacienti pa 
               where p.id_pacient=pa.id_pacient"""
        )
        for row in query_select:
            self.table.insert("", "end", values=row)

    def populate_table_administrated_tests(self):
        if self.table:
            self.table.clear_table()
            self.table.destroy()
        query = list(map("".join, self.controller.get_columns_name("teste_efectuate")))[:1]
        query.extend(list(map("".join, self.controller.get_columns_name("tipuri_teste")))[1:2])
        query.extend(list(map("".join, self.controller.get_columns_name("teste")))[1:3])
        query.extend(list(map("".join, self.controller.get_columns_name("teste_efectuate")))[1:2])
        query.extend(list(map("".join, self.controller.get_columns_name("asistenti")))[1:2])
        query.extend(list(map("".join, self.controller.get_columns_name("pacienti")))[1:3])

        self.table = TableFrame(self.base_frame, query)
        self.table.grid(row=1, column=1, columnspan=6, rowspan=9, sticky=tk.NSEW)
        self.table.tree.bind("<<TreeviewSelect>>")
        query_select = self.controller.run_query(
            """select id_test_efectuat,denumire_tip_test, nume_test, pret_test,data_recoltare, cod_asistent, nume_pacient,cnp 
                from teste_efectuate e, teste t, tipuri_teste ti, asistenti a, pacienti p 
                where p.id_pacient=e.id_pacient 
                and a.id_asistent=e.id_asistent 
                and t.id_test=e.id_test 
                and t.id_tip_test=ti.id_tip_test"""
        )
        for row in query_select:
            self.table.insert("", "end", values=row)
