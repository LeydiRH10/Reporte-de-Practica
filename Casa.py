from turtle import*
setup(640, 480 ,0 ,0)
title("Casa")
screensize(200, 100)
hideturtle()

pensize(5)
fillcolor("magenta")
begin_fill()
goto(100, 0)
goto(100, -100)
goto(-100, -100)
goto(-100, 0)
end_fill()

begin_fill()
goto(100, 0)
end_fill()

penup()
goto(-100, 0)
pendown()
begin_fill()
goto(10, 0)
end_fill()

penup()
goto(-58, 58)
pendown()
begin_fill()
goto(58, 58)
end_fill()

penup()
goto(-100, 0)
pendown()
begin_fill()
goto(-60, 56)
end_fill()

penup()
goto(100, 0)
pendown()
begin_fill()
goto(60, 56)
end_fill()

penup()
goto(-30, -100)
pendown()
fillcolor("gray")
begin_fill()
goto(30, -100)
goto(30, -20)
goto(-30, -20)
goto(-30, -100)
end_fill()
