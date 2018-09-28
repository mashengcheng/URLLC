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

#from __future__ import division 
import matplotlib
import math

#default parameters
var_lambda = 20.0
var_service = 50.0
var_num_server = 3
var_a = 1
var_b = 2
var_epsilon = 0.01
var_delay = 1

str_lambda=''
str_service=''
str_num_server=''
str_a=''
str_b=''
str_epsilon=''
str_delay=''

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
    var_lambda.set
    
def calculate_delay():
    var_lambda = float(e_lambda.get())
    var_service = float(e_C.get())
    var_num_server = float(e_number.get())
    var_a = float(e_a.get())
    var_b = float(e_b.get())
    var_b = float(e_epsilon.get())
    
    delay = 1/(var_service - var_lambda) * ((var_num_server+1)//var_b) *\
    math.log(var_a*(var_num_server+1)//var_epsilon)
    
    print(delay)
    
    

    
window = Tk()
window.geometry("800x400+10+10")
window.title("SNC Tool")

label_top = Label(window, text='URLLC Simulator')
label_top.config(font='Helvetica -15 bold')
label_top.place(anchor='center' )
label_top.pack()

frame_input = Frame(window)
frame_input.place(x=20, y=30)
frame_input.pack(fill=X)

#arrival rate
l_lambda = Label(frame_input, text='Arrival Rate')
l_lambda.grid(row=1, column=0)

e_lambda = Entry(frame_input, textvariable=str_lambda)
e_lambda.grid(row=1, column=1)

#service rate
l_C = Label(frame_input, text='Service Rate')
l_C.grid(row=2, column=0)

e_C = Entry(frame_input, textvariable=str_service)
e_C.grid(row=2, column=1)

#number of servers
l_number = Label(frame_input, text='Server count')
l_number.grid(row=3, column=0)

e_number = Entry(frame_input, textvariable=str_num_server)
e_number.grid(row=3, column=1)

#var a
l_a = Label(frame_input, text='a')
l_a.grid(row=4, column=0)

e_a = Entry(frame_input, textvariable=str_a)
e_a.grid(row=4, column=1)

#var b
l_b = Label(frame_input, text='b')
l_b.grid(row=5, column=0)

e_b = Entry(frame_input, textvariable=str_b)
e_b.grid(row=5, column=1)

#var epsilon
l_epsilon = Label(frame_input, text='violation probability')
l_epsilon.grid(row=6, column=0)

e_epsilon = Entry(frame_input, textvariable=str_epsilon)
e_epsilon.grid(row=6, column=1)

#var delay
l_delay = Label(frame_input, text='Latency')
l_delay.grid(row=7, column=0)

e_delay = Entry(frame_input, textvariable=str_delay)
e_delay.grid(row=7, column=1)

b_cal = Button(frame_input, text='Calculate', command = calculate_delay)
b_cal.grid(row=8, column = 0)

l_result = Label(frame_input, text='Latency: ')
l_result.grid(row=8, column = 1)

b1 = Button(frame_input, text="Run", command = test_var)
b1.grid(row=9, column = 0)   #这个位置是按钮在左上角的位置的坐标。

window.mainloop()
print('test')


