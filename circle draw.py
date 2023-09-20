import turtle 
    
t = turtle.Turtle()

#This function draw a circle in x,y of radius r
def drawCircle(x,y,r):
    t.pu()
    t.goto(x,y-r) #-r because we want xy as center and Turtles starts from border
    t.pd()
    t.circle(r)


#draw a circle in (50,30) with r=50
drawCircle(50,30,50)

#draw a circle in (20,50) with r=100
drawCircle(20,50,100)

#draw a circle in (0,0) with r=10
drawCircle(0,0,10) #0,0 is the center of the screen
