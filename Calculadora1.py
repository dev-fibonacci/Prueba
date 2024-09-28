from tkinter import *

# Función para agregar números y operadores a la entrada de texto
def click_boton(valor):
    e_texto.insert(END, valor)

# Función para borrar el contenido de la entrada de texto
def borrar():
    e_texto.delete(0, END)

# Función para borrar solo el último carácter de la entrada de texto
def borrar_uno():
    e_texto.delete(len(e_texto.get())-1, END)

# Función para evaluar la expresión y mostrar el resultado
def evaluar():
    try:
        resultado = eval(e_texto.get())
        e_texto.delete(0, END)
        e_texto.insert(END, resultado)
    except Exception as e:
        e_texto.delete(0, END)
        e_texto.insert(END, "Error")

# Creación de la ventana principal
ventana = Tk()
ventana.title("Calculadora 5to PC")
ventana.configure(bg="#800080")  # Fondo morado

e_texto = Entry(ventana, font=("Calibri 20"), bg="#D8BFD8")
e_texto.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# Creación de botones numéricos y de operaciones
botones = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '(', '+'
]

fila = 1
columna = 0
for boton in botones:
    Button(ventana, text=boton, width=5, height=2, bg="#D8BFD8", command=lambda b=boton: click_boton(b)).grid(row=fila, column=columna, padx=5, pady=5)
    columna += 1
    if columna > 3:
        columna = 0
        fila += 1

# Botones adicionales: "AC" para borrar todo, ")" para agregar paréntesis, "=" para evaluar, y una flecha para borrar un solo carácter
Button(ventana, text="AC", width=5, height=2, bg="#D8BFD8", command=borrar).grid(row=fila, column=0, padx=5, pady=5)
Button(ventana, text=")", width=5, height=2, bg="#D8BFD8", command=lambda: click_boton(')')).grid(row=fila, column=1, padx=5, pady=5)
Button(ventana, text="=", width=5, height=2, bg="#D8BFD8", command=evaluar).grid(row=fila, column=2, padx=5, pady=5)
Button(ventana, text="←", width=5, height=2, bg="#D8BFD8", command=borrar_uno).grid(row=fila, column=3, padx=5, pady=5)

ventana.mainloop()
