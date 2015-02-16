from Tkinter import *
import tkMessageBox
level2 = Tk()
level2.title("Level 2")
level2.resizable(0,0)
canvas = Canvas(level2, width = 1280, height = 720, bg = "White")
canvas.pack()

level2Map = canvas.create_rectangle(20, 20, 1000, 700, fill = 'white', width = 2) 

class interface:
    def __init__(self, name):
        self.timerLabel = Label(name, text = "Timer:", width = 10, height = 2, font = ("Arial", 16), bg = "Gray")
        self.timerLabel.place(x = 1020, y = 20)

        self.minShowLabel = Label(name, text = "00", width = 5, height = 2, font = ("Arial", 16), bg = "Gray")
        self.minShowLabel.place(x = 1120, y = 20)

        self.spacerLabel = Label(name, text = ":", width = 2, height = 2, font = ("Arial", 16), bg = "Gray")
        self.spacerLabel.place(x = 1180, y = 20)

        self.secShowLabel = Label(name, text = "00", width = 5, height = 2, font = ("Arial", 16), bg = "Gray")
        self.secShowLabel.place(x = 1200, y = 20)

        self.startButton = Button(name, text = "Start", width = 20, command = self.start, font = ("Arial", 16), bg = "LightGreen")
        self.startButton.place(x = 1020, y = 80)

        self.resetButton = Button(name, text = "Reset", width = 20, command = self.reset, font = ("Arial", 16), bg = "Orange")
        self.resetButton.place(x = 1020, y = 130)

        self.pauseButton = Button(name, text = "Pause", width = 20, command = '', font = ("Arial", 16), bg = "Yellow")

        self.levelSelectButton = Button(name, text = "Level Select", width = 20, command = self.levelSelect, font = ("Arial", 16), bg = "LightBlue")
        self.levelSelectButton.place(x = 1020, y = 180)

        self.scoreLabel = Label(name, text = "Score", width = 10, height = 2, font = ("Arial", 16), bg = "LightGray")
        self.scoreLabel.place(x = 1020, y = 240)

        self.scoreShowLabel = Label(name, text = "000", width = 10, height = 2, font = ("Arial", 16), bg = "LightGray")
        self.scoreShowLabel.place(x = 1140, y = 240)

        self.treasureCollectedLabel = Label(name, text = "Treasure Collected", width = 20, height = 1, font = ("Arial", 16), bg = "LightGray")
        self.treasureCollectedLabel.place(x = 1020, y = 300)

        self.treasureBackgroundLabel = Label(name, width = 34, height = 7, bg = "LightGray")
        self.treasureBackgroundLabel.place(x = 1020, y = 330)

    def timer(level2):
         global counter, resetpressed, pausepressed
         counter==counter
         if (counter != 0):
            counter=counter-1
            interface.minuteConvert()
            level2.secShowLabel.after(1000, level2.timer)
         else:
            level2.counter_stop()

    def timerShow(level2,self):
        global counter, RoboFinished
        RoboFinished=False
        interface.timer()   

    def minuteConvert(level2):
        level2.secShowLabel.config(text = str(counter%60))
        level2.minShowLabel.config(text = str(counter//60))

    def timerWindow(level2):
        global timerWindow, wishlistWindow
        timerWindow = Tk()
        timerWindow.title("Collection Time")
        timerWindow.resizable(0,0)
        
        timerCanvas = Canvas(timerWindow, width = 210, height = 200, bg = "White")
        
        interface.timerselect_label = Label(timerCanvas, text = "Time to collect:", wraplength = 100, width = 20, font = ("Arial", 9), bg = "White")
        interface.timerselect_label.place(x = 35, y = 10)

        interface.timermessage_label = Label(timerCanvas, text = "Minutes                Seconds",  width = 22, font = ("Arial", 9), bg = "White")
        interface.timermessage_label.place(x = 30, y = 90)

        interface.timermessage_label = Label(timerCanvas, text = "Please enter a value greater than 0",  wraplength = 100 ,width = 22, font = ("Arial", 9), bg = "White")
        interface.timermessage_label.place(x = 30, y = 120)
        
        interface.timeEntrymin = Entry(timerCanvas, text = "" , width = 8, bd = 5)
        interface.timeEntrymin.insert(0,"0")
        interface.timeEntrymin.place(x = 30,y = 60)
        
        
        interface.timeEntrysec = Entry(timerCanvas, text = "" , width = 8, bd = 5)
        interface.timeEntrysec.insert(0,"0")
        interface.timeEntrysec.place(x = 130,y = 60)
        
        interface.timeEntryButton = Button(timerCanvas, text = "Start", width = 10, font = ("Arial", 10), command = interface.timerWindowGet, bg = "LightGreen")
        interface.timeEntryButton.place(x = 65, y = 170)
        
        timerCanvas.pack()
        wishlistWindow.destroy()
        timerWindow.grab_set() #these dont work 100% yet
        timerWindow.focus_force()


        
    def timerWindowGet(level2):
        global counter, timerWindow
        if (interface.timeEntrysec.get())=="" or (((interface.timeEntrysec.get())=="0") and ((interface.timeEntrymin.get())=="0")):
            counter=0
    
        else:
            counter=int(interface.timeEntrysec.get())
            counter=counter+((int(interface.timeEntrymin.get())*60))
            interface.timerShow(interface)
            print "Run this"
            timerWindow.destroy()

    def wishlistWindow(self):
        global wishlistWindow, timerWindow
        wishlistWindow = Tk()
        wishlistWindow.title("Wishlist")
        wishlistWindow.resizable(0,0)

        wishlistCanvas = Canvas(wishlistWindow, width = 210, height = 280, bg = "White")

        Boarder1 = wishlistCanvas.create_rectangle(105, 50, 108, 165, fill = 'Black', width = 2)
        Boarder2 = wishlistCanvas.create_rectangle(11, 65, 211, 60, fill = 'Black', width = 2)
        Boarder3 = wishlistCanvas.create_rectangle(11, 94, 211, 99, fill = 'Black', width = 2)        
        Boarder4 = wishlistCanvas.create_rectangle(11, 129, 211, 133, fill = 'Black', width = 2)
        Boarder5 = wishlistCanvas.create_rectangle(11, 164, 211, 167, fill = 'Black', width = 2)

        interface.wishlistEntryButton = Button(wishlistCanvas, text = "Ok", width = 10, font = ("Arial", 10), command = self.timerWindow, bg = "LightGray")
        interface.wishlistEntryButton.place(x = 60, y = 250)

        interface.wishlistEntryLabel = Label(wishlistCanvas, text = "Please select your desired items", width = 24, font = ("Arial", 10),  bg = "LightGray")
        interface.wishlistEntryLabel.place(x = 10, y = 10)

        C1=Checkbutton(wishlistWindow,text="Square  ",onvalue=1,offvalue=0,height=1,width=11)
        C1.place(x=110,y=65)

        c2=Checkbutton(wishlistWindow,text="Triangle",onvalue=1,offvalue=0,height=1,width=11)
        c2.place(x=110,y=100)

        c3=Checkbutton(wishlistWindow,text="Circle    ",onvalue=1,offvalue=0,height=1,width=11)
        c3.place(x=110,y=135)

        interface.wishlistQuantityLabel=Label(wishlistCanvas,text="Quantity",width=12,font=("Arial",10), bg="LightGray")
        interface.wishlistQuantityLabel.place(x = 10, y = 38)

        interface.wishlistShapeLabel=Label(wishlistCanvas,text="Objects",width=12,font=("Arial",10), bg="LightGray")
        interface.wishlistShapeLabel.place(x = 110, y = 38)

        interface.squareQuantity = Entry(wishlistCanvas, text = "" , width = 8, bd = 5)
        interface.squareQuantity.insert(0,"0")
        interface.squareQuantity.place(x = 10,y = 66)

        interface.triangleQuantity = Entry(wishlistCanvas, text = "" , width = 8, bd = 5)
        interface.triangleQuantity.insert(0,"0")
        interface.triangleQuantity.place(x = 10,y = 101)

        interface.circleQuantity = Entry(wishlistCanvas, text = "" , width = 8, bd = 5)
        interface.circleQuantity.insert(0,"0")
        interface.circleQuantity.place(x = 10,y = 136)

        interface.multiplicationLabel1=Label(wishlistCanvas,text="*",width=2,font=("Arial",12), bg="LightGray")
        interface.multiplicationLabel1.place(x = 75, y = 67)
        
        interface.multiplicationLabel2=Label(wishlistCanvas,text="*",width=2,font=("Arial",12), bg="LightGray")
        interface.multiplicationLabel2.place(x = 75, y = 102)

        interface.multiplicationLabel3=Label(wishlistCanvas,text="*",width=2,font=("Arial",12), bg="LightGray")
        interface.multiplicationLabel3.place(x = 75, y = 138)

        interface.wishlistColourSelectLabel = Label(wishlistCanvas, text = "Choose the item colours", width = 24, font = ("Arial", 10),  bg = "LightGray")
        interface.wishlistColourSelectLabel.place(x = 10, y = 170)
        

        yellowRec = wishlistCanvas.create_rectangle(10, 200, 25, 215, fill = 'Yellow')
        redRec = wishlistCanvas.create_rectangle(65, 200, 80, 215, fill = 'Red')
        greenRec = wishlistCanvas.create_rectangle(125, 200, 140, 215, fill = 'Green')
        blueRec = wishlistCanvas.create_rectangle(185, 200, 200, 215, fill = 'Blue')

        yellowCheck=Checkbutton(wishlistWindow,onvalue=1,offvalue=0,height=1,font=("Arial",3))
        yellowCheck.place(x=7,y=220)

        redCheck=Checkbutton(wishlistWindow,onvalue=1,offvalue=0,height=1,font=("Arial",3))
        redCheck.place(x=62,y=220)

        greenCheck=Checkbutton(wishlistWindow,onvalue=1,offvalue=0,height=1,font=("Arial",3))
        greenCheck.place(x=122,y=220)

        blueCheck=Checkbutton(wishlistWindow,onvalue=1,offvalue=0,height=1,font=("Arial",3))
        blueCheck.place(x=182,y=220)


        wishlistCanvas.pack()
        
    def start(self):
        self.wishlistWindow()
        interface.startButton.place_forget()
        interface.pauseButton.place(x = 1020, y = 80)

    def reset(self):
        interface.pauseButton.place_forget()
        interface.startButton.place(x = 1020, y = 80)
        counter = 0

    def pause(self):
        print "Pause"
        
    def levelSelect(self):
        global levelWindow
        levelWindow = Tk()
        levelWindow.title("Level Select")
        levelWindow.resizable(0,0)
        
        levelCanvas = Canvas(levelWindow, width = 200, height = 180, bg = "White")
        
        interface.level1Button = Button(levelCanvas, text = "Level 1", width = 20, font = ("Arial", 10),command= self.levelSelectLevel1, bg = "LightBlue")
        interface.level1Button.place(x = 15, y = 10)
        
        interface.level2Button = Button(levelCanvas, text = "Level 2", width = 20, font = ("Arial", 10),command= self.levelSelectLevel2, bg = "LightBlue")
        interface.level2Button.place(x = 15, y = 50)
        
        interface.level3Button = Button(levelCanvas, text = "Level 3", width = 20, font = ("Arial", 10),command= self.levelSelectLevel3, bg = "LightBlue")
        interface.level3Button.place(x = 15, y = 90)
        
        interface.levelCancelButton = Button(levelCanvas, text = "Cancel", width = 10, font = ("Arial", 10),command = levelWindow.destroy , bg = "LightGray")
        interface.levelCancelButton.place(x = 50, y = 140)
        
        levelCanvas.pack()

    def levelSelectLevel1(self):
        global levelWindow
        levelWindow.destroy()
        level2.destroy()
        import Level1

    def levelSelectLevel2(self):
        global levelWindow
        levelWindow.destroy()
        level2.destroy()
        import Level2

    def levelSelectLevel3(self):
        global levelWindow
        levelWindow.destroy()
        level2.destroy()
        import Level3

    #def wishlistquitconfirm(self):
    #Red,Green,yellow,Blue

interface = interface(level2)

level2.mainloop()    
