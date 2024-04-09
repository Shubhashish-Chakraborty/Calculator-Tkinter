
from tkinter import *
#from PIL import ImageTk,Image
import math


screen = Tk()
screen.title('CALCULATOR APP')
#screen.iconbitmap('c:/codepurposes/icon.ico')

#exiting_button_

exit = Button(screen,text="EXIT",padx=30,pady=40,borderwidth=8,fg='black',bg='grey',command=screen.quit)
exit.grid(row=5,column=0)


#ENTRY_SCREEN_

valueentry = Entry(screen,width=20,borderwidth=5,fg='light green',bg='black')
valueentry.grid(row=0,column=0,columnspan=4,padx=20,pady=20) #columnspan_important!

'''

columnspan = (number of columns used)

'''




#functional_part_

def clicktask(number):
    currentnum = valueentry.get()
    valueentry.delete(0,END)
    valueentry.insert(0, str(currentnum) + str(number))

def cleartask():
    valueentry.delete(0,END)



#now ye following functions hum code karr rhe kii koi operation button dabane ke baad kya hoga


def addop():

    num1 = valueentry.get()

    global fnum
    global OP

    fnum = float(num1)
    OP = 'addition'

    valueentry.delete(0,END)


def subop():

    num1 = valueentry.get()

    global fnum
    global OP

    fnum = float(num1)
    OP = 'subtraction'

    valueentry.delete(0,END)


def mulop():

    num1 = valueentry.get()

    global fnum
    global OP

    fnum = float(num1)
    OP = 'multiplication'

    valueentry.delete(0,END)


def divop():

    num1 = valueentry.get()

    global fnum
    global OP

    fnum = float(num1)
    OP = 'division'

    valueentry.delete(0,END)


def powop():

    num1 = valueentry.get()

    global fnum
    global OP

    fnum = float(num1)
    OP = 'power'

    valueentry.delete(0,END)


def decimalop():
    curdata = valueentry.get()
    valueentry.delete(0,END)
    valueentry.insert(0, str(curdata) + '.')



#now the following function is for the output of final answer

def RESULT():

    num2 = valueentry.get()

    global snum

    snum = float(num2)

    if OP == 'addition':
        answer = fnum + snum

    elif OP == 'subtraction':
        answer = fnum - snum

    elif OP == 'multiplication':
        answer = fnum * snum

    elif OP == 'division':
        if snum == 0:
            valueentry.delete(0,END)
            valueentry.insert(0,'ERROR')
        answer = fnum / snum

    elif OP == 'power':
        
        if (fnum == 0) and (snum == 0):

            answer = "NOT DEFINED"

        else:
            answer = math.pow(fnum,snum)


    valueentry.delete(0,END)
    valueentry.insert(0,answer)




#NUMBER_BUTTONS_

b0 = Button(screen,text='0',padx=35,pady=40,borderwidth=8,fg='white',bg='black',command= lambda: clicktask(0),font=16)
b1 = Button(screen,text='1',padx=35,pady=40,borderwidth=8,fg='white',bg='black',command= lambda: clicktask(1),font=16)
b2 = Button(screen,text='2',padx=35,pady=40,borderwidth=8,fg='white',bg='black',command= lambda: clicktask(2),font=16)
b3 = Button(screen,text='3',padx=35,pady=40,borderwidth=8,fg='white',bg='black',command= lambda: clicktask(3),font=16)
b4 = Button(screen,text='4',padx=35,pady=40,borderwidth=8,fg='white',bg='black',command= lambda: clicktask(4),font=16)
b5 = Button(screen,text='5',padx=35,pady=40,borderwidth=8,fg='white',bg='black',command= lambda: clicktask(5),font=16)
b6 = Button(screen,text='6',padx=35,pady=40,borderwidth=8,fg='white',bg='black',command= lambda: clicktask(6),font=16)
b7 = Button(screen,text='7',padx=35,pady=40,borderwidth=8,fg='white',bg='black',command= lambda: clicktask(7),font=16)
b8 = Button(screen,text='8',padx=35,pady=40,borderwidth=8,fg='white',bg='black',command= lambda: clicktask(8),font=16)
b9 = Button(screen,text='9',padx=35,pady=40,borderwidth=8,fg='white',bg='black',command= lambda: clicktask(9),font=16)


#OPERATION_BUTTONS_


b_add = Button(screen,text='+',padx=35,pady=40,borderwidth=8,fg='black',bg='grey',command=addop,font=16)
b_subtract = Button(screen,text='-',padx=35,pady=40,borderwidth=8,fg='black',bg='grey',command=subop,font=16)
b_multiply = Button(screen,text='X',padx=35,pady=40,borderwidth=8,fg='black',bg='grey',command=mulop,font=16)
b_divide = Button(screen,text='/',padx=35,pady=40,borderwidth=8,fg='black',bg='grey',command=divop,font=16)
b_power = Button(screen,text='^',padx=35,pady=40,borderwidth=8,fg='black',bg='grey',command=powop,font=16)
b_clear = Button(screen,text='Clear',padx=10,pady=10,borderwidth=8,fg='black',bg='grey',command=cleartask,font=16)
b_EQUAL = Button(screen,text='=',padx=140,pady=40,borderwidth=8,fg='black',bg='grey',command=RESULT,font=16)


b_decimal = Button(screen,text='.',padx=35,pady=40,borderwidth=8,fg='black',bg='grey',command=decimalop,font=16)


#PUTTING_NUMBER_BUTTONS_and_OPERATION_BUTTONS_ONSCREEN_


b_clear.grid(row=0,column=3)


b7.grid(row=1,column=0)
b8.grid(row=1,column=1)
b9.grid(row=1,column=2)
b_multiply.grid(row=1,column=3)

b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)
b_subtract.grid(row=2,column=3)

b1.grid(row=3,column=0)
b2.grid(row=3,column=1)
b3.grid(row=3,column=2)
b_add.grid(row=3,column=3)

b_power.grid(row=4,column=0)
b0.grid(row=4,column=1)
b_decimal.grid(row=4,column=2)
b_divide.grid(row=4,column=3)

b_EQUAL.grid(row=5,column=1,columnspan=4)#herealsocolumnspanused!



screen.mainloop()