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
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

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

pic_label = ""

#测试函数
def test_var():
    #print(var_lambda, var_service)
    #show message
    window.update()
    var_lambda = float(e_lambda.get())
    var_service = float(e_C.get())
    print(var_lambda,var_service)
    messagebox.showinfo('Parameters', 'arrival rate:%f\nservice rate:%f '\
                        %(var_lambda,var_service))
    
#将多有的输入参数的文本框清空
def clear_entry():
    str_lambda.set("")
    str_service.set("")    
    str_num_server.set("")
    str_a.set("")
    str_b.set("")
    str_epsilon.set("")
    str_delay.set("")
    #l_result.config(text="Latency:")
    
#计算时延
def calculate_delay():
    var_lambda = float(str_lambda.get())    #泊松分布的数据到达速率
    var_service = float(str_service.get())    #系统提供的服务速率
    var_num_server = float(str_num_server.get())    #串联服务节点的数量
    var_a = float(str_a.get())    #服务概率边界参数a
    var_b = float(str_b.get())    #服务概率边界参数b
    var_epsilon = float(str_epsilon.get())    #时延概率边界epsilon
    
    delay = 1/(var_service - var_lambda) * ((var_num_server+1)/var_b) *\
    math.log(var_a*(var_num_server+1)/var_epsilon)
    
    str_delay.set(str(delay))
    #e_delay.config(text=str(delay))
    #print(delay)
    
 
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
l_number = Label(frame_input, text='Number of Servers')
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
l_epsilon = Label(frame_input, text='Violation Probability')
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

l_compare = Label(frame_input, text='变更参数')
l_compare.grid(row=10, column = 0)

compare_label = StringVar()
comb2 = ttk.Combobox(frame_input,textvariable=compare_label)
comb2['values']=('Arrival Rate','Service Rate','Number of Server',\
          'a','b','Violation Probability','Latency (ms)')
comb2.grid(row=10, column=1)
#comb2.current(0)

def highlight_compare(*args):    
    l_lambda.config(text='Arrival Rate')
    l_C.config(text='Service Rate')
    l_number.config(text='Number of Servers')
    l_a.config(text='a')
    l_b.config(text='b')
    l_epsilon.config(text='Violation')
    global pic_label
    if compare_label.get()[:1] == var_comb1.get()[:1]:
        messagebox.showinfo('Error!','Select a repetitive Parameters!')
        return;
    if compare_label.get().startswith("Arrival"):
        l_lambda.config(text='Arrival Rate -->>>>')        
        pic_label = "Arrival Rate:"
        #在这里就知道改的是哪个了！
    elif compare_label.get().startswith("Service"):
        l_C.config(text='Service Rate -->>>>')
        pic_label = "Service Rate:"
    elif compare_label.get().startswith("Number"):
        l_number.config(text='Number of Servers -->>>>')
        pic_label = "Number of Servers: "
    elif compare_label.get().startswith("a"):
        l_a.config(text='a -->>>>')
        pic_label = "a"
    elif compare_label.get().startswith("b"):
        l_b.config(text='b -->>>>')
        pic_label = "b"
    elif compare_label.get().startswith("Violation"):
        l_epsilon.config(text='Violation -->>>>')
        pic_label = "Violation Probability"
    #messagebox.showinfo('Parameters', 'label: %s '%(pic_label))
    

comb2.bind("<<ComboboxSelected>>", highlight_compare)

