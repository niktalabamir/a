from tkinter import *
#-------------------------tk-------------------------------------
top = Tk()
top.config(bg="black")
top.geometry("160x200")
top.title("my first ap")
#----------------------------------------------widgets-------------------------------------
l1 = labe1(top,text="this is my first app",bg="red"fg="black")
#----------------pack-------------------------------------------
l1.pack

#-----------------------end------------------------------------------

top.mainloop()

