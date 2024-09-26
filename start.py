import turtle

ventana = turtle.Screen()
ventana.bgcolor("black")

tortuga = turtle.Turtle()
tortuga.speed(2)
tortuga.color("yellow")

#Dibujando una estrella
for _ in range(5):
    tortuga.forward(250)
    tortuga.right(144)  

ventana.exitonclick()