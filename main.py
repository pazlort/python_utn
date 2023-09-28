from tkinter import *
from tkinter import ttk
import sqlite3
import re
from tkinter import messagebox

# --------------------
# MODELO
# --------------------


# crear base
def create_db():
    conexion = sqlite3.connect("db_tp_final.db")
    return conexion


# crear tabla
def crear_tabla():
    conexion = create_db()
    cursor = conexion.cursor()
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


conexion = create_db()
crear_tabla()


def update_tree(tree):
    ids = tree.get_children()
    for i in ids:
        tree.delete(i)
    sql = "SELECT * FROM historiaclinica ORDER BY nro_historia_clinica ASC"
    conexion = create_db()
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


def alta(
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
):
    patron = "([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
    if re.match(patron, mail):
        conexion = create_db()
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
        update_tree(tree)
        vaciar_campos()
        messagebox.showinfo(
            message="Su historia clínica se dio de alta exitosamente",
            title="Historias Clinicas Veterinarias",
        )
    else:
        messagebox.showinfo(message="No ingreso un mail valido", title="ERROR")


def seleccionar(
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
):
    vaciar_campos()
    valor = tree.selection()
    item = tree.item(valor)
    mi_id = item["text"]
    if mi_id:
        conexion = create_db()
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
):
    valor = tree.selection()
    item = tree.item(valor)
    mi_id = item["text"]
    if (
        mi_id
        and var_nombre_mascota.get()
        and var_ciudad.get()
        and var_color.get()
        and var_direccion.get()
        and var_edad.get()
        and var_especie.get()
        and var_nombre_duenio.get()
        and var_raza.get()
        and var_sexo.get()
        and var_telefono.get()
    ):
        res = messagebox.askquestion(
            "Modificar historia clínica",
            "¿Está seguro que desea modificar esta historia clínica?",
        )
        if res == "yes":
            conexion = create_db()
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
            update_tree(tree)
            vaciar_campos()
    elif not mi_id:
        messagebox.showinfo(
            message="Por favor hacer click en una historia clínica del listado",
            title="ERROR",
        )
    elif (  # esto deberia validarlo en el alta pero como pidio solo usemos un regex lo valido aca de forma rustica
        not var_nombre_mascota.get()
        and not var_ciudad.get()
        and not var_color.get()
        and not var_direccion.get()
        and not var_edad.get()
        and not var_especie.get()
        and not var_nombre_duenio.get()
        and not var_raza.get()
        and not var_sexo.get()
        and not var_telefono.get()
    ):
        messagebox.showinfo(
            message="Por favor presione el botón seleccionar y realice las modificaciones que considere necesarias",
            title="ERROR",
        )
    elif (
        not var_nombre_mascota.get()
        or not var_ciudad.get()
        or not var_color.get()
        or not var_direccion.get()
        or not var_edad.get()
        or not var_especie.get()
        or not var_nombre_duenio.get()
        or not var_raza.get()
        or not var_sexo.get()
        or not var_telefono.get()
    ):
        messagebox.showinfo(
            message="Por favor ingrese todos los datos solicitados",
            title="ERROR",
        )


def baja(tree):
    valor = tree.selection()
    item = tree.item(valor)
    mi_id = item["text"]
    if mi_id:
        res = messagebox.askquestion(
            "Eliminar historia clínica",
            "¿Está seguro que desea eliminar esta historia clínica?",
        )
        if res == "yes":
            conexion = create_db()
            cursor = conexion.cursor()
            data = (mi_id,)
            sql = "DELETE FROM historiaclinica WHERE nro_historia_clinica = ?;"
            cursor.execute(sql, data)
            conexion.commit()
            tree.delete(valor)
    else:
        messagebox.showinfo(
            message="No seleccionó una historia clínica para eliminar", title="ERROR"
        )


