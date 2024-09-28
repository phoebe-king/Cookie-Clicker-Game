import turtle 

#function to update the clicks when user clicks the cookie
#x, y being passed through allow the onclick() method to work
def clicked(x, y):
    global clicks
    clicks += 1
    pen.clear()
    pen.write(f"Clicks: {clicks}", align="center", font=("Calibri", 32, "normal"))

#set up the turtle window
wn = turtle.Screen()
wn.title("Cookie Clicker")
wn.bgcolor("#ede8d0")

#gives program the particular image you want to use
wn.register_shape("cookie.gif")

#set up the image
cookie = turtle.Turtle()
cookie.shape("cookie.gif")
cookie.speed(0)

#intialize the clicks
clicks = 0

#display text for user to see how many clicks
pen = turtle.Turtle()
pen.hideturtle()
pen.color("black")
pen.penup()
pen.goto(0,250)
pen.write(f"Clicks: {clicks}", align="center", font=("Calibri", 32, "normal"))

cookie.onclick(clicked)

wn.mainloop()