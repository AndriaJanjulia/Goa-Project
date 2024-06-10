from turtle import*

#drawing house

#drawing a square
width(7)
color("purple")
begin_fill()
forward(200)
left(90)

forward(200) 
left(90)


forward(200)
left(90)


forward(200)
left(90)
end_fill()
 
forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)
right(90)  
forward(60)    
right(90)
forward(120)
end_fill()

penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#drawing a windows

penup()
goto(20,180)
pendown()
left(30) 
color("blue")
begin_fill()
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()

penup()
goto(180,180)
pendown()
begin_fill()
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()


exitonclick()