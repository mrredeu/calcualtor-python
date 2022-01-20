import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
import math
from math import pi

window=tk.Tk()
window.title("Calculator - Standard")

Tk_Width = 350
Tk_Height = 350
positionRight = int(window.winfo_screenwidth()/15 - Tk_Width/2 )
positionDown = int(window.winfo_screenheight()/1.21 - Tk_Height/2 )
window.geometry("{}x{}+{}+{}".format(350,350,positionRight, positionDown))
window.configure(bg="black")

#=======================================================================================================================================================================================================================================================================================================================================================================

previousans = tk.StringVar()
equation = tk.StringVar() 
textbox = tk.Entry(window, textvariable=equation) 
inverted = 1

def press(num):
    cursorpos = textbox.index(tk.INSERT)
    wordstart = textbox.get()[:cursorpos]
    wordfinish = textbox.get()[cursorpos:]
    equation.set(wordstart + str(num) + wordfinish)
    textbox.icursor("end")


def roundPointZero(number):
    total = number
    roundedNumLEN = len(str(math.floor(float(total))))
    numLEN = len(str(total))
    lenTotal = roundedNumLEN - numLEN
    if total != 0 or total == 0.0:
        modtotal = math.fmod(total, 1)
        if modtotal == 0:
            if lenTotal == -2:
                total = round(total)
            else:
                total = "{:.6e}".format(float(total)) 
        else:
            total = round(total, 9)
        equation.set(total)
        previousans.set(total)
        textbox.icursor("end")

def calcsolve(): 
    if textbox.get() != "":
        try: 
            total = str(eval(textbox.get()))
            total = float(total)
            if str(total)[-5:] >= "e+300":
                equation.set("inf")
                previousans.set("inf")
                textbox.icursor("end")
            else:
                roundPointZero(total)
        except: 
            if previousans.get() =="inf":
                equation.set("inf") 
                previousans.set("inf")
                textbox.icursor("end")
            else:
                equation.set("ERROR") 
                textbox.icursor("end")

def keysolve(event, key): 
    if key == "0":
        textbox.delete(len(textbox.get())-1) # deletes equal sign from having error to solve
    else: 
        pass
    if textbox.get() != "":
        try: 
            total = str(eval(textbox.get()))
            total = float(total)
            if str(total)[-5:] >= "e+300":
                equation.set("inf")
                previousans.set("inf")
                textbox.icursor("end")
            else:
                roundPointZero(total)
        except: 
            if previousans.get() =="inf":
                equation.set("inf") 
                previousans.set("inf")
            else:
                equation.set("ERROR") 

#=======================================================================================================================================================================================================================================================================================================================================================================

def filevar():
    global filewin
    filewin=tk.Tk()
    filewin.title("File")
    filewin.geometry("200x200+350+1180")
    Tk_Width = 200
    Tk_Height = 200
    positionRight = int(window.winfo_screenwidth()/5.75 - Tk_Width/2 )
    positionDown = int(window.winfo_screenheight()/1.138 - Tk_Height/2 )
    filewin.geometry("{}x{}+{}+{}".format(200,200,positionRight, positionDown))
    filewin.configure(bg="black")
    #functions
    Standardfunc=tk.Button(filewin, text="Standard", command=lambda:[Standard()], font=("Calibri", 25), bg="black", fg="white", activebackground="grey")
    Scientificfunc=tk.Button(filewin, text="Scientific", command=lambda:[Scientific("file")], font=("Calibri", 25), bg="black", fg="white", activebackground="grey")
    Standardfunc.place(x=0,y=0, height=100, width=200)
    Scientificfunc.place(x=0,y=100, height=100, width=200)
    filewin.mainloop()

def Scientific(destroy):
    global window
    window.destroy()
    window=tk.Tk()
    window.title("Calculator - Scientific")
    Tk_Width = 350
    Tk_Height = 700
    positionRight = int(window.winfo_screenwidth()/15 - Tk_Width/2 )
    positionDown = int(window.winfo_screenheight()/1.42 - Tk_Height/2 )
    window.geometry("{}x{}+{}+{}".format(350,700,positionRight, positionDown))
    window.configure(bg="black")
    calcscientific()
    if destroy == "file":
        filewin.destroy()
    else:
        pass
    window.mainloop()

def Standard():
    global window
    window.destroy()
    window=tk.Tk()
    window.title("Calculator - Standard")
    Tk_Width = 350
    Tk_Height = 350
    positionRight = int(window.winfo_screenwidth()/15 - Tk_Width/2 )
    positionDown = int(window.winfo_screenheight()/1.21 - Tk_Height/2 )
    window.geometry("{}x{}+{}+{}".format(350,350,positionRight, positionDown))
    window.configure(bg="black")
    calcstandard()
    filewin.destroy()
    window.mainloop()

#=======================================================================================================================================================================================================================================================================================================================================================================

