from tkinter import *
ventana =Tk()
ventana.title("Calculadora")
ventana.configure(bg="grey")

#recursos
mensaje = StringVar()


#Funciones a usar para las cuatro operaciones aritmentias
def sumar():
    a=int(e_texto.get())
    b=int(e_texto2.get())
    print(a," + ",b)
    print('la suma es: ',a+b)
    mensaje.set(a+b)
    e_texto.delete(0, END)
    e_texto2.delete(0, END)

def restar():
    a=int(e_texto.get())
    b=int(e_texto2.get())
    print(a, " - ", b)
    print('la resta es: ',a-b)
    mensaje.set(a-b)
    e_texto.delete(0, END)
    e_texto2.delete(0, END)

def mult():
    a=int(e_texto.get())
    b=int(e_texto2.get())
    print(a, " * ", b)
    print('la multiplicacion es: ',a*b)
    mensaje.set(a*b)
    e_texto.delete(0, END)
    e_texto2.delete(0, END)

def div():
    a=int(e_texto.get())
    b=int(e_texto2.get())
    print(a, " / ", b)
    print('la divicion es: ',a/b)
    mensaje.set(a/b)
    e_texto.delete(0, END)
    e_texto2.delete(0, END)

#Entrada de texto
e_texto=Entry(ventana,bg="black",fg="white",justify='center')
e_texto2=Entry(ventana,bg="black",fg="white",justify='center')
salida=Label(ventana,textvariable=mensaje,justify='center',bg='grey')
msj=Label(ventana,text="Respuesta:",justify='center',bg='grey')

e_texto.grid(row=0,column=0,columnspan=2,padx=5,pady=5)
e_texto2.grid(row=0,column=2,columnspan=2,padx=5,pady=5)
salida.grid(row=4,column=1,columnspan=2,padx=5,pady=5)
msj.grid(row=4,column=0,columnspan=2,padx=5,pady=5)

#botones
btn_sum=Button(ventana,bg="grey",bd=5, text="+", width=5,height=2,command = lambda: sumar())
btn_rest=Button(ventana,bg="grey",bd=5, text="-", width=5,height=2,command = lambda: restar())
btn_mult=Button(ventana,bg="grey",bd=5, text="*", width=5,height=2,command = lambda: mult())
btn_div=Button(ventana,bg="grey",bd=5, text="/", width=5,height=2,command = lambda: div())


#agregamos los botones a la pantalla
btn_sum.grid(row=2,column=0,padx=5,pady=5)
btn_rest.grid(row=2,column=1,padx=5,pady=5)
btn_mult.grid(row=2,column=2,padx=5,pady=5)
btn_div.grid(row=2,column=3,padx=5,pady=5)

#fin del programa
ventana.mainloop()
print('***GRACIAS POR USAR EL PROGRAMA')