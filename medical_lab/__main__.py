from .gui import GUI
import tkinter as tk


def main():
    root = tk.Tk()
    GUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()