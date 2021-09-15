from tkinter import *
from tkinter import ttk, messagebox
import pymysql

import mainfile



class MyLogin:
    def __init__(self):
        self.mywindow = Tk()
        self.mywindow.wm_title("Login")
        self.mywindow.wm_minsize(600, 400)

        heading = Label(self.mywindow, text="Login", font=("Georgia", 18, 'bold'), fg='maroon')
        heading.place(x=300, y=10)

        username_msg = Label(self.mywindow, text="Username")
        username_msg.place(x=50, y=80)

        self.username_input_box = Entry(self.mywindow)
        self.username_input_box.place(x=180, y=80)

        password_msg = Label(self.mywindow, text="Password")
        password_msg.place(x=50, y=130)

        self.password_input_box = Entry(self.mywindow, show="*")
        self.password_input_box.place(x=180, y=130)


        login_button = Button(self.mywindow, text="Login", command=self.mylogin, padx=10)
        login_button.place(x=180, y=170)






        self.mywindow.mainloop()



    def mylogin(self):
        try:
            myconnection = pymysql.connect(host='localhost', user='root', password='', db='computerdb')
            try:
                with myconnection.cursor() as myconn:
                    myquery = "select username from computer_institute where username=%s and password=%s"
                    myconn.execute(myquery, (self.username_input_box.get(), self.password_input_box.get()))

                    if myconn.fetchone() is not None:
                        self.mywindow.withdraw()
                        self.mywindow.destroy()
                        mainfile.myParentFrame()

                    else:
                        messagebox.showwarning("Wrong Credentials", "Wrong username/password")
            except Exception as ex:
                messagebox.showerror("Error", "Error in Query due to " + str(ex))

        except Exception as ex:
            messagebox.showerror("Error", "Error in Connection due to " + str(ex))



