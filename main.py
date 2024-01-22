# juego piedra papel y tijera
import random

rounds = 1
playerWins = 0
computerWins = 0
options = ('piedra', 'papel', 'tijera')

while True:
  print('*' * 10)
  print('Ronda', rounds)
  print('*' * 10)
  print('\n')

  player = input("piedra, papel o tijera: ")
  bot = "piedra"
  optionsDir = {1: "piedra", 2: "papel", 3: "tijera"}
  bot = optionsDir.get(random.randint(1, 3))

  if(options.count(player.lower()) == 0):
    print("Esa opcion no es valida")
    rounds += 1
    continue
  
  print('Bot selecciono: ', bot)
  if player.lower() == bot:
    print("Empate, ambos eligieron la misma opcion")
  elif player == "tijera":
    if bot == "piedra":
      print("Perdiste gano Computadora, piedra gana a tijera")
      computerWins += 1
    else:
      print("Ganaste, tijera gana a papel")
      playerWins += 1
  elif player == "papel":
    if bot == "piedra":
      print("Ganaste, papel gana piedra")
      playerWins += 1
    else:
      print("Perdiste gano Computadora, tijera gana a papel")
      computerWins += 1
  elif player == "piedra":
    if bot == "papel":
      print("Perdiste gano Computadora, papel gana a piedra")
      computerWins += 1
    else:
      print("Ganaste, piedra gana a tijera")
      playerWins += 1

  rounds += 1
  print('\n')
  print('*' * 10)
  print('Puntaje')
  print(f'Tu: {playerWins} - Computadora: {computerWins}')
  print('*' * 10)
  print('\n')

  if(playerWins == 3):
    print('Ganaste el juego')
    break
    
  if(computerWins == 3):
    print('Perdiste el juego')
    break