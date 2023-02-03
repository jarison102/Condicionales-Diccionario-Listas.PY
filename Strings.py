#la \n es para dar un saldo de linea en consola
salto_de_linea=("hola con\nsalto de linea")
## la \t es para dar una tabulacion en la consola
linea_tabulada=("\t texto con tabulacion XD")
#se pueden crear una cadena de variables con las respectivas cosas que almacenan 
variable_1,variable_2=("hola 1" + " "," " + "hola 2")
print (variable_1 + variable_2)
print(salto_de_linea + linea_tabulada)    


mi_nombre =("jarison")
mi_edad = 15
mi_pais=("colombia ")
#el {} es porque estamos esperando lo que almacena la variable en este caso mi_nombre es jarison,mi_edad es 15 y mi_pais es colombia
print("mi nombre es {} mi edad es {} y mi pais es {}".format(mi_nombre,mi_edad,mi_pais))




#el %d es para que el parametro espere un valor numerico aca estamos haciendo que los valores %s esperen las variables mi nombre mi edad y mi pais
print("mi nombre es %s mi edad es %d y mi pais es  %s "%(mi_nombre,mi_edad,mi_pais))


##inferencia de datos
#la f  sirve para formatear o para  que vaya inferiendo las variables 
print(f"mi nombre es {mi_nombre} mi edad es {mi_edad} y mi pais es  {mi_pais} ")

#desempaquetado de caracteres

idioma=("español")
a,b,c,d,e,f,g=idioma

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)

#traer los caracteres del string el 0 es donde comienza y el 7 donde va a terminar
traer_letras_idioma=idioma[0:7]
print(traer_letras_idioma)

#capitalize Vuelve la primera en mayus
print(idioma.capitalize())
#para que se vuelva todo mayus
print(idioma.upper())
#para que vuelva todo minuscula
print(idioma.lower())
#el count sirve para encontrar si hay e o lo que tu pones de parametro
print(idioma.count("e"))
#aca el isnumeric es para que diga si la variable idioma es un tipo numerico da false ya que no es un tipo numerico 
print(idioma.isnumeric())
#el isupper es para comprobar si esta en mayuscula (aca estoy haciendo que idioma se mayus para que isupper me compruve si esta mayus sale true ya que si la esta encontrando mayus ya que la comvertimos con el upper)
print(idioma.upper().isupper())
#el startswith es para comprovar si idioma empieza por "es" da true ya que si es verdadero porque es español
print(idioma.startswith("es"))


