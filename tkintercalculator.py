import parser
from tkinter import *
root=Tk()
root.title("Calculator")
# Create an entry widget for the display
display = Entry(root, width=51, borderwidth=5, justify=RIGHT, font=('Courier New', 16))
display.grid(row=0, column=0, columnspan=10, padx=10, pady=10)
i=0
# Define button style
button_style = {
    'font': ('Courier New', 16),
    'padx': 20,
    'pady': 20,
    'width': 5,
    'height': 2,
    'bg': '#FFFFFF',
    'fg': '#000000',
    'borderwidth': 1,
    'relief': 'raised'
}


def fun1(num):
    global i
    display.insert(i,num)
    i+=1
def clear_all():
    display.delete(0,END)

def fun3():
    newstr=display.get()
    if len(newstr):
        newstr2=newstr[:-1]
        clear_all()
        display.insert(0,newstr2)
    else:
        clear_all()
        display(0,"Error")

def fun4(opr):
    global  i
    length=len(opr)
    display.insert(i,opr)
    i+=length

def calculate():
    calc=display.get()
    try:
        a=parser.expr(calc).compile()
        result=eval(a)
        clear_all()
        display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0,"Error")
# Create buttons
Button(root, text="1", command=lambda: fun1(1), **button_style).grid(row=2, column=0)
Button(root, text="2", command=lambda: fun1(2), **button_style).grid(row=2, column=1)
Button(root, text="3", command=lambda: fun1(3), **button_style).grid(row=2, column=2)
Button(root, text="4", command=lambda: fun1(4), **button_style).grid(row=3, column=0)
Button(root, text="5", command=lambda: fun1(5), **button_style).grid(row=3, column=1)
Button(root, text="6", command=lambda: fun1(6), **button_style).grid(row=3, column=2)
Button(root, text="7", command=lambda: fun1(7), **button_style).grid(row=4, column=0)
Button(root, text="8", command=lambda: fun1(8), **button_style).grid(row=4, column=1)
Button(root, text="9", command=lambda: fun1(9), **button_style).grid(row=4, column=2)
Button(root, text="0", command=lambda: fun1(0), **button_style).grid(row=5, column=0)
Button(root, text="AC", command=lambda: clear_all(), **button_style).grid(row=5, column=1)
Button(root, text="->", command=lambda: fun3(), **button_style).grid(row=5, column=2)
Button(root, text="=", command=lambda: calculate(), **button_style).grid(row=2, column=3)
Button(root, text="+", command=lambda: fun4('+'), **button_style).grid(row=2, column=4)
Button(root, text="-", command=lambda: fun4('-'), **button_style).grid(row=2, column=5)
Button(root, text="/", command=lambda: fun4('/'), **button_style).grid(row=3, column=3)
Button(root, text="pi", command=lambda: fun4('*3.14'), **button_style).grid(row=3, column=4)
Button(root, text="%", command=lambda: fun4('%'), **button_style).grid(row=3, column=5)
Button(root, text=")", command=lambda: fun4(')'), **button_style).grid(row=4, column=3)
Button(root, text="(", command=lambda: fun4('('), **button_style).grid(row=4, column=4)
Button(root, text="^2", command=lambda: fun4('**2'), **button_style).grid(row=4, column=5)
Button(root, text="exp", command=lambda: fun4('**'), **button_style).grid(row=5, column=3)
Button(root, text="*", command=lambda: fun4('*'), **button_style).grid(row=5, column=5)
Button(root, text="x!", **button_style).grid(row=5, column=4)

root.mainloop()