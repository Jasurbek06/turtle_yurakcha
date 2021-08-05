import turtle

qalam = turtle.Turtle()
wn = turtle.Screen()
wn.title("YURAKCHA")
wn.bgcolor("#b6ffbb")
def egri_chiziq():
    for i in range(200):
        qalam.right(1)
        qalam.forward(1)
def yurakcha():
    qalam.fillcolor("blue")
    qalam.begin_fill()
    qalam.left(140)
    qalam.forward(113)
    egri_chiziq()
    qalam.left(120)
    egri_chiziq()
    qalam.forward(112)
    qalam.end_fill()
def tex():
    qalam.up()
    qalam.setpos(-72, 95)
    qalam.down()
    qalam.color("red")
    qalam.write("JaSuR 0606",font=("Verdana",16,"bold"))
    qalam.hideturtle()
yurakcha()
tex()
wn.mainloop()
