from tkinter import *
import parser

root = Tk()
root.configure(background="lightblue")
root.title("Calculator")

#get the user input
i = 0
def get_val(num):
    global i
    display.insert(i,num)
    i += 1

def calculate():
    entire_string = display.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        clear_all()
        display.insert(0,result)
    except Exception:    
        clear_all()
        display.insert(0,"Error")

        
def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i,operator)
    i += length


def clear_all():
    display.delete(0,END)

def clear_ele():
    entire_string = display.get()
    if len(entire_string):
        new_string =entire_string[:-1]
        clear_all()
        display.insert(0,new_string)   
    else:
        clear_all()
        display.insert(0,"ERROR")   




#adding the input field
display = Entry(root)
display.grid(row=1,columnspan=6,sticky=W+E)
 
#adding buttons to the Calculator

Button(root,text="1",bg="green",command = lambda:get_val(1),height=1,width=2,border=5).grid(row=2,column=0)
Button(root,text="2",bg="green",command = lambda:get_val(2),height=1,width=2,border=5).grid(row=2,column=1)
Button(root,text="3",bg="green",command = lambda:get_val(3),height=1,width=2,border=5).grid(row=2,column=2)

Button(root,text="4",bg="green",command = lambda:get_val(4),height=1,width=2,border=5).grid(row=3,column=0)
Button(root,text="5",bg="green",command = lambda:get_val(5),height=1,width=2,border=5).grid(row=3,column=1)
Button(root,text="6",bg="green",command = lambda:get_val(6),height=1,width=2,border=5).grid(row=3,column=2)

Button(root,text="7",bg="green",command = lambda:get_val(7),height=1,width=2,border=5).grid(row=4,column=0)
Button(root,text="8",bg="green",command = lambda:get_val(8),height=1,width=2,border=5).grid(row=4,column=1)
Button(root,text="9",bg="green",command = lambda:get_val(9),height=1,width=2,border=5).grid(row=4,column=2,padx=1)

Button(root,text="AC",bg="green",command = lambda:clear_all(),height=1,width=2,border=5).grid(row=5,column=0)
Button(root,text="0",bg="green",height=1,width=2,border=5).grid(row=5,column=1)
Button(root,text="=",bg="green",command= lambda:calculate(),height=1,width=2,border=5).grid(row=5,column=2)

Button(root,text="+",bg="green",command= lambda:get_operation("+"),height=1,width=2,border=5).grid(row=2,column=3)
Button(root,text="-",bg="green",command= lambda:get_operation("-"),height=1,width=2,border=5).grid(row=3,column=3)
Button(root,text="*",bg="green",command= lambda:get_operation("*"),height=1,width=2,border=5).grid(row=4,column=3)
Button(root,text="/",bg="green",command= lambda:get_operation("/"),height=1,width=2,border=5).grid(row=5,column=3)

Button(root,text="pi",bg="green",command= lambda:get_operation("*3.14"),height=1,width=2,border=5).grid(row=2,column=4)
Button(root,text="%",bg="green",command= lambda:get_operation("%"),height=1,width=2,border=5).grid(row=3,column=4)
Button(root,text="(",bg="green",command= lambda:get_operation("("),height=1,width=2,border=5).grid(row=4,column=4)
Button(root,text="exp",bg="green",command= lambda:get_operation("**"),height=1,width=2,border=5).grid(row=5,column=4)

Button(root,text="Clr",bg="green",command = lambda:clear_ele(),height=1,width=2,border=5).grid(row=2,column=5)
Button(root,text=")",bg="green",command= lambda:get_operation(")"),height=1,width=2,border=5).grid(row=3,column=5)
Button(root,text="^2",bg="green",command= lambda:get_operation("**2"),height=1,width=2,border=5).grid(row=4,column=5)




root.mainloop()