def htu():
    global window
    window.destroy()
    window=tk.Tk()
    window.resizable(width=False, height=False)
    window.title("Calculator - How To Use")
    Tk_Width = 450
    Tk_Height = 330
    positionRight = int(window.winfo_screenwidth()/2 - Tk_Width/2)
    positionDown = int(window.winfo_screenheight()/2 - Tk_Height/2)
    window.geometry("{}x{}+{}+{}".format(450,330,positionRight, positionDown))
    window.configure(bg="black")
    htucFont = tkFont.Font(family="Calibri", size=26, weight=tkFont.BOLD, underline=1)
    htuc=tk.Label(window, text="How to use Calculator", font=htucFont, bg="black", fg="white")
    htuc.place(relx=0, rely=0, relheight=0.25, relwidth=1)
    text = tk.Label(window, bg="black", fg="white", activebackground="grey")
    text.place(relx=0, rely=0.25, relheight=0, relwidth=0)
    htb = tk.Button(window, text="1) How to use Standard buttons", command=lambda: StandardButtons(), font=("Calibri", 25), borderwidth=2.5, relief="groove", bg="black", fg="white", activebackground="grey")
    htb.place(relx=0, rely=0.25, relheight=0.25, relwidth=1)
    htinv=tk.Button(window, text="2) How to use Scientific buttons", command=lambda: ScientificButtons(), font=("Calibri", 25), borderwidth=2.5, relief="groove", bg="black", fg="white", activebackground="grey")
    htinv.place(relx=0, rely=0.5, relheight=0.25, relwidth=1)
    backbtn=tk.Button(window, text="3) Go Back", command=lambda: Scientific("none"), font=("Calibri", 25), borderwidth=2.5, relief="groove", bg="black", fg="white", activebackground="grey")
    backbtn.place(relx=0, rely=0.75, relheight=0.25, relwidth=1)

    def StandardButtons():
        htb.place_forget()
        htinv.place_forget()
        window.title("Standard Buttons - How To Use")
        text.config(text="1) Choose your number. It can be a decimal number.\n2) Press any operation. 3) Select another number\nthat could be nalso a decimal number. 4) Hit =, then\nit gives you the answer of your equation. 5) That\nanswer will be stored as Ans which is located\nto the left of =.", font=("Calibri", 15))
        text.place_configure(relheight=0.5, relwidth=1)
        backbtn.config(text="Go Back", command=lambda: htu())

    def ScientificButtons():
        htb.place_forget()
        window.title("Scientifc Buttons - How To Use")
        text.config(text="1) Choose your number. It can be a decimal number.\n2) Press any scientific opertion. 3) If the number\nyou chose isn't and operation error, then it gives\nyou an answer. 4) That answer will be stored as\nAns which is located to the left of =.", font=("Calibri", 15))
        text.place_configure(relheight=0.5, relwidth=1)
        htinv.config(text="Go Forward", command=lambda: next())
        htinv.place_configure(relheight=0.25, relwidth=0.5, relx=0.5, rely=0.75)
        backbtn.config(text="Go Back", command=lambda: htu())
        backbtn.place_configure(relheight=0.25, relwidth=0.5)
        def next():
            htb.place_forget()
            htinv.place_forget()
            window.title("Scientifc Buttons - How To Use hyp Button")
            text.config(text="1) The hyp button has three modes. The first mode\nhas cos, tan, and sin, the second mode has acos,\natan, and asin, and the third mode has cosh, tanh,\nand sinh. 2) After you get to third mode, you\nwill be sent to first mode.", font=("Calibri", 15))
            text.place_configure(relheight=0.5, relwidth=1)
            backbtn.config(text="Go Back", command=lambda: ScientificButtons())
            backbtn.place_configure(relheight=0.25, relwidth=1)


    window.mainloop()

#=======================================================================================================================================================================================================================================================================================================================================================================

def delete():
    cursor_position = textbox.index(tk.INSERT)
    textbox.delete(cursor_position-1)

def clear():  
    equation.set("")

def clearbuttonerror():
    global buttonerror
    buttonerror.config(text="No Error Found")

#=======================================================================================================================================================================================================================================================================================================================================================================

