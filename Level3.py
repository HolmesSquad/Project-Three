from Tkinter import *
import tkMessageBox
level3 = Tk()
level3.title("Level 3")
level3.resizable(0,0)
canvas = Canvas(level3, width = 1280, height = 720, bg = "White")
canvas.pack()

level3Canvas = canvas.create_rectangle(20, 20, 1000, 700, fill = 'white', width = 2) 

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

        self.pauseButton = Button(name, text = "Pause", width = 20, command = self.pause, font = ("Arial", 16), bg = "Yellow")

        self.levelSelectButton = Button(name, text = "Level Select", width = 20, command = '', font = ("Arial", 16), bg = "LightBlue")
        self.levelSelectButton.place(x = 1020, y = 180)

        self.scoreLabel = Label(name, text = "Score", width = 10, height = 2, font = ("Arial", 16), bg = "LightGray")
        self.scoreLabel.place(x = 1020, y = 240)

        self.scoreShowLabel = Label(name, text = "000", width = 10, height = 2, font = ("Arial", 16), bg = "LightGray")
        self.scoreShowLabel.place(x = 1140, y = 240)

        self.treasureCollectedLabel = Label(name, text = "Treasure Collected", width = 20, height = 1, font = ("Arial", 16), bg = "LightGray")
        self.treasureCollectedLabel.place(x = 1020, y = 300)

        self.treasureBackgroundLabel = Label(name, width = 20, height = 7, font = ("Arial", 16), bg = "LightGray")
        self.treasureBackgroundLabel.place(x = 1020, y = 330)

    def timer(level3):
         global counter, resetpressed, pausepressed
         counter==counter
         if (counter != 0):
            counter=counter-1
            interface.minuteConvert()
            level3.secShowLabel.after(1000, level3.timer)
            
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
        
        interface.timerselect_label = Label(timerCanvas, text = "Time to collect: (In Seconds)", wraplength = 100, width = 20, font = ("Arial", 9), bg = "White")
        interface.timerselect_label.place(x = 35, y = 10)
        
        interface.timeEntry = Entry(timerCanvas, text = "" , width = 20, bd = 5)
        interface.timeEntry.place(x = 45,y = 60)
        
        interface.timeEntryButton = Button(timerCanvas, text = "Start", width = 10, font = ("Arial", 10), command = interface.timerWindowGet, bg = "LightGreen")
        interface.timeEntryButton.place(x = 65, y = 100)
        
        timerCanvas.pack()
        wishlistWindow.destroy()

    def timerwingeterror(self):
        tkMessageBox.showinfo("Timer Error", "Please enter a value greater than 0")
        
    def timerWindowGet(level3):
        global counter, timerWindow
        if (interface.timeEntry.get())=="" or (interface.timeEntry.get())=="0":
            counter=0
            interface.timerwingeterror()
        else:
            counter=int(interface.timeEntry.get())
            interface.timerShow(interface)
            timerWindow.destroy()

    def wishlistWindow(self):
        global wishlistWindow, timerWindow
        wishlistWindow = Tk()
        wishlistWindow.title("Wishlist")
        wishlistWindow.resizable(0,0)

        wishlistCanvas = Canvas(wishlistWindow, width = 210, height = 200, bg = "White")

        interface.wishlistEntryButton = Button(wishlistCanvas, text = "Ok", width = 10, font = ("Arial", 10), command = self.timerWindow, bg = "LightGray")
        interface.wishlistEntryButton.place(x = 10, y = 10)

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

    def sortByWindow(self):
        sortByWindow = Tk()
        sortByWindow.title("Sort By")
        sortByWindow.resizable(0,0)

        sortByCanvas = Canvas(sortByWindow, width = 200, height = 100, bg = "White")

        interface.sortByAscendingButton = Button(sortByCanvas, text = "Ascending", width = 20, font = ("Arial", 10), command = '', bg = "LightBlue")
        interface.sortByAscendingButton.place (x = 20, y = 20)

        interface.sortByDescendingButton = Button(sortByCanvas, text = "Descending", width = 20, font = ("Arial", 10), command = '', bg = "LightGreen")
        interface.sortByDescendingButton.place(x = 20, y = 60)
        
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
        
interface = interface(level3)
interface.sortByWindow()

level3.mainloop()    
