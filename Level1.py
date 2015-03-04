from Tkinter import *
import time
import tkMessageBox
import webbrowser

def main():
       
    level1 = Tk()
    level1.title("Level 1")
    level1.resizable(0,0)
    canvas = Canvas(level1, width = 1280, height = 720, bg = "White")
    canvas.pack()

    level1Map = canvas.create_rectangle(20, 20, 1000, 700, fill = 'white', width = 2)

    global RoboFinish,abcdefg,CoordsBank,ListofCoords,TreasuresFound,d,ScoreBank
    global NumberOfTreasures, NumberOfRobots, resetPressed, score, pausepressed, pauseCounter, ListOfRobots
    
    score = 0
    ListOfTreasures=[]
    d = 0
    ScoreBank=[]
    ListOfRobots=[]
    NumberOfTreasures=0
    NumberOfRobots=0
    ProgramActive=False
    TreasuresFound=[]
    ListofCoords = []
    CoordsBank = []
    pauseCounter=0
    abcdefg = 0
    RoboFinish = False
    pausepressed=False
    
    def sortAnimation():
        global d
        for i in ListOfRobots:
            canvas.delete(i.shape)
        for i in TreasuresFound:
            if i.type == "Triangle":
                canvas.coords(i.name,CoordsBank[d][0]+10,CoordsBank[d][1],CoordsBank[d][0],CoordsBank[d][3],CoordsBank[d][0]+20,CoordsBank[d][3])
            else:
                canvas.coords(i.name,CoordsBank[d][0],CoordsBank[d][1],CoordsBank[d][2],CoordsBank[d][3])
                        
            d += 1
            time.sleep(0.5)                
            canvas.update()

    #Ascending`
    def mergeSortAsc(List,anotherList):
    
        if len(List) > 1:
            midMA = len(List) // 2
            lHalfMA = List[:midMA]
            rHalfMA = List[midMA:]
            amidMA = len(anotherList) // 2
            alHalfMA = anotherList[:amidMA]
            arHalfMA = anotherList[amidMA:]
    
            mergeSortAsc(lHalfMA,alHalfMA)
            mergeSortAsc(rHalfMA,arHalfMA)

            aMA = 0
            bMA = 0
            cMA = 0
            aaMA = 0
            abMA = 0
            acMA = 0
    
            while aMA < len(lHalfMA) and bMA < len(rHalfMA):
                if lHalfMA[aMA] < rHalfMA[bMA]:
                    List[cMA] = lHalfMA[aMA]                               
                    aMA += 1
                    anotherList[acMA] = alHalfMA[aaMA]                               
                    aaMA += 1
                    iteration += 1
                    
                else:
                    List[cMA] = rHalfMA[bMA]
                    bMA += 1
                    anotherList[acMA] = arHalfMA[abMA]
                    abMA += 1
                    iteration += 1
                cMA += 1
                acMA += 1
    
            while aMA < len(lHalfMA):
                List[cMA] = lHalfMA[aMA]
                aMA += 1
                cMA += 1
                anotherList[acMA] = alHalfMA[aaMA]
                aaMA += 1
                acMA += 1
                iteration += 1
    
            while bMA < len(rHalfMA):
                List[cMA] = rHalfMA[bMA]
                bMA += 1
                cMA += 1
                anotherList[acMA] = arHalfMA[abMA]
                abMA += 1
                acMA += 1
                iteration += 1
                
        if iteration == len(TreasuresFound):
            sortAnimation()

    #Descending 
    def mergeSortDes(List,anotherList):
        iteration = 0
        
        if len(List) > 1:
            midMD = len(List) // 2
            lHalfMD = List[:midMD]
            rHalfMD = List[midMD:]
            amidMD = len(anotherList) // 2
            alHalfMD = anotherList[:amidMD]
            arHalfMD = anotherList[amidMD:]
    
            mergeSortDes(lHalfMD,alHalfMD)
            mergeSortDes(rHalfMD,arHalfMD)

            aMD = 0
            bMD = 0
            cMD = 0
            aaMD = 0
            abMD = 0
            acMD = 0
    
            while aMD < len(lHalfMD) and bMD < len(rHalfMD):
                if lHalfMD[aMD] > rHalfMD[bMD]:
                    List[cMD] = lHalfMD[aMD]                               
                    aMD += 1
                    anotherList[acMD] = alHalfMD[aaMD]                               
                    aaMD += 1
                    iteration += 1

                else:
                    List[cMD] = rHalfMD[bMD]
                    bMD += 1
                    anotherList[acMD] = arHalfMD[abMD]
                    abMD += 1
                    iteration += 1

                cMD += 1
                acMD += 1
    
            while aMD < len(lHalfMD):
                List[cMD] = lHalfMD[aMD]
                aMD += 1
                cMD += 1
                anotherList[acMD] = alHalfMD[aaMD]
                aaMD += 1
                acMD += 1
                iteration += 1

    
            while bMD < len(rHalfMD):
                List[cMD] = rHalfMD[bMD]
                bMD += 1
                cMD += 1
                anotherList[acMD] = arHalfMD[abMD]
                abMD += 1
                acMD += 1
                iteration += 1

        if iteration == len(TreasuresFound):
            sortAnimation()

    def mergeSortAsc(List, anotherList):
        iteration = 0
        
        if len(List) > 1:
            midMA = len(List) // 2
            lHalfMA = List[:midMA]
            rHalfMA = List[midMA:]
            amidMA = len(anotherList) // 2
            alHalfMA = anotherList[:amidMA]
            arHalfMA = anotherList[amidMA:]
        
            mergeSortAsc(lHalfMA,alHalfMA)
            mergeSortAsc(rHalfMA,arHalfMA)
    
            aMA = 0
            bMA = 0
            cMA = 0
            aaMA = 0
            abMA = 0
            acMA = 0
    
            while aMA < len(lHalfMA) and bMA < len(rHalfMA):
                if lHalfMA[aMA] < rHalfMA[bMA]:
                    List[cMA] = lHalfMA[aMA]                               
                    aMA += 1
                    anotherList[acMA] = alHalfMA[aaMA]                               
                    aaMA += 1
                    iteration += 1
                    
                else:
                    List[cMA] = rHalfMA[bMA]
                    bMA += 1
                    anotherList[acMA] = arHalfMA[abMA]
                    abMA += 1
                    iteration += 1

                cMA += 1
                acMA += 1
    
            while aMA < len(lHalfMA):
                List[cMA] = lHalfMA[aMA]
                aMA += 1
                cMA += 1
                anotherList[acMA] = alHalfMA[aaMA]
                aaMA += 1
                acMA += 1
                iteration += 1

    
            while bMA < len(rHalfMA):
                List[cMA] = rHalfMA[bMA]
                bMA += 1
                cMA += 1
                anotherList[acMA] = arHalfMA[abMA]
                abMA += 1
                acMA += 1
                iteration += 1
        if iteration == len(TreasuresFound):
            sortAnimation()
            
    def callback(event):
        global NumberOfTreasures
        global NumberOfRobots
        global TreasurePromptLabel
        if NumberOfTreasures<int(interface.MaxTreasures) and ProgramActive is False:
            ListOfTreasures.append(treasures(event.x,event.y))
            NumberOfTreasures+=1
            interface.TreasurePromptLabel.place_forget()
            interface.ChangePromptLabel.place_forget()
            if NumberOfTreasures==int(interface.MaxTreasures):
                interface.robotWindow()
        elif NumberOfRobots<int(interface.MaxRobots) and ProgramActive is False:
            ListOfRobots.append(robot(event.x,event.y))
            NumberOfRobots+=1
            interface.RoboPromptLabel.place_forget()
            if NumberOfRobots==int(interface.MaxRobots):
                    interface.timerWindow()
                
    canvas.tag_bind(level1Map,"<Button-1>", callback)
    canvas.pack()

    class interface:
        global score
        def __init__(self, name):
            self.timerLabel = Label(name, text = "Timer:", width = 10, height = 2, font = ("Arial", 16), bg = "Gray")
            self.timerLabel.place(x = 1020, y = 20)
            
            self.PressStartLabel = Label(name, text = "Press Start to Begin", width = 20, height = 2, font = ("Arial", 16), bg = "White")
            self.PressStartLabel.place(x=400, y=300)

            self.minShowLabel = Label(name, text = "00", width = 5, height = 2, font = ("Arial", 16), bg = "Gray")
            self.minShowLabel.place(x = 1120, y = 20)

            self.spacerLabel = Label(name, text = ":", width = 2, height = 2, font = ("Arial", 16), bg = "Gray")
            self.spacerLabel.place(x = 1180, y = 20)

            self.secShowLabel = Label(name, text = "00", width = 5, height = 2, font = ("Arial", 16), bg = "Gray")
            self.secShowLabel.place(x = 1200, y = 20)

            self.startButton = Button(name, text = "Start", width = 20, command = self.start, font = ("Arial", 16),bg = "LightGreen")
            self.startButton.place(x = 1020, y = 80)

            self.pauseButton = Button(name, text = "Pause", width = 20, command = self.pause, font = ("Arial", 16), bg = "Yellow")

            self.helpButton = Button(name, text = "Help", width = 20, command = self.webHelp, font = ("Arial", 16), bg = "Orange")
            self.helpButton.place(x = 1020, y = 660)
            
            self.levelSelectButton = Button(name, text = "Level Select", width = 20, command = self.levelSelect, font = ("Arial", 16), bg = "LightBlue")
            self.levelSelectButton.place(x = 1020, y = 130)

            self.scoreLabel = Label(name, text = "Score", width = 10, height = 2, font = ("Arial", 16), bg = "LightGray")
            self.scoreLabel.place(x = 1020, y = 180)

            self.scoreShowLabel = Label(name, text = score, width = 10, height = 2, font = ("Arial", 16), bg = "LightGray")
            self.scoreShowLabel.place(x = 1140, y = 180)

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

        def webHelp(self):
            webbrowser.open('https://github.com/HolmesSquad/Project-Three/wiki/Level-1')

        def windowHelp(self):
            webbrowser.open('https://github.com/HolmesSquad/Project-Three/wiki/Level-1#windows')

        def timer(level1):
            global counter, resetPressed, pausepressed, pauseCounter, RoboFinish
            counter==counter
            if (counter != 0) and (pausepressed!=True) and (RoboFinish!=True):
                counter=counter-1
                print RoboFinish
                interface.minuteConvert()
                level1.secShowLabel.after(1000, level1.timer)
            elif (pausepressed==True):
                pauseCounter=counter
                print "Hello"
            else:
                RoboFinish=True
                TreasuresRemaining=0
                return False
                

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
            interface.timeEntrysec.insert(0,"1")
            interface.timeEntrysec.place(x = 130,y = 60)
            
            interface.timeEntryButton = Button(timerCanvas, text = "Start", width = 10, font = ("Arial", 10), command = interface.timerWindowGet, bg = "LightGreen")
            interface.timeEntryButton.place(x = 65, y = 170)

            interface.windowHelpButton = Button(timerCanvas, text = "?", width = 2, font = ("Arial", 10), command = interface.windowHelp, bg = "Orange")
            interface.windowHelpButton.place(x = 180, y = 170)
            
            timerCanvas.pack()
            timerWindow.grab_set() #these dont work 100% yet
            timerWindow.focus_force()
       
        def assignScoreWindow(self):
            global squareScore,circleScore,triangleScore,assignScoreWindow
            
            assignScoreWindow = Tk()
            assignScoreWindow.title("Assign Score")
            assignScoreWindow.resizable(0,0)

            assignScoreCanvas = Canvas(assignScoreWindow, width = 280, height = 200, bg = "White")

            interface.typeHeader=Label(assignScoreCanvas,text="Types",width=9,font=("Arial",10), bg="White")
            interface.typeHeader.place(x = 1, y = 15)

            interface.squareLabel=Label(assignScoreCanvas,text="Square",width=9,font=("Arial",10), bg="White")
            interface.squareLabel.place(x = 1, y = 50)

            interface.circleLabel=Label(assignScoreCanvas,text="Circle",width=9,font=("Arial",10), bg="White")
            interface.circleLabel.place(x = 1, y = 90)

            interface.triangleLabel=Label(assignScoreCanvas,text="Triangle",width=9,font=("Arial",10), bg="White")
            interface.triangleLabel.place(x = 1, y = 130)
            
            interface.pointsHeader=Label(assignScoreCanvas,text="Points",width=12,font=("Arial",10), bg="White")
            interface.pointsHeader.place(x = 110, y = 15)

            interface.squareEntry = Entry(assignScoreCanvas, text= "" , width = 20, bd = 5)
            interface.squareEntry.place(x = 110,y = 50)

            interface.circleEntry = Entry(assignScoreCanvas, text= "" , width = 20, bd = 5)
            interface.circleEntry.place(x = 110,y = 90)

            interface.triangleEntry = Entry(assignScoreCanvas, text= "" , width = 20, bd = 5)
            interface.triangleEntry.place(x = 110,y = 130)

            interface.entryButton = Button(assignScoreCanvas, text="Ok", width = 10, font = ("Arial", 10),command=interface.treasureWindow, bg = "LightGreen")
            interface.entryButton.place(x = 110, y = 170)

            interface.windowHelpButton = Button(assignScoreCanvas, text = "?", width = 2, font = ("Arial", 10), command = interface.windowHelp, bg = "Orange")
            interface.windowHelpButton.place(x = 250, y = 170)
            
            assignScoreCanvas.pack()
            
        def treasureWindow(level1):
            global treasureWindow,assignScoreWindow,squareScore,circleScore,triangleScore
            squareScore = int(interface.squareEntry.get())
            circleScore = int(interface.circleEntry.get())
            triangleScore = int(interface.triangleEntry.get())
            assignScoreWindow.destroy()
            treasureWindow = Tk()
            treasureWindow.title("Number of Treasures")
            treasureWindow.resizable(0,0)
            
            treasureCanvas = Canvas(treasureWindow, width = 210, height = 200, bg = "White")
            
            interface.treasureLabel = Label(treasureCanvas, text = "Number of Treasures (Max:15)", wraplength = 100, width = 20, font = ("Arial", 9), bg = "White")
            interface.treasureLabel.place(x = 35, y = 10)
            
            interface.treasureEntry = Entry(treasureCanvas, text= "" , width = 20, bd = 5)
            interface.treasureEntry.place(x = 45,y = 60)
            interface.treasureEntry.insert(0,"5")
            
            interface.treasureEntryButton = Button(treasureCanvas, text="Ok", width = 10, font = ("Arial", 10),command=interface.assignmaxtreasures, bg = "LightGreen")
            interface.treasureEntryButton.place(x = 65, y = 100)

            interface.windowHelpButton = Button(treasureCanvas, text = "?", width = 2, font = ("Arial", 10), command = interface.windowHelp, bg = "Orange")
            interface.windowHelpButton.place(x = 180, y = 170)
            
            treasureCanvas.pack()
            
        def assignmaxtreasures(self):
            global TreasuresRemaining
            if int(interface.treasureEntry.get())>15:
                tkMessageBox.showinfo("Error","No more than fifteen treasures can be created")
            elif int(interface.treasureEntry.get())<2:
                tkMessageBox.showinfo("Error","Enter more treasure!")
            else:
                self.MaxTreasures=interface.treasureEntry.get()
                TreasuresRemaining=int(self.MaxTreasures)
                treasureWindow.destroy()
                self.TreasurePromptLabel = Label(text = "Click anywhere to place a treasure", width = 30, height = 2, font = ("Arial", 16), bg = "White")
                self.TreasurePromptLabel.place(x=350, y=300)

        def robotWindow(level1):
            global robotWindow, timerWindow
            robotWindow = Tk()
            robotWindow.title("Number of Robots")
            robotWindow.resizable(0,0)
            
            robotCanvas = Canvas(robotWindow, width = 210, height = 200, bg = "White")
            
            interface.robot_label = Label(robotCanvas, text = "Number of Robots (Max: 2)", wraplength = 100, width = 20, font = ("Arial", 9), bg = "White")
            interface.robot_label.place(x = 35, y = 10)
            
            interface.robotEntry = Entry(robotCanvas, text= "" , width = 20, bd = 5)
            interface.robotEntry.place(x = 45,y = 60)
            interface.robotEntry.insert(0,"1")
            
            interface.robotEntryButton = Button(robotCanvas, text="Ok", width = 10, font = ("Arial", 10),command=interface.assignmaxrobots, bg = "LightGreen")
            interface.robotEntryButton.place(x = 65, y = 100)

            interface.windowHelpButton = Button(robotCanvas, text = "?", width = 2, font = ("Arial", 10), command = interface.windowHelp, bg = "Orange")
            interface.windowHelpButton.place(x = 180, y = 170)
            
            robotCanvas.pack()
            interface.w.place_forget()
            
        def assignmaxrobots(self):
            if int(interface.robotEntry.get())>1:
                print "No more than two robots can be created"
            elif int(interface.robotEntry.get())<1:
                print "No more than one robots can be created"
            else:
            
                self.MaxRobots=interface.robotEntry.get()
                robotWindow.destroy()
                self.RoboPromptLabel = Label(text = "Click anywhere to place a robot", width = 30, height = 2, font = ("Arial", 16), bg = "White")
                self.RoboPromptLabel.place(x=350, y=300)

        def start(self):
            self.assignScoreWindow()
            interface.startButton.place_forget()
            interface.pauseButton.place(x = 1020, y = 80)
            self.w.place(x = 1020, y = 550)
            self.PressStartLabel.place_forget()
            self.ChangePromptLabel = Label(text="Use this Dropdown Menu to change Treasure -->", width = 40,height = 2, font = ("Arial", 16), bg = "white")
            self.ChangePromptLabel.place(x=510, y= 540)
            
        def timerWindowGet(self):
            global counter, timerWindow
            if (interface.timeEntrysec.get())=="" or (((interface.timeEntrysec.get())=="0") and ((interface.timeEntrymin.get())=="0")):
                counter=0
            else:
                counter=int(interface.timeEntrysec.get())
                counter=counter+((int(interface.timeEntrymin.get())*60))
                interface.timerShow(interface)
                timerWindow.destroy()
            ListOfRobots[0].TreasuresFoundPositions=[[1025,390,1045,410],[1055,390,1075,410],[1085,390,1105,410],[1115,390,1135,410],[1145,390,1165,410],[1175,390,1195,410],[1205,390,1225,410],[1235,390,1255,410],[1025,420,1045,440],[1055,420,1075,440],[1085,420,1105,440],[1115,420,1135,440],[1145,420,1165,440],[1175,420,1195,440],[1205,420,1225,440]]
            if NumberOfRobots==2:
                ListOfRobots[1].TreasuresFoundPositions=[[1025,490,1045,510],[1055,490,1075,510],[1085,490,1105,510],[1115,490,1135,510],[1145,490,1165,510],[1175,490,1195,510],[1205,490,1225,510],[1235,490,1255,510],[1025,520,1045,540],[1055,520,1075,540],[1085,520,1105,540],[1115,520,1135,540],[1145,520,1165,540],[1175,520,1195,540],[1205,520,1225,540]]
            interface.pauseButton['state']='normal'
            for robot in ListOfRobots:
                robot.closesttreasure()
                robot.moveto(robot.ClosestTreasure.x,robot.ClosestTreasure.y)
            self.initiateMovement()

        def initiateMovement(self):
            while TreasuresRemaining>0:
                if pausepressed==False:
                    for robot in ListOfRobots:
                        robot.move()
                else:
                    break

        def pause(self):
            global counter, pausepressed, pauseCounter
            if pausepressed==False:
                pausepressed=True
            else:
                pausepressed=False
                counter=pauseCounter
                interface.timer()
                self.initiateMovement()

        def sortByWindow(self):
            global sortByWindow
            sortByWindow = Tk()
            sortByWindow.title("Sort By")
            sortByWindow.resizable(0,0)

            sortByCanvas = Canvas(sortByWindow, width = 200, height = 100, bg = "White")

            interface.sortByAscendingButton = Button(sortByCanvas, text = "Ascending", width = 20, font = ("Arial", 10), command = self.sortAsc , bg = "LightBlue")
            interface.sortByAscendingButton.place (x = 20, y = 20)

            interface.sortByDescendingButton = Button(sortByCanvas, text = "Descending", width = 20, font = ("Arial", 10), command = self.sortDes , bg = "LightGreen")
            interface.sortByDescendingButton.place(x = 20, y = 60)

            interface.windowHelpButton = Button(sortByCanvas, text = "?", width = 2, font = ("Arial", 10), command = interface.windowHelp, bg = "Orange")
            interface.windowHelpButton.place(x = 180, y = 170)
            
            sortByCanvas.pack()

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

        def sortAsc(self):
            global sortByWindow
            mergeSortAsc(ScoreBank,TreasuresFound)
            sortByWindow.destroy()
            
        def sortDes(self):
            global sortByWindow
            mergeSortDes(ScoreBank,TreasuresFound)
            sortByWindow.destroy()
                   
        def levelSelectLevel1(self):
            global levelWindow
            levelWindow.destroy()
            level1.destroy()
            import Level1
            Level1.main()

        def levelSelectLevel2(self):
            global levelWindow
            levelWindow.destroy()
            level1.destroy()
            import Level2
            Level2.main()

        def levelSelectLevel3(self):
            global levelWindow
            levelWindow.destroy()
            level1.destroy()
            import Level3
            Level3.main()

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
                self.score=squareScore
                self.colour='Blue'
            elif self.type=="Circle":
                self.name=canvas.create_oval(self.x-10,self.y-10,self.x+10,self.y+10,fill='yellow')
                self.score=circleScore
                self.colour='Yellow'
            elif self.type=="Triangle":
                self.name=canvas.create_polygon(self.x,self.y-10,self.x-10,self.y+10,self.x+10,self.y+10,fill='green')
                self.score=triangleScore
                self.colour='Green'
            self.ShapeLabel = Label(level1, text = "Shape = "+self.type, bg = "White", font = ("Arial", 10))
            self.ColourLabel = Label(level1, text = "Colour = "+self.colour, bg = "White", font = ("Arial", 10))
            self.ScoreLabel = Label(level1, text = "Score = "+str(self.score), bg = "White", font = ("Arial", 10))
            canvas.tag_bind(self.name,"<Enter>", self.MouseRollover)
            canvas.tag_bind(self.name, "<Leave>", self.MouseOff)
        def showLabels(self):
            self.x1,self.y1,self.x2,self.y2=self.canvas.coords(self.name)
            self.x=self.x1-60
            self.y=self.y2+25
            self.ShapeLabel = Label(level1, text = "Shape = "+self.type, bg = "White", font = ("Arial", 10))
            self.ColourLabel = Label(level1, text = "Colour = "+self.colour, bg = "White", font = ("Arial", 10))
            self.ScoreLabel = Label(level1, text = "Score = "+str(self.score), bg = "White", font = ("Arial", 10))   
            
        def MouseRollover(self,level1):
            if self.ShapeLabel != None and self.ColourLabel != None and self.ScoreLabel != None:
                self.ShapeLabel.place(x = self.x + 20, y = self.y - 20)
                self.ColourLabel.place(x = self.x + 20, y = self.y)
                self.ScoreLabel.place(x = self.x + 20, y = self.y+20)

        def MouseOff(self,level1):
            if self.ShapeLabel != None and self.ColourLabel != None and self.ScoreLabel != None:
                self.ShapeLabel.place_forget()
                self.ColourLabel.place_forget()
                self.ScoreLabel.place_forget()

        def destroylabels(self):
            self.ShapeLabel = None
            self.ColourLabel = None
            self.ScoreLabel = None

    class robot:
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
            self.distanceleft=int(totaldistance)

        def stopMoving(self):
            global TreasuresRemaining,RoboFinish,abcdefg,CoordsBank,ListofCoords, counter
            global d,ListOfRobots,TreasuresFound,score
            TreasuresRemaining=0
            self.distanceleft=0
            self.ClosestTreasure.found=True
            self.vx=0
            self.vy=0
            print "Helloooo"
            interface.sortByWindow()
                    
            return 0

        def move(self):
            global TreasuresRemaining,RoboFinish,abcdefg,CoordsBank,ListofCoords, counter
            global d,ListOfRobots,TreasuresFound,score
            if self.distanceleft>0 and self.ClosestTreasure.found==False and RoboFinish==False:
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
            elif (RoboFinish!=False):
                print ("hello")
                self.stopMoving()
            
            else:
                if self.ClosestTreasure.found==False and RoboFinish==False:
                    self.ClosestTreasure.found=True
                    TreasuresFound.append(self.ClosestTreasure)
                    self.canvas.coords(self.ClosestTreasure.name,self.TreasuresFoundPositions[self.NumberOfTreasuresFound][0],self.TreasuresFoundPositions[self.NumberOfTreasuresFound][1],self.TreasuresFoundPositions[self.NumberOfTreasuresFound][2],self.TreasuresFoundPositions[self.NumberOfTreasuresFound][3])
                    self.canvas.update()
                    score += self.ClosestTreasure.score
                    interface.scoreShowLabel.config(text = score)
                    ScoreBank.append(self.ClosestTreasure.score)
                    ListofCoords = ([250,40,270,60],[280,40,300,60],[310,40,330,60],[340,40,360,60],[370,40,390,60],[400,40,420,60],[430,40,450,60],[460,40,480,60],[490,40,510,60],[520,40,540,60],[550,40,570,60],[580,40,600,60],[610,40,630,60],[640,40,660,60],[670,40,690,60])
                    CoordsBank.append(ListofCoords[abcdefg])
                    abcdefg += 1
                    self.ClosestTreasure.MouseOff(level1)
                    self.ClosestTreasure.destroylabels()
                    #self.TreasuresFound.append(self.ClosestTreasure)
               
                    
                    if self.ClosestTreasure.type=="Triangle":
                        self.canvas.coords(self.ClosestTreasure.name,self.TreasuresFoundPositions[self.NumberOfTreasuresFound][0]+10,self.TreasuresFoundPositions[self.NumberOfTreasuresFound][1],self.TreasuresFoundPositions[self.NumberOfTreasuresFound][0],self.TreasuresFoundPositions[self.NumberOfTreasuresFound][3],self.TreasuresFoundPositions[self.NumberOfTreasuresFound][0]+20,self.TreasuresFoundPositions[self.NumberOfTreasuresFound][3])
                    else:
                        self.canvas.coords(self.ClosestTreasure.name,self.TreasuresFoundPositions[self.NumberOfTreasuresFound][0],self.TreasuresFoundPositions[self.NumberOfTreasuresFound][1],self.TreasuresFoundPositions[self.NumberOfTreasuresFound][2],self.TreasuresFoundPositions[self.NumberOfTreasuresFound][3])
                    self.canvas.update()
                    TreasuresRemaining-=1
                    self.NumberOfTreasuresFound+=1
                if TreasuresRemaining>0:
                    self.closesttreasure()
                    self.moveto(self.ClosestTreasure.x,self.ClosestTreasure.y)
                else:
                    RoboFinish=True
                    interface.sortByWindow()
                
                    

    interface = interface(level1)
    level1.mainloop()
    
main()