def scientificChoice(chosen):
    errorName = tk.StringVar()
    errorTime = tk.IntVar()
    extraString = tk.StringVar()
    errorString = tk.StringVar()
    allow = FALSE
    global buttonerror
    try: 
        global textbox
        expression = ""
        expression = textbox.get()

        if expression == "" or expression == "0.0" or expression == "ERROR":
            errorName = chosen
            errorTime = 5000
            errorString = "You didn't select a number before pressing "  + errorName + ". Please\npress a button that you want, then press "  + errorName + "."
            buttonerror.config(text=errorString)
            window.after(errorTime, clearbuttonerror)
        else:
            if chosen == "sin":
                errorName = "sin"
                errorTime = 6000
                extraString = ""
                expression =  math.sin(math.radians(float(expression))) 
            elif chosen == "cos":
                errorName = "cos"
                errorTime = 6000
                extraString = ""
                expression =  math.cos(math.radians(float(expression))) 
            elif chosen == "tan":
                errorName = "tan"
                errorTime = 6000
                expression =  math.tan(math.radians(float(expression))) 
            elif chosen == "asin":
                errorName = "asin"
                extraString = "Choose\nany number or decimal number from 1 to -1."
                errorTime = 7000
                expression =  math.asin(float(expression)) 
            elif chosen == "acos":
                errorName = "acos"
                extraString = "Choose\nany number or decimal number from 1 to -1."
                errorTime = 7000
                expression =  math.acos(float(expression)) 
            elif chosen == "atan":
                errorName = "atan"
                errorTime = 6000
                extraString = ""
                expression =  math.atan(float(expression)) 
            elif chosen == "sinh":
                errorName = "sinh"
                extraString = "Choose\nany number or decimal number from 710 to -710."
                errorTime = 5000
                expression =  math.sinh(float(expression)) 
            elif chosen == "cosh":
                errorName = "cosh"
                extraString = "Choose\nany number or decimal number from 710 to -710."
                errorTime = 6000
                expression =  math.cosh(float(expression)) 
            elif chosen == "tanh":
                errorName = "tanh"
                errorTime = 6000
                extraString = ""
                expression =  math.tanh(float(expression)) 
            elif chosen == "sqrt":
                errorName = "sqrt"
                errorTime = 5000
                extraString = "Choose\nany number or decimal number from 1 to infinite."
                expression =  math.sqrt(float(expression)) 
            elif chosen == "lgamma":
                errorName = "lgamma"
                errorTime = 6000
                extraString = ""
                expression = math.lgamma(float(expression))
            elif chosen == "log":
                errorName = "log"
                extraString = "Choose\nany number from 1 to infinite."
                errorTime = 7000
                expression =  math.log(float(expression)) 
            elif chosen == "log2":
                errorName = "log2"
                extraString = "Choose\nany number from 1 to infinite."
                errorTime = 7000
                expression =  math.log2(float(expression)) 
            elif chosen == "log1p":
                errorName = "log1p"
                extraString = "Choose\nany number from 0 to infinite."
                errorTime = 7000
                expression =  math.log1p(float(expression)) 
            elif chosen == "log10":
                errorName = "log10"
                extraString = "Choose\nany number from 1 to infinite."
                errorTime = 6000
                expression =  math.log10(float(expression)) 
            elif chosen == "exp":
                errorName = "exp"
                errorTime = 6000
                extraString = "Choose\nany number from 709 to -709."
                expression = math.exp(float(float(expression)))
            elif chosen == "expm1":
                errorName = "expm1"
                errorTime = 6000
                extraString = "Choose\nany number from 709 to -709."
                expression = math.expm1(float(float(expression)))
            elif chosen == "deg":
                errorName = "deg"
                errorTime = 6000
                extraString = ""
                expression = math.degrees(float(expression))

            equation.set(expression)
            try:
                number = math.floor(float(equation.get()))
                lenEqaution = len(str(number)) - 10
                if lenEqaution >= 0:
                    equationNEW = "{:.6e}".format(float(equation.get()))
                    if str(equationNEW)[-5:] >= "e+300":
                        equation.set("inf")
                        previousans.set("inf")
                    else:
                        equation.set(equationNEW)
                        previousans.set(equationNEW)
                    textbox.icursor("end")
                else:
                    equationNEW = round(float(equation.get()), 9)
                    roundPointZero(equationNEW)
            except:
                if previousans.get() == "inf":
                    equation.set("inf")
                else:
                    equation.set("Error")
            textbox.icursor("end") 
    except:
        errorString = "You selected an incorrect number before pressing "  + errorName + ".\nPlease press a button that you want, then press "  + errorName + ". " + extraString
        buttonerror.config(text=errorString)
        window.after(errorTime, clearbuttonerror)

def hyp():
    global inverted
    global buttontan
    global buttonsin
    global buttoncos
    if inverted == 0:
        inverted = inverted + 1
        buttontan.config(text="tan", command=lambda: scientificChoice("tan"))
        buttoncos.config(text="cos", command=lambda: scientificChoice("cos"))
        buttonsin.config(text="sin", command=lambda: scientificChoice("sin"))
    elif inverted == 1:
        inverted = inverted + 1
        buttontan.config(text="atan", command=lambda: scientificChoice("atan"))
        buttoncos.config(text="acos", command=lambda: scientificChoice("acos"))
        buttonsin.config(text="asin", command=lambda: scientificChoice("asin"))
    elif inverted == 2:
        inverted = 0
        buttontan.config(text="tanh", command=lambda: scientificChoice("tanh"))
        buttoncos.config(text="cosh", command=lambda: scientificChoice("cosh"))
        buttonsin.config(text="sinh", command=lambda: scientificChoice("sinh"))

def InvertAns(total):
    if textbox.get != "":
        try:
            previousans.set(total)
            equation.set(-(int(total)))
            textbox.icursor("end")
        except:
            buttonerror.config(text="You didn't select a number before inverting your\nanswer. Please press button that you want, then\npress -+. The inversion will not work on an equation,\ndecimal and negative numbers.")
            window.after(7000, clearbuttonerror)

#========================================================================================================================================================================================================================================================================================================================================================================
        
