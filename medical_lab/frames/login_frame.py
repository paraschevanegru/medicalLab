import tkinter as tk
from tkinter import font as tkfont, ttk
from .base_frame import TitleFrame


class LoginFrame(TitleFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.init()

    def init(self):
        width_label = 10
        width_entry = 25

        text_font = tkfont.Font(family="Helvetica", size=13)
        button_font = tkfont.Font(family="Helvetica", size=10)

        login_frame = tk.Frame(master=self, bg="gold")
        login_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        login_frame.grid_rowconfigure(0, weight=1)
        login_frame.grid_columnconfigure(0, weight=1)

        login_label_frame = tk.LabelFrame(login_frame, bg="white")
        login_label_frame.grid(row=0, column=0)

        tk.Label(
            login_label_frame,
            text="account",
            font=text_font,
            bg=login_label_frame["bg"],
            fg="#000000",
            width=width_label,
        ).grid(row=0, column=0, padx=5, pady=10)
        self.variable = tk.StringVar(login_label_frame)
        self.variable.set("asistent")
        self.account_entry = tk.OptionMenu(login_label_frame, self.variable, "asistent", "laborant", "pacient")
        self.account_entry.grid(
            row=0,
            column=1,
        )

        tk.Label(
            login_label_frame,
            text="id",
            font=text_font,
            bg=login_label_frame["bg"],
            fg="#000000",
            width=width_label,
        ).grid(row=1, column=0, padx=5, pady=10)
        self.employee_id_entry = tk.Entry(login_label_frame, show="*", width=width_entry)
        self.employee_id_entry.grid(row=1, column=1, padx=5, pady=10)

        self.login_button = tk.Button(
            login_label_frame, text="Login", font=button_font, command=self.on_login, bg="#4380FA", fg="white"
        )
        self.login_button.grid(row=2, column=1, padx=5, pady=5)

    def set_states(self, user_level):
        if user_level == "pacient":
            return
        else:
            print("hey")
            if user_level == "laborant":
                print("buna")
            if user_level == "asistent":
                print("ziua")

    def on_login(self):
        query = ""
        account = self.variable.get()
        code = self.employee_id_entry.get()
        if account == "asistent":
            query = f"select a.id_asistent, a.nume_asistent, a.email from asistenti a where a.cod_asistent='{code}'"
        elif account == "laborant":
            query = f"select l.id_laborant, l.nume_laborant, l.email from laboranti l where l.cod_laborant='{code}'"
        elif account == "pacient":
            query = f"select p.id_pacient, p.nume_pacient, p.email from pacienti p where p.cnp='{code}'"

        user_info = [item for t in self.controller.run_query(query) for item in t]
        if user_info:
            self.controller.user_info["user_id"] = user_info[0]
            self.controller.user_info["name"] = user_info[1]
            self.controller.user_info["email"] = user_info[2]

            self.controller.recreate_frame()
            self.set_states(account)

            self.controller.render_frame("LoginFrame")
        else:
            from tkinter import messagebox

            messagebox.showinfo("Login Failed", "Wrong id")