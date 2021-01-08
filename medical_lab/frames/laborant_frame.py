from tkinter import messagebox
from medical_lab.frames.table_frame import TableFrame
import tkinter as tk
from tkinter import font as tkfont, ttk
from tkinter.constants import NW
from .base_frame import TitleFrame
from tkcalendar import Calendar
from datetime import datetime


class LaborantFrame(TitleFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.init()

    def init(self):
        self.bg_color = "gray97"
        self.btn_fg = "white"
        self.button_font = tkfont.Font(family="Helvetica", size=10)

        self.main_frame_welcome_label_var = tk.StringVar()

        laborant_frame = tk.Frame(master=self, bg=self.bg_color)
        laborant_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        for r in range(10):
            laborant_frame.rowconfigure(r, weight=1)
        for c in range(7):
            laborant_frame.columnconfigure(c, weight=1)

        welcome_label_frame = tk.Frame(laborant_frame, bg="gray97", bd=0)
        welcome_label_frame.grid(column=1, row=0, columnspan=6, rowspan=3, sticky=tk.NSEW)

        self.init_dashboard(laborant_frame)

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
        ).grid(row=0, column=5)
        self.search_button = tk.Entry(welcome_label_frame)
        self.search_button.grid(row=0, column=6, padx=5, pady=10)
        self.base_frame = laborant_frame
        self.table = None
        self.populate_table_bulletin_test()

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

        self._dashboard_button("View tests bulletin", lambda: self.populate_table_bulletin_test(), 1, (30, 5))
        self._dashboard_button("Add test bulletin", lambda: self.add_testBulletin(), 2)
        self._dashboard_button("Remove test bulletin", lambda: self.remove_testBulletin(), 3)
        self._dashboard_button("Update Test bulletin", lambda: self.update_testBulletin(), 4)
        self._dashboard_button("View administered tests", lambda: self.populate_table_administrated_tests(), 5, (30, 5))
        self._dashboard_button("Add administrated test", lambda: self.add_administeredTest(), 6)
        self._dashboard_button("Remove administrated test", lambda: self.remove_administratedtest(), 7)

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
        from tkinter import messagebox

        if messagebox.askokcancel("Logout", "Are you sure you want to logout?"):
            self.controller.render_frame("LoginFrame")

    def add_administeredTest(self):

        self.win2 = tk.Toplevel()
        self.win2.title("Add Administered Test")
        self.win2.geometry("500x500")
        self.win2.resizable(0, 0)
        self.win2.config(bg="gray97")
        width_label = 15

        nume_test_insert_frame = tk.LabelFrame(self.win2, bg="gray94")
        nume_test_insert_frame.grid(row=1, column=0, pady=15, padx=80, sticky="w")
        tk.Label(
            nume_test_insert_frame,
            text="Choose the administered test ",
            bg=nume_test_insert_frame["bg"],
            fg="#4380FA",
            width=30,
        ).grid(row=0, column=0)

        self.nume_test_insert = ttk.Combobox(self.win2, values=self._get_tests())
        self.nume_test_insert.grid(column=0, row=2)
        self.nume_test_insert.current(1)

        data_recoltare_insert_frame = tk.LabelFrame(self.win2, bg="gray94")
        data_recoltare_insert_frame.grid(row=3, column=0, pady=5, padx=80, sticky="w")
        tk.Label(
            data_recoltare_insert_frame,
            text="Date Collecting Blood Sample",
            bg=data_recoltare_insert_frame["bg"],
            fg="#4380FA",
            width=25,
        ).grid(row=0, column=0)
        now = datetime.now()
        self.data_recoltare_insert = Calendar(
            self.win2,
            font="Helvetica",
            selectmode="day",
            locale="en_US",
            cursor="hand1",
            year=now.year,
            month=now.month,
            day=now.day,
            mindate=now,
            maxdate=now,
            date_pattern="dd.mm.y",
        )
        self.data_recoltare_insert.grid(row=4, column=0, padx=5, pady=10)

        cnp_insert_frame = tk.LabelFrame(self.win2, bg="gray94")
        cnp_insert_frame.grid(row=5, column=0, pady=5, padx=80, sticky="w")
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
            command=lambda: self.insert_administrated_test(),
        ).place(x=80, y=450)
        self._exit_button(self.win2)

        self.win2.mainloop()

    def remove_administratedtest(self):

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
            text="Validation ",
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
        self._exit_button(self.win2)
        self.win2.mainloop()

    def add_testBulletin(self):

        self.win2 = tk.Toplevel()
        self.win2.title("Add Test Bulletin")
        self.win2.geometry("500x500")
        self.win2.resizable(0, 0)
        self.win2.config(bg="gray97")
        width_label = 18

        # cod_programare_insert_frame = tk.LabelFrame(self.win2, bg="gray94")
        # cod_programare_insert_frame.grid(row=0, column=0, pady=20, padx=80, sticky="w")
        # tk.Label(
        #     cod_programare_insert_frame,
        #     text="Validation Date ",
        #     bg=cod_programare_insert_frame["bg"],
        #     fg="#4380FA",
        #     width=width_label,
        # ).grid(row=0, column=0)
        # self.cod_programare_insert = tk.Entry(cod_programare_insert_frame)
        test_bulletin_insert_frame = tk.LabelFrame(self.win2, bg="gray94")
        test_bulletin_insert_frame.grid(row=1, column=0, pady=5, padx=80, sticky="w")
        tk.Label(
            test_bulletin_insert_frame,
            text="Validation Date",
            bg=test_bulletin_insert_frame["bg"],
            fg="#4380FA",
            width=25,
        ).grid(row=0, column=0)
        now = datetime.now()
        self.validation_date_insert = Calendar(
            self.win2,
            font="Helvetica",
            selectmode="day",
            locale="en_US",
            cursor="hand1",
            year=now.year,
            month=now.month,
            day=now.day,
            mindate=now,
            maxdate=now,
            date_pattern="dd.mm.y",
        )
        self.validation_date_insert.grid(row=2, column=0, padx=5, pady=10)

        data_insert_frame = tk.LabelFrame(self.win2, bg="gray94")
        data_insert_frame.grid(row=3, column=0, pady=20, padx=80, sticky="w")
        tk.Label(data_insert_frame, text="Result ", bg=data_insert_frame["bg"], fg="#4380FA", width=width_label).grid(
            row=0, column=0
        )
        self.result_insert = tk.Entry(data_insert_frame)
        self.result_insert.grid(row=0, column=1, padx=5, pady=10)

        cnp_insert_frame = tk.LabelFrame(self.win2, bg="gray94")
        cnp_insert_frame.grid(row=4, column=0, pady=20, padx=80, sticky="w")
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
            command=lambda: self.insert_test_bulletin(),
        ).place(x=80, y=450)
        self._exit_button(self.win2)
        self.win2.mainloop()

    def update_testBulletin(self):

        self.win2 = tk.Toplevel()
        self.win2.title("Update Test Bulletin")
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
        self._exit_button(self.win2)
        self.win2.mainloop()

    def remove_testBulletin(self):

        self.win2 = tk.Toplevel()
        self.win2.title("Remove Bulletin Test")
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

        self._command_button(self.win2, "Remove", lambda: self.Quit)
        self._exit_button(self.win2)
        self.win2.mainloop()

    def _command_button(self, window, title, command, y_axis=450):
        tk.Button(
            window,
            text=title,
            font=("Helvetica", 10),
            bg="gray97",
            fg="#4380FA",
            relief="flat",
            width=15,
            height=2,
            command=command,
        ).place(x=80, y=y_axis)

    def _exit_button(self, window, y_axis=450):
        tk.Button(
            window,
            text=("Exit"),
            font=("Helvetica", 10),
            bg="gray97",
            fg="#4380FA",
            relief="flat",
            width=15,
            height=2,
            command=self.Quit,
        ).place(x=270, y=y_axis)

    def Quit(self):
        answer = messagebox.askokcancel("Quit", "      Are you sure?")
        if answer:
            self.win2.destroy()

    def _return_id(self, table, id_suffix, filter_value, value):
        if not value:
            return
        query_select = f"SELECT id_{id_suffix} FROM {table} WHERE {filter_value} = '{value}'"
        result = self.controller.run_query(query_select)
        if len(result) > 1:
            print("nunu")
        else:
            return result[0][0]

    def _get_tests(self):
        query_select = "SELECT nume_test from teste"
        result = self.controller.run_query(query_select)
        flatten = [item for sublist in result for item in sublist]
        return flatten

    def insert_appointment(self):
        if not self.cod_programare_insert:
            return
        if not self.data_prog_insert:
            return
        if not self.cnp_insert:
            return
        id_pacient = self._return_id("pacienti", "pacient", "cnp", self.cnp_insert.get())
        id_asistent = self._return_id("asistenti", "asistent", "cod_asistent", self.employee_code.get())
        query_appointment = f"INSERT INTO programari VALUES (NULL, {self.cod_programare_insert.get()}, TO_DATE('{self.data_prog_insert.get_date()}', 'DD.MM.YYYY'), {id_pacient}, {id_asistent})"

        self.controller.run_query(query_appointment)
        self.populate_table_appointments()

    def populate_table_payments(self):
        if self.table:
            self.table.clear_table()
            self.table.destroy()
        query_view = list(map("".join, self.controller.get_columns_name("plati")))[:4]
        query_view.extend(list(map("".join, self.controller.get_columns_name("pacienti")))[1:3])

        self.table = TableFrame(self.base_frame, query_view)
        self.table.grid(row=1, column=1, columnspan=6, rowspan=9, sticky=tk.NSEW)
        self.table.tree.bind("<<TreeviewSelect>>")
        query_select = self.controller.run_query(
            """select id_plata, data_plata, total_plata,moneda, nume_pacient,cnp 
               from plati p, pacienti pa 
               where p.id_pacient=pa.id_pacient"""
        )
        for row in query_select:
            self.table.insert("", "end", values=row)

    def insert_payment(self):
        if not self.total_plata_insert:
            return
        if not self.data_plata_insert:
            return
        if not self.cnp_insert:
            return
        id_pacient = self._return_id("pacienti", "pacient", "cnp", self.cnp_insert.get())
        query_payment = f"INSERT INTO plati VALUES (NULL, TO_DATE('{self.data_plata_insert.get_date()}', 'DD.MM.YYYY'), {self.total_plata_insert.get()}, DEFAULT,  {id_pacient})"

        self.controller.run_query(query_payment)
        self.populate_table_payments()

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

    def insert_test_bulletin(self):
        if not self.result_insert:
            return
        if not self.cnp_insert:
            return
        if not self.validation_date_insert:
            return
        id_pacient = self._return_id("pacienti", "pacient", "cnp", self.cnp_insert.get())
        query_id_test_efectuat = f"SELECT t.id_test_efectuat FROM teste_efectuate t, pacienti p WHERE p.cnp = '{id_pacient}' AND t.id_pacient = p.id_pacient"
        id_test_efectuat = self.controller.run_query(query_id_test_efectuat)
        query_test_bulletin = f"INSERT INTO buletine_teste VALUES (NULL, TO_DATE('{self.validation_date_insert.get_date()}', 'DD.MM.YYYY'),'{self.result_insert.get()}','{id_test_efectuat}' )"
        self.controller.run_query(query_test_bulletin)
        self.populate_table_test_bulletin()

    def insert_administrated_test(self):
        if not self.data_recoltare_insert:
            return
        if not self.nume_test_insert:
            return
        if not self.cnp_insert:
            return
        id_pacient = self._return_id("pacienti", "pacient", "cnp", self.cnp_insert.get())
        id_asistent = self._return_id("asistenti", "asistent", "cod_asistent", self.employee_code.get())
        id_laborant = self._return_id("laboranti", "laborant", "cod_laborant", "0")
        id_test = self._return_id("teste", "test", "nume_test", self.nume_test_insert.get())
        query_administrated_test = f"INSERT INTO teste_efectuate VALUES (NULL, TO_DATE('{self.data_recoltare_insert.get_date()}', 'DD.MM.YYYY'), NULL, {id_pacient}, {id_asistent},{id_laborant}, {id_test})"

        self.controller.run_query(query_administrated_test)
        self.populate_table_administrated_tests()

    def populate_table_bulletin_test(self):
        if self.table:
            self.table.clear_table()
            self.table.destroy()
        query_view = list(map("".join, self.controller.get_columns_name("buletine_teste")))[:1]
        query_view.extend(list(map("".join, self.controller.get_columns_name("pacienti")))[1:3])
        query_view.extend(list(map("".join, self.controller.get_columns_name("teste")))[1:2])
        query_view.extend(list(map("".join, self.controller.get_columns_name("buletine_teste")))[2:3])
        query_view.extend(list(map("".join, self.controller.get_columns_name("detalii_teste")))[1:2])
        query_view.extend(list(map("".join, self.controller.get_columns_name("buletine_teste")))[1:2])

        self.table = TableFrame(self.base_frame, query_view)
        self.table.grid(row=1, column=1, columnspan=6, rowspan=9, sticky=tk.NSEW)
        self.table.tree.bind("<<TreeviewSelect>>")
        query_select = self.controller.run_query(
            """SELECT b.id_buletin_test, p.nume_pacient,p.cnp, t.nume_test, b.rezultat, d.interval_referinta, b.data_validare
                FROM teste_efectuate e, teste t, pacienti p, detalii_teste d, buletine_teste b
                WHERE e.id_test = t.id_test 
                AND d.id_test =  t.id_test
                AND p.id_pacient = e.id_pacient
                AND b.id_test_efectuat = e.id_test_efectuat"""
        )
        for row in query_select:
            self.table.insert("", "end", values=row)
