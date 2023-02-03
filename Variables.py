#variables 
primer_nombre=("mi nombre es Jarison")
Mi_edad=(" " + "Tengo 18 Años")
Vivo_En=(" " + "Vivo en Colombia")
Estoy_Estudiando=(" "+ "Estoy estudiando Programacion")
lenguaje=(" " + "Me Gusta Mucho Python Tengo ")
experiencia=input(("escribe tu experiencia que tienes programando"))
continuidad_input=(" " +"años de experiencia")
trabajo_en=(" " + "Mi sona de trabajo en " + '2' + " " + "Monitores" + " " + "Tengo ")
#se agraga tipo entero asi 
celular= '1' + " " + "Celular"
moto=("Me quiero Comprar una moto de CC" + " "+ '200')
#forzamos el tipo y que ahora quede 250
moto=(" " + '250')

#estoy concatenando cadenas de cada variable
print(primer_nombre + Mi_edad + Vivo_En + Estoy_Estudiando + lenguaje + experiencia + continuidad_input + trabajo_en + celular + moto)

#funciones pre cargadas del sistema (len) cuenta cuantas palabras hay en la cadena de texto 
print(len(primer_nombre))