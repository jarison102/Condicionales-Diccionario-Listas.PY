mi_diccionario = dict()
mi_otro_diccionario = {}

print(type(mi_diccionario))

#aqui una relacion clave valor nombre clave y el valor es el nombre 
mi_otro_diccionario = {"nombre":"Jarison",
"Apellido":"Mican",
"Años":18, 
"Ciudad":"Bogota",
"Nombre Prima": "Paula",
"Vive":"Con el primo",
"lenguajes":{"Python","Java","PHP"},
"Estaruta":1.77
}
print (len(mi_otro_diccionario))

#aca accedemos a un valor en especifico esta vez es lengajes
print (mi_otro_diccionario["lenguajes"])

#aca es para agregar cosas al diccionario 
mi_otro_diccionario["Calle"] = "Villa Diana"
print (len(mi_otro_diccionario))

#esta es la forma de eliminar un solo elemento de un diccionario 
del mi_otro_diccionario ["Calle"] 
print (len(mi_otro_diccionario))


mi_otro_diccionario_2 = {"nombre":"Jarison",
"Apellido":"Mican",
"Años":18, 
"Ciudad":"Bogota",
"Nombre Prima": "Paula",
"Vive":"Con el primo",
"lenguajes":{"Python","Java","PHP"},
"Estatura":1.77
}


print (mi_otro_diccionario_2)

#aca busca es por el clave
print("Apellido" in mi_otro_diccionario_2)
#items retorna todos los items que tenemos en el diccionario 
#keys retorna todos las claves que tengas en el diccionario 
#en values retorna son los valores que tenga el diccionario 
print(mi_otro_diccionario_2.items())
print(mi_otro_diccionario_2.keys())
#el value es un valor que se va a duplicar enj todas las claves 
print(mi_otro_diccionario_2.values())

mi_nuevo_diccionario = dict.fromkeys((mi_otro_diccionario_2))

print(mi_nuevo_diccionario)


mi_nuevo_diccionario = dict.fromkeys(mi_otro_diccionario_2,("Mican","Bogota"))

print (mi_nuevo_diccionario)

#si se convierte a lista solo trae las claves 
print(list(mi_otro_diccionario_2))