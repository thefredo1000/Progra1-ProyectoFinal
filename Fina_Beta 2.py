#=====================================================
#Proyecto Temario de Fisica
#20 de Noviember del 2018
#Autores
#A01231795 Diego Garza
#A0123--- Rodrigo Casale
#Programa desarollado en Python 3.6
#Este programa consta de funciones con las formulas de fisica 1
#el usuario ingresa los datos segun el problema dado
#es necesario que el usuario cuente con informacion sobre el tema de fisica


import numpy as np
import matplotlib
import matplotlib.pyplot as plt
#==========================
#Funcion main para que el programa sepa que funcion usar principal
#Entrada: la opcion seleccionada
#submenu para el tema escogido
#Autor: Rodrigo Casale
#============================
def main():

    print("Fisica 1")
    print("\nTEMARIO\n")
    
    option = menu()
    
    if (option <= 0):
        print("Gracias!")
    elif(option == 1):
        r = vectores()
        escribirArchivo(r)
    elif(option == 2):
        r = unaDimension()
        escribirArchivo(r)
    elif(option == 3):
        r = energia_potencial_gravitacional()
        escribirArchivo(r)
    elif(option == 4):
        r = energia_cinetica()
        escribirArchivo(r)
    elif(option == 5):
        r = potencia()
        escribirArchivo(r)
    elif(option == 6):
        r = energia_cinetica_resorte()
        escribirArchivo(r)
    elif(option == 7):
        r = trabajo()
        escribirArchivo(r)
    elif(option == 8):
        r = velocidad_relativa()
        escribirArchivo(r)
    elif(option == 9):
        r = segunda_ley_newton()
        escribirArchivo(r)
    elif(option == 10):
        r = friccion()
        escribirArchivo(r)
    elif(option == 11):
        r = trabajo_friccion()
        escribirArchivo(r)
    elif(option == 12):
        r = impulso()
        escribirArchivo(r)
    elif(option == 13):
        r = momentum()
        escribirArchivo(r)
    elif(option == 14):
        r = torsion()
        escribirArchivo(r)
    elif(option == 15):
        r = fuerza_centripeda()
        escribirArchivo(r)
    elif(option == 16):
        r = centro_de_masa()
        escribirArchivo(r)
    elif(option == 17):
        r = inersia()
        escribirArchivo(r)
    elif(option == 18):
        r = aceleracion_tangencial()
        escribirArchivo(r)
    elif(option == 19):
        imprime()
    elif(option== 20):
        borrar()
    print("-"*80)
    input("Presiona Enter para continuar")
    while(option!=0):
        main()
        
#==========================
#Funcion para escrivir archivo con los resultados daods
#Entrada: el resultado arrojado por el programa
#Salida: archivo de texto con los resultados
#Autor: Rodrigo Casale
#============================
def escribirArchivo(r):
    textFile = open("Historial_de_resultado.txt", "a")
    textFile.write("Tu resultado es ")
    textFile.write(str(r))
    textFile.write("\n")
    textFile.close()
#==========================
#Funcion para borrar los resultados hasta ahora
#Entrada: .
#salida: resultado 
#Autor: Diego Garza
#============================ 
def borrar():
    textFile = open("Historial_de_resultado.txt", "w")
    textFile.write(" ")
    textFile.close()
    
#==========================
#Funcion para leer e imprimir los resultados hasta ahora
#Entrada: resultados
#salida: resultado 
#Autor: Diego Garza
#============================ 
def imprime():
    t = open("Historial_de_resultado.txt", "r")
    t.seek(0,0)
    print("Tus resultados hasta ahora son:","\n")
    print(t.read())
    t.close()
