#Import Tkinter Module
from Tkinter import *
import tkMessageBox
#Create Window
main = Tk(className = "level 1")
canvas = Canvas(main, width = 1280, height = 720, bg = "White")
canvas.pack()
def displayText():
    if entryWidget.get().strip() == "":
        tkMessageBox.showerror("Tkinter Entry Widget", "Enter a text value")
    else:
        tkMessageBox.showinfo("Tkinter Entry Widget", "Text value =" + entryWidget.get().strip())
mainCanvas = canvas.create_rectangle(20, 20, 1000, 700, fill = 'white', width = 2) 
ListOfTreasures=['treasure1','treasure2','treasure3','treasure4','treasure5','treasure6','treasure7','treasure8']
def callback(event):
    global NumberOfTreasures
    global MaxTreasures
    if NumberOfTreasures<MaxTreasures and ProgramActive is False:
        ListOfTreasures[NumberOfTreasures]=treasures(event.x,event.y)
        NumberOfTreasures+=1
        print NumberOfTreasures
canvas.tag_bind(mainCanvas,"<Button-1>", callback)
canvas.pack()
ProgramActive=False
NumberOfTreasures=0
class treasures:
    def __init__(self,x,y):
        global NumberOfTreasures
        self.type=interface.variable.get()
        self.x=x
        self.y=y
        if self.type=="Rectangle":
            canvas.create_rectangle(self.x-10,self.y-10,self.x+10,self.y+10,fill='blue')
            self.score=50
        elif self.type=="Circle":
            canvas.create_oval(self.x-10,self.y-10,self.x+10,self.y+10,fill='yellow')
            self.score=75
        elif self.type=="Triangle":
            canvas.create_polygon(self.x,self.y-20,self.x-10,self.y,self.x+10,self.y,fill='green')
            self.score=100
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

        self.startButton = Button(name, text = "Start", width = 20, command = self.start, font = ("Arial", 16),bg = "LightGreen")
        self.startButton.place(x = 1020, y = 80)

        self.resetButton = Button(name, text = "Reset", width = 20, command = '', font = ("Arial", 16), bg = "Orange")
        self.resetButton.place(x = 1020, y = 130)

        self.pauseButton = Button(name, text = "Pause", width = 20, command = '', font = ("Arial", 16), bg = "Yellow")
        self.pauseButton.place(x = 1020, y = 180)

        self.levelSelectButton = Button(name, text = "Level Select", width = 20, command = '', font = ("Arial", 16), bg = "LightBlue")
        self.levelSelectButton.place(x = 1020, y = 230)

        self.scoreLabel = Label(name, text = "Score", width = 10, height = 2, font = ("Arial", 16), bg = "LightGray")
        self.scoreLabel.place(x = 1020, y = 290)

        self.scoreShowLabel = Label(name, text = "000", width = 10, height = 2, font = ("Arial", 16), bg = "LightGray")
        self.scoreShowLabel.place(x = 1140, y = 290)

        self.treasureCollectedLabel = Label(name, text = "Treasure Collected", width = 20, height = 1, font = ("Arial", 16), bg = "LightGray")
        self.treasureCollectedLabel.place(x = 1020, y = 350)

        self.treasureBackgroundLabel = Label(name, width = 34, height = 7, bg = "LightGray")
        self.treasureBackgroundLabel.place(x = 1020, y = 380)

        #Create DropDown List for selecting which type of treasure to create
        self.OPTIONS = [
            "Rectangle",
            "Circle",
            "Triangle"
        ]

        self.variable = StringVar(main)
        self.variable.set(self.OPTIONS[0]) # default value

        self.w = apply(OptionMenu, (main, self.variable) + tuple(self.OPTIONS))
        self.w.pack()

    def Timer(main):
         global counter, resetpressed, pausepressed
         counter==counter
         if (counter != 0):
            counter=counter-1
            interface.minuteconvert()
            main.secShowLabel.after(1000, main.Timer)
         else:
            main.counter_stop()

    def Timer_label(main,self):
        
            global counter, RoboFinished
            
            RoboFinished=False
            interface.Timer()
                

    def minuteconvert(main):
        
        main.secShowLabel.config(text = str(counter%60))
        main.minShowLabel.config(text = str(counter//60))


    def timerwin(main):
        timerwin = Tk(className = "Timer Window")
        timercanvas = Canvas(timerwin, width = 205, height = 320, bg = "Grey")
        interface.timerselect_label = Label(timercanvas, text = "Please Enter Robot Running Time", width = 26, font = ("Arial", 9))
        interface.timerselect_label.place(x = 10, y = 30)
        interface.time_entry=Entry(timercanvas,text= "0" ,bd=5)
        interface.time_entry.place(x=50,y=150)
        interface.time_entry_button = Button(timercanvas, text="Start", width = 8, font = ("Arial", 10),command=interface.timerwinget, bg = "Yellow")
        interface.time_entry_button.place(x = 50, y = 200)
        timercanvas.pack()

    def treasurewin(main):
        treasurewin = Tk(className = "Treasure Window")
        treasurecanvas = Canvas(treasurewin, width = 205, height = 320, bg = "Grey")
        interface.treasureselect_label = Label(treasurecanvas, text = "Please Enter the Number of Treasures you wish to create", width = 26, font = ("Arial", 9))
        interface.treasureselect_label.place(x = 10, y = 30)
        interface.treasure_entry=Entry(treasurecanvas,text= "0" ,bd=5)
        interface.treasure_entry.place(x=50,y=150)
        interface.treasure_entry_button = Button(treasurecanvas, text="Ok", width = 8, font = ("Arial", 10),command=interface.assignmaxtreasures, bg = "Yellow")
        interface.treasure_entry_button.place(x = 50, y = 200)
        treasurecanvas.pack()
        
    def assignmaxtreasures(main):
        global MaxTreasures
        MaxTreasures=interface.treasure_entry.get()
        print MaxTreasures
        
    def start(self):
        global ProgramActive
        ProgramActive=True
        self.timerwin()
        interface.startButton.place_forget()
        

    def timerwinget(main):
        global counter
        if (interface.time_entry.get())=="":
            counter=0
        else:
            counter=int(interface.time_entry.get())
        interface.Timer_label(interface)

        def start(self):
            print "Start"

        def reset(self):
            print "Reset"

        def pause(self):
            print "Pause"

        def levelSelect(self):
            print "Level Select"
            '''level = Tk()
            level.title("Level Select")
            levelCanvas = Canvas(level, width = 100'''

interface = interface(main)
#Popup window to ask how many treasures to create
interface.treasurewin()
#User is then asked to click on where they want to place treasures using the dropdown box to choose what type of treasure
#User is then asked how many robots they want
#User is then asked to click where the robots are to be placed
main.mainloop()    