def vaciar_campos():
    entry_nombre_mascota.delete(0, END)
    entry_edad.delete(0, END)
    entry_color.delete(0, END)
    entry_especie.delete(0, END)
    entry_raza.delete(0, END)
    entry_sexo.delete(0, END)
    entry_nombre_duenio.delete(0, END)
    entry_mail.delete(0, END)
    entry_telefono.delete(0, END)
    entry_direccion.delete(0, END)
    entry_ciudad.delete(0, END)


def cerrar():
    master.destroy()


# ##############################################
# VISTA
# ##############################################

# declaro variables
master = Tk()
var_nombre_mascota = StringVar()
var_edad = StringVar()
var_color = StringVar()
var_especie = StringVar()
var_raza = StringVar()
var_sexo = StringVar()
var_nombre_duenio = StringVar()
var_mail = StringVar()
var_telefono = StringVar()
var_direccion = StringVar()
var_ciudad = StringVar()


# pongo un título de la página
master.attributes("-fullscreen", True)
master.title("Historias clínicas veterinarias")

# Escribo el título del contenido
insert_text = Label(
    master,
    text="HISTORIA CLÍNICA",
    bg="#FFBCBA",
    fg="#5e6472",
    font=("Arial", 20, "bold"),
    anchor=CENTER,
)
insert_text.place(relx=0.5, y=20, anchor=CENTER)

master.configure(bg="#FFBCBA")


# formulario
nombre_mascota = Label(
    master,
    text="Nombre mascota: ",
    bg="#FFBCBA",
    fg="#5e6472",
    font=("Arial", 11, "bold"),
)
nombre_mascota.place(x=150, y=50)
edad = Label(
    master, text="Edad: ", bg="#FFBCBA", fg="#5e6472", font=("Arial", 11, "bold")
)
edad.place(x=150, y=80)
color = Label(
    master, text="Color: ", bg="#FFBCBA", fg="#5e6472", font=("Arial", 11, "bold")
)
color.place(x=150, y=110)
especie = Label(
    master, text="Especie: ", bg="#FFBCBA", fg="#5e6472", font=("Arial", 11, "bold")
)
especie.place(x=150, y=140)
raza = Label(
    master, text="Raza: ", bg="#FFBCBA", fg="#5e6472", font=("Arial", 11, "bold")
)
raza.place(x=150, y=170)
sexo = Label(
    master, text="Sexo: ", bg="#FFBCBA", fg="#5e6472", font=("Arial", 11, "bold")
)
sexo.place(x=150, y=200)
nombre_duenio = Label(
    master,
    text="Nombre dueño: ",
    bg="#FFBCBA",
    fg="#5e6472",
    font=("Arial", 11, "bold"),
)
nombre_duenio.place(x=600, y=50)
mail = Label(
    master, text="E-mail: ", bg="#FFBCBA", fg="#5e6472", font=("Arial", 11, "bold")
)
mail.place(x=600, y=80)
telefono = Label(
    master, text="Teléfono: ", bg="#FFBCBA", fg="#5e6472", font=("Arial", 11, "bold")
)
telefono.place(x=600, y=110)
direccion = Label(
    master, text="Dirección: ", bg="#FFBCBA", fg="#5e6472", font=("Arial", 11, "bold")
)
direccion.place(x=600, y=140)
ciudad = Label(
    master, text="Ciudad: ", bg="#FFBCBA", fg="#5e6472", font=("Arial", 11, "bold")
)
ciudad.place(x=600, y=170)


entry_nombre_mascota = Entry(master, textvariable=var_nombre_mascota)
entry_nombre_mascota.place(x=300, y=50)
entry_edad = Entry(master, textvariable=var_edad)
entry_edad.place(x=300, y=80)
entry_color = Entry(master, textvariable=var_color)
entry_color.place(x=300, y=110)
entry_especie = Entry(master, textvariable=var_especie)
entry_especie.place(x=300, y=140)
entry_raza = Entry(master, textvariable=var_raza)
entry_raza.place(x=300, y=170)
entry_sexo = Entry(master, textvariable=var_sexo)
entry_sexo.place(x=300, y=200)
entry_nombre_duenio = Entry(master, textvariable=var_nombre_duenio)
entry_nombre_duenio.place(x=750, y=50)
entry_mail = Entry(master, textvariable=var_mail)
entry_mail.place(x=750, y=80)
entry_telefono = Entry(master, textvariable=var_telefono)
entry_telefono.place(x=750, y=110)
entry_direccion = Entry(master, textvariable=var_direccion)
entry_direccion.place(x=750, y=140)
entry_ciudad = Entry(master, textvariable=var_ciudad)
entry_ciudad.place(x=750, y=170)


