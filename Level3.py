from Tkinter import *
main = Tk(className = "level 3")
canvas = Canvas(main, width = 1280, height = 720, bg = "White")
canvas.pack()

mainCanvas = canvas.create_rectangle(20, 20, 1000, 700, fill = 'white', width = 2) 

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

    def start(self):
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

main.mainloop()    
