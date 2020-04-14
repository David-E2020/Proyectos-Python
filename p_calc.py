menu='''==========MENU==========
1. Sumar
2. Restar
3. Multiplicar
4. dividir
5. salir
========================'''

sw=True

#Creamos las funciones para sumar restar multiplicar y dividir dos numeros

def sumar():
    a,b=pedir_numero()
    print('la suma es: ',a+b)

def restar():
    a,b=pedir_numero()
    print('la resta es:  ',a-b)

def multiplicar():
    a, b = pedir_numero()
    print('la multiplicacion es:  ',a * b)

def dividir():
    a, b = pedir_numero()
    print('la multiplicacion es:  ',a / b)

def pedir_numero():
    a = int(input('digite el primer numero:  '))
    b = int(input('digite el segundo numero:  '))
    return a,b

#creamos el bucle
while sw:
    print(menu)
    op=int(input('Digite una opcion:  '))
    if (op==1): sumar()
    elif(op==2): restar()
    elif(op==3): multiplicar()
    elif(op==4): dividir()
    elif(op==5): sw=False
    else: print("opcion incorrecta!")
print('***GRACIAS POR USAR EL PROGRAMA***')

#modo grafico


