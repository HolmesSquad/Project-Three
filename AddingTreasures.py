from Tkinter import *
import time
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

        self.treasureCollectedLabel = Label(name, text = "Robot 1 Treasure Collected", width = 22, height = 1, font = ("Arial", 14), bg = "LightGray")
        self.treasureCollectedLabel.place(x = 1020, y = 350)
        self.treasureCollectedLabel2 = Label(name, text = "Robot 2 Treasure Collected", width = 22, height = 1, font = ("Arial", 14), bg = "LightGray")
        self.treasureCollectedLabel2.place(x = 1020, y = 450)

        
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
        
        interface.treasure_label = Label(treasureCanvas, text = "Number of Treasures (Max:10)", wraplength = 100, width = 20, font = ("Arial", 9), bg = "White")
        interface.treasure_label.place(x = 35, y = 10)
        
        interface.treasureEntry = Entry(treasureCanvas, text= "" , width = 20, bd = 5)
        interface.treasureEntry.place(x = 45,y = 60)
        
        interface.treasureEntryButton = Button(treasureCanvas, text="Ok", width = 10, font = ("Arial", 10),command=interface.assignmaxtreasures, bg = "LightGreen")
        interface.treasureEntryButton.place(x = 65, y = 100)
        
        treasureCanvas.pack()
        
    def assignmaxtreasures(self):
        global TreasuresRemaining
        if int(interface.treasureEntry.get())>10:
            print "No more than ten treasures can be created"
        else:
            self.MaxTreasures=interface.treasureEntry.get()
            TreasuresRemaining=int(self.MaxTreasures)
            treasureWindow.destroy()

    def robotWindow(level1):
        global robotWindow
        robotWindow = Tk()
        robotWindow.title("Number of Robots")
        robotWindow.resizable(0,0)
        
        robotCanvas = Canvas(robotWindow, width = 210, height = 200, bg = "White")
        
        interface.robot_label = Label(robotCanvas, text = "Number of Robots (Max: 2)", wraplength = 100, width = 20, font = ("Arial", 9), bg = "White")
        interface.robot_label.place(x = 35, y = 10)
        
        interface.robotEntry = Entry(robotCanvas, text= "" , width = 20, bd = 5)
        interface.robotEntry.place(x = 45,y = 60)
        
        interface.robotEntryButton = Button(robotCanvas, text="Ok", width = 10, font = ("Arial", 10),command=interface.assignmaxrobots, bg = "LightGreen")
        interface.robotEntryButton.place(x = 65, y = 100)
        
        robotCanvas.pack()
        
    def assignmaxrobots(self):
        if int(interface.robotEntry.get())>2:
            print "No more than two robots can be created"
        else:
            self.MaxRobots=interface.robotEntry.get()
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
        ListOfRobots[0].TreasuresFoundPositions=[[1025,390,1045,410],[1055,390,1075,410],[1085,390,1105,410],[1115,390,1145,410],[1145,390,1165,410],[1175,390,1195,410],[1205,390,1225,410],[1235,390,1255,410],[1025,420,1045,440],[1055,420,1075,440]]
        ListOfRobots[1].TreasuresFoundPositions=[[1025,490,1045,510],[1055,490,1075,510],[1085,490,1105,510],[1115,490,1145,510],[1145,490,1165,510],[1175,490,1195,510],[1205,490,1225,510],[1235,490,1255,510],[1025,520,1045,540],[1055,520,1075,540]]
        interface.pauseButton['state']='normal'
        for robot in ListOfRobots:
            robot.closesttreasure()
            robot.moveto(robot.ClosestTreasure.x,robot.ClosestTreasure.y)
        while TreasuresRemaining>0:
            for robot in ListOfRobots:
                robot.move()
        
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
        self.found=False
        if self.type=="Rectangle":
            self.name=canvas.create_rectangle(self.x-10,self.y-10,self.x+10,self.y+10,fill='blue')
            self.score=50
        elif self.type=="Circle":
            self.name=canvas.create_oval(self.x-10,self.y-10,self.x+10,self.y+10,fill='yellow')
            self.score=75
        elif self.type=="Triangle":
            self.name=canvas.create_polygon(self.x,self.y-20,self.x-10,self.y,self.x+10,self.y,fill='green')
            self.score=100
    def delete(self):
        canvas.itemconfig(self.name,fill="white",width=0)
