# Juego de Piedra, Papel y Tijera
import random

def eleccionANombre(eleccion):
  if (eleccion == 1):
    return 'PIEDRA'
  elif (eleccion == 2):
    return 'PAPEL'
  elif (eleccion == 3):
    return 'TIJERA'
  else:
    print("Por favor ingresa una opción válida")
    startGame()

def elecciones():
  user1 = int(input("Jugador 1: "))
  user2 = random.randint(1,3)
  
  return user1, user2

def combate(j, c):
  jugador = eleccionANombre(j)
  print(f"User:  {jugador}")
  compu = eleccionANombre(c)
  print(f"Compu: {compu}")
  
  if (j == c):
    return 0
  elif (j == 1 and c == 3 or j == 2 and c == 1 or j == 3 and c == 2):
    return 1
  else:
    return 2

def vidas():
  vidas = 3
  print(f"Tinenes {vidas} vidas\n")
  while vidas > 0:
    user1, user2 = elecciones()
    resultadoCombate = combate(user1, user2)
    if resultadoCombate == 2:
      vidas = vidas - 1
      print(f"Te quedan: {vidas} vidas\n")
    elif resultadoCombate == 0:
      pass
    elif resultadoCombate == 1:
      print("¡GANASTE!")
      break  
    else:
      print("PERDISTE TE QUEDASTE SIN VIDAS")
      break  
    
def startGame():
  vidas()

print("***** BIENVENIDO AL JUEGO *****")
print("1 - PIEDRA\n2 - PAPEL\n3 - TIJERA\n")
startGame()