from tkinter import *
from math import *

root = Tk()
root.title("Calculator")
root.configure(bg="#404040")
root.geometry("500x500")

e = Entry(root, width=30, borderwidth=0, bg="#404040", font=('TimesNewRoman',25), fg="White")
e.grid(row=0, column=0, columnspan=6, rowspan=2, padx=30, pady=11, sticky="nsew", ipadx=10, ipady=40)


# Define Colours


def ButtonHover(e):
    buttonAdd["bg"] = "#323232"


def ButtonHover0(e):
    button0["bg"] = "#323232"


def ButtonHover1(e):
    button1["bg"] = "#323232"


def ButtonHover2(e):
    button2["bg"] = "#323232"


def ButtonHover3(e):
    button3["bg"] = "#323232"


def ButtonHover4(e):
    button4["bg"] = "#323232"


def ButtonHover5(e):
    button5["bg"] = "#323232"


def ButtonHover6(e):
    button6["bg"] = "#323232"


def ButtonHover7(e):
    button7["bg"] = "#323232"


def ButtonHover8(e):
    button8["bg"] = "#323232"


def ButtonHover9(e):
    button9["bg"] = "#323232"


def ButtonHoverAdd(e):
    buttonAdd["bg"] = "#323232"


def ButtonHoverSubtract(e):
    buttonSubtract["bg"] = "#323232"


def ButtonHoverMultiply(e):
    buttonMultiply["bg"] = "#323232"


def ButtonHoverDivide(e):
    buttonDivide["bg"] = "#323232"


def ButtonHoverEqual(e):
    buttonEqual["bg"] = "#323232"


def ButtonHoverDot(e):
    buttonDot["bg"] = "#323232"


def ButtonHoverpi(e):
    buttonpi["bg"] = "#323232"


def ButtonHoverClear(e):
    buttonClear["bg"] = "#323232"


def ButtonHoverSin(e):
    buttonSin["bg"] = "#323232"


def ButtonHoverCos(e):
    buttonCos["bg"] = "#323232"


def ButtonHoverTan(e):
    buttonTan["bg"] = "#323232"


# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# def ButtonLeave(e):
#	buttonAdd["bg"]= "#121212"


def ButtonLeave0(e):
    button0["bg"] = "#121212"


def ButtonLeave1(e):
    button1["bg"] = "#121212"


def ButtonLeave2(e):
    button2["bg"] = "#121212"


def ButtonLeave3(e):
    button3["bg"] = "#121212"


def ButtonLeave4(e):
    button4["bg"] = "#121212"


def ButtonLeave5(e):
    button5["bg"] = "#121212"


def ButtonLeave6(e):
    button6["bg"] = "#121212"


def ButtonLeave7(e):
    button7["bg"] = "#121212"


def ButtonLeave8(e):
    button8["bg"] = "#121212"


def ButtonLeave9(e):
    button9["bg"] = "#121212"


def ButtonLeaveAdd(e):
    buttonAdd["bg"] = "#282828"


def ButtonLeaveSubtract(e):
    buttonSubtract["bg"] = "#282828"


def ButtonLeaveMultiply(e):
    buttonMultiply["bg"] = "#282828"


def ButtonLeaveDivide(e):
    buttonDivide["bg"] = "#282828"


def ButtonLeaveDot(e):
    buttonDot["bg"] = "#121212"


def ButtonLeaveEqual(e):
    buttonEqual["bg"] = "#404040"


def ButtonLeaveClear(e):
    buttonClear["bg"] = "#282828"


def ButtonLeavepi(e):
    buttonpi["bg"] = "#282828"


def ButtonLeaveSin(e):
    buttonSin["bg"] = "#282828"


def ButtonLeaveCos(e):
    buttonCos["bg"] = "#282828"


def ButtonLeaveTan(e):
    buttonTan["bg"] = "#282828"


def pi_click(π):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(3.14159265359))


def sin_click():
    global Operator
    Operator = "sin"
    e.delete(0, END)


def dot_click(dot):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + dot)


