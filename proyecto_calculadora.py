from tkinter import *
ventana =Tk()
ventana.title("Calculadora")
ventana.configure(bg="grey")
i=0

#Entrada
e_texto = Entry(ventana, font=("Calibri 20"))
e_texto.grid(row =0, column=0, columnspan =4,padx =5, pady =5)
e_texto.configure(bg="CYAN")



#funciones
def clic_boton(valor):
    global i
    e_texto.insert(i,valor)
    i+=1

#borramos la pantalla
def borrar():
    e_texto.delete(0, END)
    i=0

#utilisamos una funcion de python eval que evalua una ecuacion en una cadena de caracteres
def hacer_operacion():
    ecuacion=e_texto.get()
    resultado=eval(ecuacion)
    e_texto.delete(0,END)
    e_texto.insert(0,resultado)
    i=0

#creamos los botones

bt1=Button(ventana,bg="grey",bd=5, text="1", width=5, height=2, command = lambda: clic_boton(1))
bt2=Button(ventana,bg="grey",bd=5, text="2", width=5, height=2, command = lambda: clic_boton(2))
bt3=Button(ventana,bg="grey",bd=5, text="3", width=5, height=2, command = lambda: clic_boton(3))
bt4=Button(ventana,bg="grey",bd=5, text="4", width=5, height=2, command = lambda: clic_boton(4))
bt5=Button(ventana,bg="grey",bd=5, text="5", width=5, height=2, command = lambda: clic_boton(5))
bt6=Button(ventana,bg="grey",bd=5, text="6", width=5, height=2, command = lambda: clic_boton(6))
bt7=Button(ventana,bg="grey",bd=5, text="7", width=5, height=2, command = lambda: clic_boton(7))
bt8=Button(ventana,bg="grey",bd=5, text="8", width=5, height=2, command = lambda: clic_boton(8))
bt9=Button(ventana,bg="grey",bd=5, text="9", width=5, height=2, command = lambda: clic_boton(9))
bt0=Button(ventana,bg="grey",bd=5, text="0", width=16, height=2, command = lambda: clic_boton(0))

bt_borrar = Button(ventana,bg="grey",bd=5, text="Limpiar", width=5, height=2, command = lambda: borrar())
bt_pa1=Button(ventana,bg="grey",bd=5, text="(", width=5, height=2, command = lambda: clic_boton("("))
bt_pa2=Button(ventana,bg="grey",bd=5, text=")", width=5, height=2, command = lambda: clic_boton(")"))
bt_punto=Button(ventana,bg="grey",bd=5, text=".", width=5, height=2, command = lambda: clic_boton("."))

bt_div=Button(ventana,bg="grey",bd=5, text="/", width=5, height=2, command = lambda: clic_boton("/"))
bt_mult=Button(ventana,bg="grey",bd=5, text="*", width=5, height=2, command = lambda: clic_boton("*"))
bt_sum=Button(ventana,bg="grey",bd=5, text="+", width=5, height=2, command = lambda: clic_boton("+"))
bt_rest=Button(ventana,bg="grey",bd=5, text="-", width=5, height=2, command = lambda: clic_boton("-"))
bt_igual=Button(ventana,bg="grey",bd=5, text="=", width=5, height=2, command = lambda: hacer_operacion())

#Agregar botones en pantalla

bt_borrar.grid(row=1,column=0,padx=5,pady=5)
bt_pa1.grid(row= 1,column= 1,padx=5,pady=5)
bt_pa2.grid(row= 1,column= 2,padx=5,pady=5)
bt_div.grid(row= 1,column= 3,padx=5,pady=5)

bt7.grid(row= 2,column= 0,padx=5,pady=5)
bt8.grid(row= 2,column= 1,padx=5,pady=5)
bt9.grid(row= 2,column= 2,padx=5,pady=5)
bt_mult.grid(row= 2,column= 3,padx=5,pady=5)

bt4.grid(row= 3,column= 0,padx=5,pady=5)
bt5.grid(row= 3,column= 1,padx=5,pady=5)
bt6.grid(row= 3,column= 2,padx=5,pady=5)
bt_sum.grid(row= 3,column= 3,padx=5,pady=5)

bt1.grid(row= 4,column= 0,padx=5,pady=5)
bt2.grid(row= 4,column= 1,padx=5,pady=5)
bt3.grid(row= 4,column= 2,padx=5,pady=5)
bt_rest.grid(row= 4,column= 3,padx=5,pady=5)

bt0.grid(row= 5,column= 0,columnspan=2,padx=5,pady=5)
bt_punto.grid(row= 5,column=2,padx=5,pady=5)
bt_igual.grid(row= 5,column= 3,padx=5,pady=5)

ventana.mainloop()