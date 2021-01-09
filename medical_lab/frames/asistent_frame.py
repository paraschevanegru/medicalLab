from tkinter import messagebox
from medical_lab.frames.table_frame import TableFrame
import tkinter as tk
from tkinter import font as tkfont, ttk
from tkinter.constants import NONE, NW
from .base_frame import TitleFrame
from tkcalendar import Calendar
from datetime import datetime
from tkinter import messagebox


class AsistentFrame(TitleFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.init()

    def init(self):
        self.bg_color = "gray97"
        self.btn_fg = "white"
        self.button_font = tkfont.Font(family="Helvetica", size=10)
        self.popup_width_label = 18

        self.main_frame_welcome_label_var = tk.StringVar()
        self.employee_code = tk.StringVar()

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

        tk.Label(
            self.dashboard_frame,
            text="Dashboard",
            font=self.title_font,
            bg="gray97",
            fg="#99CCFF",
        ).grid(row=0, column=0, padx=10, pady=15)
        self._dashboard_button("View payments", lambda: self.populate_table_payments(), 1, (5, 5))
        self._dashboard_button("Add payment", lambda: self.add_payment(), 2, 0)
        self._dashboard_button("Remove payment", lambda: self.remove_payment(), 3)
        self._dashboard_button("Update payment", lambda: self.update_payment(), 4)
        self._dashboard_button("View appointments", lambda: self.populate_table_appointments(), 5, (30, 5))
        self._dashboard_button("Add appointment", lambda: self.add_appointment(), 6)
        self._dashboard_button("Remove appointment", lambda: self.remove_appointment(), 7)
        self._dashboard_button("Update appointment", lambda: self.update_appointment(), 8)
        self._dashboard_button("View administered tests", lambda: self.populate_table_adminstered_tests(), 9, (30, 5))
        self._dashboard_button("Add administered test", lambda: self.add_administeredTest(), 10)

        self._dashboard_button("Remove administered test", lambda: self.remove_administeredTest(), 11)

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

    def _popup_window(self, title,dim="500x500"):
        win2 = tk.Toplevel()
        win2.title(title)
        win2.geometry(dim)
        win2.resizable(0, 0)
        win2.config(bg="gray97")
        return win2

    def add_appointment(self):
        self.win2 = self._popup_window("Add Appointment")

        cod_programare_insert_frame = self._popup_labelframe(0, "Appointment Code", self.popup_width_label)
        self.cod_programare_insert = tk.Entry(cod_programare_insert_frame)
        self.cod_programare_insert.grid(row=0, column=1, padx=5, pady=10)

        self._popup_labelframe(1, "Appointment Date", self.popup_width_label)
        now = datetime.now()
        self.data_prog_insert = Calendar(
            self.win2,
            font="Helvetica",
            selectmode="day",
            locale="en_US",
            cursor="hand1",
            year=now.year,
            month=now.month,
            day=now.day,
            mindate=now,
            date_pattern="dd.mm.y",
        )
        self.data_prog_insert.grid(row=2, column=0, pady=20, padx=80, sticky="w")

        cnp_insert_frame = self._popup_labelframe(3, "Pacient CNP", self.popup_width_label)
        self.cnp_insert = tk.Entry(cnp_insert_frame)
        self.cnp_insert.grid(row=0, column=1, padx=5, pady=10)

        self._command_button(self.win2, "Insert", lambda: self.insert_appointment(), 450)
        self._exit_button(self.win2, 450)
        self.win2.mainloop()

    def update_appointment(self):

        self.win2 = self._popup_window("Update Appointment")

        cod_programare_update_frame = self._popup_labelframe(0, "Appointment Code", self.popup_width_label)
        self.cod_programare_update = tk.Entry(cod_programare_update_frame)
        self.cod_programare_update.grid(row=0, column=1, padx=5, pady=10)

        self._popup_labelframe(1, "Appointment Date", self.popup_width_label)
        now = datetime.now()
        self.data_prog_update = Calendar(
            self.win2,
            font="Helvetica",
            selectmode="day",
            locale="en_US",
            cursor="hand1",
            year=now.year,
            month=now.month,
            day=now.day,
            mindate=now,
            date_pattern="dd.mm.y",
        )
        self.data_prog_update.grid(row=2, column=0, pady=20, padx=80, sticky="w")

        cnp_update_frame = self._popup_labelframe(3, "Pacient CNP", self.popup_width_label)
        self.cnp_update = tk.Entry(cnp_update_frame)
        self.cnp_update.grid(row=0, column=1, padx=5, pady=10)

        self._command_button(self.win2, "Update", lambda: self.update_Appointment(), 450)
        self._exit_button(self.win2, 450)
        self.win2.mainloop()

    def remove_appointment(self):

        self.win2 = self._popup_window("Remove Appointment","500x300")

        cod_programare_remove_frame = self._popup_labelframe(0, "Appointment Code", self.popup_width_label)
        self.cod_programare_remove = tk.Entry(cod_programare_remove_frame)
        self.cod_programare_remove.grid(row=0, column=1, padx=5, pady=10)

        cnp_remove_frame = self._popup_labelframe(1, "Pacient CNP", self.popup_width_label)
        self.cnp_remove = tk.Entry(cnp_remove_frame)
        self.cnp_remove.grid(row=0, column=1, padx=5, pady=10)

        self._command_button(self.win2, "Remove", lambda: self.delete_appointment(),220)
        self._exit_button(self.win2,220)
        self.win2.mainloop()

    def add_administeredTest(self):

        self.win2 = self._popup_window("Add Adminstered Test")

        self._popup_labelframe(1, "Choose the administrated test", 25)

        self.nume_test_insert = ttk.Combobox(self.win2, values=self._get_tests())
        self.nume_test_insert.grid(column=0, row=2)
        self.nume_test_insert.current(1)

        self._popup_labelframe(3, "Date Collecting Blood Sample", 25)
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

        cnp_insert_frame = self._popup_labelframe(5, "Pacient CNP", self.popup_width_label)
        self.cnp_insert = tk.Entry(cnp_insert_frame)
        self.cnp_insert.grid(row=0, column=1, padx=5, pady=10)

        self._command_button(self.win2, "Remove", lambda: self.delete_payment(), 450)
        self._exit_button(self.win2, 450)
        self.win2.mainloop()

    def remove_administeredTest(self):

        self.win2 = self._popup_window("Remove Administered Test","500x300")

        self._popup_labelframe(0, "Choose the administrated test", 25)

        self.nume_test_remove = ttk.Combobox(self.win2, values=self._get_tests())
        self.nume_test_remove.grid(column=0, row=1)
        self.nume_test_remove.current(1)

        cnp_remove_frame = self._popup_labelframe(2, "Pacient CNP", self.popup_width_label)
        self.cnp_remove = tk.Entry(cnp_remove_frame)
        self.cnp_remove.grid(row=0, column=1, padx=5, pady=10)

        self._command_button(self.win2, "Remove", lambda: self.delete_adminstered_test(),220)
        self._exit_button(self.win2,220)
        self.win2.mainloop()

    def add_payment(self):

        self.win2 = self._popup_window("Add Payment")

        self._popup_labelframe(0, "Payment Date", self.popup_width_label)
        now = datetime.now()
        self.data_plata_insert = Calendar(
            self.win2,
            font="Helvetica",
            selectmode="day",
            locale="en_US",
            cursor="hand1",
            year=now.year,
            month=now.month,
            day=now.day,
            mindate=now,
            date_pattern="dd.mm.y",
        )
        self.data_plata_insert.grid(row=1, column=0, padx=5, pady=5)

        total_plata_insert_frame = self._popup_labelframe(2, "Total Payment", self.popup_width_label)
        self.total_plata_insert = tk.Entry(total_plata_insert_frame)
        self.total_plata_insert.grid(row=0, column=1, padx=5, pady=5)

        cnp_insert_frame = self._popup_labelframe(3, "Pacient CNP", self.popup_width_label)
        self.cnp_insert = tk.Entry(cnp_insert_frame)
        self.cnp_insert.grid(row=0, column=1, padx=5, pady=5)

        self._command_button(self.win2, "Insert", lambda: self.insert_payment(), 450)
        self._exit_button(self.win2, 450)
        self.win2.mainloop()

    def update_payment(self):

        self.win2 = self._popup_window("Update Payment","500x300")

        id_plata_update_frame = self._popup_labelframe(0, "Payment ID", self.popup_width_label)
        self.id_plata_update = tk.Entry(id_plata_update_frame)
        self.id_plata_update.grid(row=0, column=1, padx=5, pady=5)

        total_plata_update_frame = self._popup_labelframe(1, "Total Payment", self.popup_width_label)
        self.total_plata_update = tk.Entry(total_plata_update_frame)
        self.total_plata_update.grid(row=0, column=1, padx=5, pady=5)

        cnp_update_frame = self._popup_labelframe(2, "Pacient CNP", self.popup_width_label)
        self.cnp_update = tk.Entry(cnp_update_frame)
        self.cnp_update.grid(row=0, column=1, padx=5, pady=5)

        self._command_button(self.win2, "Update", lambda: self.update_Payment(),220)
        self._exit_button(self.win2,220)
        self.win2.mainloop()

    def remove_payment(self):

        self.win2 = self._popup_window("Remove Payment","500x300")

        id_plata_remove_frame = self._popup_labelframe(0, "Payment ID", self.popup_width_label)
        self.id_plata_remove = tk.Entry(id_plata_remove_frame)
        self.id_plata_remove.grid(row=0, column=1, padx=5, pady=5)

        cnp_remove_frame = self._popup_labelframe(1, "Pacient CNP", self.popup_width_label)
        self.cnp_remove = tk.Entry(cnp_remove_frame)
        self.cnp_remove.grid(row=0, column=1, padx=5, pady=10)

        self._command_button(self.win2, "Remove", lambda: self.delete_payment(),220)
        self._exit_button(self.win2,220)
        self.win2.mainloop()

    def _popup_labelframe(self, row, title, width_label):
        label_frame = tk.LabelFrame(self.win2, bg="gray94")
        label_frame.grid(row=row, column=0, pady=10, padx=80, sticky="w")
        tk.Label(
            label_frame,
            text=title,
            bg=label_frame["bg"],
            fg="#4380FA",
            width=width_label,
        ).grid(row=0, column=0)
        return label_frame

    def _command_button(self, window, title, command, y_axis=220):
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

    def _exit_button(self, window, y_axis=220):
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

    def update_Appointment(self):
        if not self.table.is_item_selected():
            messagebox.showinfo("Update Error", "Item not selected")
            return
        if not self.cod_programare_update:
            return
        if not self.data_prog_update:
            return
        if not self.cnp_update:
            return
        id_pacient = self._return_id("pacienti", "pacient", "cnp", self.cnp_update.get())
        query_update = f"UPDATE programari SET cod_programare='{self.cod_programare_update.get()}', data_programare=TO_DATE('{self.data_prog_update.get_date()}', 'DD.MM.YYYY') WHERE id_pacient={id_pacient}"
        self.controller.run_query(query_update)
        self.populate_table_appointments()

    def delete_appointment(self):
        if not self.table.is_item_selected():
            messagebox.showinfo("Delete Error", "Item not selected")
            return
        id_pacient = self._return_id("pacienti", "pacient", "cnp", self.cnp_remove.get())
        query_delete = f"DELETE FROM programari WHERE cod_programare='{self.cod_programare_remove.get()}' AND id_pacient={id_pacient}"
        self.controller.run_query(query_delete)
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

    def update_Payment(self):
        if not self.table.is_item_selected():
            messagebox.showinfo("Update Error", "Item not selected")
            return
        if not self.id_plata_update:
            return
        if not self.cnp_update:
            return
        id_pacient = self._return_id("pacienti", "pacient", "cnp", self.cnp_update.get())
        query_update = f"UPDATE plati SET total_plata='{self.total_plata_update.get()}'  WHERE id_pacient={id_pacient} AND id_plata='{self.id_plata_update.get()}'"
        self.controller.run_query(query_update)
        self.populate_table_payments()

    def delete_payment(self):
        if not self.table.is_item_selected():
            messagebox.showinfo("Delete Error", "Item not selected")
            return
        id_pacient = self._return_id("pacienti", "pacient", "cnp", self.cnp_remove.get())
        query_delete = f"DELETE FROM plati WHERE id_plata='{self.id_plata_remove.get()}' AND id_pacient={id_pacient}"
        self.controller.run_query(query_delete)
        self.populate_table_payments()

    def populate_table_adminstered_tests(self):
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

    def insert_adminstered_test(self):
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
        query_adminstered_test = f"INSERT INTO teste_efectuate VALUES (NULL, TO_DATE('{self.data_recoltare_insert.get_date()}', 'DD.MM.YYYY'), NULL, {id_pacient}, {id_asistent}, {id_laborant}, {id_test})"

        self.controller.run_query(query_adminstered_test)
        self.populate_table_adminstered_tests()

    def delete_adminstered_test(self):
        if not self.table.is_item_selected():
            messagebox.showinfo("Delete Error", "Item not selected")
            return
        id_pacient = self._return_id("pacienti", "pacient", "cnp", self.cnp_remove.get())
        id_test = self._return_id("teste", "test", "nume_test", self.nume_test_remove.get())
        query_delete = f"DELETE FROM teste_efectuate WHERE id_test='{id_test}' AND id_pacient={id_pacient}"
        self.controller.run_query(query_delete)
        self.populate_table_adminstered_tests()
