# Importa la clase messagebox del módulo tkinter
from tkinter import messagebox


class Mensajes:
    def showinfo(self, mensaje):
        # Muestra un cuadro de diálogo de información.
        # Parameters:
        # - mensaje (str): El mensaje que se mostrará en el cuadro de diálogo.
        # Returns:
        # - str: El resultado del cuadro de diálogo.
        return messagebox.showinfo(
            message=mensaje, title="Historias Clinicas Veterinarias"
        )

    def askquestion(self, mensaje1, mensaje2):
        # Muestra un cuadro de diálogo de pregunta.
        # Parameters:
        # - mensaje1 (str): El mensaje principal de la pregunta.
        # - mensaje2 (str): El mensaje secundario de la pregunta.
        # Returns:
        # - str: El resultado de la pregunta.
        return messagebox.askquestion(mensaje1, mensaje2)
