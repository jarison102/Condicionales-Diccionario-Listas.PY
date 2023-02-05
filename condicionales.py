#es la manera de establecer flujos de ejecucion de nuestro codigo 

#si se cumple una condicion yo ejecuto lo que esta dentro e la condicional
mi_condicion = True

if mi_condicion:
    print ("Se ejecuta la condicion del if ")

print("la ejecucion continua")

#############################################################
mi_condicion = 5 * 2

#si cumple la condicion que le digas sigue si no no aca le estamos diciendo si cumple 5 * 2 que es 10 siga si no cumple para
if mi_condicion == 10:
    print ("Se ejecuta la condicion del if 2 ")

print("la ejecucion continua")


#aca le estoy diciendo si es mayor o igual sigue si no no 
if mi_condicion >= 10 :
    print ("Se ejecuta la condicion del if 3 ")

print("la ejecucion continua")


mi_condicion_2 = 50 + 50 
#si esta condicion da true imprime es mayor que 100
if mi_condicion_2 >= 100 :
    print ("es mayor que 100 ")
else:#si no se cumple imprime es menor o igual que 100

    print ("es menor o igual que 100")

print("la ejecucion continua")

#aca le decimos a la condicion que tiene que hacer tipo ejemplo la madre tiene que tener tantos años para seguir 
#le estamos diciendo si cumple con 45 años imprimimos tienen 45 años si no imprimimos no cumple con los años requeridos
mi_madre = 20

if mi_madre >= 45:
    print("tiene 45 de años")
else:
    print("no cumple con los años requeridos")

#########################################################################
    mi_tio =  27

if mi_tio >= 28:
    print("si tiene los años requeridos  tio ")
else:
    print("no tiene los años requeridos tio ")
###########################################################

    mi_madre_trabajo = 25

    if mi_madre_trabajo > 10 and mi_madre_trabajo < 20:
        print("si trabajo mas de 10 años y menor que 20")

        #para el elsif se necesita una condicion
    elif mi_madre_trabajo >= 25:
        print("trabajo mas de 25 años o igual")
    else:
        print("no trabajo menos que 10 años o distinto a 20")

##########################################################################
    #asi se hacen con cadenas de texto aca comprueba que no esta vacia 
    mi_cadena = "si"

    if mi_cadena:
        print("no esta vacia")



#############################################
#aca estamos negando y estamos diciendo que mi cadena de texto es vacia 
    mi_cadena_negada = ""

    if not mi_cadena_negada:
        print("mi cadena de texto es vacia")
#########################################################################
    ##edad=int (input("cuantos años tienes?"))
    ##if edad >18:
      ##  print("usted ya es mayor")
    ##else:
        ##print("le falta años")
######################################################
    nombre =(input("Cuales tu nombre:")) 
    if nombre== "Jarison":
        print("usted si es Jarison Bienvenido")
    elif nombre == "pedro":
         print("Usted es el administrador")
    else:
        print("Usted no esta en lista")


#################################################

    bitacora =(input("has echo las mitacoras:?")) 
    if bitacora== "no":
        print("usted no a echo las bitacoras michi")
    elif nombre == "si":
         print("Pongase jusiosa michi")
    else:
        print("Michiii has esooooo")
















