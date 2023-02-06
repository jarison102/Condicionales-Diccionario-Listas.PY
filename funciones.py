fiesta = 10
fiesta_menores= 10
def  mi_funcion():
    if fiesta  >= 20:
        print("si dentro bienvenido")
    elif fiesta_menores == 10:
        print("dentras solo fiesta menores")
    else:
        print("no puedes entrar")

mi_funcion()

#una funcion puede devolver codigo y recibir codigo

def suma_de_numero(primer_numero,segundo_numero):#aca indicas el parametro
    print(primer_numero * segundo_numero)#aca indicas que quieres sumar dividir etc
suma_de_numero(5 , 5)#y aca dices que quieres sumar multiplicar etc 

def mis_nombre (primer_nombre,segundo_nombre): 
    print(primer_nombre,segundo_nombre)
mis_nombre("Jarison","Stived")

def mis_apellido(primer_apellido,segundo_apellido):
    return(primer_apellido + segundo_apellido)#el return los esta llamando
guardo_los_datos = mis_apellido ("Mican","Cespedes")#esta funcion es capaz de asignarle el resultado a una variable
print(guardo_los_datos)#y aca imprime los datos que tenemos guardados en la variable 

def edades (primer_edad,segunda_edad,tercera_edad):
 (f"{primer_edad}{segunda_edad}{tercera_edad}")
print(14, 18,45)

def mis_nombre (primer_nombre,segundo_nombre): 
    print(f"{primer_nombre},{segundo_nombre}")
mis_nombre(segundo_nombre="Jarison",primer_nombre="Stived")#aca estamos reordenando el orden que tengan los parametros

################################################################
 #aca le estoy diciendo vale si tu no tienes alias yo te pongo uno que va hacer Sin alias
def mis_nombre (primer_nombre, segundo_nombre, alias="Sin alias"): #un valor por defecto significa que puedo ejecutarlo con o sin parametro
    print(f"{primer_nombre},{segundo_nombre},{alias}")
mis_nombre(segundo_nombre="Jarison",primer_nombre="Stived")
#######################
def mis_nombre (primer_nombre, segundo_nombre, alias="Sin alias"): #un valor por defecto significa que puedo ejecutarlo con o sin parametro
    print(f"{primer_nombre},{segundo_nombre},{alias}")
mis_nombre(segundo_nombre="Jarison",primer_nombre="Stived",alias="Stivur")
####################################################
def String (*text):
    print(text)
String ("Jarison")