#==========================
#Funcion para el menu principal
#Entrada: la opcion seleccionada
#salida:submenu para el tema escogido
#Autor: Rodrigo Casale
#============================  
def menu():
    option = 28
    
    while option > 20:
        
        print("\t1)  Vectores")
        print("\t2)  Movimiento en una dimension")
        print("\t3)  Energia Gravitacional Protencial")
        print("\t4)  Energia Cinetica")
        print("\t5)  Potencia")
        print("\t6)  Energia Potencial de Resorte")
        print("\t7)  Trabajo")
        print("\t8)  Velocidad Relativa")
        print("\t9)  Segunda Ley de Newton")
        print("\t10) Friccion")
        print("\t11) Trabajo friccion")
        print("\t12) Impulso")
        print("\t13) Momentum")
        print("\t14) Torsion")
        print("\t15) Fuerza Centripeda")
        print("\t16) Centro de Masa")
        print("\t17) Inersia")
        print("\t18) Aceleracion Tangencial")
        print("\t19) IMPRIMIR RESULTADOS")
        print("\t20) BORRAR RESULTADOS")
        print("\t0)  APAGAR PROGRAMA")
    
        print("\n\tINTRODUCIR UN VALOR DEL 0 AL 20")
        
        option = int(input("Introduce la opcion: "))
        print("-"*80)
        if option > 20:
            input("OPCION NO VALIDA - PRESIONE ENTER PARA CONTINUAR")
            
    return option
#==========================
#Funcion para el tema de vectores
#Entrada: opcion deseada por el usuario
#salida: resultado 
#Autor: Rodrigo Casale
#============================           
def vectores():
    print("FORMULARIO VECTORES\n")
    print("\t1) Componentes de vector \tAx")
    print("\t2) Componentes de vector \tAy")
    print("\t3) Resultante de vector  \tR")
    print("\t4) Notacion vectorial    \tA")
    print("\t5) Angulo entre vectores \tθ")
    print("\t6) Producto de vectores  \t→A·→B")
    print("\t7) Producto de vectores  \t|→A x →B|")
    
    option1 = int(input("¿Que quieres sacar? "))
    print("-"*80)

    if option1 == 1:
        print("\nAx = A*cos(θ)")
        
        valorA = float(input("\tIntroduce tu valor A: "))
        valorAngulo = float(input("\tIntroduce tu valor θ: "))
        
        valorAx = valorA * np.cos(np.deg2rad(valorAngulo))
        print("\nAx =", valorAx)
        return "Ax = " + str(valorAx)
        
    elif option1 == 2:
        print("\nAy = A*sin(θ)")
        
        valorA = float(input("\tIntroduce tu valor A: "))
        valorAngulo = float(input("\tIntroduce tu valor θ: "))
        
        valorAy = valorA * np.sin(np.deg2rad(valorAngulo))
        print("\nAy =", valorAy)
        return "Ay = " + str(valorAy)

    elif option1 == 3:
        print("R = √[(Ax^2) + (Ay^2)]")
        
        valorAx = float(input("\tIntroduce tu valor Ax: "))
        valorAy = float(input("\tIntroduce tu valor Ay: "))
        
        valorR = np.sqrt((valorAx**2) + (valorAy**2))
        
        print("\nR =", valorR)
        return "R = " + str(valorR)
        
    elif option1 == 4:
        print("Ā = (Ax, Ay, Az)")
        
        valorAx = float(input("\tIntroduce tu valor Ax: "))
        valorAy = float(input("\tIntroduce tu valor Ay: "))
        valorAz = float(input("\tIntroduce tu valor Az: "))
        
        valorA = "("+ str(valorAx) + ", "+ str(valorAy) + ", "+ str(valorAz)+ ")"
        
        print("\nĀ =", valorA)
        return "Ā = " + str(valorA)
        
    elif option1 == 5:
        print("θ = arctan( Ay/Ax )")
        
        valorAx = float(input("\tIntroduce tu valor Ax: "))
        valorAy = float(input("\tIntroduce tu valor Ay: "))
        
        valorAngulo = np.arctan(valorAy / valorAx)
        
        print("\nθ =", valorAngulo)
        return "θ = " + str(valorAngulo)
        
    elif option1 == 6:
        print("→A·→B = A*B * cos(θ))")
        
        valorA = float(input("\tIntroduce tu valor A: "))
        valorB = float(input("\tIntroduce tu valor B: "))
        valorAngulo = float(input("\tIntroduce tu valor θ: "))
        
        valorABpunto = valorA * valorB * np.cos(valorAngulo)
        
        print("\n→A·→B =", valorABpunto)
        return "→A·→B =" + str(valorABpunto)

    elif option1 == 7:
        print("|→A x →B| = A*B * sin(θ))")
        
        valorA = float(input("\tIntroduce tu valor A: "))
        valorB = float(input("\tIntroduce tu valor B: "))
        valorAngulo = float(input("\tIntroduce tu valor θ: "))
        
        valorABproducto = np.absolute(valorA * valorB * np.sin(valorAngulo))
        
        print("\n|→A x →B| =", valorABproducto)
        return "|→A x →B| = " + str(valorABproducto)
    else:
        print("Pon un valor real")
