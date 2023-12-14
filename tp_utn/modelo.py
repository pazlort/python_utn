import re
from tkinter import messagebox
from database import Historiaclinica


class Crud:
    def __init__(self):
        self.complementos = Complementos()

    def alta(
        self,
        nombre_mascota,
        edad,
        color,
        especie,
        raza,
        sexo,
        nombre_duenio,
        mail,
        telefono,
        direccion,
        ciudad,
        tree,
        entry_nombre_mascota,
        entry_edad,
        entry_color,
        entry_especie,
        entry_raza,
        entry_sexo,
        entry_nombre_duenio,
        entry_mail,
        entry_telefono,
        entry_direccion,
        entry_ciudad,
    ):
        patron = "([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+([A-Z|a-z]{2,})+"
        if re.match(patron, mail):
            hc = Historiaclinica()
            hc.nombre_mascota = nombre_mascota
            hc.edad = edad
            hc.color = color
            hc.especie = especie
            hc.raza = raza
            hc.sexo = sexo
            hc.nombre_duenio = nombre_duenio
            hc.mail = mail
            hc.telefono = telefono
            hc.direccion = direccion
            hc.ciudad = ciudad
            hc.save()
            self.complementos.update_tree(tree)
            self.complementos.vaciar_campos(
                entry_nombre_mascota,
                entry_edad,
                entry_color,
                entry_especie,
                entry_raza,
                entry_sexo,
                entry_nombre_duenio,
                entry_mail,
                entry_telefono,
                entry_direccion,
                entry_ciudad,
            )
            messagebox.showinfo(
                message="Su historia clínica se dio de alta exitosamente",
                title="Historias Clinicas Veterinarias",
            )
        else:
            messagebox.showinfo(message="No ingreso un mail valido", title="ERROR")

    def modificar(
        self,
        par_nombre_mascota,
        par_edad,
        par_color,
        par_especie,
        par_raza,
        par_sexo,
        par_nombre_duenio,
        par_mail,
        par_telefono,
        par_direccion,
        par_ciudad,
        tree,
        entry_nombre_mascota,
        entry_edad,
        entry_color,
        entry_especie,
        entry_raza,
        entry_sexo,
        entry_nombre_duenio,
        entry_mail,
        entry_telefono,
        entry_direccion,
        entry_ciudad,
    ):
        valor = tree.selection()
        item = tree.item(valor)
        mi_id = item["text"]
        if (
            mi_id
            and par_nombre_mascota
            and par_ciudad
            and par_color
            and par_direccion
            and par_edad
            and par_especie
            and par_nombre_duenio
            and par_raza
            and par_sexo
            and par_telefono
        ):
            res = messagebox.askquestion(
                "Modificar historia clínica",
                "¿Está seguro que desea modificar esta historia clínica?",
            )
            if res == "yes":
                actualizar = Historiaclinica.update(
                    nombre_mascota=par_nombre_mascota,
                    edad=par_edad,
                    color=par_color,
                    especie=par_especie,
                    raza=par_raza,
                    sexo=par_sexo,
                    nombre_duenio=par_nombre_duenio,
                    mail=par_mail,
                    telefono=par_telefono,
                    direccion=par_direccion,
                    ciudad=par_ciudad,
                ).where(Historiaclinica.nro_historia_clinica == mi_id)
                actualizar.execute()
                self.complementos.update_tree(tree)
                self.complementos.vaciar_campos(
                    entry_nombre_mascota,
                    entry_edad,
                    entry_color,
                    entry_especie,
                    entry_raza,
                    entry_sexo,
                    entry_nombre_duenio,
                    entry_mail,
                    entry_telefono,
                    entry_direccion,
                    entry_ciudad,
                )
        elif not mi_id:
            messagebox.showinfo(
                message="Por favor hacer click en una historia clínica del listado",
                title="ERROR",
            )
        elif (
            # esto deberia validarlo en el alta pero como pidio solo usemos un regex lo valido aca de forma rustica
            not par_nombre_mascota
            and not par_ciudad
            and not par_color
            and not par_direccion
            and not par_edad
            and not par_especie
            and not par_nombre_duenio
            and not par_raza
            and not par_sexo
            and not par_telefono
        ):
            messagebox.showinfo(
                message="Por favor presione el botón seleccionar y realice las modificaciones que considere necesarias",
                title="ERROR",
            )
        elif (
            not par_nombre_mascota
            and not par_ciudad
            and not par_color
            and not par_direccion
            and not par_edad
            and not par_especie
            and not par_nombre_duenio
            and not par_raza
            and not par_sexo
            and not par_telefono
        ):
            messagebox.showinfo(
                message="Por favor ingrese todos los datos solicitados",
                title="ERROR",
            )

    def seleccionar(
        self,
        entry_nombre_mascota,
        entry_edad,
        entry_color,
        entry_especie,
        entry_raza,
        entry_sexo,
        entry_nombre_duenio,
        entry_mail,
        entry_telefono,
        entry_direccion,
        entry_ciudad,
        tree,
    ):
        self.complementos.vaciar_campos(
            entry_nombre_mascota,
            entry_edad,
            entry_color,
            entry_especie,
            entry_raza,
            entry_sexo,
            entry_nombre_duenio,
            entry_mail,
            entry_telefono,
            entry_direccion,
            entry_ciudad,
        )
        valor = tree.selection()
        item = tree.item(valor)
        mi_id = item["text"]
        if mi_id:
            hc = Historiaclinica.get_by_id(mi_id)
            entry_nombre_mascota.insert(0, hc.nombre_mascota)
            entry_edad.insert(0, hc.edad)
            entry_color.insert(0, hc.color)
            entry_especie.insert(0, hc.especie)
            entry_raza.insert(0, hc.raza)
            entry_sexo.insert(0, hc.sexo)
            entry_nombre_duenio.insert(0, hc.nombre_duenio)
            entry_mail.insert(0, hc.mail)
            entry_telefono.insert(0, hc.telefono)
            entry_direccion.insert(0, hc.direccion)
            entry_ciudad.insert(0, hc.ciudad)
        else:
            messagebox.showinfo(
                message="Por favor hacer click en una historia clínica del listado",
                title="ERROR",
            )

    def baja(self, tree):
        valor = tree.selection()
        item = tree.item(valor)
        mi_id = item["text"]
        if mi_id:
            res = messagebox.askquestion(
                "Eliminar historia clínica",
                "¿Está seguro que desea eliminar esta historia clínica?",
            )
            if res == "yes":
                borrar = Historiaclinica.get(
                    Historiaclinica.nro_historia_clinica == mi_id
                )
                borrar.delete_instance()
                tree.delete(valor)
        else:
            messagebox.showinfo(
                message="No seleccionó una historia clínica para eliminar",
                title="ERROR",
            )


