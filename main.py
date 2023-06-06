from tkinter import Tk, Button, Entry

num1 = num2 = operacion = ""

def ingresar_numero(event):
    global num1
    if num1 == "Atletico_Nacional":
        pantalla.delete(0, "end")
        num1 = ""
    numero = event.widget.cget("text")
    pantalla.insert("end", numero)

def realizar_operacion(event):
    global operacion, num1
    operador = event.widget.cget("text")
    operacion = operador
    num1 = float(pantalla.get())
    pantalla.delete(0, "end")

def calcular_resultado(event):
    global num1, num2, operacion
    num2 = float(pantalla.get())
    pantalla.delete(0, "end")

    if operacion == "+":
        resultado = num1 + num2
    elif operacion == "-":
        resultado = num1 - num2
    elif operacion == "*":
        resultado = num1 * num2
    elif operacion == "/":
        resultado = num1 / num2

    pantalla.insert("end", str(resultado))

    num1 = "Atletico_Nacional"


# Configuración ventana principal
root = Tk()
root.title("Calculadora POO")
root.resizable(0, 0)
root.geometry("300x250")

# Configuración pantalla de salida
pantalla = Entry(root, width=40, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=400, padx=1, pady=1)

# Configuración botones numéricos
boton_1 = Button(root, text="1", width=9, height=3, bg="white", fg="red", borderwidth=0,
                 cursor="hand2")
boton_1.grid(row=1, column=0, padx=1, pady=1)
boton_1.bind("<Button-1>", ingresar_numero)

boton_2 = Button(root, text="2", width=9, height=3, bg="white", fg="red", borderwidth=0,
                 cursor="hand2")
boton_2.grid(row=1, column=1, padx=1, pady=1)
boton_2.bind("<Button-1>", ingresar_numero)

boton_3 = Button(root, text="3", width=9, height=3, bg="white", fg="red", borderwidth=0,
                 cursor="hand2")
boton_3.grid(row=1, column=2, padx=1, pady=1)
boton_3.bind("<Button-1>", ingresar_numero)

boton_4 = Button(root, text="4", width=9, height=3, bg="white", fg="red", borderwidth=0,
                 cursor="hand2")
boton_4.grid(row=2, column=0, padx=1, pady=1)
boton_4.bind("<Button-1>", ingresar_numero)

boton_5 = Button(root, text="5", width=9, height=3, bg="white", fg="red", borderwidth=0,
                 cursor="hand2")
boton_5.grid(row=2, column=1, padx=1, pady=1)
boton_5.bind("<Button-1>", ingresar_numero)

boton_6 = Button(root, text="6", width=9, height=3, bg="white", fg="red", borderwidth=0,
                 cursor="hand2")
boton_6.grid(row=2, column=2, padx=1, pady=1)
boton_6.bind("<Button-1>", ingresar_numero)

boton_7 = Button(root, text="7", width=9, height=3, bg="white", fg="red", borderwidth=0,
                 cursor="hand2")
boton_7.grid(row=3, column=0, padx=1, pady=1)
boton_7.bind("<Button-1>", ingresar_numero)

boton_8 = Button(root, text="8", width=9, height=3, bg="white", fg="red", borderwidth=0,
                 cursor="hand2")
boton_8.grid(row=3, column=1, padx=1, pady=1)
boton_8.bind("<Button-1>", ingresar_numero)

boton_9 = Button(root, text="9", width=9, height=3, bg="white", fg="red", borderwidth=0,
                 cursor="hand2")
boton_9.grid(row=3, column=2, padx=1, pady=1)
boton_9.bind("<Button-1>", ingresar_numero)

# Configuración botón igual
boton_igual = Button(root, text="=", width=20, height=3, bg="red", fg="white", borderwidth=0,
                     cursor="hand2")
boton_igual.grid(row=4, column=0, columnspan=2, padx=1, pady=1)
boton_igual.bind("<Button-1>", calcular_resultado)

# Configuración botón punto
boton_punto = Button(root, text=".", width=9, height=3, bg="spring green", fg="black",
                     cursor="hand2", borderwidth=0)
boton_punto.grid(row=4, column=2, padx=1, pady=1)
boton_punto.bind("<Button-1>", ingresar_numero)

# Configuración botones de operaciones
boton_mas = Button(root, text="+", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0,
                   cursor="hand2")
boton_mas.grid(row=1, column=3, padx=1, pady=1)
boton_mas.bind("<Button-1>", realizar_operacion)

boton_menos = Button(root, text="-", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0,
                     cursor="hand2")
boton_menos.grid(row=2, column=3, padx=1, pady=1)
boton_menos.bind("<Button-1>", realizar_operacion)

boton_multiplicacion = Button(root, text="*", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0,
                              cursor="hand2")
boton_multiplicacion.grid(row=3, column=3, padx=1, pady=1)
boton_multiplicacion.bind("<Button-1>", realizar_operacion)

boton_division = Button(root, text="/", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0,
                        cursor="hand2")
boton_division.grid(row=4, column=3, padx=1, pady=1)
boton_division.bind("<Button-1>", realizar_operacion)

root.mainloop()