#==========================
#Funcion para el tema de movimiento en una dimension
#Entrada: opcion deseada por el usuario
#salida: resultado 
#Autor: Rodrigo Casale
#============================  
def unaDimension():
    print("FORMULARIO MOVIMIENTO EN UNA DIMENSION\n")
    print("\t1) Velocidad promedio    \tv")
    print("\t2) Desplacamiento final  \txf")
    print("\t3) Aceleracion promedio  \ta")
    print("\t4) Velocidad final       \tvf (con t)")
    print("\t5) Velocidad final       \tvf (con x)")
    
    option2 = int(input("¿Que quieres sacar? "))
    
    if option2 == 1:
        print("\nv = (xf - xo)/(Δt)")
        
        valorXf = float(input("\tIntroduce tu valor xf: "))
        valorXo = float(input("\tIntroduce tu valor xo: "))
        valorTiempo = float(input("\tIntroduce tu valor Δt: "))
        
        valorV = (valorXf - valorXo)/valorTiempo
        print("\nv =", valorV)
        return "v = " + str(valorV)
    
    elif option2 == 2:
        print("\nxf = xo + (vo * t) + (a * t^2 * 1/2)")
        
        valorXo = float(input("\tIntroduce tu valor xo: "))
        valorVo = float(input("\tIntroduce tu valor vo: "))
        valorTiempo = float(input("\tIntroduce tu valor t: "))
        valorA = float(input("\tIntroduce tu valor a: "))
        
        valorXf = valorXo + (valorVo*valorTiempo) + (valorA * (valorTiempo**2))/2
        print("\nxf =", valorXf)
        return "f = " + str(valorXf)
        
    elif option2 == 3:
        print("\na = (vf - vo)/(Δt)")
        
        valorVf = float(input("\tIntroduce tu valor vf: "))
        valorVo = float(input("\tIntroduce tu valor vo: "))
        valorTiempo = float(input("\tIntroduce tu valor Δt: "))
        
        valorA = (valorVf - valorVo)/valorTiempo
        valorVfo = valorVf - valorVo
        
        t = np.arange(-5.0, 15.0, 1)
        
        fig, ax = plt.subplots()
        ax.plot(t, t/valorVfo)
        
        ax.set(xlabel='time (s)', ylabel='velocity (s)',
               title='Grafica')
        ax.grid()
        
        fig.savefig("test.png")
        plt.show()
        
        print("\na =", valorA)
        return "a = "+ str(valorA)
    
    elif option2 == 4:
        print("\nvf = vo + (a * t)")
        
        valorVo = float(input("\tIntroduce tu valor vo: "))
        valorTiempo = float(input("\tIntroduce tu valor Δt: "))
        valorA = float(input("\tIntroduce tu valor a: "))
        
        valorVf = valorVo + (valorTiempo * valorA)
        print("\nvf =", valorVf)
        return "vf =" + str(valorVf)
        
    elif option2 == 5:
        print("\nvf = √[vo^2 + 2 * a * (xf - xo)]")
        
        valorVo = float(input("\tIntroduce tu valor vo: "))
        valorA = float(input("\tIntroduce tu valor a: "))
        valorXf = float(input("\tIntroduce tu valor xf: "))
        valorXo = float(input("\tIntroduce tu valor xo: "))
        
        valorVf = np.sqrt( (valorVo**2) + 2*valorA*(valorXf - valorXo) )
        print("\nvf =", valorVf)
        return "vf = " + str(valorVf)

