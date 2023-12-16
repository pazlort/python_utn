# Importa la clase Tk del módulo tkinter. Tk es la clase principal que representa la ventana principal de la interfaz gráfica.
from tkinter import Tk

# Importa la clase Ventana desde un módulo llamado "vista". Este módulo contiene la implementación de la interfaz gráfica.
from vista import Ventana

# Verifica si el script está siendo ejecutado directamente (no importado como un módulo).
if __name__ == "__main__":
    # Crea una instancia de la clase Tk, que representa la ventana principal de la interfaz gráfica. El nombre "master" es una convención común para referirse a la ventana principal.
    master = Tk()
    # Crea una instancia de la clase Ventana (definida en el módulo "vista"), pasando la ventana principal (master) como argumento. Esto inicializa y configura la interfaz gráfica.
    Ventana(master)
    # Inicia el bucle principal de eventos de la interfaz gráfica, lo que permite que la ventana se mantenga abierta y responda a las interacciones del usuario hasta que la ventana se cierre.
    master.mainloop()
