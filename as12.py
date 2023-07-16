from tkinter import *

def latte():
    if chk1.get() == "latte" :
        s1.grid(row=0,column=1)
    else:
        s1.grid_forget()



def icelatte():
    if chk2.get() == "ice latte" :
        s2.grid(row=1,column=1)
    else:
        s2.grid_forget()


def americano():
    if chk3.get() == "americano" :
        s3.grid(row=2,column=1)
    else:
        s3.grid_forget()


def iceamercano():
    if chk4.get() == "ice amercano" :
        s4.grid(row=3,column=1)
    else:
        s4.grid_forget()


def tea():
    if chk5.get() == "tea" :
        s5.grid(row=4,column=1)
    else:
        s5.grid_forget()


def coffee():
    if chk6.get() == "coffee" :
        s6.grid(row=5,column=1)
    else:
        s6.grid_forget()

    

def show():
    total=0
    t = Toplevel()
    if chk1.get() == "latte" :
        total = total + int(s1.get())*40000

    if chk2.get() == "ice latte" :
        total = total + int(s2.get())*40000
    
    if chk3.get() == "americano" :
        total = total + int(s3.get())*40000

    if chk4.get() == "ice americano" :
        total = total + int(s4.get())*40000

    if chk5.get() == "tea" :
        total = total + int(s5.get())*40000

    if chk6.get() == "coffee" :
        total = total + int(s6.get())*40000

        
    l1 = Label(t,text=total)
    l1.pack()



root = Tk()


#________________________________widgets_____________________

chk1 =StringVar()

chk2 =StringVar()

chk3 =StringVar()

chk4 =StringVar()

chk5 =StringVar()

chk6 =StringVar()






ch1 = Checkbutton(root,text="latte",                               onvalue="latte",variable=chk1,command=latte)
ch1.deselect()


ch2 =  Checkbutton(root,text="ice latte",                               onvalue="ice latte",variable=chk2,command=icelatte)
ch2.deselect()


ch3 =  Checkbutton(root,text="americano",                               onvalue="americano",variable=chk3,command=americano)
ch3.deselect()


ch4 =  Checkbutton(root,text="ice americano",                               onvalue="ice americano",variable=chk4,command=iceamercano)
ch4.deselect()


ch5 = Checkbutton(root,text="tea",                               onvalue="tea",variable=chk5,command=tea)
ch5.deselect()


ch6 = Checkbutton(root,text="coffee",                               onvalue="coffee",variable=chk6,command=coffee)
ch6.deselect()


#____________________________________spinbox___________________________<@>


s1 = Spinbox(root,from_=1,to=10)

s2 = Spinbox(root,from_=1,to=10)

s3 = Spinbox(root,from_=1,to=10)

s4 = Spinbox(root,from_=1,to=10)

s5 = Spinbox(root,from_=1,to=10)

s6 = Spinbox(root,from_=1,to=10)



b1 = Button(root,text="ok",command=show)



ch1.grid(row=0,column=0)


ch2.grid(row=1,column=0)


ch3.grid(row=2,column=0)


ch4.grid(row=3,column=0)


ch5.grid(row=4,column=0)


ch6.grid(row=5,column=0)


b1.grid(row=6,column=0)



#________________grids___________________


root.mainloop()


#______________end___________________
#https://www.unfair-mario.com/