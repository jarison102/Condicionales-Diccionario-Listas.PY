#una array no es lo mismo que una lista una lista digamos que por debajo tiene un array pero una lista nos proporsiona operadores propias de la lista 
#en cambio el array en como una estrotuctura mas inamobible
mi_lista=list()
mi_otra_lista=[]

#se pude guardar el mismo valor 2 veces 
mi_lista= [18,24,62,52,30,15]
print(len(mi_lista))

#el -1 ejemplo es como si lo contaras del ultimo para atras por ejemplo de mican para atras jarison despues 1.77 etc
mi_otra_lista=[17, 1.77, "Jarison","Mican"]

print(mi_otra_lista[2])

#print(mi_otra_lista[4]) esto es un error porque no encuentras mas de 4 elementos en una lista (indexError)

#esta recogiendo los datos de mi_otra_lista tiene que ir en orden como tu las tienes en la lista (necesita todos los elementos)
edad,estatura,nombre,apellido=(mi_otra_lista)

print(mi_otra_lista)


#se pueden concatenar listas (se concatenan en el orden que estan )
print(mi_otra_lista + mi_lista)
#append para insertar datos en la lista
mi_otra_lista.append("Colombia")
print(mi_otra_lista)
#agrega datos segun donde quieras
mi_otra_lista.insert(-4,"tengo pc")
print(mi_otra_lista)
#remove sirve para eliminar
mi_otra_lista.remove("tengo pc")
print(mi_otra_lista)

#esta es la forma de elimar un elemento de un lugar en concreto pero retornando el mismo 
mi_pop_elemento = mi_lista.pop(2)
print(mi_pop_elemento)
print(mi_lista)
#con (Del) elimina por indice definitivamente ejemplo:
del mi_lista[2]
print (mi_lista)
#con el (CLEAR ES PARA ELIMINAR LA LISTA) EJEMPLO :
mi_lista.clear()
print(mi_lista)
#aca modificas el valor donde antes era jarison ahora pasa hacer Stived
mi_otra_lista[2]="Stived"
print(mi_otra_lista)

#hemmos creado una nueva referencia donde crea una nueva referencia a copiado el objeto en ese punto y desde ese punto mi lista es igual a mi_nueva_lista pero que lo que hagamos desde ese momomento con mi_lista no importa
mi_nueva_lista=mi_lista.copy()
print(mi_lista)
print(mi_nueva_lista)

#el sort le indicamos criterios para ordenar hace una ordenacion de mayor a menor
mi_nueva_lista.sort()
print(mi_nueva_lista[1:3])