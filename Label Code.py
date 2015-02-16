from Tkinter import*
import time
main = Tk(className = " Robot Label Test 1")
canvas = Canvas(main, width = 700, height = 500, bg = "Black")
canvas.pack()

Treasure1 = canvas.create_rectangle(250, 120, 270, 140, fill = "White")
Treasure2 = canvas.create_rectangle(250, 170, 270, 190, fill = "Orange")
HoneyBee = canvas.create_rectangle(100,120,120,140, fill = "Yellow")


'''for i in range(0,100):
    Bx1,By1,Bx2,By2 = canvas.coords(HoneyBee)
    Tx1,Ty1,Tx2,Ty2 = canvas.coords(Treasure1)
    canvas.coords(HoneyBee, Bx1+10, By1, Bx2+10,By2)
    canvas.update()
    time.sleep(0.125)
    Bx1,By1,Bx2,By2 = canvas.coords(HoneyBee)
    if Bx1 == Tx1 or Bx2 == Tx2:
        break'''

Bx1,By1,Bx2,By2 = canvas.coords(HoneyBee)
T1x1,T1y1,T1x2,T1y2 = canvas.coords(Treasure1)
T2x1,T2y1,T2x2,T2y2 = canvas.coords(Treasure2)
'''main.bind("<Enter>", lambda e, x=x: e.widget.config(text=x))
main.bind("<Leave>", lambda e, i=i: e.widget.config(text="Label "+str(i)))'''
Shapes = [Treasure1]
ShapeLabel = Label(main, text = "Shape = SQUARE  ", bg = "White", font = ("Arial", 10))
ColourLabel = Label(main, text = "Colour = WHITE     ", bg = "White", font = ("Arial", 10))
WorthLabel = Label(main, text = "Worth = N POINTS ", bg = "White", font = ("Arial", 10))

def MouseRollover(self):
    ShapeLabel.place(x = T1x2 + 20, y = T1y1 - 20)
    ColourLabel.place(x = T1x2 + 20, y = T1y1)
    WorthLabel.place(x = T1x2 + 20, y = T1y1+20)

def MouseOff(self):
    ShapeLabel.place_forget()
    ColourLabel.place_forget()
    WorthLabel.place_forget()

canvas.tag_bind(Treasure1,"<Enter>", MouseRollover)
canvas.tag_bind(Treasure1, "<Leave>", MouseOff)


main.mainloop()
