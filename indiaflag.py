import turtle as t
def rect(clr):
    t.color(clr)
    t.pencolor("black")
    t.begin_fill()
    t.forward(200)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(50)
    t.end_fill()
    t.forward(50)
    t.left(90)

rect("orange")
rect("white")
rect("green")
t.left(90)
t.forward(100)
t.right(90)
t.forward(100)
t.pencolor("blue")
t.circle(25)
t.left(90)
t.forward(25)
for _ in range(24):
    t.forward(25)
    t.back(25)
    t.right(15)


t.mainloop()

