from tkinter import *
import sys

print (sys.version)
window=Tk()

def km_to_miles():
    print(e1_value.get())
    miles=float(el.value.get())*1.6
    t1.insert(END,miles)

b1=Button(window, text="Convert", command=km_to_miles)
b1.grid(row=0, column=1)

l1=Label(window, text="Kg")
l1.grid(row=0, column=0)

e1_value=StringVar()
e1=Entry(window, textvariable=e1_value)
e1.grid(row=1, column=0)


t1=Text(window, height=1,width=20)
t1.grid(row=1, column=1)



#print(type(e1_value))


window.mainloop()
