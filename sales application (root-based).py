# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 18:19:29 2022

@author: ramak
"""
from tkinter import *
root= Tk()
root.title("Sales Application")
root.geometry("400x400")
root.configure(bg="light blue")

month = ('January','February','March','April','May','June','July','August','September','October','November','December')

profit=(2000, 5000, 10000, 70000, 2000, 1000, 7500, 1700, 9900, 7020, 6000, 12002)

months_label=Label(root, bg="yellow", fg="black")
months_label["text"]="Months: "+ str(month)

profit_label= Label(root, bg="yellow", fg="black")
profit_label["text"]="Profits: "+str(profit)

max_label= Label(root, bg="yellow", fg="black")

min_label=Label(root, bg="yellow", fg="black")


def getmax():
    max_profit= max(profit)
    max_profit_index= profit.index(max_profit)
    print(max_profit_index)

    max_profit_month=month[max_profit_index]
    max_label["text"]= "The maximum profit of "+ str(max_profit)+ " was recorded in the month of "+ str(max_profit_month)


def getmin():
    min_profit= min(profit)
    min_profit_index= profit.index(min_profit)
    print(min_profit_index)

    min_profit_month=month[min_profit_index]
    min_label["text"]="The minimum profit of "+ str(min_profit)+ " was recorded in the month of "+ str(min_profit_month)

btn_max= Button(root, bg="blue", fg="white", text="Get Maximum Profit", command=getmax)
btn_min= Button(root, bg="blue", fg="white", text="Get Minimum Profit", command=getmin)



months_label.place(relx=0.5, rely=0.2, anchor=CENTER)
profit_label.place(relx=0.5, rely=0.3, anchor=CENTER)
btn_max.place(relx=0.5, rely=0.4, anchor=CENTER)
max_label.place(relx=0.5, rely=0.5, anchor=CENTER)
btn_min.place(relx=0.5, rely=0.6, anchor=CENTER)
min_label.place(relx=0.5, rely=0.7, anchor=CENTER)













