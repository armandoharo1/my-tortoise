import turtle

ventana = turtle.Screen()
ventana.bgcolor("green")

tortuga = turtle.Turtle()
tortuga.speed(1)

#Dibujando un cuadrado con el movimiento de la tortuga
for _ in range(4):
    tortuga.forward(100)
    tortuga.right(90)  

ventana.exitonclick()