from tkinter import *
tk=Tk()

def add():
    c=a.get()+b.get();
    Label(tk,text=c,pady=10,padx=10).grid(row=3,column=2)
def sub():
    c=a.get()-b.get();
    Label(tk,text=c,pady=10,padx=10).grid(row=3,column=2)
def mult():
    c=a.get()*b.get();
    Label(tk,text=c,pady=10,padx=10).grid(row=3,column=2)
def div():
    c=a.get()/b.get();
    Label(tk,text=c,pady=10,padx=10).grid(row=3,column=2)





a=IntVar()
b=IntVar()
c=IntVar()
tk.geometry("350x300")
Label(tk,text="Calculator",pady=20).grid(row=0,column=2)
Label(tk,text="Enter first No.",pady=10,padx=10).grid(row=1)
Label(tk,text="Enter second No.",pady=10,padx=10).grid(row=2)
Label(tk,text="Result.",pady=10,padx=10).grid(row=3)


Entry(tk,textvariable=a).grid(row=1,column=2)
Entry(tk,textvariable=b).grid(row=2,column=2)

Button(tk,text="   +   ", command=add).grid(row=4,column=0)
Button(tk,text="   -   ", command=sub).grid(row=4,column=1)
Button(tk,text="   *   ", command=mult).grid(row=4,column=2)
Button(tk,text="   /   ", command=div).grid(row=4,column=3)


tk.mainloop()