import math
R = "R"
#==========================
#Funcion para el tema de energia potencial 
#Entrada: datos del problema y dato deseado
#salida: resultado 
#Autor: Diego Garza
#============================ 
def energia_potencial_gravitacional():
    print("Ingresa los datos dados, dato desconocido ingresalo como R")
    m=(input("Ingresa la masa de tu objeto: "))
    a=(input("Ingresa la altura de donde sera lanzado: "))
    g=(input("Ingresa la gravedad de tu entorno: "))
    e=(input("Ingresa la energia potencial dada: "))
    if (m==R):
        a=float(a)
        g=float(g)
        e=float(e)
        r=(e/(g*a))
        
        print("Tu masa es de:",r)
        return "m = " + str(r)
    elif (a==R):
        m=float(m)
        g=float(g)
        e=float(e)
        r=(e/(g*m))
        print("Tu altura es de:",r)
        return r
    elif (g==R):
        m=float(m)
        a=float(a)
        e=float(e)
        r=(e/(m*a))
        print("Tu gravedad es de:",r)
        return "g = " + str(r)
    elif (e==R):
        a=float(a)
        g=float(g)
        m=float(m)
        r=(m*a*g)
        print("Tu energia potencial es de:",r)
        return "e = " + str(r)
#==========================
#Funcion para el tema de energia cinetica
#Entrada: datos del problema y dato deseado
#salida: resultado 
#Autor: Diego Garza
#============================ 
def energia_cinetica():
    m = "-1.0"
    print("Ingresa los datos dados, dato desconocido ingresalo como R")
    while float(m) <= 0 :
        m=(input("Ingresa la masa de tu objeto: "))
    v=(input("Ingresa la velocidad del objeto: "))
    j=(input("Ingresa los joules del objeto: "))
    if(m==R):
        v=float(v)
        j=float(j)
        r=(j/(.5*(v**2)))
        print("Tu masa es de: ",r)
        return "m = " + str(r)
    elif(v==R):
        m=float(m)
        j=float(j)
        r=(math.sqrt(j/(.5*m)))
        print("Tu velocidad es de:",r)
        return "v = " + str(r)
    elif(j==R):
        m=float(m)
        v=float(v)
        r=(.5*m*(v**2))
        print("Tu energia cinetica es de:",r)
        return "j = " + str(r)
#==========================
#Funcion para el tema de potencia
#Entrada: datos del problema y dato deseado
#salida: resultado 
#Autor: Diego Garza
#============================ 
def potencia():
    print("Ingresa los datos dados, dato desconocido ingresalo como R")
    w=(input("Ingresa el trabajo de tu objeto: "))
    t=(input("Ingresa el tiempo: "))
    p=(input("Ingresa la potencia de tu objeto: "))
    if(w=="R"):
        t=float(t)
        p=float(p)
        r=p*t
        print("Tu trabajo es de:",r)
        return "w = " + str(r)
    elif(t==r):
        w=float(w)
        p=float(p)
        r=(w/p)
        print("Tu tiempo es de:",r)
        return "t = " + str(r)
    elif(p==r):
        w=float(w)
        t=float(t)
        r=(w/t)
        print("Tu potencia es de:",r)
        return "p = " + str(r)
