import turtle

canvas=turtle.Screen()
canvas.bgcolor("black")

turtle.speed(0)

turtle= turtle.Turtle()
turtle.penup()
turtle.color("red")

class A:
    x = []
    

class System:
    def __init__(self,pos):
        self.planets=[]
        self.faction =1
        self.cordinates =[pos]

def hola():
    print("hola")


def mk_fxn(thing):
     def fxn(x,y):       
        # some motion 
        turtle.right(90) 
        turtle.forward(100)



    
solar =System((4,2))
solar.faction=10
solar.planets.extend((1,2))

andromeda= System((9,1))
andromeda.faction=8


print(andromeda.faction, solar.faction, andromeda.planets, solar.planets)

Galaxy=[]


for size in range(5, 200, 2):
    carballo=System(turtle.pos())
    carbello.click(mk_fxn(turtle))
    Galaxy.append(carballo)
    turtle.stamp()
    turtle.forward(size)
    turtle.right(50)

print(Galaxy[6].cordinates)

turtle.onclick(fxn)
