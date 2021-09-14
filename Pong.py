
#turtle is a pre-installed Python library that enables users to create
# pictures and shapes by providing them with a virtual canvas.

import turtle
import winsound

window = turtle.Screen() # Creamos una ventana
window.title("Pong") #Le damos un título a la ventana
window.bgcolor("black") #Cambiamos el fondo a color negro
window.setup(width=800, height=600) #Definimos el tamaño de la ventana
window.tracer(0) #No deja que la ventana se actualice. Acelerar el juego

#Ahora vamos a crear las barras de los extremos y la bola

#Puntos
puntosA = 0
puntosB = 0

#Barra A
barraA = turtle.Turtle() #Definimos el objeto
barraA.speed(0) #Esto es necesario por usar turtle, acelera el ritmo, pero no es la velocidad a la que se mueve la barra
barraA.shape("square") #Por defecto 20x20 pixeles
barraA.shapesize(stretch_wid=5, stretch_len=1) #Multiplica por 5 la anchura y por 1 la altura
barraA.color("white")
barraA.penup() #Por defecto turtle dibuja una linea con el movimiento, esto es para que no lo haga
barraA.goto(-350, 0) #El centro es el 0,0. -350 indica que empieza a la izquierda y en el centro

#Barra B
barraB = turtle.Turtle()
barraB.speed(0)
barraB.shape("square")
barraB.shapesize(stretch_wid=5, stretch_len=1)
barraB.color("white")
barraB.penup()
barraB.goto(350, 0)

#Bola
bola = turtle.Turtle()
bola.speed(0)
bola.shape("square")
bola.color("white")
bola.penup()
bola.goto(0, 0)
bola.dx = 0.1
bola.dy= 0.1 #Esto define el incremento en pixeles para la bola en las 2 direcciones

#Texto
escrito = turtle.Turtle()
escrito.speed(0)
escrito.color("white")
escrito.penup()
escrito.hideturtle() #Esconder el objeto, sino sale una forma además del texto
escrito.goto (0, 260)
escrito.write("Jugador A: 0 Jugador B: 0", align = "center", font = ("Courier", 15, "normal"))


#Ahora empezamos con los movimientos. Definimos funciones

def barraA_up():
    y = barraA.ycor() #Se mueve verticalmente, necesitamos la coordenada y
    y += 20 #Añade 20 pixeles
    barraA.sety(y) #La nueva posición se la asignamos a y

def barraA_down():
    y = barraA.ycor()
    y -= 20
    barraA.sety(y)

def barraB_up():
    y = barraB.ycor()
    y += 20
    barraB.sety(y)

def barraB_down():
    y = barraB.ycor()
    y -= 20
    barraB.sety(y)

#Incluimos el teclado (es necesario para mover las barras)
window.listen() #Esto es propio de turtle, indica que hay que tener en cuenta el input del teclado
window.onkeypress(barraA_up, "w") #Cuando se pulsa w, llama a la funcion barraA_up
window.onkeypress(barraA_down, "s") #Cuando se pulsa s, llama a la funcion barraA_down
window.onkeypress(barraB_up, "Up") #Flecha hacia arriba
window.onkeypress(barraB_down, "Down") #Flecha hacia abajo


#Main game loop

while True:
    window.update() #Cada vez que el bucle se ejecuta se actualiza

    #Movimiento de la bola (se hace aquí porque es lo principal del juego)
    bola.setx(bola.xcor() + bola.dx) #Empieza en 0,0 y añade
    bola.sety(bola.ycor() + bola.dy)


    #Definir los bordes
    if bola.ycor() > 290: #La mitad del ancho de la bola la quitamos del pixel superior (mitad de 600)
        bola.sety(290)
        bola.dy *= -1 #invierte la direccion


    if bola.ycor() < -290:
        bola.sety(-290)
        bola.dy *= -1


    if bola.xcor() > 390:
        bola.goto(0, 0) #En los laterales no queremos que rebote porque se pierde cuando llega
        bola.dx *= -1
        bola.dx = 0.1
        bola.dy = 0.1
        puntosA +=1
        escrito.clear() #Así no se superponen los números
        escrito.write("Jugador A: {} Jugador B: {}".format(puntosA, puntosB), align="center",
                      font=("Courier", 15, "normal"))

    if bola.xcor() < -390:
        bola.goto(0, 0)
        bola.dx *= -1
        bola.dx = 0.1
        bola.dy = 0.1
        puntosB +=1
        escrito.clear()
        escrito.write("Jugador A: {} Jugador B: {}".format(puntosA, puntosB), align="center",
                      font=("Courier", 15, "normal"))

 # Definir choque entre bola y barras
    if (bola.xcor() > 340 and bola.xcor() < 350) and (
            bola.ycor() < barraB.ycor() + 40 and bola.ycor() > barraB.ycor() - 40):
        bola.setx(340)
        bola.dx += 0.05
        bola.dy += 0.05
        bola.dx *= -1
        winsound.PlaySound("golpe.wav", winsound.SND_ASYNC)

    # El centro de la barra esta en 350 y la mitad del ancho de la bola es 10. La primera parte me define el eje x
    # Quiero además que invierta direccion si está a la misma distancia en eje X, pero también que la barra esté tocando
    # a la bola (que esté entre los límites de altura de la barra)

    if (bola.xcor() < -340 and bola.xcor() > -350) and (
            bola.ycor() < barraA.ycor() + 40 and bola.ycor() > barraA.ycor() - 40):
        bola.setx(-340)
        bola.dx += -0.05
        bola.dy += -0.05
        bola.dx *= -1
        winsound.PlaySound("golpe.wav", winsound.SND_ASYNC)

    if puntosA-puntosB >= 5 or puntosB-puntosA >= 5:
        gameOver = turtle.Turtle()
        gameOver.speed(0)
        gameOver.color("white")
        gameOver.penup()
        gameOver.hideturtle()  # Esconder el objeto, sino sale una forma además del texto
        gameOver.goto(0, 0)
        gameOver.write("PARTIDA TERMINADA", align = "center", font = ("Courier", 25, "normal"))
        bola.hideturtle()