#==========================
#Funcion para el tema de energia cinetica de un resorte
#Entrada: datos del problema y dato deseado
#salida: resultado 
#Autor: Diego Garza
#============================  
def energia_cinetica_resorte():
    print("Ingresa los datos dados, dato desconocido ingresalo como R")
    k=(input("Ingresa el coeficiente de resorte: "))
    x=(input("Ingresa el desplasamiento: "))
    j=(input("Ingresa los joules del objeto: "))
    if(k==R):
        x=float(x)
        j=float(j)
        r=(j/(.5*(x**2)))
        print("El coeficiente del resorte es de:",r)
        return "k = " + str(r)
    elif(x==R):
        k=float(k)
        j=float(j)
        r=(math.sqrt(j/(.5*k)))
        print("El desplasamiento del resorte es de:",r)
        return "x = " + str(r)
    elif(j==R):
        k=float(k)
        x=float(x)
        r=(.5*k*(x**2))
        print("Tu energia cinetica es de:",r)
        return "j = " + str(r)
#==========================
#Funcion para el tema de trabajo
#Entrada: datos del problema y dato deseado
#salida: resultado 
#Autor: Diego Garza
#============================ 
def trabajo():
    print("Ingresa los datos dados, dato desconocido ingresalo como R")
    f=(input("Ingresa la fuerza que lleva tu objeto: "))
    d=(input("Ingresa la distancia que recorre tu objeto: "))
    a=(input("Ingresa el angulo que lleva tu objeto: "))
    j=(input("Ingresa el trabajo de tu objeto: "))
    if (f==R):
        d=float(d)
        a=float(a)
        j=float(j)
        r=(j/(d*math.cos(a)))
        print("La fuerza de tu objeto es de:",r)
        return "f = " + str(r)
    elif (d==R):
        f=float(f)
        a=float(a)
        j=float(j)
        r=(j/(f*math.cos(a)))
        print("La distancia que recorrio tu objeto fue de:",r)
        return "d = " + str(r)
    elif (a==R):
        f=float(f)
        d=float(d)
        j=float(j)
        r=(math.acos((j/(f*d))))
        print("El angulo enel que tu objeto se desplaso:",r)
        return "a = " + str(r)
    elif (j==R):
        d=float(d)
        a=float(a)
        f=float(f)
        r=(f*d*math.cos(a))
        print("La fuerza de tu objeto es de:",r)
        return "j = " + str(r)
#==========================
#Funcion para el tema de velocidad relativa
#Entrada: datos del problema y dato deseado
#salida: resultado 
#Autor: Diego Garza
#============================ 
def velocidad_relativa():
    print("Ingresa los datos dados, dato desconocido ingresalo como R")
    a=(input("Ingresa la velocidad del objeto 1: "))
    b=(input("Ingresa la velocidad del objeto 2: "))
    c=(input("Ingresa la velocidad relativa: "))
    if(a==R):
        b=float(b)
        c=float(c)
        r=c-b
        print("La velocidad del objeto 1 es de:",r)
    elif(b==R):
        a=float(a)
        c=float(c)
        r=c-a
        print("La velocidad del objeto 2 es de:",r)
    elif(c==R):
        a=float(a)
        b=float(b)
        r=a+b
        print("La velocidad relativa es de:",r)
    return "v = " + str(r)
#==========================
#Funcion para el tema de la segunda ley de newton
#Entrada: datos del problema y dato deseado
#salida: resultado 
#Autor: Diego Garza
#============================ 
def segunda_ley_newton():
    print("Ingresa los datos dados, dato desconocido ingresalo como R")
    m=(input("Ingresa la masa del objeto: "))
    a=(input("Ingresa la aceleracion del objeto: "))
    f=(input("Ingresa la fuerza: "))
    if(m==R):
        a=float(a)
        f=float(f)
        r=f/a
        print("La masa del objeto es de:",r)
        return "m = " + str(r)
    elif(a==R):
        m=float(m)
        f=float(f)
        r=f/m
        print("La aceleracion:",r)
        return "a = " + str(r)
    elif(f==R):
        a=float(a)
        m=float(m)
        r=m*a
        print("La fuerza del objeto es de:",r)
        return "f = " + str(r)
