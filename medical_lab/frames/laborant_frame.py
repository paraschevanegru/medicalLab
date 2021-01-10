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
        self.popup_width_label = 18

        self.main_frame_welcome_label_var = tk.StringVar()
        self.employee_code = tk.StringVar()

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

        self.base_frame = laborant_frame
        self.table = None
        self.populate_table_test_bulletin()

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

        self._dashboard_button("View tests bulletin", lambda: self.populate_table_test_bulletin(), 1, (30, 5))
        self._dashboard_button("Add test bulletin", lambda: self.add_testBulletin(), 2)
        self._dashboard_button("Remove test bulletin", lambda: self.remove_testBulletin(), 3)
        self._dashboard_button("Update Test bulletin", lambda: self.update_testBulletin(), 4)
        self._dashboard_button("View administered tests", lambda: self.populate_table_adminstered_tests(), 5, (30, 5))
        self._dashboard_button("Update administered test", lambda: self.update_administeredTest(), 6)
        self._dashboard_button("Remove administered test", lambda: self.remove_adminsteredtest(), 7)

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

    def _popup_window(self, title, dim="500x500"):
        if hasattr(self, "win2"):
            self.win2.destroy()
        win2 = tk.Toplevel()
        win2.title(title)
        win2.geometry(dim)
        win2.resizable(0, 0)
        win2.config(bg="gray97")
        return win2

    def update_administeredTest(self):

        self.win2 = self._popup_window("Update Administered Test")

        id_test_efec_update_frame = self._popup_labelframe(0, "Administered Test ID", 25)
        self.id_test_efec_update = tk.Entry(id_test_efec_update_frame)
        self.id_test_efec_update.grid(row=0, column=1, padx=5, pady=5)

        self._popup_labelframe(1, "Date Processing Blood Sample", 25)
        now = datetime.now()
        self.data_prelucrare_update = Calendar(
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
        self.data_prelucrare_update.grid(row=2, column=0, padx=5, pady=10)

        cnp_update_frame = self._popup_labelframe(3, "Pacient CNP", self.popup_width_label)
        self.cnp_update = tk.Entry(cnp_update_frame)
        self.cnp_update.grid(row=0, column=1, padx=5, pady=10)

        self._command_button(self.win2, "Update", lambda: self.update_adminstered_test())
        self._exit_button(self.win2)

        self.win2.mainloop()

    def remove_adminsteredtest(self):

        self.win2 = self._popup_window("Remove Administered Test", "500x300")
        test_idefectuat_remove_frame = self._popup_labelframe(0, "Administered Test ID", self.popup_width_label)
        self.test_idefectuat_remove = tk.Entry(test_idefectuat_remove_frame)
        self.test_idefectuat_remove.grid(row=0, column=1, padx=5, pady=10)

        cnp_remove_frame = self._popup_labelframe(1, "Pacient CNP", self.popup_width_label)
        self.cnp_remove = tk.Entry(cnp_remove_frame)
        self.cnp_remove.grid(row=0, column=1, padx=5, pady=10)

        self._command_button(self.win2, "Remove", lambda: self.delete_administered_test(), 220)
        self._exit_button(self.win2, 220)
        self.win2.mainloop()

    def add_testBulletin(self):

        self.win2 = self._popup_window("Add Test Bulletin")

        id_test_efec_insert_frame = self._popup_labelframe(0, "Adminstered Test ID", 25)
        self.id_test_efec_insert = tk.Entry(id_test_efec_insert_frame)
        self.id_test_efec_insert.grid(row=0, column=1, padx=5, pady=10)

        self._popup_labelframe(1, "Validation Date", self.popup_width_label)
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

        result_insert_frame = self._popup_labelframe(3, "Result ", self.popup_width_label)
        self.result_insert = tk.Entry(result_insert_frame)
        self.result_insert.grid(row=0, column=1, padx=5, pady=10)

        cnp_insert_frame = self._popup_labelframe(4, "Pacient CNP", self.popup_width_label)
        self.cnp_insert = tk.Entry(cnp_insert_frame)
        self.cnp_insert.grid(row=0, column=1, padx=5, pady=10)

        self._command_button(self.win2, "Insert", lambda: self.insert_test_bulletin())
        self._exit_button(self.win2)
        self.win2.mainloop()

    def update_testBulletin(self):

        self.win2 = self._popup_window("Update Test Bulletin", "500x500")

        id_bulletinTest_update_frame = self._popup_labelframe(0, "Test Bulletin ID", self.popup_width_label)
        self.id_bulletinTest_update = tk.Entry(id_bulletinTest_update_frame)
        self.id_bulletinTest_update.grid(row=0, column=1, padx=35, pady=10)

        self._popup_labelframe(1, "Validation Date", self.popup_width_label)
        now = datetime.now()
        self.validation_date_update = Calendar(
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
        self.validation_date_update.grid(row=2, column=0, padx=35, pady=10)

        result_update_frame = self._popup_labelframe(3, "Result ", self.popup_width_label)
        self.result_update = tk.Entry(result_update_frame)
        self.result_update.grid(row=0, column=1, padx=35, pady=10)

        self._command_button(self.win2, "Update", lambda: self.update_test_bulletin())
        self._exit_button(self.win2)
        self.win2.mainloop()

    def remove_testBulletin(self):

        self.win2 = self._popup_window("Remove Test Bulletin", "500x200")

        id_bulletinTest_remove_frame = self._popup_labelframe(0, "Test Bulletin ID", self.popup_width_label)
        self.id_bulletinTest_remove = tk.Entry(id_bulletinTest_remove_frame)
        self.id_bulletinTest_remove.grid(row=0, column=1, padx=35, pady=35)

        self._command_button(self.win2, "Remove", lambda: self.delete_test_bulletin(), 120)
        self._exit_button(self.win2, 120)
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

    def populate_table_adminstered_tests(self):
        if self.table:
            self.table.clear_table()
            self.table.destroy()
        query = list(map("".join, self.controller.get_columns_name("teste_efectuate")))[:1]
        query.extend(list(map("".join, self.controller.get_columns_name("tipuri_teste")))[1:2])
        query.extend(list(map("".join, self.controller.get_columns_name("teste")))[1:3])
        query.extend(list(map("".join, self.controller.get_columns_name("teste_efectuate")))[2:3])
        query.extend(list(map("".join, self.controller.get_columns_name("laboranti")))[1:2])
        query.extend(list(map("".join, self.controller.get_columns_name("pacienti")))[1:3])

        self.table = TableFrame(self.base_frame, query)
        self.table.grid(row=1, column=1, columnspan=6, rowspan=9, sticky=tk.NSEW)
        self.table.tree.bind("<<TreeviewSelect>>")
        query_select = self.controller.run_query(
            """select id_test_efectuat,denumire_tip_test, nume_test, pret_test,data_prelucrare, cod_laborant, nume_pacient,cnp 
                from teste_efectuate e, teste t, tipuri_teste ti, laboranti l, pacienti p 
                where p.id_pacient=e.id_pacient 
                and l.id_laborant=e.id_laborant 
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
        else:
            self.check_cnp(self.cnp_insert.get())
        if not self.validation_date_insert:
            return
        query_test_bulletin = f"INSERT INTO buletine_teste VALUES (NULL, TO_DATE('{self.validation_date_insert.get_date()}', 'DD.MM.YYYY'),'{self.result_insert.get()}','{self.id_test_efec_insert.get()}' )"
        self.controller.run_query(query_test_bulletin)
        self.populate_table_test_bulletin()

    def check_cnp(self, value):
        if len(value) == 13 and int(value[0]) in [1, 2, 5, 6]:
            pass
        else:
            messagebox.showinfo("OK", "Wrong CNP")

    def update_adminstered_test(self):
        if not self.table.is_item_selected():
            messagebox.showinfo("Update Error", "Item not selected")
            return
        if not self.data_prelucrare_update:
            return
        if not self.id_test_efec_update:
            return
        if not self.cnp_update:
            return
        else:
            self.check_cnp(self.cnp_update.get())
        id_pacient = self._return_id("pacienti", "pacient", "cnp", self.cnp_update.get())
        id_laborant = self._return_id("laboranti", "laborant", "cod_laborant", self.employee_code.get())
        query_adminstered_test = f"UPDATE teste_efectuate SET data_prelucrare = TO_DATE('{self.data_prelucrare_update.get_date()}', 'DD.MM.YYYY'), id_laborant='{id_laborant}' WHERE id_pacient='{id_pacient}' AND id_test_efectuat='{self.id_test_efec_update.get()}'"

        self.controller.run_query(query_adminstered_test)
        self.populate_table_adminstered_tests()

    def delete_administered_test(self):
        if not self.table.is_item_selected():
            messagebox.showinfo("Delete Error", "Item not selected")
            return
        if not self.test_idefectuat_remove:
            return
        if not self.cnp_remove:
            return
        else:
            self.check_cnp(self.cnp_remove.get())
        id_pacient = self._return_id("pacienti", "pacient", "cnp", self.cnp_remove.get())
        query_delete = f"DELETE from teste_efectuate where id_test_efectuat = '{self.test_idefectuat_remove.get()}' and id_pacient = '{id_pacient}'"

        self.controller.run_query(query_delete)
        self.populate_table_adminstered_tests()

    def delete_test_bulletin(self):
        if not self.table.is_item_selected():
            messagebox.showinfo("Delete Error", "Item not selected")
            return
        if not self.id_bulletinTest_remove:
            return
        query_delete = f"DELETE from buletine_teste where id_buletin_test = '{self.id_bulletinTest_remove.get()}'"

        self.controller.run_query(query_delete)
        self.populate_table_test_bulletin()

    def update_test_bulletin(self):
        if not self.table.is_item_selected():
            messagebox.showinfo("Update Error", "Item not selected")
            return
        if not self.cnp_update:
            return
        else:
            self.check_cnp(self.cnp_update.get())
        if not self.id_bulletinTest_update:
            return
        if not self.validation_date_update:
            return
        if not self.result_update:
            return
        id_pacient = self._return_id("pacienti", "pacient", "cnp", self.cnp_update.get())
        query_update = f"UPDATE buletine_teste SET data_validare=TO_DATE('{self.validation_date_update.get_date()}', 'DD.MM.YYYY'), rezultat = '{self.result_update.get()}' where id_buletin_test = '{self.id_bulletinTest_update.get()}' and id_test_efectuat = '{id_pacient}' "

        self.controller.run_query(query_update)
        self.populate_table_test_bulletin()

    def populate_table_test_bulletin(self):
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
