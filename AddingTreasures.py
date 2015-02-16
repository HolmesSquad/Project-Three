from Tkinter import *
level1 = Tk()
level1.title("Level 1")
level1.resizable(0,0)
canvas = Canvas(level1, width = 1280, height = 720, bg = "White")
canvas.pack()
level1Map = canvas.create_rectangle(20, 20, 1000, 700, fill = 'white', width = 2) 
ListOfTreasures=[]
ListOfRobots=[]
NumberOfTreasures=0
NumberOfRobots=0
ProgramActive=False
def callback(event):
    global NumberOfTreasures
    global NumberOfRobots
    if NumberOfTreasures<int(interface.MaxTreasures) and ProgramActive is False:
        ListOfTreasures.append(treasures(event.x,event.y))
        NumberOfTreasures+=1
        print interface.MaxTreasures
        print NumberOfTreasures
        if NumberOfTreasures==int(interface.MaxTreasures):
            interface.robotWindow()
    elif NumberOfRobots<int(interface.MaxRobots) and ProgramActive is False:
        ListOfRobots.append(robots(event.x,event.y))
        NumberOfRobots+=1
        if NumberOfRobots==int(interface.MaxRobots):
            interface.startButton['state']='normal'
            
canvas.tag_bind(level1Map,"<Button-1>", callback)
canvas.pack()

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

        self.startButton = Button(name, text = "Start", width = 20, command = self.start, font = ("Arial", 16),bg = "LightGreen",state=DISABLED)
        self.startButton.place(x = 1020, y = 80)

        self.resetButton = Button(name, text = "Reset", width = 20, command = '', font = ("Arial", 16), bg = "Orange")
        self.resetButton.place(x = 1020, y = 130)

        self.pauseButton = Button(name, text = "Pause", width = 20, command = '', font = ("Arial", 16), bg = "Yellow",state=DISABLED)
        self.pauseButton.place(x = 1020, y = 180)

        self.levelSelectButton = Button(name, text = "Level Select", width = 20, command = self.levelSelect, font = ("Arial", 16), bg = "LightBlue")
        self.levelSelectButton.place(x = 1020, y = 230)

        self.scoreLabel = Label(name, text = "Score", width = 10, height = 2, font = ("Arial", 16), bg = "LightGray")
        self.scoreLabel.place(x = 1020, y = 290)

        self.scoreShowLabel = Label(name, text = "000", width = 10, height = 2, font = ("Arial", 16), bg = "LightGray")
        self.scoreShowLabel.place(x = 1140, y = 290)

        self.treasureCollectedLabel = Label(name, text = "Treasure Collected", width = 20, height = 1, font = ("Arial", 16), bg = "LightGray")
        self.treasureCollectedLabel.place(x = 1020, y = 350)

        self.treasureBackgroundLabel = Label(name, width = 20, height = 8, font = ("Arial", 16), bg = "LightGray")
        self.treasureBackgroundLabel.place(x = 1020, y = 380)
        
        #Create DropDown List for selecting which type of treasure to create
        self.OPTIONS = [
            "Rectangle",
            "Circle",
            "Triangle"
        ]

        self.variable = StringVar(level1)
        self.variable.set(self.OPTIONS[0]) # default value

        self.w = apply(OptionMenu, (level1, self.variable) + tuple(self.OPTIONS))
        self.w.pack()

    def timer(level1):
         global counter, resetpressed, pausepressed
         counter==counter
         if (counter != 0):
            counter=counter-1
            interface.minuteConvert()
            level1.secShowLabel.after(1000, level1.timer)
         else:
            level1.counter_stop()

    def timerShow(level1,self):
        global counter, RoboFinished
        RoboFinished=False
        interface.timer()
                
    def minuteConvert(level1):
        level1.secShowLabel.config(text = str(counter%60))
        level1.minShowLabel.config(text = str(counter//60))

    def timerWindow(level1):
        global timerWindow
        timerWindow = Tk()
        timerWindow.title("Collection Time")
        timerWindow.resizable(0,0)
        
        timerCanvas = Canvas(timerWindow, width = 210, height = 200, bg = "White")
        
        interface.timerselect_label = Label(timerCanvas, text = "Time to collect: (In Seconds)", wraplength = 100, width = 20, font = ("Arial", 9), bg = "White")
        interface.timerselect_label.place(x = 35, y = 10)
        
        interface.timeEntry = Entry(timerCanvas, text= "" , width = 20, bd = 5)
        interface.timeEntry.place(x = 45,y = 60)
        
        interface.timeEntryButton = Button(timerCanvas, text="Start", width = 10, font = ("Arial", 10),command=interface.timerwinget, bg = "LightGreen")
        interface.timeEntryButton.place(x = 65, y = 100)
        
        timerCanvas.pack()

    def treasureWindow(level1):
        global treasureWindow
        treasureWindow = Tk()
        treasureWindow.title("Number of Treasures")
        treasureWindow.resizable(0,0)
        
        treasureCanvas = Canvas(treasureWindow, width = 210, height = 200, bg = "White")
        
        interface.treasure_label = Label(treasureCanvas, text = "Number of Treasures", wraplength = 100, width = 20, font = ("Arial", 9), bg = "White")
        interface.treasure_label.place(x = 35, y = 10)
        
        interface.treasureEntry = Entry(treasureCanvas, text= "" , width = 20, bd = 5)
        interface.treasureEntry.place(x = 45,y = 60)
        
        interface.treasureEntryButton = Button(treasureCanvas, text="Ok", width = 10, font = ("Arial", 10),command=interface.assignmaxtreasures, bg = "LightGreen")
        interface.treasureEntryButton.place(x = 65, y = 100)
        
        treasureCanvas.pack()
        
    def assignmaxtreasures(self):
        self.MaxTreasures=interface.treasureEntry.get()
        print self.MaxTreasures
        treasureWindow.destroy()

    def robotWindow(level1):
        global robotWindow
        robotWindow = Tk()
        robotWindow.title("Number of Robots")
        robotWindow.resizable(0,0)
        
        robotCanvas = Canvas(robotWindow, width = 210, height = 200, bg = "White")
        
        interface.robot_label = Label(robotCanvas, text = "Number of Robots", wraplength = 100, width = 20, font = ("Arial", 9), bg = "White")
        interface.robot_label.place(x = 35, y = 10)
        
        interface.robotEntry = Entry(robotCanvas, text= "" , width = 20, bd = 5)
        interface.robotEntry.place(x = 45,y = 60)
        
        interface.robotEntryButton = Button(robotCanvas, text="Ok", width = 10, font = ("Arial", 10),command=interface.assignmaxrobots, bg = "LightGreen")
        interface.robotEntryButton.place(x = 65, y = 100)
        
        robotCanvas.pack()
        
    def assignmaxrobots(self):
        self.MaxRobots=interface.robotEntry.get()
        print self.MaxRobots
        robotWindow.destroy()
        
    def start(self):
        self.timerWindow()
        interface.startButton.place_forget()
        
    def timerwinget(level1):
        global counter, timerWindow
        if (interface.timeEntry.get())=="":
            counter=0
        else:
            counter=int(interface.timeEntry.get())
        interface.timerShow(interface)
        timerWindow.destroy()
        
    def reset(self):
        print "Reset"

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
        level1.destroy()
        import Level1

    def levelSelectLevel2(self):
        global levelWindow
        levelWindow.destroy()
        level1.destroy()
        import Level2

    def levelSelectLevel3(self):
        global levelWindow
        levelWindow.destroy()
        level1.destroy()
        import Level3

class treasures:
    global canvas
    global NumberOfTreasures
    def __init__(self,x,y):
        global NumberOfTreasures
        self.type=interface.variable.get()
        self.x=x
        self.y=y
        self.name="Treasure"+str(NumberOfTreasures)
        if self.type=="Rectangle":
            self.name=canvas.create_rectangle(self.x-10,self.y-10,self.x+10,self.y+10,fill='blue')
            self.score=50
        elif self.type=="Circle":
            self.name=canvas.create_oval(self.x-10,self.y-10,self.x+10,self.y+10,fill='yellow')
            self.score=75
        elif self.type=="Triangle":
            self.name=canvas.create_polygon(self.x,self.y-20,self.x-10,self.y,self.x+10,self.y,fill='green')
            self.score=100
'''        canvas.tag_bind(self.name,"<Enter>",self.MouseRollover)
    def MouseRollover(self):
        ShapeLabel = Label(main, text = "Shape = SQUARE  ", bg = "White", font = ("Arial", 10))
        ShapeLabel.place(x = Treasure.x + 40, y = Treasure.y - 20)
        ColourLabel = Label(main, text = "Colour = WHITE     ", bg = "White", font = ("Arial", 10))
        ColourLabel.place(x = Treasure.x + 40, y = Treasure.y)
        WorthLabel = Label(main, text = "Worth = N POINTS ", bg = "White", font = ("Arial", 10))
        WorthLabel.place(x = Treasure.x + 40, y = Treasure.y+20)
    def MouseOff(self):
        ShapeLabel.place_forget()
        ColourLabel.place_forget()
        WorthLabel.place_forget()'''
class robots:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        canvas.create_rectangle(self.x-15,self.y-15,self.x+15,self.y+15,fill='cyan')
interface = interface(level1)
interface.MaxTreasures=0
interface.MaxRobots=0
interface.treasureWindow()
level1.mainloop()    