#==========================
#Funcion para el tema de friccion
#Entrada: datos del problema y dato deseado
#salida: resultado 
#Autor: Diego Garza
#============================ 
def friccion():
    print("Ingresa los datos dados, dato desconocido ingresalo como R")
    n=(input("Ingresa la fuerza normal del objeto: "))
    c=(input("Ingresa el coeficiente de friccion: "))
    f=(input("Ingresa la fuerza de friccion: "))
    if(n==R):
        c=float(c)
        f=float(f)
        r=f/c
        print("La fuerza normal del objeto es de:",r)
        return "Fn = " + str(r)
    elif(c==R):
        n=float(n)
        f=float(f)
        r=f/n
        print("El coeficiente de friccion:",r)
        return "k = " + str(r)
    elif(f==R):
        n=float(n)
        c=float(c)
        r=n*c
        print("La fuerza de friccion del objeto es de:",r)
        return "Fk = " + str(r)
#==========================
#Funcion para el tema del trabajo de friccion
#Entrada: datos del problema y dato deseado
#salida: resultado 
#Autor: Diego Garza
#============================ 
def trabajo_friccion():
    print("Ingresa los datos dados, dato desconocido ingresalo como R")
    f=(input("Ingresa la friccion kinetica: "))
    d=(input("Ingresa la distancia: "))
    w=(input("Ingresa el trabajo de friccion: "))
    if(f==R):
        d=float(d)
        w=float(w)
        r=w/d
        print("El coeficiente de friccion kinetica es de:",r)
        return "k = " + str(r)
    elif(d==R):
        f=float(f)
        w=float(w)
        r=w/f
        print("La distancia recorrida fue de:",r)
        return "d = " + str(r)
    elif(w==R):
        f=float(f)
        d=float(d)
        r=f*d
        print("El trabajo de friccion es de:",r)
        return "wk = " + str(r)
#==========================
#Funcion para el tema de impulso
#Entrada: datos del problema y dato deseado
#salida: resultado 
#Autor: Diego Garza
#============================ 
def impulso():
    print("Ingresa los datos dados, dato desconocido ingresalo como R")
    f=(input("Ingresa la fuerza: "))
    t=(input("Ingresa el tiempo: "))
    i=(input("Ingresa el impulso: "))
    if(f==R):
        t=float(t)
        i=float(i)
        r=i/t
        print("La fuerza del objeto era de:",r)
        return "F = " + str(r)
    elif(t==R):
        f=float(f)
        i=float(i)
        r=i/f
        print("El tiempo de contacto era de:",r)
        return "t = " + str(r)
    elif(i==R):
        f=float(f)
        t=float(t)
        r=f*t
        print("El impulso es de:",r)
        return "I = " + str(r)
#==========================
#Funcion para el tema de momentum
#Entrada: datos del problema y dato deseado
#salida: resultado 
#Autor: Diego Garza
#============================ 
def momentum():
    print("Ingresa los datos dados, dato desconocido ingresalo como R")
    f=(input("Ingresa la masa: "))
    t=(input("Ingresa la velocidad: "))
    i=(input("Ingresa el momentum: "))
    if(f==R):
        t=float(t)
        i=float(i)
        r=i/t
        print("La masa del objeto es  de:",r)
        return "m = " + str(r)
    elif(t==R):
        f=float(f)
        i=float(i)
        r=i/f
        print("La velocidad del objeto es de:",r)
        return "v = " + str(r)
    elif(i==R):
        f=float(f)
        t=float(t)
        r=f*t
        print("El momentum es de:",r)
        return "I = " + str(r)
