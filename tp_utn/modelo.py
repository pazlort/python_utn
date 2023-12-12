import sqlite3
import re
from tkinter import messagebox


class DataBase:
    def __init__(
        self,
    ):
        self.conexion = self.create_db()
        self.crear_tabla()

    # crear base
    def create_db(
        self,
    ):
        conexion = sqlite3.connect("db_tp_final.db")
        return conexion

    # crear tabla
    def crear_tabla(
        self,
    ):
        conexion = self.create_db()
        cursor = self.conexion.cursor()
        sql = """CREATE TABLE IF NOT EXISTS historiaclinica(
                nro_historia_clinica INTEGER PRIMARY KEY, 
                nombre_mascota TEXT, 
                edad INTEGER, 
                color TEXT, 
                especie TEXT, 
                raza TEXT, 
                sexo TEXT, 
                nombre_duenio TEXT, 
                mail TEXT, 
                telefono INTEGER, 
                direccion TEXT, 
                ciudad TEXT)
        """
        cursor.execute(sql)
        conexion.commit()


class Crud:
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
        print(
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
        )
        patron = "([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
        if re.match(patron, mail):
            conexion = db.create_db()
            cursor = conexion.cursor()
            data = (
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
            )
            sql = "INSERT INTO historiaclinica(nombre_mascota, edad, color, especie, raza, sexo, nombre_duenio, mail, telefono, direccion, ciudad) VALUES(?,?,?,?,?,?,?,?,?,?,?)"
            cursor.execute(sql, data)
            conexion.commit()
            complementos.update_tree(tree)
            complementos.vaciar_campos(
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
        complementos.vaciar_campos(
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
            conexion = db.create_db()
            cursor = conexion.cursor()
            data = (mi_id,)
            sql = "SELECT * FROM historiaclinica WHERE nro_historia_clinica= ?"
            cursor.execute(sql, data)
            seleccion = cursor.fetchall()
            for i in seleccion:
                entry_nombre_mascota.insert(0, i[1])
                entry_edad.insert(0, i[2])
                entry_color.insert(0, i[3])
                entry_especie.insert(0, i[4])
                entry_raza.insert(0, i[5])
                entry_sexo.insert(0, i[6])
                entry_nombre_duenio.insert(0, i[7])
                entry_mail.insert(0, i[8])
                entry_telefono.insert(0, i[9])
                entry_direccion.insert(0, i[10])
                entry_ciudad.insert(0, i[11])
            conexion.commit()
        else:
            messagebox.showinfo(
                message="Por favor hacer click en una historia clínica del listado",
                title="ERROR",
            )

    def modificar(
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
        valor = tree.selection()
        item = tree.item(valor)
        mi_id = item["text"]
        if (
            mi_id
            and nombre_mascota
            and ciudad
            and color
            and direccion
            and edad
            and especie
            and nombre_duenio
            and raza
            and sexo
            and telefono
        ):
            res = messagebox.askquestion(
                "Modificar historia clínica",
                "¿Está seguro que desea modificar esta historia clínica?",
            )
            if res == "yes":
                conexion = db.create_db()
                cursor = conexion.cursor()
                row = cursor.fetchall()
                print(row)
                data = (
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
                    mi_id,
                )
                sql = "UPDATE historiaclinica SET nombre_mascota = ?, edad=?,color=?, especie=?,raza=?, sexo=?, nombre_duenio=?,mail=?,telefono=?,direccion=?,ciudad=? WHERE nro_historia_clinica = ?"
                cursor.execute(sql, data)
                conexion.commit()
                complementos.update_tree(tree)
                complementos.vaciar_campos(
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
        elif (  # esto deberia validarlo en el alta pero como pidio solo usemos un regex lo valido aca de forma rustica
            not nombre_mascota
            and not ciudad
            and not color
            and not direccion
            and not edad
            and not especie
            and not nombre_duenio
            and not raza
            and not sexo
            and not telefono
        ):
            messagebox.showinfo(
                message="Por favor presione el botón seleccionar y realice las modificaciones que considere necesarias",
                title="ERROR",
            )
        elif (
            not nombre_mascota
            and not ciudad
            and not color
            and not direccion
            and not edad
            and not especie
            and not nombre_duenio
            and not raza
            and not sexo
            and not telefono
        ):
            messagebox.showinfo(
                message="Por favor ingrese todos los datos solicitados",
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
                conexion = db.create_db()
                cursor = conexion.cursor()
                data = (mi_id,)
                sql = "DELETE FROM historiaclinica WHERE nro_historia_clinica = ?;"
                cursor.execute(sql, data)
                conexion.commit()
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
        sql = "SELECT * FROM historiaclinica ORDER BY nro_historia_clinica ASC"
        conexion = db.create_db()
        cursor = conexion.cursor()
        datos = cursor.execute(sql)
        rows = datos.fetchall()
        for row in rows:
            tree.insert(
                "",
                0,
                text=row[0],
                values=(
                    row[1],
                    row[2],
                    row[3],
                    row[4],
                    row[5],
                    row[6],
                    row[7],
                    row[8],
                    row[9],
                    row[10],
                    row[11],
                ),
            )


db = DataBase()
complementos = Complementos()
