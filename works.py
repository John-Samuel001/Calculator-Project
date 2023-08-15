
from tkinter import *

window=Tk()
window.geometry("450x600+100+200")
window.title("Calculator")
window.resizable(False,False)
window.configure(bg="#17161b")


label=Label(window,width=25,height=2,text="",font=("arial",30))


equation =""

def clear():
    global equation
    equation = ""
    label.config(text=equation)

button=Button(window,text="C",command=lambda: clear() ,font="bold",bd=8,width=19,height=2,bg="#25bfc4")
button.grid(row=0,column=1)
button.place(x=25, y=225)


def show(value):
    global equation
    equation+=value
    label.config(text=equation)

def calculate():
    global equation
    result =""
    if equation !="":
        try:
            result= eval(equation)
        except:
            result ="error"
            equation =""
    label.config(text=result)


button9=Button(window,text=9,command=lambda: show("9"),font="bold",bd=8,width=5,height=2,bg="#23ba92")
button9.place(x=175, y=300)


button8=Button(window,text=8,command=lambda:show("8"),font="bold",bd=8,width=5,height=2,bg="#23ba92")
button8.place(x=100, y=300)


button7=Button(window,text=7,command=lambda:show("7"),font="bold",bd=8,width=5,height=2,bg="#23ba92")
button7.place(x=25, y=300)


button4=Button(window,text=4,command=lambda:show("4"),font="bold",bd=8,width=5,height=2,bg="#23ba92")
button4.place(x=25, y=375)


button5=Button(window,text=5,command=lambda:show("5"),font="bold",bd=8,width=5,height=2,bg="#23ba92")
button5.place(x=100, y=375)


button6=Button(window,text=6,command=lambda:show("6"),font="bold",bd=8,width=5,height=2,bg="#23ba92")
button6.place(x=175, y=375)


button1=Button(window,text=1,command=lambda:show("1"),font="bold",bd=8,width=5,height=2,bg="#23ba92")
button1.place(x=25, y=450)


button2=Button(window,text=2,command=lambda:show("2"),font="bold",bd=8,width=5,height=2,bg="#23ba92")
button2.place(x=100, y=450)


button3=Button(window,text=3,command=lambda:show("3"),font="bold",bd=8,width=5,height=2,bg="#23ba92")
button3.place(x=175, y=450)


button0=Button(window,text=0,command=lambda:show("0"),font="bold",bd=8,width=12,height=2,bg="#23ba92")
button0.place(x=25, y=525)

buttondot=Button(window,text=".",command=lambda:show("."),font="bold",bd=8,width=5,height=2,bg="#23ba92")
buttondot.place(x=175, y=525)

buttonmod=Button(window,text="%",command=lambda:show("%"),font="bold",bd=8,width=5,height=2,bg="#dede10")
buttonmod.place(x=260, y=225)

buttondiv=Button(window,text="/",command=lambda:show("/"),font="bold",bd=8,width=5,height=2,bg="#dede10")
buttondiv.place(x=260, y=300)

buttonmul=Button(window,text="*",command=lambda:show("*"),font="bold",bd=8,width=5,height=2,bg="#dede10")
buttonmul.place(x=260, y=375)

buttonmin=Button(window,text="-",command=lambda:show("-"),font="bold",bd=8,width=5,height=2,bg="#dede10")
buttonmin.place(x=260, y=450)

buttonplus=Button(window,text="+",command=lambda:show("+"),font="bold",bd=8,width=5,height=2,bg="#dede10")
buttonplus.place(x=260, y=525)

buttonequal=Button(window,text="=",command=lambda:calculate(),font="bold",bd=8,width=7,height=3,bg="#15c3e6")
buttonequal.place(x=344, y=501)


# entry_widget = Entry(window,fg="red")
# entry_widget.insert(0, "Type your text here")
# entry_widget.pack()


label.pack()
window.mainloop()
