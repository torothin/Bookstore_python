from tkinter import *
import sys

print (sys.version)
window=Tk()

def kg_convert():

    gram=float(e1_value.get())*1000
    t1.insert(END,gram)
    lbs=float(e1_value.get())*2.20462
    t2.insert(END,lbs)
    oz=float(e1_value.get())*35.274
    t3.insert(END,oz)

b1=Button(window, text="Convert", command=kg_convert)
b1.grid(row=0, column=2)

l1=Label(window, text="Kg")
l1.grid(row=0, column=0)

e1_value=StringVar()
e1=Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

#Second Row Outputs
t1=Text(window, height=1,width=10)
t1.grid(row=1, column=0)

l2=Label(window, text="grams")
l2.grid(row=1, column=1)

t2=Text(window, height=1,width=10)
t2.grid(row=1, column=2)

l3=Label(window, text="lbs")
l3.grid(row=1, column=3)

t3=Text(window, height=1,width=10)
t3.grid(row=1, column=4)

l4=Label(window, text="ounces")
l4.grid(row=1, column=5)



#print(type(e1_value))


window.mainloop()
