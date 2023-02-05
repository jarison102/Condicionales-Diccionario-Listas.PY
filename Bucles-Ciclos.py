#que es es un mecanismo para iterar 
#que es itear es intentar repetir algo 


#mientras sea verdadero haz algo asi funcina un while
#while
my_condicion = 0
#cero es menor que 10 imprime 0 se vuelve a ejecutar el bucle porque la funcion sigue verdadera
while my_condicion <= 20: #la condicion es menor que 20 
    print(my_condicion)
    if my_condicion == 15:
        print("se detiene la condicion")
        print ("mi condicion es 15")
        break #es para parar el bucle
         
    my_condicion += 1 # y lo sigue haciendo 2 4  sumando de 2 en 2 hasta el 20 depende de cuanto pongas en el valor
    #cuado pasa 20 se va para el else
else:
    print("mi condicion es mayor o igual a 20")

print("la ejecucion continua")
#########################################################
#For
#nos sirve para iterar un listado de elementos
mi_lista= [18,24,62,52,30,15]
for elemento in  mi_lista:
    print(elemento)

    mi_set ={18,"Jaris","Mican"}
    mi_diccionario = {"nombre":"Jarison",
"Apellido":"Mican",
"Años":18, 
"Ciudad":"Bogota",
"Nombre Prima": "Paula",
"Vive":"Con el primo",
"lenguajes":{"Python","Java","PHP"},
"Estatura":1.77
}
for elemento in  mi_diccionario.values():#el values es capas de volverte una estructura en formato lista
    print(elemento)
    if elemento == "Años":
     break #cuando rompemos el bucle ya no se muestra el else

else:
    print("el bucle for para mi diccionario a finalizado")
    
for elemento in  mi_set:
     print(elemento)

##############################################################

for elemento in  mi_diccionario.values():#el values es capas de volverte una estructura en formato lista
    print(elemento)
    if elemento == "Años":
     continue 

else:
    print("el bucle for para mi diccionario a finalizado")
    
for elemento in  mi_set:
     print(elemento)
