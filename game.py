from http.client import SWITCHING_PROTOCOLS
from random import choice, randrange
from datetime import datetime

# Operadores posibles
operators = ["+", "-","*","/"]
# Cantidad de cuentas a resolver
times = 5
# Contador inicial de tiempo.
# Esto toma la fecha y hora actual.
init_time = datetime.now()
correctas=0
incorrectas=0
result_2=0
print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")
for i in range(0, times):
    #Se eligen números y operador al azar
  number_1 = randrange(10)
  number_2 = randrange(10)
  operator = choice(operators)
    # Se imprime la cuenta.
  print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")
    # Le pedimos al usuario el resultado
  result = float(input("resultado: "))
  if( operator == "+"):
      result_2= number_1 + number_2
      print( result ,  " y" , result_2)
  elif( operator =="-"):
     result_2= number_1 + number_2
  elif(operator == " *"):
     result_2= number_1 * number_2
  elif(operator == "/"):
     result_2 = number_1 / number_2
  if( result == result_2 ):
      correctas +=1
      print(" respuesta correcta")
  else:
     print( "respuesta incorrecta")
     incorrectas +=1
# Al terminar toda la cantidad de cuentas por resolver.
# Se vuelve a tomar la fecha y la hora.
  end_time = datetime.now()
# Restando las fechas obtenemos el tiempo transcurrido.
  total_time = end_time - init_time
# Mostramos ese tiempo en segundos.
print(f"\n Tardaste {total_time.seconds} segundos.")
print( "respondio corectamentes "  , correctas  , " operaciones" )
print( "respondio incorectas "  , incorrectas  , " operaciones" )