# treeview
tree = ttk.Treeview(master, selectmode="browse", height=20)
tree["columns"] = (
    "col1",
    "col2",
    "col3",
    "col4",
    "col5",
    "col6",
    "col7",
    "col8",
    "col9",
    "col10",
    "col11",
)
tree.column("#0", width=50, minwidth=50, anchor=W)
tree.column("col1", width=150, minwidth=150, anchor=W)
tree.column("col2", width=50, minwidth=50, anchor=W)
tree.column("col3", width=75, minwidth=75, anchor=W)
tree.column("col4", width=100, minwidth=100, anchor=W)
tree.column("col5", width=100, minwidth=100, anchor=W)
tree.column("col6", width=100, minwidth=100, anchor=W)
tree.column("col7", width=150, minwidth=150, anchor=W)
tree.column("col8", width=200, minwidth=200, anchor=W)
tree.column("col9", width=100, minwidth=100, anchor=W)
tree.column("col10", width=200, minwidth=200, anchor=W)
tree.column("col11", width=100, minwidth=100, anchor=W)


tree.heading("#0", text="Nro")
tree.heading("col1", text="nombre_mascota")
tree.heading("col2", text="edad")
tree.heading("col3", text="color")
tree.heading("col4", text="especie")
tree.heading("col5", text="raza")
tree.heading("col6", text="sexo")
tree.heading("col7", text="nombre_duenio")
tree.heading("col8", text="mail")
tree.heading("col9", text="telefono")
tree.heading("col10", text="direccion")
tree.heading("col11", text="ciudad")
tree.place(x=0, y=300)

update_tree(tree)
# insertamos botones
boton_alta = Button(
    master,
    text="Alta",
    command=lambda: alta(
        var_nombre_mascota.get(),
        var_edad.get(),
        var_color.get(),
        var_especie.get(),
        var_raza.get(),
        var_sexo.get(),
        var_nombre_duenio.get(),
        var_mail.get(),
        var_telefono.get(),
        var_direccion.get(),
        var_ciudad.get(),
        tree,
    ),
)
boton_alta.place(x=200, y=240)
boton_selecccionar = Button(
    master,
    text="Seleccionar",
    command=lambda: seleccionar(
        var_nombre_mascota.get(),
        var_edad.get(),
        var_color.get(),
        var_especie.get(),
        var_raza.get(),
        var_sexo.get(),
        var_nombre_duenio.get(),
        var_mail.get(),
        var_telefono.get(),
        var_direccion.get(),
        var_ciudad.get(),
    ),
)
boton_selecccionar.place(x=350, y=240)
boton_modificar = Button(
    master,
    text="Modificar",
    command=lambda: modificar(
        var_nombre_mascota.get(),
        var_edad.get(),
        var_color.get(),
        var_especie.get(),
        var_raza.get(),
        var_sexo.get(),
        var_nombre_duenio.get(),
        var_mail.get(),
        var_telefono.get(),
        var_direccion.get(),
        var_ciudad.get(),
        tree,
    ),
)
boton_modificar.place(x=500, y=240)
boton_baja = Button(master, text="Eliminar", command=lambda: baja(tree))
boton_baja.place(x=650, y=240)
boton_borrar = Button(master, text="Vaciar campos", command=vaciar_campos)
boton_borrar.place(x=800, y=240)
boton_cerrar = Button(master, text="Cerrar", command=cerrar)
boton_cerrar.place(relx=1, y=20, anchor=E)


# ejecuto
master.mainloop()