#画图的按钮
def draw_line():
    pic = f.add_subplot(111)
    #pic = f.subplot(111) 
    var_lambda = float(str_lambda.get())
    var_service = float(str_service.get())
    var_num_server = float(str_num_server.get())
    var_a = float(str_a.get())
    var_b = float(str_b.get())
    var_epsilon = float(str_epsilon.get())
    cur_var = ""
    global pic_label
    if pic_label.startswith("Arrival"):
        cur_var = str_lambda.get() + "Gbit/s"
    elif pic_label.startswith("Servic"):
        cur_var = str_service.get() + "Gbit/s"
    elif pic_label.startswith("Number"):
        cur_var = str_num_server.get()
    elif pic_label.startswith("a"):
        cur_var = str_a.get()
    elif pic_label.startswith("b"):
        cur_var = str_b.get()
    elif pic_label.startswith("Violation"):
        cur_var = str_epsilon.get()   
    
    #messagebox.showinfo('Parameters', 'label: %s '%(pic_label))
    if scope_1.get() == "":
        messagebox.showerror("INPUT","Empty blank!")
        return
        
    pic_label_cur = "%s %s" %(pic_label,cur_var)
    
    if var_comb1.get().startswith("Arrival"):
        scope = scope_1.get().split(':')
        var_lambda = np.linspace(float(scope[0]),float(scope[1]),int(scope[2]))
        delay = 1/(var_service - var_lambda) * ((var_num_server+1)/var_b) *\
    np.log(var_a*(var_num_server+1)/var_epsilon)        
        pic.plot(var_lambda, delay, label=pic_label_cur)    
        pic.set_xlabel('Arrival Rate (Gbit/s)', fontsize=10)       
        
    elif var_comb1.get().startswith("Service"):
        scope = scope_1.get().split(':')
        var_service = np.linspace(float(scope[0]),float(scope[1]),int(scope[2]))  
        print(var_service)
        delay = 1/(var_service - var_lambda) * ((var_num_server+1)/var_b) *\
    np.log(var_a*(var_num_server+1)/var_epsilon)        
        pic.plot(var_service, delay, label=pic_label_cur)  
        pic.set_xlabel('Service Rate (Gbit/s)', fontsize=10)  
        
    elif var_comb1.get().startswith("Number"):
        scope = scope_1.get().split(':')
        var_num_server= np.linspace(float(scope[0]),float(scope[1]),int(scope[2]))
        delay = 1/(var_service - var_lambda) * ((var_num_server+1)/var_b) *\
    np.log(var_a*(var_num_server+1)/var_epsilon)
        #pic_label_cur = "%s %s" %(pic_label,cur_var)
        pic.plot(var_num_server, delay, label=pic_label_cur)  
        pic.set_xlabel('Number of Servers', fontsize=10)  
        
    elif var_comb1.get().startswith("Violation"):
        scope = scope_1.get().split(':')
        var_epsilon = np.linspace(float(scope[0]),float(scope[1]),int(scope[2]))
        delay = 1/(var_service - var_lambda) * ((var_num_server+1)/var_b) *\
    np.log(var_a*(var_num_server+1)/var_epsilon)                
        pic.plot(var_epsilon, delay, label=pic_label_cur)         
        pic.set_xlabel('Violation Probability', fontsize=10)  
    
    pic.set_ylabel('Delay (ms)', fontsize=10)   
    pic.grid(True)
    
    if pic_label != "":
        pic.legend()
            
    canvas.draw()

b_draw_line = Button(frame_input, text='Draw Line', command = draw_line)
b_draw_line.grid(row=11, column=0)


def save_figure():
    figure_name = '%s.jpg'%(compare_label.get());
    #if(os.path.exists(figure_name)):
    #    figure_name = '%s_%s.jpg'%(figure_name, 'new');
    f.savefig(figure_name);
    messagebox.showinfo('Info!', 'Save figure: %s '%(figure_name))

b_save_figure = Button(frame_input, text='Save Figure', command = save_figure)
b_save_figure.grid(row=12, column=0)

#清除图像的按钮
def clear_pic():
    f.clf()
    pic_label = ""
    canvas.draw()    
    
b_clear = Button(frame_input, text='Clear Figure', command = clear_pic)
b_clear.grid(row=11,column=1)


f = Figure(figsize=(5,4), dpi=100)
canvas = FigureCanvasTkAgg(f, master=frame_pic)
canvas.draw() 
canvas.get_tk_widget().grid(row=0, columnspan=3) 


window.mainloop()
print('test')


