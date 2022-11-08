'''
Materia: Lenguaje De Programación Python
Nombre: López Mercado Brayan
Matrícula: 1280838
Grupo: 531
Practica 12: args y kwargs
Archivo De Funciones
Fecha: 10 De Noviembre De 2022
'''
import math

def Area (*args):
    try:
        if len(args)==1:
            area=pow(args[0],2)
            print("El Area Del Cuadrado Es:",round(area,2),"u^2")
        elif len(args)==2:
            area=args[0]*args[1]
            print("El Area del Rectangulo Es:",round(area,2),"u^2")
        elif len(args)==3:
            semi=0
            for t in args:
                semi+=t
            semif=semi/2
            product=semif*(semif-args[0])*(semif-args[1])*(semif-args[2])
            area=math.sqrt(product)
            print("El Area Del Triangulo Es:",round(area,2),"u^2")
    except Exception:
        print("Error, Los Parametros No Son Validos")

def busqueda(buscado,**di):
    try:
        if buscado.title() in di:
            print("El Nombre Se Encuentra En El Diccionario")
        else:
            print("El Nombre No Se Encuentra En El Diccionario")
    except Exception:
        print("No Se Recibieron Parametros Válidos")

def dividirTupla(*args):
    print("Números Divididos Por El 1er Número De La Tupla")
    try:
        divisor=args[0]
        for x in range(1,len(args)):
            print(round(args[x]/divisor,2), end=" ")
    except Exception:
        print("La Tupla No Contiene Elementos o El Dato No Es Válido")

def printArray(array):
    print("\nElementos De La Tupla")
    for y in array:
        print(y,end=" ")
    print()

def menu():
    print("       Ménu")
    print("1) Area De Figuras")
    print("2) Busqueda De Nombres")
    print("3) Divisiones")
    print("4) Salir")

def main():
    d={
        'Billy':78,
        'Vanessa':87,
        'Joseph':78,
        'Brayan':86.7,
        'Jimmy':91,
        'Mandy':92,
        'Mari':100
    }
    try:
        menu()
        opc=int(input("Selecciona Una Opción: "))
        while opc<1 or opc>4:
            opc=int(input("Selecciona Una Opción Válida: "))
        if opc==1:
            a=[]
            for x in range(3):
                lado=float(input("Captura Un Lado: "))
                a.append(lado)
                opc=int(input("Continuar? (0/1): "))
                while opc<0 or opc>1:
                    opc=int(input("Continuar? (0/1): "))
                if opc==0:
                    break
            Area(*a)
        elif opc==2:
            buscar=input("Escribe Un Nombre A Buscar: ")
            busqueda(buscar,**d)
        elif opc==3:
            b=[]
            for t in range(100):
                N=float(input("Captura Un Número: "))
                b.append(N)
                opc=int(input("Continuar? (0/1): "))
                while opc<0 or opc>1:
                    opc=int(input("Continuar? (0/1): "))
                if opc==0:
                    break
            printArray(b)
            dividirTupla(*b)
            print()
        else:
            print("Hasta La Proxima")
    except Exception:
        print("Error En La Captura De Datos")
