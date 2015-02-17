from Tkinter import *
level1 = Tk()
level1.title("Level 1")
level1.resizable(0,0)
canvas = Canvas(level1, width = 1280, height = 720, bg = "White")
canvas.pack()

level1Map = canvas.create_rectangle(20, 20, 1000, 700, fill = 'white', width = 2) 

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
        
        self.levelSelectButton = Button(name, text = "Level Select", width = 20, command = self.levelSelect, font = ("Arial", 16), bg = "LightBlue")
        self.levelSelectButton.place(x = 1020, y = 180)

        self.scoreLabel = Label(name, text = "Score", width = 10, height = 2, font = ("Arial", 16), bg = "LightGray")
        self.scoreLabel.place(x = 1020, y = 240)

        self.scoreShowLabel = Label(name, text = "000", width = 10, height = 2, font = ("Arial", 16), bg = "LightGray")
        self.scoreShowLabel.place(x = 1140, y = 240)

        self.treasureCollectedLabel = Label(name, text = "Treasure Collected", width = 20, height = 1, font = ("Arial", 16), bg = "LightGray")
        self.treasureCollectedLabel.place(x = 1020, y = 300)

        self.treasureBackgroundLabel = Label(name, width = 20, height = 8, font = ("Arial", 16), bg = "LightGray")
        self.treasureBackgroundLabel.place(x = 1020, y = 330)

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
        timerWindow.grab_set() #these dont work 100% yet
        timerWindow.focus_force()

    def start(self):
        self.timerWindow()
        interface.startButton.place_forget()
        interface.pauseButton.place(x = 1020, y = 80)
        
    def timerWindowGet(level1):
        global counter, timerWindow
        if (interface.timeEntrysec.get())=="" or (((interface.timeEntrysec.get())=="0") and ((interface.timeEntrymin.get())=="0")):
            counter=0
    
        else:
            counter=int(interface.timeEntrysec.get())
            counter=counter+((int(interface.timeEntrymin.get())*60))
            interface.timerShow(interface)
            timerWindow.destroy()
        
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


interface = interface(level1)

level1.mainloop()    
