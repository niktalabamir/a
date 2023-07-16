from tkinter import *
from tkinter.ttk import Combobox
def show():
    a=c1.get()
    print(a)
    l1.config( text=a, bg=a)
root=Tk()
root.geometry("200x200")
root.title("WII")
root.config(bg="black")
c1 = Combobox(root,values=["black"  ,  "blue"  ,  "green"  ,  "yellow"],state="readonly")
b1 = Button(root,text="get data",command=show)
l1=Label(root,fg="pink")
c1.grid(row = 0 , column = 0 , padx=10 , pady=20)
b1.grid(row=1,column=0)
l1.grid(row=2 , column=0 ,pady=20)
root.mainloop()