class Complementos:
    def vaciar_campos(
        self,
        entry_nombre_mascota,
        entry_edad,
        entry_color,
        entry_especie,
        entry_raza,
        entry_sexo,
        entry_nombre_duenio,
        entry_mail,
        entry_telefono,
        entry_direccion,
        entry_ciudad,
    ):
        entry_nombre_mascota.delete(0, "end")
        entry_edad.delete(0, "end")
        entry_color.delete(0, "end")
        entry_especie.delete(0, "end")
        entry_raza.delete(0, "end")
        entry_sexo.delete(0, "end")
        entry_nombre_duenio.delete(0, "end")
        entry_mail.delete(0, "end")
        entry_telefono.delete(0, "end")
        entry_direccion.delete(0, "end")
        entry_ciudad.delete(0, "end")

    def update_tree(self, tree):
        ids = tree.get_children()
        for i in ids:
            tree.delete(i)
        for row in Historiaclinica.select():
            tree.insert(
                "",
                0,
                text=row.nro_historia_clinica,
                values=(
                    row.nombre_mascota,
                    row.edad,
                    row.color,
                    row.especie,
                    row.raza,
                    row.sexo,
                    row.nombre_duenio,
                    row.mail,
                    row.telefono,
                    row.direccion,
                    row.ciudad,
                ),
            )
