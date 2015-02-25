from Tkinter import *

def main():
    levelSelect = Tk()
    levelSelect.title("Level Selection")
    levelSelect.resizable(0,0)
    canvas = Canvas(levelSelect, width = 300, height = 400, bg = "White")
    canvas.pack()

    class interface:
        def __init__(self, name):
            self.levelOneButton = Button(name, text = "Level One", width = 20, command = self.Level1, font = ("Arial", 16), bg = "LightBlue")
            self.levelOneButton.place(x = 25, y = 20)

            self.levelTwoButton = Button(name, text = "Level Two", width = 20, command = self.Level2, font = ("Arial", 16), bg = "LightGreen")
            self.levelTwoButton.place(x = 25, y = 80)

            self.levelThreeButton = Button(name, text = "Level Three", width = 20, command = self.Level3, font = ("Arial", 16), bg = "Yellow")
            self.levelThreeButton.place(x = 25, y = 140)

            self.exit = Button(name, text = "Exit", width = 10, command = '', font = ("Arial", 16), bg = "Pink")
            self.exit.place(x = 85, y = 200)

        def Level1(self):
            levelSelect.destroy()
            from Level1 import main

        def Level2(self):
            levelSelect.destroy()
            from Level2 import main

        def Level3(self):
            levelSelect.destroy()
            from Level3 import main
            
            
    interface = interface(levelSelect)
    levelSelect.mainloop()
main()

