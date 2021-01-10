from tkinter import messagebox
from medical_lab.frames.table_frame import TableFrame
import tkinter as tk
from tkinter import font as tkfont
from tkinter.constants import NW
from .base_frame import TitleFrame
from tkinter import messagebox


class PacientFrame(TitleFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.init()

    def init(self):

        self.bg_color = "gray97"
        self.btn_fg = "white"
        self.button_font = tkfont.Font(family="Helvetica", size=10)

        self.main_frame_welcome_label_var = tk.StringVar()

        pacient_frame = tk.Frame(master=self, bg=self.bg_color)
        pacient_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        for r in range(10):
            pacient_frame.rowconfigure(r, weight=1)
        for c in range(7):
            pacient_frame.columnconfigure(c, weight=1)

        welcome_label_frame = tk.Frame(pacient_frame, bg="gray97", bd=0)
        welcome_label_frame.grid(column=1, row=0, columnspan=6, rowspan=2, sticky=tk.NSEW)

        self.init_dashboard(pacient_frame)

        tk.Label(
            welcome_label_frame,
            textvariable=self.main_frame_welcome_label_var,
            font=self.title_font,
            bg=self.bg_color,
            fg="#99CCFF",
        ).grid(row=0, column=1, padx=5)
        tk.Button(
            welcome_label_frame,
            text="Logout",
            font=self.button_font,
            command=self.on_logout,
            bg="#4380FA",
            fg=self.btn_fg,
        ).grid(row=0, column=2, padx=5, sticky="e")

        self.base_frame = pacient_frame
        self.table = None

    def init_dashboard(self, parent):
        self.pacient_code = tk.StringVar()
        self.dashboard_frame = tk.Frame(parent, bg="gray97", bd=0)
        self.dashboard_frame.grid(row=0, column=0, rowspan=3, sticky=tk.NSEW)

        tk.Label(
            self.dashboard_frame,
            text="Dashboard",
            font=self.title_font,
            bg="gray97",
            fg="#99CCFF",
        ).grid(row=0, column=0, padx=10, pady=15)

        self._dashboard_button("View tets bulletin", lambda: self.populate_table_bulletin_test(), 2)
        self._dashboard_button("View Payments", lambda: self.populate_table_payments(), 3)

    def _dashboard_button(self, title, command, row, pady=5):
        tk.Button(
            self.dashboard_frame,
            text=title,
            font=self.button_font,
            bg="gray97",
            fg="#4380FA",
            relief="flat",
            width=20,
            command=command,
        ).grid(row=row, column=0, padx=35, pady=pady)

    def on_logout(self):
        if messagebox.askokcancel("Logout", "Are you sure you want to logout?"):
            if hasattr(self, "win2"):
                self.win2.destroy()
            self.controller.render_frame("LoginFrame")

    def populate_table_bulletin_test(self):
        if self.table:
            self.table.clear_table()
            self.table.destroy()
        query_view = list(map("".join, self.controller.get_columns_name("pacienti")))[1:3]
        query_view.extend(list(map("".join, self.controller.get_columns_name("teste")))[1:2])
        query_view.extend(list(map("".join, self.controller.get_columns_name("buletine_teste")))[2:3])
        query_view.extend(list(map("".join, self.controller.get_columns_name("detalii_teste")))[1:2])
        query_view.extend(list(map("".join, self.controller.get_columns_name("buletine_teste")))[1:2])

        self.table = TableFrame(self.base_frame, query_view)
        self.table.grid(row=1, column=1, columnspan=6, rowspan=9, sticky=tk.NSEW)
        self.table.tree.bind("<<TreeviewSelect>>")
        query_select = self.controller.run_query(
            f"""SELECT  p.nume_pacient,p.cnp, t.nume_test, b.rezultat, d.interval_referinta, b.data_validare
                FROM teste_efectuate e, teste t, pacienti p, detalii_teste d, buletine_teste b
                WHERE e.id_test = t.id_test 
                AND d.id_test =  t.id_test
                AND p.id_pacient = e.id_pacient
                AND b.id_test_efectuat = e.id_test_efectuat
                AND p.cnp = '{self.pacient_code.get()}'"""
        )
        for row in query_select:
            self.table.insert("", "end", values=row)

    def populate_table_payments(self):
        if self.table:
            self.table.clear_table()
            self.table.destroy()
        query_view = list(map("".join, self.controller.get_columns_name("pacienti")))[1:2]
        query_view.extend(list(map("".join, self.controller.get_columns_name("teste")))[1:2])
        query_view.extend(list(map("".join, self.controller.get_columns_name("teste")))[2:3])
        query_view.extend(list(map("".join, self.controller.get_columns_name("teste")))[3:4])
        query_view.extend(list(map("".join, self.controller.get_columns_name("plati")))[1:2])

        self.table = TableFrame(self.base_frame, query_view)
        self.table.grid(row=1, column=1, columnspan=6, rowspan=9, sticky=tk.NSEW)
        self.table.tree.bind("<<TreeviewSelect>>")
        query_select = self.controller.run_query(
            f"""SELECT  p.nume_pacient, t.nume_test, t.pret_test,t.moneda,pl.data_plata
                FROM teste_efectuate e, teste t, pacienti p, detalii_teste d, buletine_teste b,plati pl
                WHERE e.id_test = t.id_test 
                AND d.id_test =  t.id_test
                AND p.id_pacient = e.id_pacient
                AND b.id_test_efectuat = e.id_test_efectuat
                AND p.id_pacient = pl.id_pacient
                AND p.cnp = '{self.pacient_code.get()}'"""
        )
        for row in query_select:
            self.table.insert("", "end", values=row)