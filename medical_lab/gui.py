import tkinter as tk
import cx_Oracle
from .frames.login_frame import LoginFrame
from .frames.asistent_frame import AsistentFrame
from .frames.laborant_frame import LaborantFrame
from .frames.pacient_frame import PacientFrame


class GUI:
    def __init__(self, window, config) -> None:
        self.window = window
        self.window.resizable(False, False)

        self.window.wm_title("🏥 Medical Laboratory")

        self.container = tk.Frame(bg="gray97")
        self.container.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        db_conf = config["Database"]
        dsn = cx_Oracle.makedsn(db_conf["host"], int(db_conf["port"]), service_name=db_conf["service_name"])
        self.connection = cx_Oracle.connect(db_conf["user"], db_conf["password"], dsn, encoding="UTF-8")

        self.user_info = {}

        self.frames = {}
        for F in (PacientFrame, AsistentFrame, LaborantFrame, LoginFrame):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky=tk.NSEW)
        self.render_frame("LoginFrame")

    def recreate_frame(self):
        for frame in self.frames.values():
            for widget in frame.winfo_children():
                widget.destroy()
        for F in (PacientFrame, AsistentFrame, LaborantFrame, LoginFrame):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky=tk.NSEW)
        self.render_frame("LoginFrame")

    def render_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()

    def run_query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        try:
            query_results = [row for row in cursor]
            self.connection.commit()
            cursor.close()
        except cx_Oracle.InterfaceError:
            self.connection.commit()
            cursor.close()
            return None
        return query_results

    def run_query_2(self, query1, query2):
        cursor = self.connection.cursor()
        cursor.execute(query1)
        cursor.execute(query2)
        try:
            self.connection.commit()
            cursor.close()
        except cx_Oracle.InterfaceError:
            self.connection.commit()
            cursor.close()
            return None

    def get_columns_name(self, table_name):
        query = f"SELECT column_name FROM USER_TAB_COLUMNS WHERE lower(table_name) = '{table_name}'"
        return self.run_query(query)

    @staticmethod
    def set_entry_text(widget, text):
        widget.delete(0, tk.END)
        widget.insert(0, text)

    def set_state(self, widget, state="disabled"):
        try:
            widget.configure(state=state)
        except tk.TclError:
            pass
        for child in widget.winfo_children():
            self.set_state(child, state=state)
