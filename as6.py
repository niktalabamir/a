#______A-M-I-R________<._.>

from datetime import datetime

from tkinter import *

a = 0

numbers = []

#____________def___________#
def gtnbr():
    t = datetime.now()
    global a
    a=a+1
    l4.config(text=a)
    numbers.append(a)
    people = len(numbers)-1
    l9.config(text=people)
    l11.config(text=f"{people*5} min")
    l7.config(text=f"{t.hour} : {t.minute} : {t.second}")
     
def operate(n):

    if n == "a":
        if len(numbers)>5 :
            op = numbers.pop(0)
            l1.config(text=op)
        else :
            l1.config(text="waiting...")
    elif n == "b":
        if len(numbers)>0 :

            op = numbers.pop(0)
            l2.config(text=op)
        else :
            l2.config(text="waiting...")
    elif n == "c":
        if len(numbers)>0 :

            op = numbers.pop(0)
            l3.config(text=op)
        else :
            l3.config(text="waiting...")
def exit():
    root.destroy()
         
#____________________________$
root=Tk()

c=Toplevel()

op=Toplevel()

#_____________C_______________&

c.config(bg="green")

c.geometry("170x250")

b1=Button(c,text="Get a Number",bg="yellow",font=100,height=5,width=15,command=gtnbr)

b2=Button(c,text="cancel",bg="red",font=300,height=10,width=15,command=exit)

b1.grid(row=1,column=1,pady=10,padx=13)

b2.grid(row=3,column=1,pady=10,padx=13)

#_______________op_____________!

op.config(bg="blue")

op.geometry("420x200")

b1=Button(op,text="operatore-1",height=3,width=10,font=100,bg="lightgreen",command=lambda:operate("a"))

b2=Button(op,text="operatore-2",height=3,width=10,font=100,bg="lightgreen",command=lambda:operate("b"))

b3=Button(op,text="operatore-3",height=3,width=10,font=100,bg="lightgreen",command=lambda:operate("c"))


b1.grid(row=2,column=1,padx=17,pady=5)

b2.grid(row=2,column=3,padx=17,pady=10)

b3.grid(row=2,column=5,padx=17,pady=10)


l1=Label(op,text="",height=3,width=7,font=100,bg="white")

l2=Label(op,text="",height=3,width=7,font=100,bg="white")

l3=Label(op,text="",height=3,width=7,font=100,bg="white")


l1.grid(row=3,column=1,padx=17,pady=10)

l2.grid(row=3,column=3,padx=17,pady=10)

l3.grid(row=3,column=5,padx=17,pady=10)

#_______________root_______________~<^>

root.config(bg="pink")

root.geometry("200x150")

l5=Label(root,text="your turn",bg="black",fg="white",font=50)

l4=Label(root,text="0",bg="black",fg="white",font=50)

l6=Label(root,text="time <^>",bg="black",fg="white",font=50)

l7=Label(root,text="0 : 0 :0",bg="black",fg="white",font=50)

l8=Label(root,text="people list :",bg="black",fg="white",font=50)

l9=Label(root,text="0",bg="black",fg="white",font=50)

l10=Label(root,text="waiting time :",bg="black",fg="white",font=50)

l11=Label(root,text="0",bg="black",fg="white",font=50)


l4.grid(row=0,column=1,padx=10,pady=10)

l5.grid(row=0,column=0,padx=10,pady=10)

l6.grid(row=1,column=0,padx=10)

l7.grid(row=1,column=1,padx=10)

l8.grid(row=2,column=0,padx=10,pady=10)

l9.grid(row=2,column=0,padx=10,pady=10)

l10.grid(row=3,column=1,padx=10)

l11.grid(row=3,column=0,padx=10)

#________________ML___________________```~`

root.mainloop()

#________.