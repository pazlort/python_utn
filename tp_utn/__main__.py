from tkinter import Tk
from vista import Ventana
from modelo import DataBase

if __name__ == "__main__":
    master = Tk()
    DataBase()
    Ventana(master)
    master.mainloop()