#==========================
#Funcion para el tema de torsion
#Entrada: datos del problema y dato deseado
#salida: resultado 
#Autor: Diego Garza
#============================ 
def torsion():
    print("Ingresa los datos dados, dato desconocido ingresalo como R")
    f=(input("Ingresa la fuerza: "))
    t=(input("Ingresa el tamaño de la palanca: "))
    i=(input("Ingresa la torsion: "))
    if(f==R):
        t=float(t)
        i=float(i)
        r=i/t
        print("La fuerza es de:",r)
        return "F = " + str(r)
    elif(t==R):
        f=float(f)
        i=float(i)
        r=i/f
        print("El tamaño de la palanca es de:",r)
        return "d = " + str(r)
    elif(i==R):
        f=float(f)
        t=float(t)
        r=f*t
        print("La torsion es de:",r)
        return "Torsion = " + str(r)
#=========================
#Funcion para el tema de fuerza centripeda
#Entrada: datos del problema y dato deseado
#salida: resultado 
#Autor: Diego Garza
#============================ 
def fuerza_centripeda():
    print("Ingresa los datos dados, dato desconocido ingresalo como R")
    f=(input("Ingresa la masa: "))
    t=(input("Ingresa la aceleracion centripeda: "))
    i=(input("Ingresa la fuerza centripeda: "))
    if(f==R):
        t=float(t)
        i=float(i)
        r=i/t
        print("La masa del objeto es  de:",r)
        return "m = " + str(r)
    elif(t==R):
        f=float(f)
        i=float(i)
        r=i/f
        print("La aceleracion centripeda es de:",r)
        return "Ac = " + str(r)
    elif(i==R):
        f=float(f)
        t=float(t)
        r=f*t
        print("La fuerza centripeda es de:",r)
        return "Fc = " + str(r)
#==========================
#Funcion para el tema de centro de masa
#Entrada: datos del problema y dato deseado
#salida: resultado 
#Autor: Diego Garza
#============================ 
def centro_de_masa():
    print("Ingresa los datos dados, dato desconocido ingresalo como R")
    print("Utiliza esta formula una vez por dimension")
    m=0
    xm=0
    nm=int(input("Cuantas masas son"))
    for i in range(0,(nm+1)):
        x=float(input("¿Cual es masa del objeto? "))
        t=float(input("¿Donde esta el objeto? "))
        m=m+x
        xm=xm+(x*t)
    r=(xm/m)
    print("el centro de masa se encuentra en",r)
    return r
