#para realizar una tarea muy concreta no sirve para todo lo que este dentro de esa clase tiene que reponder a cierta logica si la clase es de persona tiene que tener logica de persona
#identificar nuestro codigo dentro de un ambito de actuación
class Persona:
    def __init__(self,Nombre,Apellido,Pais):#el init se define el constructor 
        #pass #el pass se deja si nosotros estamos creando un bloque de codigo que en realidad no tenemos nada
        self.Nombre = Nombre #los valores que le llegas a la clase persona ahora si los estoy almacenando 
        self.Apellido = Apellido#self se refiere a la instacia de la clase en este caso persona
        self.Pais = Pais
my_persona = Persona(Nombre="Jarison",Apellido="Mican",Pais="Colombia")
#print(my_persona.Nombre + my_persona.Apellido)#una forma es esta
print(f"{my_persona.Nombre} {my_persona.Apellido} {my_persona.Pais}")

#####################################################################################################
#otra forma

class Persona:
    def __init__(self,nombre,apellido):#el init es el constructor
        self.nombrecompleto= f"{nombre} {apellido}"#con cama y tv me estoy creando una propiedad almacenada que es habitacion
    def caminar(self): 
        print(f"{self.nombrecompleto}Esta Caminando")#si yo le paso self voy a poder acceder a todo lo que este en el 
my_Persona = Persona("Jarison","Mican"+ " " )
print(my_Persona.nombrecompleto)#yo pasandole una cama un tv lo que acabo creando es una clase my_casa que lo que tiene es una propiedad almacenada que se llama habitacion  
my_Persona.caminar()



