import turtle
import random

# Configuración de la ventana
ventana = turtle.Screen()
ventana.title("Juego de Adivinanza")
ventana.bgcolor("lightblue")

# Creación de la tortuga para el texto
texto_tortuga = turtle.Turtle()
texto_tortuga.speed(0)
texto_tortuga.color("black")
texto_tortuga.penup()
texto_tortuga.hideturtle()
texto_tortuga.goto(0, 250)
texto_tortuga.write("¡Adivina el número entre 1 y 100!", align="center", font=("Arial", 18, "bold"))

# Generación del número secreto
numero_secreto = random.randint(1, 100)

# Bucle principal del juego
while True:
    conjetura = int(turtle.textinput("Adivina el número", "Ingresa tu conjetura:"))

    if conjetura == numero_secreto:
        texto_tortuga.clear()
        texto_tortuga.goto(0, 250)
        texto_tortuga.write(f"¡Felicidades! Adivinaste el número {numero_secreto}.", align="center", font=("Arial", 18, "bold"))
        break
    elif conjetura < numero_secreto:
        texto_tortuga.clear()
        texto_tortuga.goto(0, 250)
        texto_tortuga.write("El número es más grande. ¡Sigue intentando!", align="center", font=("Arial", 18, "bold"))
    else:
        texto_tortuga.clear()
        texto_tortuga.goto(0, 250)
        texto_tortuga.write("El número es más pequeño. ¡Sigue intentando!", align="center", font=("Arial", 18, "bold"))

ventana.mainloop()

