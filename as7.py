from tkinter import*

root = Tk()

root.geometry("300x300")

a = Toplevel()
a.config(bg="black")
a.geometry("400x400")

b = Toplevel()
b.config(bg="red")
b.geometry("350x350")

c = Toplevel()
c.config(bg="green")
c.geometry("550x550")

bl = Button(root,text="clik")
bl.pack()

root.mainloop()
