import tkinter as tk
from tkinter import font as tkfont, ttk
from .base_frame import TitleFrame


class PacientFrame(TitleFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
