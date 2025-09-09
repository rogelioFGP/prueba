# piedra_papel_tijera 2.py
# Juego simple contra la computadora: Segunda version, existe la victoria temprana o al mejor de 5 rondas
import random
opciones = ["piedra", "papel", "tijera"]
print("¡Bienvenido! Vamos a jugar a Piedra, Papel o Tijera.")
print("Escribí tu jugada (piedra/papel/tijera).")
ronda = 1
puntos_usuario = 0
puntos_pc = 0
rondas_totales = 5
while ronda <= rondas_totales:
 print(f"\nRonda {ronda}")
 jugada_usuario = input("Tu jugada: ").strip().lower()
 if jugada_usuario not in opciones:
  print("Entrada no válida. Debe ser piedra, papel o tijera.")
  continue # no cuenta la ronda si la entrada es inválida
 jugada_pc = random.choice(opciones)
 print(f"La computadora eligió: {jugada_pc}")
 if jugada_usuario == jugada_pc:
  print("Empate.")
  
 elif (
   (jugada_usuario == "piedra" and jugada_pc == "tijera") or
   (jugada_usuario == "papel" and jugada_pc == "piedra") or
   (jugada_usuario == "tijera" and jugada_pc == "papel")
 ):
   print("¡Ganaste la ronda!")
   puntos_usuario += 1
   
 else:
  print("Perdiste la ronda.")
  puntos_pc += 1
#Caso en el que un jugador gane antes de que se cumplan las 5 rondas totales

 puntos_necesarios_para_ganar = (rondas_totales // 2) + 1  # Por ejemplo, para 5 rondas necesitas 3 puntos para asegurar la victoria

# Si el usuario ya ganó 3 rondas, gana de inmediato
 if puntos_usuario >= puntos_necesarios_para_ganar:
      print("¡Ganaste el juego antes de tiempo! 🎉")
      break
# Si la PC ya ganó 3 rondas, gana de inmediato
 elif puntos_pc >= puntos_necesarios_para_ganar:
      print("La computadora ganó el juego antes de tiempo.")
      break

 ronda += 1
print("\n=== Resultado final ===")
print(f"Tus puntos: {puntos_usuario} | Puntos de la PC: {puntos_pc}")

if puntos_usuario > puntos_pc:
 print("¡Ganaste el juego! 🎉")
elif puntos_usuario < puntos_pc:
 print("La computadora ganó el juego.")
else:
    print("Empate total.")