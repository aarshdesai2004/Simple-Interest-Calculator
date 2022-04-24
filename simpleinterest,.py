
from tkinter import *
window=Tk()

window.title('Simple Interest Calculator')
window.geometry("380x400")
window.configure(bg='lightcyan')

app_label=Label(window, text="Simple Interest CALCULATOR", fg = "black", bg = "lightcyan", font=("Calibri", 20),bd=5)
app_label.place(x=50, y=20)


principal_label = Label(window,text='Enter the principal amount in Rs',fg='black',bg='grey',font=("Calibri",12),bd=1)
principal_label.place(x=20,y=100)

principal_entry = Entry(window,text="",bd=2,width=22)
principal_entry.place(x=300,y=100)

rate_label = Label(window,text='Enter the rate of interest',fg='black',bg='grey',font=("Calibri",12),bd=1)
rate_label.place(x=20,y=140)

rate_entry = Entry(window,text="",bd=2,width=22)
rate_entry.place(x=300,y=140)

time_label = Label(window,text='Enter the time period in years',fg='black',bg='grey',font=("Calibri",12),bd=1)
time_label.place(x=20,y=180)

time_entry = Entry(window,text="",bd=2,width=22)
time_entry.place(x=300,y=180)


result_frame = LabelFrame(window,text="Result", bg = "grey", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20,y=300)

result_label=Label(result_frame,text="Your result will be displayed here.", bg = "lightcyan", font=("Calibri", 12), width=55)
result_label.place(x=20,y=20)
result_label.pack()

def calculate_interest():
    p = float(principal_entry.get())
    r = float(rate_entry.get())
    t = float(time_entry.get())
    i = (p*r*t)/100
    interest = round(i,2)
    result_label.destroy() 
    message_label = Label(result_frame,text='Interest on Rs.'+str(p)+' at rate of interest '+str(r)+' for '+str(t)+' years is Rs.'+str(interest) ,fg='black',bg='grey',font=("Calibri",12),bd=1)
    message_label.place(x=20,y=40)
    message_label.pack()

calc = Button( window,text='Calculate Simple Interest',fg='black',bg='grey',bd=2,font=("Calibri",12),command=calculate_interest)  
calc.place(x=20,y=250)


window.mainloop()