#==========================
#Funcion para el tema de inersia
#Entrada: datos del problema y resultado deseado
#salida: resultado 
#Autor: Diego Garza
#============================ 
def inersia():
    print("Que tipo de objeto es")
    print("1) cilindro solido o disco eje simetrico")
    print("2) anillo sobre un eje simetrico")
    print("3) esfera solida")
    print("4) varilla sobre el centro")
    print("5) anillo sobre un diametro")
    print("6) delgada capa esferica")
    print("7) varilla sobre un extremo")
    o=int(input("Ingresa tu tipo de objeto: "))
    print("Ingresa los datos dados, dato desconocido ingresalo como R")
    m=(input("Ingresa la masa del objeto: "))
    r=(input("Ingresa el radio o longitud del objeto: "))
    i=(input("Ingresa la inersi: a"))
    if (o==1):
        if(m==R):
            r=float(r)
            i=float(i)
            r=i/(.5*(r**2))
            print("La masa del objeto es  de:",r)
            return "m = " + str(r)
        elif(r==R):
            m=float(m)
            i=float(i)
            r=(math.sqrt(i/(.5*m)))
            print("El radio es de:",r)
            return "R = " + str(r)
        elif(i==R):
            m=float(m)
            r=float(r)
            r=(.5*m*(r**2))
            print("La inersia es de:",r)
            return "Inersia = " + str(r)
    elif (o==2):
        if(m==R):
            r=float(r)
            i=float(i)
            r=i/(r**2)
            print("La masa del objeto es  de:",r)
            return "m = " + str(r)
        elif(r==R):
            m=float(m)
            i=float(i)
            r=(math.sqrt(i/(1*m)))
            print("El radio es de:",r)
            return "R = " + str(r)
        elif(i==R):
            m=float(m)
            r=float(r)
            r=(1*m*(r**2))
            print("La inersia es de:",r)
            return "Inersia = " + str(r)
    elif (o==3):
        if(m==R):
            r=float(r)
            i=float(i)
            r=i/(.4*(r**2))
            print("La masa del objeto es  de:",r)
            return "m = " + str(r)
        elif(r==R):
            m=float(m)
            i=float(i)
            r=(math.sqrt(i/(.4*m)))
            print("El radio es de:",r)
            return "R = " + str(r)
        elif(i==R):
            r=float(r)
            m=float(m)
            r=(.4*m*(r**2))
            print("La inersia es de:",r)
            return "Inersia = " + str(r)
    elif (o==4):
        if(m==R):
            r=float(r)
            i=float(i)
            r=i/((1/12)*(r**2))
            print("La masa del objeto es  de:",r)
            return "m = " + str(r)
        elif(r==R):
            m=float(m)
            i=float(i)
            r=(math.sqrt(i/((1/12)*m)))
            print("La longitud es de:",r)
            return "R = " + str(r)
        elif(i==R):
            r=float(r)
            m=float(m)
            r=((1/12)*m*(r**2))
            print("La inersia es de:",r)
            return "Inersia = " + str(r)
    elif (o==5):
        if(m==R):
            r=float(r)
            i=float(i)
            r=i/((1/2)*(r**2))
            print("La masa del objeto es  de:",r)
            return "m = " + str(r)
        elif(r==R):
            m=float(m)
            i=float(i)
            r=(math.sqrt(i/((1/2)*m)))
            print("El radio es de:",r)
            return "R = " + str(r)
        elif(i==R):
            r=float(r)
            m=float(m)
            r=((1/2)*m*(r**2))
            print("La inersia es de:",r)
            return "Inersia = " + str(r)
    elif (o==6):
        if(m==R):
            r=float(r)
            i=float(i)
            r=i/((2/3)*(r**2))
            print("La masa del objeto es  de:",r)
            return "m = " + str(r)
        elif(r==R):
            m=float(m)
            i=float(i)
            r=(math.sqrt(i/((2/3)*m)))
            print("El radio es de:",r)
            return "R = " + str(r)
        elif(i==R):
            r=float(r)
            m=float(m)
            r=((2/3)*m*(r**2))
            print("La inersia es de:",r)
            return "Inersia = " + str(r)
    elif (o==7):
        if(m==R):
            r=float(r)
            i=float(i)
            r=i/((1/3)*(r**2))
            print("La masa del objeto es  de:",r)
            return "m = " + str(r)
        elif(r==R):
            m=float(m)
            i=float(i)
            r=(math.sqrt(i/((1/3)*m)))
            print("La longitud es de:",r)
            return "R = " + str(r)
        elif(i==R):
            r=float(r)
            m=float(m)
            r=((1/3)*m*(r**2))
            print("La inersia es de:",r)
            return "Inersia = " + str(r)
#==========================
#Funcion para el tema de acceleracion tangencial
#Entrada: datos del problema y dato deseado
#salida: resultado 
#Autor: Diego Garza
#============================ 
def aceleracion_tangencial():
    print("Ingresa los datos dados, dato desconocido ingresalo como R")
    ra=(input("Ingresa el radio: "))
    ag=(input("Ingresa la aceleracion angular: "))
    i=(input("Ingresa la aceleracion tangencial: "))
    if(ra==R):
        ag=int(ag)
        i=int(i)
        r=i/ag
        print("El radio es de :",r)
        return "R = " + str(r)
    elif(ag==R):
        ra=int(ra)
        i=int(i)
        r=i/ra
        print("La aceleracion angular es de :",r)
        return "Aa = " + str(r)
    elif(i==R):
        ra=int(ra)
        ag=int(ag)
        r=ra*ag
        print("La aceleracion tangencial es de:",r)
        return "At = " + str(r)
    
    
main()

    
