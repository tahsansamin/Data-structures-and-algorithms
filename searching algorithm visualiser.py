#algorithm visualiser
#Copyright Tahsan Samin 2021

from tkinter import *
import numpy as np
import time
import winsound
import math
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import random


window = Tk()
def get_value(choice):
    choice = variable.get()
    return choice


def get_data():
    start_in = int(l1_entry.get())
    end_in = int(l2_entry.get())
    
    global new_list
    new_list= []
    for i in range(start_in,end_in):
        new_list.append(i)

    random.shuffle(new_list)
   

    #creating plot object on tk
    fig = Figure()
    ax = fig.add_subplot(111)
    tg = new_list[::-1]
    print(new_list)

    #ax.set_x_lim(start_in,end_in)
    #ax.set_y_lim(start_in,end_in)
    ax.bar([x for x in range(len(new_list))],new_list,color=["Red"]*len(new_list))
    canvas = FigureCanvasTkAgg(fig,window)
    canvas.get_tk_widget().place(x=2,y=200)
    
    
    canvas.draw()

def draw_graph(lst,color_array):
    fig = Figure()
    ax = fig.add_subplot(111)
    tg = new_list[::-1]
    

    #ax.set_x_lim(start_in,end_in)
    #ax.set_y_lim(start_in,end_in)
    
    ax.bar([x for x in range(len(lst))],lst,color = color_array)
    canvas = FigureCanvasTkAgg(fig,window)
    canvas.get_tk_widget().place(x=2,y=200)
    
    
    canvas.draw()
    window.update_idletasks()

def merge_sort(custom_list):
    if len(custom_list)>1:
    
        mid_point = len(custom_list)//2
        left_sublist = custom_list[:mid_point]
        right_sublist = custom_list[mid_point:]
        merge_sort(left_sublist)
        merge_sort(right_sublist)
        #left counter
        i=0
    
        #right counter
        j= 0
    
        #current counter
        k=0
        
        while i<len(left_sublist) and j < len(right_sublist):
            if left_sublist[i]<right_sublist[j]:
                custom_list[k] = left_sublist[i]
                draw_graph(new_list,['green'if x==i or x==i+1 else 'red' for x in range(len(new_list))])
                i = i+1
                k = k+1
            else:
                custom_list[k] = right_sublist[j]
                draw_graph(new_list,['green'if x==j or x==j+1 else 'red' for x in range(len(new_list))])
                j+=1
                k+=1
        
        while i <len(left_sublist):
            custom_list[k] = left_sublist[i]
            draw_graph(new_list,['green'if x==i or x==i+1 else 'red' for x in range(len(new_list))])
            i+=1
            k+=1
            
        while j < len(right_sublist):
            custom_list[k] = right_sublist[j]
            draw_graph(new_list,['green'if x==j or x==j+1 else 'red' for x in range(len(new_list))])
            j+=1
            k+=1

def selection_sort(custom_list):
    for i in range(len(custom_list)):
        min_index = i
        for j in range(i+1,len(custom_list)):
            if custom_list[j]<custom_list[min_index]:
                min_index = j
        custom_list[i],custom_list[min_index] = custom_list[min_index],custom_list[i]
        draw_graph(new_list,['green'if x==j or x==j+1 else 'red' for x in range(len(custom_list))])
        time.sleep(0.0000000000000000000001)

def insertion_sort(custom_list):
    for i in range(1,len(custom_list)):
        index_to_be = custom_list[i]
        while custom_list[i-1]>index_to_be and i>0:
            custom_list[i-1],custom_list[i] = custom_list[i],custom_list[i-1]
            i= i-1
            
            draw_graph(custom_list,['green'if x==i or x==i+1 else 'red' for x in range(len(custom_list))])
        

           
            


        
    

def sort_algo():
    
    sort_type = get_value(algorithm_options)
    if sort_type == "Bubble sort":
        for i in range(len(new_list)-1,0,-1):
            for j in range(i):
                if new_list[j]>new_list[j+1]:
                    
                    
                    new_list[j],new_list[j+1] = new_list[j+1],new_list[j]
                    draw_graph(new_list,['green'if x==j or x==j+1 else 'red' for x in range(len(new_list))])
                    time.sleep(0.0000000000000000000001)
                                    
    elif sort_type == "Insertion Sort":
        insertion_sort(new_list)
        print("insertion sort")
    elif sort_type == "Selection Sort":
        selection_sort(new_list)
        print("selection sort")
        
        
            
        print(new_list)
    elif sort_type == "Merge sort":
        merge_sort(new_list)
        
        
    





    



    
    
    
window.title("Searching Algorithm Visualiser")
window.configure(width = 800,height = 800)
C= Canvas(window,bg="black",height = 150,width=500)
C.place(x=2,y=2)

mystring = StringVar()
#mystring.set("")

variable = StringVar(window)
variable.set("Algorithm type")

algorithm_options = OptionMenu(window,variable,"Bubble sort","Insertion Sort","Selection Sort","Merge sort",command=get_value)
algorithm_options.config(bg="black",fg="white")
algorithm_options["highlightthickness"]=0
algorithm_options.place(x=10,y=10)

l1 = Label(window,text = "starting number")
l1.configure(bg="black",fg="white")
l1.place(x=150,y=10)

l1_entry = Entry(window)
l1_entry.place(x=250,y=10)


l2 = Label(window,text = "ending number")
l2.configure(bg="black",fg="white")
l2.place(x=150,y=30)

l2_entry = Entry(window)
l2_entry.place(x=250,y=30)

submit = Button(window,text="Display Sorting Algorithim",bg="gray",bd=0,relief="groove",command=get_data)
submit.place(x=150,y=70)

submit2 = Button(window,text="Start sorting",bg="gray",bd=0,relief="groove",command=sort_algo)
submit2.place(x=150,y=110)




    
    
    




