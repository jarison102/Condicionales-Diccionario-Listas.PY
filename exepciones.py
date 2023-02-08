numberOne = 5
numberTwo = 1
numberOne = "1"
#try except
try:
    print(numberOne + numberTwo)
    print("no se ha producido ningun error")
except:
    #se ejecuta si se produce una exepcion
    print("Se ha producido un error")

#try except  else

try:
    print(numberOne + numberTwo)
    print("no se ha producido ningun error")
except:
    print("Se ha producido un error")
else:
    #se ejecuta si no se produce ninguna except (opcional)
    print("la ejecucion continua correctamente")
finally:#el finally siempre se ejecuta (opcional)
    print("la ejecucion continua ")

#excepciones por tipo
try:
    print(numberOne + numberTwo)
    print("no se ha producido ningun error")
except TypeError:
    print("Se producjo un error")