def calcscientific():
    global previousans
    global equation
    global textbox
    global buttontan
    global buttonsin
    global buttoncos
    previousans = tk.StringVar()
    equation = tk.StringVar() 
    textbox = tk.Entry(window, textvariable=equation, bg="black", fg="white", insertbackground="#3C3F41", borderwidth=10, relief=tk.SUNKEN) 
    textbox.place(relx=0, rely=0, relheight=0.1, relwidth=1)
    textbox.configure(font=("Arail", 20))
    clearbutton=tk.Button(window, text="AC", font=("Calibri", 25), command=lambda:clear(), bg="black", fg="white", activebackground="grey")
    clearbutton.place(relx=0.8,rely=0.6, relheight=0.1, relwidth=0.2)
    deletebutton=tk.Button(window, text="DEL", font=("Calibri", 25),command=lambda:[delete()], bg="black", fg="white", activebackground="grey")
    deletebutton.place(relx=0.6,rely=0.6, relheight=0.1, relwidth=0.2)
    button9=tk.Button(window, text="9", command=lambda: press(9), font=("Calibri", 25), bg="black", fg="white", activebackground="grey")
    button9.place(relx=0.4,rely=0.6, relheight=0.1, relwidth=0.2)
    button8=tk.Button(window, text="8", command=lambda: press(8), font=("Calibri", 25), bg="black", fg="white", activebackground="grey")
    button8.place(relx=0.2,rely=0.6, relheight=0.1, relwidth=0.2)
    button7=tk.Button(window, text="7", command=lambda: press(7), font=("Calibri", 25), bg="black", fg="white", activebackground="grey")
    button7.place(relx=0,rely=0.6, relheight=0.1, relwidth=0.2)
    button6=tk.Button(window, text="6", command=lambda: press(6), font=("Calibri", 25), bg="black", fg="white", activebackground="grey")
    button6.place(relx=0.4,rely=0.7, relheight=0.1, relwidth=0.2)
    button5=tk.Button(window, text="5", command=lambda: press(5), font=("Calibri", 25), bg="black", fg="white", activebackground="grey")
    button5.place(relx=0.2,rely=0.7, relheight=0.1, relwidth=0.2)
    button4=tk.Button(window, text="4", command=lambda: press(4), font=("Calibri", 25), bg="black", fg="white", activebackground="grey")
    button4.place(relx=0,rely=0.7, relheight=0.1, relwidth=0.2)
    button3=tk.Button(window, text="3", command=lambda: press(3), font=("Calibri", 25), bg="black", fg="white", activebackground="grey")
    button3.place(relx=0.4,rely=0.8, relheight=0.1, relwidth=0.2)
    button2=tk.Button(window, text="2", command=lambda: press(2), font=("Calibri", 25), bg="black", fg="white", activebackground="grey")
    button2.place(relx=0.2,rely=0.8, relheight=0.1, relwidth=0.2)
    button1=tk.Button(window, text="1", command=lambda: press(1), font=("Calibri", 25), bg="black", fg="white", activebackground="grey")
    button1.place(relx=0,rely=0.8, relheight=0.1, relwidth=0.2)
    button0=tk.Button(window, text="0", command=lambda: press(0), font=("Calibri", 25), bg="black", fg="white", activebackground="grey")
    button0.place(relx=0, rely=0.9, relheight=0.1, relwidth=0.2)
    buttonperiod=tk.Button(window, text=".", command=lambda: press("."), font=("Calibri", 25), bg="black", fg="white", activebackground="grey")
    buttonperiod.place(relx=0.2,rely=0.9, relheight=0.1, relwidth=0.2)
    buttonequals=tk.Button(window, text="=", command=lambda: calcsolve(), font=("Calibri", 25), bg="black", fg="white", activebackground="grey")
    buttonequals.place(relx=0.8,rely=0.9, relheight=0.1, relwidth=0.2)
    buttonx=tk.Button(window, text="x", command=lambda: press("*"), font=("Calibri", 25), bg="black", fg="white", activebackground="grey")
    buttonx.place(relx=0.6,rely=0.7, relheight=0.1, relwidth=0.2)
    buttondivide=tk.Button(window, text=chr(247), command=lambda: press("/"), font=("Calibri", 25), bg="black", fg="white", activebackground="grey")
    buttondivide.place(relx=0.8,rely=0.7, relheight=0.1, relwidth=0.2)
    buttonadd=tk.Button(window, text="+", command=lambda: press("+"), font=("Calibri", 25), bg="black", fg="white", activebackground="grey")
    buttonadd.place(relx=0.6,rely=0.8, relheight=0.1, relwidth=0.2)
    buttonsubtract=tk.Button(window, text="-", command=lambda: press("-"), font=("Calibri", 25), bg="black", fg="white", activebackground="grey")
    buttonsubtract.place(relx=0.8,rely=0.8, relheight=0.1, relwidth=0.2)
    previousanswer=tk.Button(window, text="Ans", command=lambda: press(previousans.get()), font=("Calibri", 25), bg="black", fg="white", activebackground="grey")
    previousanswer.place(relx=0.6,rely=0.9, relheight=0.1, relwidth=0.2)
    #Others
    howtousebutton=tk.Button(window, text="How To Use Calaculator", command=lambda: htu(), font=("Calibri", 15), bg="black", fg="white", activebackground="grey")
    howtousebutton.place(relx=0,rely=0.2, relheight=0.1, relwidth=0.6)
    invertedAnsButton=tk.Button(window, text=chr(177), command=lambda: InvertAns(equation.get()), font=("Calibri", 20), bg="black", fg="white", activebackground="grey")
    invertedAnsButton.place(relx=0.6,rely=0.2, relheight=0.1, relwidth=0.2)
    #scientific
    buttonxtenx=tk.Button(window, text="*10ˣ", command=lambda: press("*10**"), font=("Calibri", 25), bg="black", fg="white", activebackground="grey")
    buttonxtenx.place(relx=0.4,rely=0.9, relheight=0.1, relwidth=0.2)
    buttonPi=tk.Button(window, text="π", command=lambda: press(pi), font=("Calibri", 25), bg="black", fg="white", activebackground="grey")
    buttonPi.place(relx=0.8, rely=0.5, relheight=0.1, relwidth=0.2)
    buttontan=tk.Button(window, text="tan", command=lambda: scientificChoice("tan"), font=("Calibri", 25), bg="black", fg="white", activebackground="grey")
    buttontan.place(relx=0.6, rely=0.5, relheight=0.1, relwidth=0.2)
    buttoncos=tk.Button(window, text="cos", command=lambda: scientificChoice("cos"), font=("Calibri", 25), bg="black", fg="white", activebackground="grey")
    buttoncos.place(relx=0.4, rely=0.5, relheight=0.1, relwidth=0.2)
    buttonsin=tk.Button(window, text="sin", command=lambda: scientificChoice("sin"), font=("Calibri", 25), bg="black", fg="white", activebackground="grey")
    buttonsin.place(relx=0.2, rely=0.5, relheight=0.1, relwidth=0.2)
    buttonsqrt=tk.Button(window, text="√", command=lambda: scientificChoice("sqrt"), font=("Calibri", 25), bg="black", fg="white", activebackground="grey")
    buttonsqrt.place(relx=0, rely=0.5, relheight=0.1, relwidth=0.2)
    buttonlog=tk.Button(window, text="log", command=lambda: scientificChoice("log"), font=("Calibri", 25), bg="black", fg="white", activebackground="grey")
    buttonlog.place(relx=0, rely=0.4, relheight=0.1, relwidth=0.2)
    buttonhyp=tk.Button(window, text="hyp", command=lambda: hyp(), font=("Calibri", 25), bg="black", fg="white", activebackground="grey")
    buttonhyp.place(relx=0.2, rely=0.4, relheight=0.1, relwidth=0.2)
    buttonlgamma=tk.Button(window, text="lgamma", command=lambda: scientificChoice("lgamma"), font=("Calibri", 15), bg="black", fg="white", activebackground="grey")
    buttonlgamma.place(relx=0.4, rely=0.4, relheight=0.1, relwidth=0.2)
    buttonexp=tk.Button(window, text="exp", command=lambda: scientificChoice("exp"), font=("Calibri", 25), bg="black", fg="white", activebackground="grey")
    buttonexp.place(relx=0.6, rely=0.4, relheight=0.1, relwidth=0.2)
    buttonlog10=tk.Button(window, text="log10", command=lambda: scientificChoice("log10"), font=("Calibri", 20), bg="black", fg="white", activebackground="grey")
    buttonlog10.place(relx=0.8, rely=0.4, relheight=0.1, relwidth=0.2)
    buttone=tk.Button(window, text="e", command=lambda: press(math.e), font=("Calibri", 25), bg="black", fg="white", activebackground="grey")
    buttone.place(relx=0, rely=0.3, relheight=0.1, relwidth=0.2)
    buttondeg=tk.Button(window, text="deg", command=lambda: scientificChoice("deg"), font=("Calibri", 25), bg="black", fg="white", activebackground="grey")
    buttondeg.place(relx=0.2, rely=0.3, relheight=0.1, relwidth=0.2)
    buttonexpm1=tk.Button(window, text="expm1", command=lambda: scientificChoice("expm1"), font=("Calibri", 17), bg="black", fg="white", activebackground="grey")
    buttonexpm1.place(relx=0.4, rely=0.3, relheight=0.1, relwidth=0.2)
    buttonrbg=tk.Button(window, text="log2", command=lambda: scientificChoice("log2"), font=("Calibri", 25), bg="black", fg="white", activebackground="grey")
    buttonrbg.place(relx=0.6, rely=0.3, relheight=0.1, relwidth=0.2)
    buttonlog1p=tk.Button(window, text="log1p", command=lambda: scientificChoice("log1p"), font=("Calibri", 20), bg="black", fg="white", activebackground="grey")
    buttonlog1p.place(relx=0.8, rely=0.3, relheight=0.1, relwidth=0.2)
    #Error
    global buttonerror
    buttonerror=tk.Label(window, text="No Error Found", justify=CENTER, font=("Calibri",10), borderwidth=2, relief="groove", bg="black", fg="white", activebackground="grey")
    buttonerror.place(relx=0, rely=0.1, relheight=0.1, relwidth=1)
    #filemenu for Standard
    filemenu = tk.Button(window, text="File", command=lambda:filevar(), font=("Calibri", 25), bg="black", fg="white", activebackground="grey") 
    filemenu.place(relx=0.8, rely=0.2, relheight=0.1, relwidth=0.2)

    def resize(e):
        size = e.width/10

        if e.height <= 1000 and e.height >= 700:
            textbox.config(font = ("Calibri", 20))
            clearbutton.config(font=("Calibri", 25))
            deletebutton.config(font=("Calibri", 25))
            previousanswer.config(font=("Calibri", 25))
            filemenu.config(font=("Calibri", 25))
            #=======================================================================
            button9.config(font=("Calibri", 25))
            button8.config(font=("Calibri", 25))
            button7.config(font=("Calibri", 25))
            button6.config(font=("Calibri", 25))
            button5.config(font=("Calibri", 25))
            button4.config(font=("Calibri", 25))
            button3.config(font=("Calibri", 25))
            button2.config(font=("Calibri", 25))
            button1.config(font=("Calibri", 25))
            button0.config(font=("Calibri", 25))
            #=======================================================================
            buttonequals.config(font=("Calibri", 25))
            buttonperiod.config(font=("Calibri", 25))
            buttonadd.config(font=("Calibri", 25))
            buttonsubtract.config(font=("Calibri", 25))
            buttonx.config(font=("Calibri", 25))
            buttondivide.config(font=("Calibri", 25))
            #=======================================================================
            buttonerror.config(font=("Calibri", 10))
            howtousebutton.config(font=("Calibri", 15))
            invertedAnsButton.config(font=("Calibri", 20))
            #=======================================================================
            buttonxtenx.config(font=("Calibri", 25))
            buttonPi.config(font=("Calibri", 25))
            buttontan.config(font=("Calibri", 25))
            buttoncos.config(font=("Calibri", 25))
            buttonsin.config(font=("Calibri", 25))
            buttonsqrt.config(font=("Calibri", 25))
            buttonlog.config(font=("Calibri", 25))
            buttonhyp.config(font=("Calibri", 25))
            buttonlgamma.config(font=("Calibri", 15))
            buttonexp.config(font=("Calibri", 25))
            buttonlog10.config(font=("Calibri", 20))
            buttone.config(font=("Calibri", 25))
            buttondeg.config(font=("Calibri", 25))
            buttonexpm1.config(font=("Calibri", 17))
            buttonrbg.config(font=("Calibri", 25))
            buttonlog1p.config(font=("Calibri", 20))
            buttonerror.config(font=("Calibri", 10))

        elif e.height <= 1350 and e.height >= 1000:
            textbox.config(font = ("Calibri", 50))
            clearbutton.config(font=("Calibri", 40))
            deletebutton.config(font=("Calibri", 40))
            previousanswer.config(font=("Calibri", 40))
            filemenu.config(font=("Calibri", 40))
            #=======================================================================
            button9.config(font=("Calibri", 40))
            button8.config(font=("Calibri", 40))
            button7.config(font=("Calibri", 40))
            button6.config(font=("Calibri", 40))
            button5.config(font=("Calibri", 40))
            button4.config(font=("Calibri", 40))
            button3.config(font=("Calibri", 40))
            button2.config(font=("Calibri", 40))
            button1.config(font=("Calibri", 40))
            button0.config(font=("Calibri", 40))
            #=======================================================================
            buttonequals.config(font=("Calibri", 40))
            buttonperiod.config(font=("Calibri", 40))
            buttonadd.config(font=("Calibri", 40))
            buttonsubtract.config(font=("Calibri", 40))
            buttonx.config(font=("Calibri", 40))
            buttondivide.config(font=("Calibri", 40))
            #=======================================================================
            buttonerror.config(font=("Calibri", 16))
            howtousebutton.config(font=("Calibri", 24))
            invertedAnsButton.config(font=("Calibri", 32))
            #=======================================================================
            buttonxtenx.config(font=("Calibri", 40))
            buttonPi.config(font=("Calibri", 40))
            buttontan.config(font=("Calibri", 40))
            buttoncos.config(font=("Calibri", 40))
            buttonsin.config(font=("Calibri", 40))
            buttonsqrt.config(font=("Calibri", 40))
            buttonlog.config(font=("Calibri", 40))
            buttonhyp.config(font=("Calibri", 40))
            buttonlgamma.config(font=("Calibri", 24))
            buttonexp.config(font=("Calibri", 40))
            buttonlog10.config(font=("Calibri", 32))
            buttone.config(font=("Calibri", 40))
            buttondeg.config(font=("Calibri", 40))
            buttonexpm1.config(font=("Calibri", 27))
            buttonrbg.config(font=("Calibri", 40))
            buttonlog1p.config(font=("Calibri", 32))
            buttonerror.config(font=("Calibri", 15))

        elif e.height <= 2000 and e.height >= 1350:
            textbox.config(font = ("Calibri", 50))
            clearbutton.config(font=("Calibri", 40))
            deletebutton.config(font=("Calibri", 40))
            previousanswer.config(font=("Calibri", 40))
            filemenu.config(font=("Calibri", 40))
            #=======================================================================
            button9.config(font=("Calibri", 40))
            button8.config(font=("Calibri", 40))
            button7.config(font=("Calibri", 40))
            button6.config(font=("Calibri", 40))
            button5.config(font=("Calibri", 40))
            button4.config(font=("Calibri", 40))
            button3.config(font=("Calibri", 40))
            button2.config(font=("Calibri", 40))
            button1.config(font=("Calibri", 40))
            button0.config(font=("Calibri", 40))
            #=======================================================================
            buttonequals.config(font=("Calibri", 40))
            buttonperiod.config(font=("Calibri", 40))
            buttonadd.config(font=("Calibri", 40))
            buttonsubtract.config(font=("Calibri", 40))
            buttonx.config(font=("Calibri", 40))
            buttondivide.config(font=("Calibri", 40))
            #=======================================================================
            buttonerror.config(font=("Calibri", 40))
            howtousebutton.config(font=("Calibri", 40))
            invertedAnsButton.config(font=("Calibri", 40))
            #=======================================================================
            buttonxtenx.config(font=("Calibri", 40))
            buttonPi.config(font=("Calibri", 40))
            buttontan.config(font=("Calibri", 40))
            buttoncos.config(font=("Calibri", 40))
            buttonsin.config(font=("Calibri", 40))
            buttonsqrt.config(font=("Calibri", 40))
            buttonlog.config(font=("Calibri", 40))
            buttonhyp.config(font=("Calibri", 40))
            buttonlgamma.config(font=("Calibri", 40))
            buttonexp.config(font=("Calibri", 40))
            buttonlog10.config(font=("Calibri", 40))
            buttone.config(font=("Calibri", 40))
            buttondeg.config(font=("Calibri", 40))
            buttonexpm1.config(font=("Calibri", 40))
            buttonrbg.config(font=("Calibri", 40))
            buttonlog1p.config(font=("Calibri", 40))
            buttonerror.config(font=("Calibri", 30))

    window.bind('<Configure>', resize)
    window.bind('<=>', lambda event: keysolve(event, key="0"))
    window.bind('<Return>', lambda event: keysolve(event, key="1"))


