def drawing(Pen,stage):
  if stage==0:
    Pen.reset()
    Pen.color("black")
    Pen.penup()
    Pen.goto(-25,-40)
    Pen.pendown()
    Pen.forward(50)
    Pen.penup() 
    Pen.forward(-25)
    Pen.pendown()
    Pen.left(90)
    Pen.forward(100)
    Pen.right(90)
    Pen.forward(50)
    Pen.right(90)
    Pen.forward(10)
    Pen.penup() 
    Pen.forward(20)
    Pen.pendown()
  if stage ==1:
    
    Pen.penup()
    Pen.goto(50,30)
    Pen.pendown()
    Pen.color("red")
    Pen.left(90)
    Pen.circle(10)
  if stage ==2:
    
    Pen.penup()
    Pen.goto(50,30)
    Pen.pendown()
    Pen.color("orange")
    Pen.right(90)
    Pen.forward(5)
    Pen.left(90)
    Pen.forward(-10)
    Pen.forward(20)
    Pen.forward(-10)
    Pen.right(90)
    Pen.forward(30)
  if stage ==3:
    
    Pen.color("yellow")
    Pen.penup()
    Pen.goto(40,25)
    Pen.pendown() 
    Pen.right(20)
    Pen.forward(30)
  if stage ==4:
    
    Pen.color("green")
    Pen.penup() 
    Pen.goto(60,25)
    Pen.pendown()
    Pen.left(40)
    Pen.forward(30)
  if stage == 5:
    
    Pen.color("blue")
    Pen.penup()
    Pen.goto(50,-5)
    Pen.pendown() 
    Pen.right(40)
    Pen.forward(30)
  if stage ==6:
    
    Pen.color("purple")
    Pen.penup() 
    Pen.goto(50,-5)
    Pen.pendown() 
    Pen.left(40)
    Pen.forward(30)
