import turtle

canvas=turtle.Screen()
canvas.bgcolor("black")

turtle.speed(0)

turtle= turtle.Turtle()
turtle.penup()
turtle.color("red")
turtle.goto(0, 200)
turtle.pendown()

a=0
b=0
b_param=2
a_param=4
mode=0
while True:

    if mode ==0:
    
        turtle.forward(a)
        turtle.right(b)

        b+=b_param
        a+=a_param
        
        if b> 240:
            mode=1
            turtle.color("black")
            
    if mode==1:

        b-=b_param
        a-=a_param
        
        turtle.left(b)
        turtle.backward(a)
        
        
        
        if b== 0:
            mode=0
            turtle.color("red")
        
    