class robots:
    def __init__(self,x,y):
        self.x1=x-10
        self.y1=y-10
        self.x2=x+10
        self.y2=y+10
        self.x=x
        self.y=y
        self.speed=1
        self.canvas=canvas
        self.shape=canvas.create_rectangle(self.x-10,self.y-10,self.x+10,self.y+10,fill='cyan')
        self.TreasuresFound=[]
        self.TreasuresFoundPositions=[]
        self.NumberOfTreasuresFound=0
    def closesttreasure(self):
        lowestdistance=100000
        for i in ListOfTreasures:
            if i.found==False:
                if i.x>self.x:
                    xdistance=i.x-self.x
                elif i.x<self.x:
                    xdistance=self.x-i.x
                else:
                    xdistance=0
                if i.y>self.y:
                    ydistance=i.y-self.y
                elif i.y<self.y:
                    ydistance=self.y-i.y
                else:
                    ydistance=0
                totaldistance=(ydistance**2+xdistance**2)**0.5
                if totaldistance<lowestdistance:
                    lowestdistance=totaldistance
                    self.ClosestTreasure=i
    def moveto(self,xdest,ydest):
        if xdest>self.x:
            xdistance=xdest-self.x
        elif xdest<self.x:
            xdistance=self.x-xdest
        else:
            xdistance=0
        if ydest>self.y:
            ydistance=ydest-self.y
        elif ydest<self.y:
            ydistance=self.y-ydest
        else:
            ydistance=0
        totaldistance=(ydistance**2+xdistance**2)**0.5
        if xdest>self.x:
            self.vx=(xdistance/totaldistance)*self.speed
        elif xdest<self.x:
            self.vx=(0-(xdistance/totaldistance))*self.speed
        else:
            self.vx=0
        if ydest>self.y:
            self.vy=(ydistance/totaldistance)*self.speed
        elif ydest<self.y:
            self.vy=(0-(ydistance/totaldistance))*self.speed
        else:
            self.vy=0
        print str(totaldistance)
        self.distanceleft=int(totaldistance)
    def move(self):
        global TreasuresRemaining
        if self.distanceleft>0 and self.ClosestTreasure.found==False:
            self.x1+=self.vx
            self.x2+=self.vx
            self.y1+=self.vy
            self.y2+=self.vy
            self.x+=self.vx
            self.y+=self.vy
            self.canvas.coords(self.shape,self.x1,self.y1,self.x2,self.y2)
            self.canvas.update()
            self.distanceleft-=1
            time.sleep(0.01)
        else:
            if self.ClosestTreasure.found==False:
                self.ClosestTreasure.found=True
                self.TreasuresFound.append(self.ClosestTreasure)
                self.canvas.coords(self.ClosestTreasure.name,self.TreasuresFoundPositions[self.NumberOfTreasuresFound][0],self.TreasuresFoundPositions[self.NumberOfTreasuresFound][1],self.TreasuresFoundPositions[self.NumberOfTreasuresFound][2],self.TreasuresFoundPositions[self.NumberOfTreasuresFound][3])
                self.canvas.update()
                TreasuresRemaining-=1
                self.NumberOfTreasuresFound+=1
            if TreasuresRemaining>0:
                self.closesttreasure()
                self.moveto(self.ClosestTreasure.x,self.ClosestTreasure.y)
            else:
                self.vx=0
                self.vy=0
interface = interface(level1)
interface.MaxTreasures=0
interface.MaxRobots=0
interface.treasureWindow()
level1.mainloop()    
