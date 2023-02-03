#se puede de estas 2 formas 
mi_set= set()
mi_otro_set = {}
print(type(mi_set))


mi_otro_set ={18,"Jaris","Mican"}
print(type(mi_otro_set))

print(len(mi_otro_set))

mi_otro_set.add("Colombia")#un set no admite repetidos 

print(mi_otro_set) #un set no es una estructura ordenada
#Aca le estoy diciendo que busque algo relacionado a Jaris le estoy diciendo Buscame Algo parecido o igual a Jaris in mi_otro_set
print("Jaris" in mi_otro_set)
print("jaris" in mi_otro_set)
#las operaciones propias de un objeto accedemos con un (punto)
mi_otro_set.remove(18)
print(mi_otro_set)
mi_lista=(mi_otro_set)
#aca tenemos un set que lo convertimos  a una lista
#mi_lista=list(mi_otro_set)
print(type(mi_otro_set))

mi_otro_set_2 = {"python","java","javascript"}
#aca hace una union mi_lista con mi_otra_set_2 y ademas de eso estamos uniendo php React
my_nueva_set = mi_lista.union(mi_otro_set_2).union({"php","React"})
print(my_nueva_set)

#aca hace una diferencia entre mi_nueva_set con mi lista
print(my_nueva_set.difference(mi_otro_set))
