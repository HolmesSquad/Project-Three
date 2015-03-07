from Tkinter import *
import tkMessageBox
import time
import random
import webbrowser

def main():
    level3 = Tk()
    level3.title("Level 3")
    level3.resizable(0,0)
    canvas = Canvas(level3, width = 1280, height = 720, bg = "White")
    canvas.pack()
    
    global roboFinished,abcdefg,CoordsBank,ListofCoords,TreasuresFound,d,ScoreBank, ClosestTreasure
    global NumberOfTreasures, NumberOfRobots, resetPressed, score, pausepressed, pauseCounter
    
    score = 0
    d = 0
    ScoreBank=[]
    global ListOfRobots
    ListOfRobots=[]
    NumberOfTreasures=0
    NumberOfRobots=0
    ProgramActive=False
    TreasuresFound=[]
    ListofCoords = []
    CoordsBank = []
    pauseCounter=0
    abcdefg = 0
    roboFinished = False
    d=0
    ListOfTreasures=[]
    ListOfRobots=[]
    NumberOfTreasures=0
    NumberOfRobots=0
    ProgramActive=False
    pausepressed=False
    ListOfTraps=[]
    level3Map = canvas.create_rectangle(20, 20, 1000, 700, fill = 'white', width = 2)

    def sortAnimation():
        global d
        for i in ListOfRobots:
            canvas.delete(i.shape)
        for i in ListOfTreasures:
            if i.x < 1000:
                canvas.delete(i.name)
        for i in ListOfTraps:
            canvas.delete(i.name)
        for i in TreasuresFound:
            if i.type == "Triangle":
                canvas.coords(i.name,CoordsBank[d][0]+10,CoordsBank[d][1],CoordsBank[d][0],CoordsBank[d][3],CoordsBank[d][0]+20,CoordsBank[d][3])
            else:
                canvas.coords(i.name,CoordsBank[d][0],CoordsBank[d][1],CoordsBank[d][2],CoordsBank[d][3])
                        
            d += 1
            time.sleep(0.5)                
            canvas.update()

    #Descending 
    def mergeSortDes(List,anotherList):
        iteration = 0
        if len(List) > 1:
            print len(anotherList)
            print iteration
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
                print len(anotherList)
                print iteration
                if lHalfMD[aMD] > rHalfMD[bMD]:
                    List[cMD] = lHalfMD[aMD]                               
                    aMD += 1
                    anotherList[acMD] = alHalfMD[aaMD]                               
                    aaMD += 1
                    iteration += 1
                else:
                    print len(anotherList)
                    print iteration
                    List[cMD] = rHalfMD[bMD]
                    bMD += 1
                    anotherList[acMD] = arHalfMD[abMD]
                    abMD += 1
                    iteration += 1

                cMD += 1
                acMD += 1
    
            while aMD < len(lHalfMD):
                print len(anotherList)
                print iteration
                List[cMD] = lHalfMD[aMD]
                aMD += 1
                cMD += 1
                anotherList[acMD] = alHalfMD[aaMD]
                aaMD += 1
                acMD += 1
                iteration += 1

            while bMD < len(rHalfMD):
                print len(anotherList)
                print iteration
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
        print ScoreBank
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
                print len(anotherList)
                print iteration
                if lHalfMA[aMA] < rHalfMA[bMA]:
                    List[cMA] = lHalfMA[aMA]                               
                    aMA += 1
                    anotherList[acMA] = alHalfMA[aaMA]                               
                    aaMA += 1
                    iteration += 1
                else:
                    print len(anotherList)
                    print iteration
                    List[cMA] = rHalfMA[bMA]
                    bMA += 1
                    anotherList[acMA] = arHalfMA[abMA]
                    abMA += 1
                    iteration += 1

                cMA += 1
                acMA += 1
    
            while aMA < len(lHalfMA):
                print len(anotherList)
                print iteration
                List[cMA] = lHalfMA[aMA]
                aMA += 1
                cMA += 1
                anotherList[acMA] = alHalfMA[aaMA]
                aaMA += 1
                acMA += 1
                iteration += 1
                
            while bMA < len(rHalfMA):
                print len(anotherList)
                print iteration
                List[cMA] = rHalfMA[bMA]
                bMA += 1
                cMA += 1
                anotherList[acMA] = arHalfMA[abMA]
                abMA += 1
                acMA += 1
                iteration += 1
        
            if iteration == len(TreasuresFound):
                print ScoreBank
                sortAnimation()
    
    def callback(event):
        global NumberOfTreasures
        global NumberOfRobots
        if NumberOfTreasures<int(interface.MaxTreasures) and ProgramActive is False:
            ListOfTreasures.append(treasures(event.x,event.y))
            NumberOfTreasures+=1
            interface.TreasurePromptLabel.place_forget()
            interface.ChangePromptLabel.place_forget()
            print interface.MaxTreasures
            print NumberOfTreasures
            if NumberOfTreasures==int(interface.MaxTreasures):
                interface.robotWindow()
        elif NumberOfRobots<int(interface.MaxRobots) and ProgramActive is False:
            ListOfRobots.append(robots(event.x,event.y))
            NumberOfRobots+=1
            if NumberOfRobots==int(interface.MaxRobots):
                    interface.wishlistWindow()
                
    canvas.tag_bind(level3Map,"<Button-1>", callback)
    canvas.pack()
    
    class interface:
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

            self.startButton = Button(name, text = "Start", width = 20, command = self.start, font = ("Arial", 16), bg = "LightGreen")
            self.startButton.place(x = 1020, y = 80)

            self.pauseButton = Button(name, text = "Pause", width = 20, command = self.pause, font = ("Arial", 16), bg = "Yellow")

            self.helpButton = Button(name, text = "Help", width = 20, command = self.webHelp, font = ("Arial", 16), bg = "Orange")
            self.helpButton.place(x = 1020, y = 660)
            
            self.levelSelectButton = Button(name, text = "Level Select", width = 20, command = self.levelSelect, font = ("Arial", 16), bg = "LightBlue")
            self.levelSelectButton.place(x = 1020, y = 130)

            self.scoreLabel = Label(name, text = "Score", width = 10, height = 2, font = ("Arial", 16), bg = "LightGray")
            self.scoreLabel.place(x = 1020, y = 180)

            self.scoreShowLabel = Label(name, text = "000", width = 10, height = 2, font = ("Arial", 16), bg = "LightGray")
            self.scoreShowLabel.place(x = 1140, y = 180)

            self.treasureCollectedLabel = Label(name, text = "Treasure Collected", width = 22, height = 1, font = ("Arial", 14), bg = "LightGray")
            self.treasureCollectedLabel.place(x = 1020, y = 350)
            
            #Create DropDown List for selecting which type of treasure to create
            self.OPTIONS = [
                "Rectangle",
                "Circle",
                "Triangle"
            ]

            self.variable = StringVar(level3)
            self.variable.set(self.OPTIONS[0]) # default value

            self.w = apply(OptionMenu, (level3, self.variable) + tuple(self.OPTIONS))

        def webHelp(self):
            webbrowser.open('https://github.com/HolmesSquad/Project-Three/wiki/Level-3')

        def windowHelp(self):
            webbrowser.open('https://github.com/HolmesSquad/Project-Three/wiki/Level-3#windows')

        def timer(level3):
             global counter, resetPressed, pausepressed ,pauseCounter, roboFinished
             counter==counter
             if (counter != 0) and (pausepressed!=True) and (roboFinished!=True):
                counter=counter-1
                interface.minuteConvert()
                level3.secShowLabel.after(1000, level3.timer)
             elif (pausepressed==True):
                 pauseCounter=counter
             else:
                return 1

        def timerShow(level3,self):
            global counter, RoboFinished
            RoboFinished=False
            interface.timer()   

        def minuteConvert(level3):
            level3.secShowLabel.config(text = str(counter%60))
            level3.minShowLabel.config(text = str(counter//60))

        def timerWindow(level3):
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
            interface.timeEntrymin.insert(1,"1")
            interface.timeEntrymin.place(x = 30,y = 60)
            
            interface.timeEntrysec = Entry(timerCanvas, text = "" , width = 8, bd = 5)
            interface.timeEntrysec.insert(0,"0")
            interface.timeEntrysec.place(x = 130,y = 60)
            
            interface.timeEntryButton = Button(timerCanvas, text = "Start", width = 10, font = ("Arial", 10), command = interface.timerWindowGet, bg = "LightGreen")
            interface.timeEntryButton.place(x = 65, y = 170)

            interface.windowHelpButton = Button(timerCanvas, text = "?", width = 2, font = ("Arial", 10), command = interface.windowHelp, bg = "Orange")
            interface.windowHelpButton.place(x = 180, y = 170)
            
            timerCanvas.pack()
            wishlistWindow.destroy()

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
            interface.squareEntry.insert(50,"50")
            interface.squareEntry.place(x = 110,y = 50)

            interface.circleEntry = Entry(assignScoreCanvas, text= "" , width = 20, bd = 5)
            interface.circleEntry.insert(75,"75")
            interface.circleEntry.place(x = 110,y = 90)

            interface.triangleEntry = Entry(assignScoreCanvas, text= "" , width = 20, bd = 5)
            interface.triangleEntry.insert(100,"100")
            interface.triangleEntry.place(x = 110,y = 130)

            interface.entryButton = Button(assignScoreCanvas, text="Ok", width = 10, font = ("Arial", 10),command=interface.treasureWindow, bg = "LightGreen")
            interface.entryButton.place(x = 110, y = 170)

            interface.windowHelpButton = Button(assignScoreCanvas, text = "?", width = 2, font = ("Arial", 10), command = interface.windowHelp, bg = "Orange")
            interface.windowHelpButton.place(x = 250, y = 170)
            
            assignScoreCanvas.pack()

        def timerWindowGet(self):
            global counter, timerWindow
            if (interface.timeEntrysec.get())=="" or (((interface.timeEntrysec.get())=="0") and ((interface.timeEntrymin.get())=="0")):
                counter=0
            elif (int(interface.timeEntrysec.get())>0) and (int((interface.timeEntrymin.get())=="0") or (interface.timeEntrymin.get())==""):
                counter=int(interface.timeEntrysec.get())
                interface.timerShow(interface)
                print "Run this 2"
                timerWindow.destroy()
            elif (int((interface.timeEntrysec.get())=="")):
                counter=((int(interface.timeEntrymin.get())*60))
                interface.timerShow(interface)
                print "Run this 3"
                timerWindow.destroy()
            else:
                counter=int(interface.timeEntrysec.get())
                counter=counter+((int(interface.timeEntrymin.get())*60))
                interface.timerShow(interface)
                print "Run this"
                timerWindow.destroy()
            Createtrap()
            ListOfRobots[0].TreasuresFoundPositions=[[1025,390,1045,410],[1055,390,1075,410],[1085,390,1105,410],[1115,390,1135,410],[1145,390,1165,410],[1175,390,1195,410],[1205,390,1225,410],[1235,390,1255,410],[1025,420,1045,440],[1055,420,1075,440]]
            if NumberOfRobots==2:
                ListOfRobots[1].TreasuresFoundPositions=[[1025,490,1045,510],[1055,490,1075,510],[1085,490,1105,510],[1115,490,1135,510],[1145,490,1165,510],[1175,490,1195,510],[1205,490,1225,510],[1235,490,1255,510],[1025,520,1045,540],[1055,520,1075,540]]
            interface.pauseButton['state']='normal'
            for robot in ListOfRobots:
                robot.closesttreasure()
                robot.moveto(robot.ClosestTreasure.x,robot.ClosestTreasure.y)
            self.initiateMovement()
            
        def initiateMovement(self):
            while ListOfRobots[0].squareswishlist>0 or ListOfRobots[0].triangleswishlist>0 or ListOfRobots[0].circleswishlist>0:
                if pausepressed==False:
                    for robot in ListOfRobots:
                        robot.move()
                else:
                    break
                
        def wishlistWindow(self):
            global wishlistWindow, timerWindow
            wishlistWindow = Tk()
            wishlistWindow.title("Wishlist")
            wishlistWindow.resizable(0,0)

            wishlistCanvas = Canvas(wishlistWindow, width = 210, height = 280, bg = "White")

            interface.wishlistEntryButton = Button(wishlistCanvas, text = "Ok", width = 10, font = ("Arial", 10), command = interface.wishlistChecker, bg = "LightGreen")
            interface.wishlistEntryButton.place(x = 60, y = 250)

            interface.wishlistEntryLabel = Label(wishlistCanvas, text = "Please select your desired items", width = 24, font = ("Arial", 10),  bg = "White")
            interface.wishlistEntryLabel.place(x = 10, y = 10)

            interface.c1=Label(wishlistWindow,text="Square  ",font = ("Arial", 10),height=1,width=11, bg="White")
            interface.c1.place(x=110,y=65)

            interface.c2=Label(wishlistWindow,text="Triangle",font = ("Arial", 10),height=1,width=11, bg="White")
            interface.c2.place(x=110,y=100)

            interface.c3=Label(wishlistWindow,text="Circle    ",font = ("Arial", 10),height=1,width=11, bg="White")
            interface.c3.place(x=110,y=135)

            interface.wishlistQuantityLabel=Label(wishlistCanvas,text="Quantity",width=9,font=("Arial",10), bg="White")
            interface.wishlistQuantityLabel.place(x = 1, y = 38)

            interface.wishlistShapeLabel=Label(wishlistCanvas,text="Objects",width=12,font=("Arial",10), bg="White")
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

            interface.trapLabel=Label(wishlistCanvas,text="Please enter the number of traps     (Max: 100)",wraplength = 100,width=24,font=("Arial",10), bg="White")
            interface.trapLabel.place(x = 10, y = 155)

            interface.trapQuantity = Entry(wishlistCanvas, text = "" , width = 8, bd = 5)
            interface.trapQuantity.insert(0,"10")
            interface.trapQuantity.place(x = 80,y = 210)

            interface.windowHelpButton = Button(wishlistCanvas, text = "?", width = 2, font = ("Arial", 10), command = interface.windowHelp, bg = "Orange")
            interface.windowHelpButton.place(x = 180, y = 250)
            
            wishlistCanvas.pack()
            
        def wishlistChecker(self):
            global trapNum
            if ((interface.squareQuantity.get())=="0" and ((interface.triangleQuantity.get())=="0") and ((interface.circleQuantity.get())=="0")) or ((interface.squareQuantity.get())=="" and ((interface.triangleQuantity.get())=="") and ((interface.circleQuantity.get())=="")) :
                return 1 #returns 1 if no value is entered in wishlist
            elif ((interface.c1==0) and (interface.c2==0) and (interface.c3==0)):
                return 2 #returns 2 if no objects are selected
            elif ((interface.c1==1) and ((interface.squareQuantity.get())=="0") or (interface.squareQuantity.get())==""):
                return 3 #returns 3 if squares are selected but no value input
            elif ((interface.c2==1) and ((interface.triangleQuantity.get())=="0") or (interface.triangleQuantity.get())==""):
                return 4 #returns 4 if triangles are selected but no value input
            elif ((interface.c3==1) and ((interface.circleQuantity.get())=="0") or (interface.circleQuantity.get())==""):
                return 5 #returns 5 if circles are selected but no value input
            elif ((interface.c1==1) and (interface.c2==1) and (interface.c2==1)):
                return 6 #returns 6 if no objects are selected
            elif (int((interface.squareQuantity.get())<"0")) or int((interface.triangleQuantity.get())<"0") or (int((interface.circleQuantity.get())<"0")):
                return 7 #returns 7 if a negative value is entered
            elif int(interface.trapQuantity.get()) > 100:
                tkMessageBox.showinfo("Error", "Please enter less than 100 traps")
            else: #continues the program if there are no errors
                ListOfRobots[0].squareswishlist=int(interface.squareQuantity.get())
                ListOfRobots[0].triangleswishlist=int(interface.triangleQuantity.get())
                ListOfRobots[0].circleswishlist=int(interface.circleQuantity.get())
                trapNum=int(interface.trapQuantity.get())
               #print trapNum
                self.timerWindow()
            
        def start(self):
            self.assignScoreWindow()
            interface.startButton.place_forget()
            interface.pauseButton.place(x = 1020, y = 80)
            self.PressStartLabel.place_forget()
            
        def treasureWindow(level3):
            global treasureWindow,assignScoreWindow,squareScore,circleScore,triangleScore
            squareScore = int(interface.squareEntry.get())
            circleScore = int(interface.circleEntry.get())
            triangleScore = int(interface.triangleEntry.get())
            interface.w.place(x = 1020, y = 550)
            interface.ChangePromptLabel = Label(text="Use this Dropdown Menu to change Treasure -->", width = 40,height = 2, font = ("Arial", 16), bg = "white")
            interface.ChangePromptLabel.place(x=510, y= 540)
            assignScoreWindow.destroy()
            treasureWindow = Tk()
            treasureWindow.title("Number of Treasures")
            treasureWindow.resizable(0,0)
            
            treasureCanvas = Canvas(treasureWindow, width = 210, height = 200, bg = "White")
            
            interface.treasure_label = Label(treasureCanvas, text = "Number of Treasures (Max:10)", wraplength = 100, width = 20, font = ("Arial", 9), bg = "White")
            interface.treasure_label.place(x = 35, y = 10)
            
            interface.treasureEntry = Entry(treasureCanvas, text= "" , width = 20, bd = 5)
            interface.treasureEntry.insert(2,"2")
            interface.treasureEntry.place(x = 45,y = 60)
            
            interface.treasureEntryButton = Button(treasureCanvas, text="Ok", width = 10, font = ("Arial", 10),command=interface.assignmaxtreasures, bg = "LightGreen")
            interface.treasureEntryButton.place(x = 65, y = 100)

            interface.windowHelpButton = Button(treasureCanvas, text = "?", width = 2, font = ("Arial", 10), command = interface.windowHelp, bg = "Orange")
            interface.windowHelpButton.place(x = 180, y = 170)
            
            treasureCanvas.pack()
            
        def assignmaxtreasures(self):
            global TreasuresRemaining
            if int(interface.treasureEntry.get())>10:
                tkMessageBox.showinfo("Error","No more than ten treasures can be created")
            elif int(interface.treasureEntry.get())<2:
                tkMessageBox.showinfo("Error","Please enter 2 or more treasures")
            else:
                self.MaxTreasures=interface.treasureEntry.get()
                TreasuresRemaining=int(self.MaxTreasures)
                treasureWindow.destroy()
                self.TreasurePromptLabel = Label(text = "Click anywhere to place an object", width = 30, height = 2, font = ("Arial", 16), bg = "White")
                self.TreasurePromptLabel.place(x=350, y=300)

        def robotWindow(level3):
            global robotWindow, timerWindow
            robotWindow = Tk()
            robotWindow.title("Number of Robots")
            robotWindow.resizable(0,0)
            
            robotCanvas = Canvas(robotWindow, width = 210, height = 200, bg = "White")
            
            interface.robot_label = Label(robotCanvas, text = "Number of Robots (Max: 1)", wraplength = 100, width = 20, font = ("Arial", 9), bg = "White")
            interface.robot_label.place(x = 35, y = 10)
            
            interface.robotEntry = Entry(robotCanvas, text= "" , width = 20, bd = 5)
            interface.robotEntry.insert(1,"1")
            interface.robotEntry.place(x = 45,y = 60)
            
            interface.robotEntryButton = Button(robotCanvas, text="Ok", width = 10, font = ("Arial", 10),command=interface.assignmaxrobots, bg = "LightGreen")
            interface.robotEntryButton.place(x = 65, y = 100)

            interface.windowHelpButton = Button(robotCanvas, text = "?", width = 2, font = ("Arial", 10), command = interface.windowHelp, bg = "Orange")
            interface.windowHelpButton.place(x = 180, y = 170)
            
            robotCanvas.pack()
            interface.w.place_forget()
            
        def assignmaxrobots(self):
            if int(interface.robotEntry.get())>1:
                tkMessageBox.showinfo("Error","One robot must be created")
            elif int(interface.robotEntry.get())<1:
                tkMessageBox.showinfo("Error","Only one robot can be created")
            else:
                self.MaxRobots=interface.robotEntry.get()
                robotWindow.destroy()

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
            
            sortByCanvas.pack()

        def sortAsc(self):
            global sortByWindow
            sortByWindow.destroy()
            mergeSortAsc(ScoreBank,TreasuresFound)
            
        def sortDes(self):
            global sortByWindow
            sortByWindow.destroy()
            mergeSortDes(ScoreBank,TreasuresFound)
            
        def levelSelect(self):
            global levelWindow
            levelWindow = Tk()
            levelWindow.title("Level Select")
            levelWindow.resizable(0,0)
            
            levelCanvas = Canvas(levelWindow, width = 200, height = 180, bg = "White")
            
            interface.level1Button = Button(levelCanvas, text = "Level 1", width = 20, font = ("Arial", 10),command= self.levelSelectLevel1, bg = "LightBlue")
            interface.level1Button.place(x = 15, y = 10)
            
            interface.level2Button = Button(levelCanvas, text = "Level 2", width = 20, font = ("Arial", 10),command= self.levelSelectlevel2, bg = "LightBlue")
            interface.level2Button.place(x = 15, y = 50)
            
            interface.level3Button = Button(levelCanvas, text = "Level 3", width = 20, font = ("Arial", 10),command= self.levelSelectLevel3, bg = "LightBlue")
            interface.level3Button.place(x = 15, y = 90)
            
            interface.levelCancelButton = Button(levelCanvas, text = "Cancel", width = 10, font = ("Arial", 10),command = levelWindow.destroy , bg = "LightGray")
            interface.levelCancelButton.place(x = 50, y = 140)
            
            levelCanvas.pack()

        def levelSelectLevel1(self):
            global levelWindow
            levelWindow.destroy()
            level3.destroy()
            import Level1

        def levelSelectlevel2(self):
            global levelWindow
            levelWindow.destroy()
            level3.destroy()
            import Level2

        def levelSelectLevel3(self):
            global levelWindow
            levelWindow.destroy()
            level3.destroy()
            import Level3

    class objects:
        def __init__(self,x,y):
            self.x=x
            self.y=y

    class treasures(objects):
        global canvas
        global NumberOfTreasures
        def __init__(self,x,y):
            objects.__init__(self,x,y)
            global NumberOfTreasures
            self.type=interface.variable.get()
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
            self.ShapeLabel = Label(level3, text = "Shape = "+self.type, bg = "White", font = ("Arial", 10))
            self.ColourLabel = Label(level3, text = "Colour = "+self.colour, bg = "White", font = ("Arial", 10))
            self.WorthLabel = Label(level3, text = "Worth = "+str(self.score), bg = "White", font = ("Arial", 10))
            canvas.tag_bind(self.name,"<Enter>", self.MouseRollover)
            canvas.tag_bind(self.name, "<Leave>", self.MouseOff)
            
        def MouseRollover(self,level3):
            if self.ShapeLabel != None and self.ColourLabel != None and self.WorthLabel != None:
                self.ShapeLabel.place(x = self.x + 20, y = self.y - 20)
                self.ColourLabel.place(x = self.x + 20, y = self.y)
                self.WorthLabel.place(x = self.x + 20, y = self.y+20)

        def MouseOff(self,level3):
            if self.ShapeLabel != None and self.ColourLabel != None and self.WorthLabel != None:
                self.ShapeLabel.place_forget()
                self.ColourLabel.place_forget()
                self.WorthLabel.place_forget()

        def destroylabels(self):
            self.ShapeLabel = None
            self.ColourLabel = None
            self.WorthLabel = None

    #Function to create a trap in a random position
    def Createtrap():
        global trapNum
        while len(ListOfTraps)<trapNum:
            InvalidPosition=False
            #Assign a random x and y coordinate
            x=random.randrange(40,980)
            y=random.randrange(40,680)
            #Check that these coords are not in the same place as a robot or treasure
            for treasure in ListOfTreasures:
                if (x+10)<=(treasure.x+29) and (y+10)<=(treasure.y+29) and (y-10)>=(treasure.y-29) and (x-10)>=(treasure.x-29):
                    InvalidPosition=True
            for robot in ListOfRobots:
                if (x+10)<=(robot.x+29) and (y+10)<=(robot.y+29) and (y-10)>=(robot.y-29) and (x-10)>=(robot.x-29):
                    InvalidPosition=True
            if len(ListOfTraps)>0:
                for trap in ListOfTraps:
                    if (x+10)<=(trap.x+29) and (y+10)<=(trap.y+29) and (y-10)>=(trap.y-29) and (x-10)>=(trap.x-29):
                        InvalidPosition=True
            if InvalidPosition==False:
                ListOfTraps.append(traps(x,y))

    class traps(objects):
        def __init__(self,x,y):
            objects.__init__(self,x,y)
            self.x1=self.x-10
            self.x2=self.x+10
            self.y1=self.y-10
            self.y2=self.y+10
            self.collision=False
            self.name = canvas.create_rectangle(self.x-10,self.y-10,self.x+10,self.y+10,fill='red')

    class robots(objects):
        def __init__(self,x,y):
            objects.__init__(self,x,y)
            self.x1=self.x-10
            self.y1=self.y-10
            self.x2=self.x+10
            self.y2=self.y+10
            self.speed=1
            self.canvas=canvas
            self.shape=canvas.create_rectangle(self.x-10,self.y-10,self.x+10,self.y+10,fill='cyan')
            self.TreasuresFound=[]
            self.TreasuresFoundPositions=[]
            self.NumberOfTreasuresFound=0
            self.squareswishlist=0
            self.circleswishlist=0
            self.triangleswishlist=0
            
        def closesttreasure(self):
            lowestdistance=100000
            for i in ListOfTreasures:
                if i.found==False and ((i.type=="Triangle" and self.triangleswishlist!=0) or (i.type=="Rectangle" and self.squareswishlist!=0) or (i.type=="Circle" and self.circleswishlist!=0)):
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
            global TreasuresRemaining,roboFinish,abcdefg,CoordsBank,ListofCoords
            global d,ListOfRobots,TreasuresFound,score

            if self.distanceleft>0 and self.ClosestTreasure.found==False:
                for trap in ListOfTraps:
                    if self.x2<=trap.x2+19 and self.y2<=trap.y2+19 and self.y1>=trap.y1-19 and self.x1>=trap.x1-19:
                        if trap.collision==False:
                            trap.collision=True
                            print "Collision with trap"
                            if len(TreasuresFound)>0:
                                time.sleep(0.5)
                                self.DeletedTreasure=TreasuresFound.pop()
                                ScoreBank.pop()
                                if self.DeletedTreasure.type=="Triangle":
                                    self.triangleswishlist+=1
                                elif self.DeletedTreasure.type=="Rectangle":
                                    self.squareswishlist+=1
                                elif self.DeletedTreasure.type=="Circle":
                                    self.circleswishlist+=1
                                canvas.delete(self.DeletedTreasure.name)
                                self.NumberOfTreasuresFound-=1
                                score -= self.DeletedTreasure.score
                                interface.scoreShowLabel.config(text = score)

                    else:
                        trap.collision=False
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
                    self.ClosestTreasure.destroylabels()
                    score += self.ClosestTreasure.score
                    interface.scoreShowLabel.config(text = score)
                    TreasuresFound.append(self.ClosestTreasure)
                    ListOfTreasures.remove(self.ClosestTreasure)
                    ScoreBank.append(self.ClosestTreasure.score)
                    ListofCoords = ([250,40,270,60],[280,40,300,60],[310,40,330,60],[340,40,360,60],[370,40,390,60],[400,40,420,60],[430,40,450,60],[460,40,480,60],[490,40,510,60],[520,40,540,60],[550,40,570,60],[580,40,600,60],[610,40,630,60],[640,40,660,60],[670,40,690,60])
                    CoordsBank.append(ListofCoords[abcdefg])
                    abcdefg += 1
                    if self.ClosestTreasure.type=="Triangle":
                        self.canvas.coords(self.ClosestTreasure.name,self.TreasuresFoundPositions[self.NumberOfTreasuresFound][0]+10,self.TreasuresFoundPositions[self.NumberOfTreasuresFound][1],self.TreasuresFoundPositions[self.NumberOfTreasuresFound][0],self.TreasuresFoundPositions[self.NumberOfTreasuresFound][3],self.TreasuresFoundPositions[self.NumberOfTreasuresFound][0]+20,self.TreasuresFoundPositions[self.NumberOfTreasuresFound][3])
                        self.triangleswishlist-=1
                    elif self.ClosestTreasure.type=="Rectangle":
                        self.canvas.coords(self.ClosestTreasure.name,self.TreasuresFoundPositions[self.NumberOfTreasuresFound][0],self.TreasuresFoundPositions[self.NumberOfTreasuresFound][1],self.TreasuresFoundPositions[self.NumberOfTreasuresFound][2],self.TreasuresFoundPositions[self.NumberOfTreasuresFound][3])
                        self.squareswishlist-=1
                    elif self.ClosestTreasure.type=="Circle":
                        self.canvas.coords(self.ClosestTreasure.name,self.TreasuresFoundPositions[self.NumberOfTreasuresFound][0],self.TreasuresFoundPositions[self.NumberOfTreasuresFound][1],self.TreasuresFoundPositions[self.NumberOfTreasuresFound][2],self.TreasuresFoundPositions[self.NumberOfTreasuresFound][3])
                        self.circleswishlist-=1
                    self.canvas.update()
                    TreasuresRemaining-=1
                    self.NumberOfTreasuresFound+=1
                if TreasuresRemaining==0 or (self.squareswishlist==0 and self.circleswishlist==0 and self.triangleswishlist==0):
                    if self.squareswishlist>0 or self.circleswishlist>0 or self.triangleswishlist>0:
                        tkMessageBox.showinfo("Level Failed","Failed to find all treasures. "+str(self.squareswishlist)+" squares, "+str(self.circleswishlist)+" circles and "+str(self.triangleswishlist)+" triangles not found.")
                        self.squareswishlist=0
                        self.triangleswishlist=0
                        self.circleswishlist=0
                    self.vx=0
                    self.vy=0
                    roboFinished=True
                    interface.sortByWindow()
                else:
                    self.closesttreasure()
                    self.moveto(self.ClosestTreasure.x,self.ClosestTreasure.y)
      
    interface = interface(level3)

    level3.mainloop()
main()
