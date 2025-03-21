import turtle as trtl
import random as rand

#TURTLES
painter = trtl.Turtle()
sun = trtl.Turtle()

#lists 
skincolors = ["antiquewhite", "saddlebrown", "tan", "darkgoldenrod", "peachpuff"]
sunrays = ["yellow", "tomato2", "darkorange", "orangered"]

#GRASS
painter.speed("fastest")
painter.penup()
painter.goto(-350,-200)
painter.color("green")
painter.fillcolor("green")
painter.begin_fill()
painter.pendown()
painter.forward(700)
painter.right(90)
painter.forward(150)
painter.right(90)
painter.forward(700)
painter.right(90)
painter.forward(150)
painter.end_fill()

#SUN 
def draw_sun():
  sun.speed("fastest")
  sun.penup()
  sun.goto(230,200)
  sun.color("yellow")
  sun.left(90)
  sun.fillcolor("gold1")
  sun.begin_fill()
  sun.circle(-70)
  sun.end_fill()
  #sun movement
#I edi
  sun.pensize(6)
  for movement in range(36): 
    sun.goto(300,200)
    sun.right(20)
    sun.forward(80)
    sun.pendown()
    sun.forward(55)
    sun.penup()
    movement = movement + 1
  if movement % 18 == 0:
    sun.color(rand.choice(sunrays))
  if movement % 36 == 0:
    painter.color("yellow")
#FACE OUTLINE
def draw_funkobody():
  print("KEEP RUNNING THE CODE TILL YOU GET A SKINCOLOR THAT REPRESENTS YOU")
  painter.penup()
  painter.goto(100,50)
  painter.pendown()
  painter.setheading(180)
  painter.color("black")
  painter.fillcolor(rand.choice(skincolors))
  painter.begin_fill()
  painter.forward(200)
  painter.circle(10,100)
  painter.setheading(-90)
  painter.forward(100)
  painter.circle(10,100)
  painter.right(10)
  painter.forward(200)
  painter.circle(10, 100)
  painter.right(10)
  painter.forward(100)
  painter.circle(10,100)
  painter.end_fill()
#was going to do a loop for this segment of the outline, but it was not succesful
#EYES
  painter.penup()
  painter.pencolor("black")
  painter.goto(0,15)
  painter.forward(50)
  painter.pendown()
  painter.pensize(13)
  painter.circle(7)
  painter.right(197)
  painter.penup()
  painter.forward(100)
  painter.pendown()
  painter.pensize(13)
  painter.circle(7)
  #shirt
  painter.penup()
  painter.goto(0,0)
  painter.setheading(270)
  painter.forward(75)
  painter.left(90)
  painter.pendown()
  painter.pensize(2)
  #put input here
  shirtcolor = input("What color would you like the shirt ? ")
  painter.fillcolor(shirtcolor)
  painter.begin_fill()
  painter.forward(70)
  painter.right(180)
  painter.forward(140)
  painter.left(90)
  painter.forward(50)
  painter.left(90)
  painter.forward(20)
  painter.left(90)
  painter.forward(25)
  painter.right(90)
  painter.forward(5)
  painter.right(90)
  painter.forward(40)
  painter.left(90)
  painter.forward(90)
  painter.left(90)
  painter.forward(40)
  painter.right(90)
  painter.forward(5)
  painter.right(90)
  painter.forward(25)
  painter.left(90)
  painter.forward(20)
  painter.left(90)
  painter.forward(50)
  painter.end_fill()
  #skirt or pants
  painter.penup()
  painter.goto(0,0)
  painter.setheading(270)
  painter.forward(140)
  painter.right(90)
  painter.forward(45)
  #costumize the gender / look of the funko pop by letting user choose colors 
  garment = input("Would you like a skirt or pants? ")
  if (garment == "skirt"):
    skirtcolor = input("what color would you like the skirt ? ")
    painter.fillcolor(skirtcolor)
    painter.begin_fill()
    painter.left(55)
    painter.pendown()
    painter.forward(60)
    painter.left(125)
    painter.forward(155)
    painter.left(120)
    painter.forward(58)
    painter.end_fill()
  elif (garment == "pants"):
    pantscolor = input("what color would you like the pants ? ")
    painter.fillcolor(pantscolor)
    painter.begin_fill()
    painter.pendown()
    painter.left(90)
    painter.forward(60)
    painter.left(90)
    painter.forward(30)
    painter.left(90)
    painter.forward(30)
    painter.right(90)
    painter.forward(30)
    painter.right(90)
    painter.forward(30)
    painter.left(90)
    painter.forward(30)
    painter.left(90)
    painter.forward(60)
    painter.end_fill()
def make_game():
  draw_sun()
  draw_funkobody() 
  
start_question = input("Would you like to start designing , Y or N: ")
if start_question == "Y":
  make_game()
  print("\nGAME OVER")

else:
  print("SEE YA LATER SUCKER")

wn = trtl.Screen()
wn.mainloop()
wn.bgcolor("lightblue")