def myClick(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_Clear():
    e.delete(0, END)


def button_Add():
    FirstNumber = e.get()
    global Operator
    Operator = "+"
    global FirstNum
    FirstNum = float(FirstNumber)
    e.delete(0, END)


def button_Equal():
    second_number = e.get()
    e.delete(0, END)

    global Operator

    if Operator == "Sin":
        e.insert(0, sin(float(second_number)))
    elif Operator == "+":
        e.insert(0, FirstNum + float(second_number))
    elif Operator == "-":
        e.insert(0, FirstNum - float(second_number))

    elif Operator == "x":
        e.insert(0, FirstNum * float(second_number))

    elif Operator == "/":
        e.insert(0, FirstNum / float(second_number))


def button_Subtract():
    FirstNumber = e.get()
    global Operator
    Operator = "-"
    global FirstNum
    FirstNum = float(FirstNumber)
    e.delete(0, END)


def button_Multiply():
    FirstNumber = e.get()
    global Operator
    Operator = "x"
    global FirstNum
    FirstNum = float(FirstNumber)
    e.delete(0, END)


def button_Divide():
    FirstNumber = e.get()
    global Operator
    Operator = "/"
    global FirstNum
    FirstNum = float(FirstNumber)
    e.delete(0, END)


# Define Buttons
button0 = Button(root, text="0", command=lambda: myClick(0), fg="white", bg="#121212", padx=40, pady=20, font=('Arial',16,'bold'))
button1 = Button(root, text="1", command=lambda: myClick(1), fg="white", bg="#121212", padx=40, pady=20, font=('Arial',16,'bold'))
button2 = Button(root, text="2", command=lambda: myClick(2), fg="white", bg="#121212", padx=40, pady=20, font=('Arial',16,'bold'))
button3 = Button(root, text="3", command=lambda: myClick(3), fg="white", bg="#121212", padx=40, pady=20, font=('Arial',16,'bold'))
button4 = Button(root, text="4", command=lambda: myClick(4), fg="white", bg="#121212", padx=40, pady=20, font=('Arial',16,'bold'))
button5 = Button(root, text="5", command=lambda: myClick(5), fg="white", bg="#121212", padx=40, pady=20, font=('Arial',16,'bold'))
button6 = Button(root, text="6", command=lambda: myClick(6), fg="white", bg="#121212", padx=40, pady=20, font=('Arial',16,'bold'))
button7 = Button(root, text="7", command=lambda: myClick(7), fg="white", bg="#121212", padx=40, pady=20, font=('Arial',16,'bold'))
button8 = Button(root, text="8", command=lambda: myClick(8), fg="white", bg="#121212", padx=40, pady=20, font=('Arial',16,'bold'))
button9 = Button(root, text="9", command=lambda: myClick(9), fg="white", bg="#121212", padx=40, pady=20, font=('Arial',16,'bold'))
buttonDot = Button(root, text=".", command=lambda: dot_click("."), fg="white", bg="#121212", padx=89, pady=20, font=('Arial',16,'bold'))
buttonEqual = Button(root, text="=", command=button_Equal, fg="white", bg="#404040", padx=99, pady=20, font=('Arial',16,'bold'))
buttonAdd = Button(root, text="➕", command=button_Add, fg="white", bg="#282828", padx=40, pady=20)

buttonSubtract = Button(root, text="➖", command=button_Subtract, fg="white", bg="#282828", padx=42.444, pady=20)
buttonMultiply = Button(root, text="❌", command=button_Multiply, fg="white", bg="#282828", padx=40, pady=20)
buttonDivide = Button(root, text="➗", command=button_Divide, fg="white", bg="#282828", padx=42, pady=20)

buttonClear = Button(root, text="Clear", command=button_Clear, fg="white", bg="#282828", padx=90, pady=20)
#3D4849
buttonSin = Button(root, text="Sin", command=sin_click, fg="white", bg="#282828", padx=35, pady=20)
buttonCos = Button(root, text="Cos", command=sin_click, fg="white", bg="#282828", padx=33, pady=20)
buttonTan = Button(root, text="Tan", command=sin_click, fg="white", bg="#282828", padx=33, pady=20)
buttonpi = Button(root, text="π", command=lambda: pi_click(3.14159265359), fg="white", bg="#282828", padx=99, pady=20)
# Put buttons on the screen


button1.grid(row=5, column=0, sticky="nsew")
button2.grid(row=5, column=1, sticky="nsew")
button3.grid(row=5, column=2, sticky="nsew")

button4.grid(row=4, column=0, sticky="nsew")
button5.grid(row=4, column=1, sticky="nsew")
button6.grid(row=4, column=2, sticky="nsew")

button7.grid(row=3, column=0, sticky="nsew")
button8.grid(row=3, column=1, sticky="nsew")
button9.grid(row=3, column=2, sticky="nsew")

button0.grid(row=6, column=0, sticky="nsew")
buttonClear.grid(row=5, column=3, columnspan=2, sticky="nsew")
buttonEqual.grid(row=6, column=3, columnspan=2, sticky="nsew")

buttonAdd.grid(row=4, column=3, sticky="nsew")
buttonSubtract.grid(row=4, column=4, sticky="nsew")
buttonMultiply.grid(row=3, column=3, sticky="nsew")
buttonDivide.grid(row=3, column=4, sticky="nsew")
buttonDot.grid(row=6, column=1, columnspan=2, sticky="nsew")
buttonSin.grid(row=2, column=0, sticky="nsew")
buttonCos.grid(row=2, column=1, sticky="nsew")
buttonTan.grid(row=2, column=2, sticky="nsew")
buttonpi.grid(row=2, column=3, columnspan=2, sticky="nsew")

button0.bind("<Enter>", ButtonHover0)
button1.bind("<Enter>", ButtonHover1)
button2.bind("<Enter>", ButtonHover2)
button3.bind("<Enter>", ButtonHover3)
button4.bind("<Enter>", ButtonHover4)
button5.bind("<Enter>", ButtonHover5)
button6.bind("<Enter>", ButtonHover6)
button7.bind("<Enter>", ButtonHover7)
button8.bind("<Enter>", ButtonHover8)
button9.bind("<Enter>", ButtonHover9)
buttonAdd.bind("<Enter>", ButtonHoverAdd)
buttonSubtract.bind("<Enter>", ButtonHoverSubtract)
buttonMultiply.bind("<Enter>", ButtonHoverMultiply)
buttonDivide.bind("<Enter>", ButtonHoverDivide)
buttonpi.bind("<Enter>", ButtonHoverpi)
buttonDot.bind("<Enter>", ButtonHoverDot)
buttonClear.bind("<Enter>", ButtonHoverClear)
buttonEqual.bind("<Enter>", ButtonHoverEqual)
buttonSin.bind("<Enter>", ButtonHoverSin)
buttonCos.bind("<Enter>", ButtonHoverCos)
buttonTan.bind("<Enter>", ButtonHoverTan)

button0.bind("<Leave>", ButtonLeave0)
button1.bind("<Leave>", ButtonLeave1)
button2.bind("<Leave>", ButtonLeave2)
button3.bind("<Leave>", ButtonLeave3)
button4.bind("<Leave>", ButtonLeave4)
button5.bind("<Leave>", ButtonLeave5)
button6.bind("<Leave>", ButtonLeave6)
button7.bind("<Leave>", ButtonLeave7)
button8.bind("<Leave>", ButtonLeave8)
button9.bind("<Leave>", ButtonLeave9)
buttonAdd.bind("<Leave>", ButtonLeaveAdd)
buttonSubtract.bind("<Leave>", ButtonLeaveSubtract)
buttonMultiply.bind("<Leave>", ButtonLeaveMultiply)
buttonDivide.bind("<Leave>", ButtonLeaveDivide)
buttonpi.bind("<Leave>", ButtonLeavepi)
buttonDot.bind("<Leave>", ButtonLeaveDot)
buttonClear.bind("<Leave>", ButtonLeaveClear)
buttonEqual.bind("<Leave>", ButtonLeaveEqual)
buttonSin.bind("<Leave>", ButtonLeaveSin)
buttonCos.bind("<Leave>", ButtonLeaveCos)
buttonTan.bind("<Leave>", ButtonLeaveTan)

for i in range(0, 5, 1):
    Grid.columnconfigure(root, index=i, weight=1)
    Grid.rowconfigure(root, index=i, weight=1)

root.mainloop()




