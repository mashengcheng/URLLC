# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 08:55:54 2018

@author: mark
"""

# a snc simulator

import sys
import os
from tkinter import *
from tkinter import messagebox
from tkinter import X
from tkinter import ttk


#from __future__ import division 
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
import math

#public 
hold_picture = False

#default parameters
var_lambda = 20.0
var_service = 50.0
var_num_server = 3
var_a = 1
var_b = 2
var_epsilon = 0.01
var_delay = 1


def test_var():
    #print(var_lambda, var_service)
    #show message
    window.update()
    var_lambda = float(e_lambda.get())
    var_service = float(e_C.get())
    print(var_lambda,var_service)
    messagebox.showinfo('Parameters', 'arrival rate:%f\nservice rate:%f '\
                        %(var_lambda,var_service))
    
def clear_entry():
    str_lambda.set("")
    str_service.set("")    
    str_num_server.set("")
    str_a.set("")
    str_b.set("")
    str_epsilon.set("")
    str_delay.set("")
    #l_result.config(text="Latency:")
    
    
def calculate_delay():
    var_lambda = float(str_lambda.get())
    var_service = float(str_service.get())
    var_num_server = float(str_num_server.get())
    var_a = float(str_a.get())
    var_b = float(str_b.get())
    var_epsilon = float(str_epsilon.get())
    
    delay = 1/(var_service - var_lambda) * ((var_num_server+1)/var_b) *\
    math.log(var_a*(var_num_server+1)/var_epsilon)
    
    str_delay.set(str(delay))
    #e_delay.config(text=str(delay))
    #print(delay)
    
matplotlib.use('TkAgg') 
window = Tk()
window.geometry("900x450+10+10")
window.title("SNC Tool")
window.resizable(width=True, height=True)

label_top = Label(window, text='URLLC Simulator')
label_top.config(font='Helvetica -15 bold')
label_top.place(anchor='center' )
label_top.pack()

#frame_label1 = Frame(window)
#frame_label1.pack(side=LEFT)

frame_input = Frame(window)
#frame_input.place(x=20, y=30)
frame_input.pack(side=LEFT)

frame_pic = Frame(window)
#frame_pic.place(x=400,y=30)
frame_pic.pack(side=RIGHT)


l_input = Label(frame_input, text='参数输入')
l_input.grid(row=0, column=0)

#arrival rate
l_lambda = Label(frame_input, text='Arrival Rate')
l_lambda.grid(row=1, column=0)

str_lambda=StringVar()
e_lambda = Entry(frame_input, textvariable=str_lambda)
e_lambda.grid(row=1, column=1)
e_lambda.insert(0,'20')

l_lambda_unit = Label(frame_input, text='Gbit/s')
l_lambda_unit.grid(row=1, column=2)

#service rate
l_C = Label(frame_input, text='Service Rate')
l_C.grid(row=2, column=0)

str_service=StringVar()
e_C = Entry(frame_input, textvariable=str_service)
e_C.grid(row=2, column=1)
e_C.insert(0,'46')

l_C_unit = Label(frame_input, text='Gbit/s')
l_C_unit.grid(row=2, column=2)

#number of servers
l_number = Label(frame_input, text='Server count')
l_number.grid(row=3, column=0)

str_num_server=StringVar()
e_number = Entry(frame_input, textvariable=str_num_server)
e_number.grid(row=3, column=1)
e_number.insert(0,'3')

#var a
l_a = Label(frame_input, text='a')
l_a.grid(row=4, column=0)

str_a=StringVar()
e_a = Entry(frame_input, textvariable=str_a)
e_a.grid(row=4, column=1)
e_a.insert(0,'1')

#var b
l_b = Label(frame_input, text='b')
l_b.grid(row=5, column=0)

str_b=StringVar()
e_b = Entry(frame_input, textvariable=str_b)
e_b.grid(row=5, column=1)
e_b.insert(0,'3')

#var epsilon
l_epsilon = Label(frame_input, text='violation probability')
l_epsilon.grid(row=6, column=0)

str_epsilon=StringVar()
e_epsilon = Entry(frame_input, textvariable=str_epsilon)
e_epsilon.grid(row=6, column=1)
e_epsilon.insert(0,'0.00001')

#var delay
l_delay = Label(frame_input, text='Latency')
l_delay.grid(row=7, column=0)

str_delay=StringVar()
e_delay = Entry(frame_input, textvariable=str_delay)
e_delay.grid(row=7, column=1)

l_lambda_unit = Label(frame_input, text='ms')
l_lambda_unit.grid(row=7, column=2)

b_cal = Button(frame_input, text='Calculate', command = calculate_delay)
b_cal.grid(row=8, column = 0)

b1 = Button(frame_input, text="Clear", command = clear_entry)
b1.grid(row=8, column = 1)   #这个位置是按钮在左上角的位置的坐标。


#准备画图的数据
var_comb1 = StringVar()
comb1 = ttk.Combobox(frame_input,textvariable=var_comb1)
comb1['values']=('Arrival Rate (Gbit/s)','Service Rate (Gbit/s)','Number of Server',\
          'Violation Probability','Latency (ms)')
comb1.grid(row=9, column = 0)

scope_1 = StringVar()
e_scope1 = Entry(frame_input, textvariable=scope_1)
e_scope1.grid(row=9, column = 1)


#画图的按钮
def draw_line():
    '''
    x = np.linspace(0,2,100)
    var_lambda = float(str_lambda.get())
    var_service = float(str_service.get())
    var_num_server = float(str_num_server.get())
    var_a = float(str_a.get())
    var_b = float(str_b.get())
    var_epsilon = float(str_epsilon.get())       
    '''         
    pic = f.add_subplot(111)
    #pic = f.subplot(111) 
    var_lambda = float(str_lambda.get())
    var_service = float(str_service.get())
    var_num_server = float(str_num_server.get())
    var_a = float(str_a.get())
    var_b = float(str_b.get())
    var_epsilon = float(str_epsilon.get())
    
    if scope_1.get() == "":
        messagebox.showerror("INPUT","Empty blank!")
        return
        
    if var_comb1.get().startswith("Arrival"):
        scope = scope_1.get().split(':')
        var_lambda = np.linspace(float(scope[0]),float(scope[1]),int(scope[2]))
        delay = 1/(var_service - var_lambda) * ((var_num_server+1)/var_b) *\
    np.log(var_a*(var_num_server+1)/var_epsilon)
        pic.plot(var_lambda, delay, label='linear')    
        pic.set_xlabel('Arrival Rate (Gbit/s)', fontsize=10)       
        
    elif var_comb1.get().startswith("Service"):
        scope = scope_1.get().split(':')
        var_service = np.linspace(float(scope[0]),float(scope[1]),int(scope[2]))  
        print(var_service)
        delay = 1/(var_service - var_lambda) * ((var_num_server+1)/var_b) *\
    np.log(var_a*(var_num_server+1)/var_epsilon)
        pic.plot(var_service, delay, label='linear')  
        
    elif var_comb1.get().startswith("Number"):
        scope = scope_1.get().split(':')
        var_num_server= np.linspace(float(scope[0]),float(scope[1]),int(scope[2]))
        delay = 1/(var_service - var_lambda) * ((var_num_server+1)/var_b) *\
    np.log(var_a*(var_num_server+1)/var_epsilon)
        pic.plot(var_num_server, delay, label='linear')  
        
    elif var_comb1.get().startswith("Violation"):
        scope = scope_1.get().split(':')
        var_epsilon = np.linspace(float(scope[0]),float(scope[1]),int(scope[2]))
        delay = 1/(var_service - var_lambda) * ((var_num_server+1)/var_b) *\
    np.log(var_a*(var_num_server+1)/var_epsilon)
        pic.plot(var_epsilon, delay, label='linear') 
    
    pic.set_ylabel('Delay (ms)', fontsize=10)   
    pic.grid(True)
    canvas.draw()

b_draw_line = Button(frame_input, text='Draw Line', command = draw_line)
b_draw_line.grid(row=10, column=0)


#清除图像的按钮
def clear_pic():
    f.clf()
    canvas.draw()    
    
b_clear = Button(frame_input, text='Clear Figure', command = clear_pic)
b_clear.grid(row=10,column=1)


f = Figure(figsize=(5,4), dpi=100)
canvas = FigureCanvasTkAgg(f, master=frame_pic)
canvas.show() 
canvas.get_tk_widget().grid(row=0, columnspan=3) 

#canvas = Canvas(frame_pic,width=400, height=500)
#canvas.create_image(0,0, image=photo)
#canvas.grid(row=0,column=0)
#img_label = Label(frame_pic, image=photo)
#img_label.grid(row=0,column=0)


window.mainloop()
print('test')


