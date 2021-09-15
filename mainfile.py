from tkinter import *


import create_user_child
from create_userlogin import adduser


class myParentFrame:
    def __init__(self):
        self.mywindow = Tk()
        mymenubar = Menu(self.mywindow)
        self.mywindow.config(menu=mymenubar)
        self.mywindow.option_add("*tearOff", False)

        self.mywindow.wm_title("Computer Education Institute")
        self.mywindow.wm_minsize(1400, 1000)
        homemenu = Menu(mymenubar)
        navigationmenu = Menu(mymenubar)
        miscmenu = Menu(mymenubar)

        mymenubar.add_cascade(menu=homemenu, label = "Home")
        mymenubar.add_cascade(menu=navigationmenu, label="Navigation")
        mymenubar.add_cascade(menu=miscmenu, label="Misc")




        homemenu.add_command(label="Home")  # accelerator="Ctrl+A")
        homemenu.add_command(label="About Us ")
        homemenu.add_command(label="Contact Us")



        navigationmenu.add_command(label="List of Students")
        navigationmenu.add_command(label="List of Teachers")


        miscmenu.add_command(label="Add Student")
        miscmenu.add_command(label="Add Teacher", command=self.show_addemployee)
        miscmenu.add_command(label="Change Password")
        miscmenu.add_command(label="Logout")



    def show_addemployee(self):
        create_user_child.CreateUserChild(self.mywindow)



