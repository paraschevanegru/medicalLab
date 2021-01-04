from .gui import GUI
import tkinter as tk
import configparser
from pathlib import Path


def main():
    config_path = Path(__file__).parent / "config.ini"
    config = configparser.ConfigParser()
    config.read(config_path)
    root = tk.Tk()
    GUI(root, config)
    root.mainloop()


if __name__ == "__main__":
    main()