def calcstandard():
    global previousans
    global equation
    global textbox
    previousans = tk.StringVar()
    equation = tk.StringVar() 
    textbox = tk.Entry(window, textvariable=equation, bg="black", fg="white", insertbackground="#3C3F41", borderwidth=10, relief=tk.SUNKEN) 
    textbox.place(relx=0, rely=0, relheight=0.2, relwidth=1)
    textbox.configure(font=("Arail", 20))
    clearbutton=tk.Button(window, text="AC", font=("Calibri", 25), command=lambda:clear(), bg="black", fg="white", activebackground="grey")
    clearbutton.place(relx=0.8,rely=0.2, relheight=0.2, relwidth=0.2)
    deletebutton=tk.Button(window, text="DEL", font=("Calibri", 25),command=lambda:[delete()], bg="black", fg="white", activebackground="grey")
    deletebutton.place(relx=0.6,rely=0.2, relheight=0.2, relwidth=0.2)
    button9=tk.Button(window, text="9", command=lambda: press(9), font=("Calibri", 25), bg="black", fg="white", activebackground="grey")
    button9.place(relx=0.4,rely=0.2, relheight=0.2, relwidth=0.2)
    button8=tk.Button(window, text="8", command=lambda: press(8), font=("Calibri", 25), bg="black", fg="white", activebackground="grey")
    button8.place(relx=0.2,rely=0.2, relheight=0.2, relwidth=0.2)
    button7=tk.Button(window, text="7", command=lambda: press(7), font=("Calibri", 25), bg="black", fg="white", activebackground="grey")
    button7.place(relx=0,rely=0.2, relheight=0.2, relwidth=0.2)
    button6=tk.Button(window, text="6", command=lambda: press(6), font=("Calibri", 25), bg="black", fg="white", activebackground="grey")
    button6.place(relx=0.4,rely=0.4, relheight=0.2, relwidth=0.2)
    button5=tk.Button(window, text="5", command=lambda: press(5), font=("Calibri", 25), bg="black", fg="white", activebackground="grey")
    button5.place(relx=0.2,rely=0.4, relheight=0.2, relwidth=0.2)
    button4=tk.Button(window, text="4", command=lambda: press(4), font=("Calibri", 25), bg="black", fg="white", activebackground="grey")
    button4.place(relx=0,rely=0.4, relheight=0.2, relwidth=0.2)
    button3=tk.Button(window, text="3", command=lambda: press(3), font=("Calibri", 25), bg="black", fg="white", activebackground="grey")
    button3.place(relx=0.4,rely=0.6, relheight=0.2, relwidth=0.2)
    button2=tk.Button(window, text="2", command=lambda: press(2), font=("Calibri", 25), bg="black", fg="white", activebackground="grey")
    button2.place(relx=0.2,rely=0.6, relheight=0.2, relwidth=0.2)
    button1=tk.Button(window, text="1", command=lambda: press(1), font=("Calibri", 25), bg="black", fg="white", activebackground="grey")
    button1.place(relx=0,rely=0.6, relheight=0.2, relwidth=0.2)
    button0=tk.Button(window, text="0", command=lambda: press(0), font=("Calibri", 25), bg="black", fg="white", activebackground="grey")
    button0.place(relx=0, rely=0.8, relheight=0.2, relwidth=0.2)
    buttonperiod=tk.Button(window, text=".", command=lambda: press("."), font=("Calibri", 25), bg="black", fg="white", activebackground="grey")
    buttonperiod.place(relx=0.2,rely=0.8, relheight=0.2, relwidth=0.2)
    buttonequals=tk.Button(window, text="=", command=lambda: calcsolve(), font=("Calibri", 25), bg="black", fg="white", activebackground="grey")
    buttonequals.place(relx=0.8,rely=0.8, relheight=0.2, relwidth=0.2)
    buttonx=tk.Button(window, text="x", command=lambda: press("*"), font=("Calibri", 25), bg="black", fg="white", activebackground="grey")
    buttonx.place(relx=0.6,rely=0.4, relheight=0.2, relwidth=0.2)
    buttondivide=tk.Button(window, text=chr(247), command=lambda: press("/"), font=("Calibri", 25), bg="black", fg="white", activebackground="grey")
    buttondivide.place(relx=0.8,rely=0.4, relheight=0.2, relwidth=0.2)
    buttonadd=tk.Button(window, text="+", command=lambda: press("+"), font=("Calibri", 25), bg="black", fg="white", activebackground="grey")
    buttonadd.place(relx=0.6,rely=0.6, relheight=0.2, relwidth=0.2)
    buttonsubtract=tk.Button(window, text="-", command=lambda: press("-"), font=("Calibri", 25), bg="black", fg="white", activebackground="grey")
    buttonsubtract.place(relx=0.8,rely=0.6, relheight=0.2, relwidth=0.2)
    previousanswer=tk.Button(window, text="Ans", command=lambda: press(previousans.get()), font=("Calibri", 25), bg="black", fg="white", activebackground="grey")
    previousanswer.place(relx=0.6,rely=0.8, relheight=0.2, relwidth=0.2)
    #filemenu for Standard
    filemenu = tk.Button(window, text="File", command=lambda:filevar(), font=("Calibri", 25), bg="black", fg="white", activebackground="grey") 
    filemenu.place(relx=0.4,rely=0.8, relheight=0.2, relwidth=0.2)

    def resize(e):
        size = e.width/10

        if e.height <= 500 and e.height >= 350:
            textbox.config(font = ("Calibri", 20))
            clearbutton.config(font=("Calibri", 25))
            deletebutton.config(font=("Calibri", 25))
            previousanswer.config(font=("Calibri", 25))
            filemenu.config(font=("Calibri", 25))
            #=======================================================================
            button9.config(font=("Calibri", 25))
            button8.config(font=("Calibri", 25))
            button7.config(font=("Calibri", 25))
            button6.config(font=("Calibri", 25))
            button5.config(font=("Calibri", 25))
            button4.config(font=("Calibri", 25))
            button3.config(font=("Calibri", 25))
            button2.config(font=("Calibri", 25))
            button1.config(font=("Calibri", 25))
            button0.config(font=("Calibri", 25))
            #=======================================================================
            buttonequals.config(font=("Calibri", 25))
            buttonperiod.config(font=("Calibri", 25))
            buttonadd.config(font=("Calibri", 25))
            buttonsubtract.config(font=("Calibri", 25))
            buttonx.config(font=("Calibri", 25))
            buttondivide.config(font=("Calibri", 25))

        elif e.height < 1000 and e.height >= 500:
            textbox.config(font = ("Calibri", 50))
            clearbutton.config(font=("Calibri", 40))
            deletebutton.config(font=("Calibri", 40))
            previousanswer.config(font=("Calibri", 40))
            filemenu.config(font=("Calibri", 40))
            #=======================================================================
            button9.config(font=("Calibri", 40))
            button8.config(font=("Calibri", 40))
            button7.config(font=("Calibri", 40))
            button6.config(font=("Calibri", 40))
            button5.config(font=("Calibri", 40))
            button4.config(font=("Calibri", 40))
            button3.config(font=("Calibri", 40))
            button2.config(font=("Calibri", 40))
            button1.config(font=("Calibri", 40))
            button0.config(font=("Calibri", 40))
            #=======================================================================
            buttonequals.config(font=("Calibri", 40))
            buttonperiod.config(font=("Calibri", 40))
            buttonadd.config(font=("Calibri", 40))
            buttonsubtract.config(font=("Calibri", 40))
            buttonx.config(font=("Calibri", 40))
            buttondivide.config(font=("Calibri", 40))

        elif e.height >= 1000:
            textbox.config(font = ("Calibri", 80))
            clearbutton.config(font=("Calibri", 60))
            deletebutton.config(font=("Calibri", 60))
            previousanswer.config(font=("Calibri", 60))
            filemenu.config(font=("Calibri", 60))
            #=======================================================================
            button9.config(font=("Calibri", 60))
            button8.config(font=("Calibri", 60))
            button7.config(font=("Calibri", 60))
            button6.config(font=("Calibri", 60))
            button5.config(font=("Calibri", 60))
            button4.config(font=("Calibri", 60))
            button3.config(font=("Calibri", 60))
            button2.config(font=("Calibri", 60))
            button1.config(font=("Calibri", 60))
            button0.config(font=("Calibri", 60))
            #=======================================================================
            buttonequals.config(font=("Calibri", 60))
            buttonperiod.config(font=("Calibri", 60))
            buttonadd.config(font=("Calibri", 60))
            buttonsubtract.config(font=("Calibri", 60))
            buttonx.config(font=("Calibri", 60))
            buttondivide.config(font=("Calibri", 60))

        elif e.height >= 2000:
            textbox.config(font = ("Calibri", 120))
            clearbutton.config(font=("Calibri", 90))
            deletebutton.config(font=("Calibri", 90))
            previousanswer.config(font=("Calibri", 90))
            filemenu.config(font=("Calibri", 90))
            #=======================================================================
            button9.config(font=("Calibri", 90))
            button8.config(font=("Calibri", 90))
            button7.config(font=("Calibri", 90))
            button6.config(font=("Calibri", 90))
            button5.config(font=("Calibri", 90))
            button4.config(font=("Calibri", 90))
            button3.config(font=("Calibri", 90))
            button2.config(font=("Calibri", 90))
            button1.config(font=("Calibri", 90))
            button0.config(font=("Calibri", 90))
            #=======================================================================
            buttonequals.config(font=("Calibri", 90))
            buttonperiod.config(font=("Calibri", 90))
            buttonadd.config(font=("Calibri", 90))
            buttonsubtract.config(font=("Calibri", 90))
            buttonx.config(font=("Calibri", 90))
            buttondivide.config(font=("Calibri", 90))

    window.bind('<Configure>', resize)
    window.bind('<=>', lambda event: keysolve(event, key="0"))
    window.bind('<Return>', lambda event: keysolve(event, key="1"))
#=======================================================================================================================================================================================================================================================================================================================================================================

calcstandard()
window.mainloop()