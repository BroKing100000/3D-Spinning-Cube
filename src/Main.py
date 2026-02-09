import turtle
import math

# [ Variables ] #

x1 = 0
y1 = 0
z1 = 0
x2 = 0
y2 = 0
z2 = 0

output1 = 0
output2 = 0

cameraX = 0
cameraY = 0
cameraZ = -180

angle = 0.001

shape = "Cube"

cameraXRot = 0
cameraYRot = 0

fieldOfView = 300

cubeColor = [1, 1, 1]
backgroundColor = [0, 0, 0]

screen = turtle.Screen()

# [ Functions ] #

# Sets variables: x1, y1, z1.
def SetVariables1(x, y, z):

    global x1, y1, z1

    x1 = x
    y1 = y
    z1 = z

# Sets variables: x2, y2, z2.
def SetVariables2(x, y, z):

    global x2, y2, z2

    x2 = x
    y2 = y
    z2 = z

# Sets variables that define the X and Y axes of rotation.
def RotatePoints(x, y, rot):
    
    global output1, output2

    output1 = ((math.cos(rot) * x) - (math.sin(rot) * y))
    output2 = ((math.sin(rot) * x) + (math.cos(rot) * y))

# Projection of 3D space on 2D screen.
def Projection(x, y, z):

    turtle.goto([(fieldOfView * x) / z, (fieldOfView * y) / z])

# Draws a 3D edge based on 2 verticles with right rotation and position:
# (First) Start verticle: x_1, y_1, z_1
# (Second) Last vericle: x_2, y_2, z_2
def DrawLine(x_1, y_1, z_1, x_2, y_2, z_2):

    # [ Calls ] #

    SetVariables1(x_1, y_1, z_1)
    RotatePoints(z1, x1, cameraXRot)
    SetVariables1(output2, y1, output1)
    RotatePoints(y1, z1, cameraYRot)
    SetVariables1(x1, output1, output2)
    SetVariables2(x_2, y_2, z_2)
    RotatePoints(z2, x2, cameraXRot)
    SetVariables2(output2, y2, output1)
    RotatePoints(y2, z2, cameraYRot)
    SetVariables2(x2, output1, output2)
    Projection((x1 - cameraX), (y1 - cameraY), (z1 - cameraZ))

    turtle.pendown()

    # [ Calls ] #

    Projection((x2 - cameraX), (y2 - cameraY), (z2 - cameraZ))

    turtle.penup()

# Draws a shape based on several edges data.
def Shape():

    if shape == "BroKing":

        # [ Calls ] #

        DrawLine(0, 0, 0, 25, 0, 0)
        DrawLine(0, -50, 0, 0, 50, 0)
        DrawLine(0, 25, 0, 50, 25, 0)
        DrawLine(25, 0, 0, 25, -25, 0)
        DrawLine(50, -50, 0, 50, 50, 0)
        DrawLine(50, 50, 0, -50, 50, 0)
        DrawLine(25, -25, 0, 50, -25, 0)
        DrawLine(50, -50, 0, -50, -50, 0)
        DrawLine(-50, -50, 0, -50, 50, 0)
        DrawLine(-22.5, -25, 0, 0, -25, 0)
        DrawLine(-50, 25, 0, -22.5, 25, 0)
        DrawLine(-22.5, -50, 0, -22.5, 25, 0)

    else:

        # [ Calls ] #

        DrawLine(50, -50, 50, 50, 50, 50)
        DrawLine(50, 50, -50, 50, 50, 50)
        DrawLine(-50, 50, 50, 50, 50, 50)
        DrawLine(50, -50, -50, 50, 50, -50)
        DrawLine(50, -50, -50, 50, -50, 50)
        DrawLine(-50, 50, -50, -50, 50, 50)
        DrawLine(-50, 50, -50, 50, 50, -50)
        DrawLine(-50, -50, 50, 50, -50, 50)
        DrawLine(-50, -50, 50, -50, 50, 50)
        DrawLine(-50, -50, -50, 50, -50, -50)
        DrawLine(-50, -50, -50, -50, 50, -50)
        DrawLine(-50, -50, -50, -50, -50, 50)

screen.tracer(0)
turtle.hideturtle()
turtle.pencolor(cubeColor)
turtle.bgcolor(backgroundColor)
turtle.title("3D Spinning Cube")
screen.getcanvas().config(highlightthickness = 0, borderwidth = 0)

# [ Loop ] #

while True:

    cameraXRot -= angle
    cameraYRot -= angle

    turtle.clear()

    # [ Calls ] #

    Shape()

    screen.update()