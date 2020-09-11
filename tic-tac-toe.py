import tkinter as tk
from tkinter import ttk
from datetime import datetime
win=tk.Tk()
win.title("Tic-Tac-Toe")



win_check=['','','','','','','','','']
c=0
player=['X','O']
note=ttk.Notebook(win)
note.pack(expand=True,fill='both')
page1=ttk.Frame(note)
page2=ttk.Frame(note)

note.add(page1,text="Game Page")
note.add(page2,text="Score Page")

def check_win(p,btns):   #called inside insert_val()
    x=False
    if(p==win_check[0] and p==win_check[1] and p==win_check[2]): #top left to right
        x=True
    if(p==win_check[0] and p==win_check[3] and p==win_check[6]):#top left to buttom
        x=True
    if(p==win_check[0] and p==win_check[4] and p==win_check[8]):#top left to diagonal right
        x=True
    if(p==win_check[1] and p==win_check[4] and p==win_check[7]):#top mid to diagonal buttom
        x=True
    if(p==win_check[2] and p==win_check[5] and p==win_check[8]):#top right to buttom
        x=True
    if(p==win_check[2] and p==win_check[4] and p==win_check[6]):#top right to diagonal left
        x=True
    if(p==win_check[3] and p==win_check[4] and p==win_check[5]):#mid left to right
        x=True
    if(p==win_check[6] and p==win_check[7] and p==win_check[8]):#buttom left to right
        x=True
    if(x):
        label.configure(text=p+" WON!!!",foreground="orange")
        with open('scores/score.txt','a') as op:
            time_current=datetime.now()
            time_year=time_current.strftime("%Y")
            time_month=time_current.strftime("%B")
            time_date=time_current.strftime("%d")
            time_hour=time_current.strftime("%H")
            time_min=time_current.strftime("%M")
            time_sec=time_current.strftime("%S")
            op.write(time_date+time_month+time_year+"\t\t"+time_hour+":"+time_min+":"+time_sec+"\t\t"+p+"WON!!"+"\n")

        for i in btns:
            i.configure(state='disabled')
    
def insert_val(player,l,btns): #called inside select_board()
    win_check[l-1]=player
    check_win(player,btns)

def select_board(b,loc,btns):
    global c
    if(c%2==0):
        label.configure(foreground="red",text=player[1]+" TURN!!")
        b.configure(text=player[0],state='disabled')
        insert_val(player[0],loc,btns)
    else:
        label.configure(foreground="blue",text=player[0]+" TURN!!")
        b.configure(text=player[1],state='disabled')
        insert_val(player[1],loc,btns)
    c+=1
    # print(c)

def reset_game(btn_list):
    global c
    for x in range(len(win_check)):
        win_check[x]=''
    for i in btn_list:
        i.configure(text='',state='enabled')
    label.configure(text='X TURN!!',foreground='blue')
    c=0
    # print(win_check)


label=tk.Label(page1,text="X TURN!!")    #giving labels
label.configure(foreground="blue",height=2,font=('Helvetica',30,'bold')) #works if tk.Button()
label.grid(row=0,column=2,padx=10) 

b1=ttk.Button(page1,text='',style='my.TButton',command=lambda:select_board(b1,1,btn_list))
b1.grid(row=1,column=1,ipady=60)

b2=ttk.Button(page1,text='',style='my.TButton',command=lambda:select_board(b2,2,btn_list))
b2.grid(row=1,column=2,ipady=60)

b3=ttk.Button(page1,text='',style='my.TButton',command=lambda:select_board(b3,3,btn_list))
b3.grid(row=1,column=3,ipady=60)

b4=ttk.Button(page1,text='',style='my.TButton',command=lambda:select_board(b4,4,btn_list))
b4.grid(row=2,column=1,ipady=60)

b5=ttk.Button(page1,text='',style='my.TButton',command=lambda:select_board(b5,5,btn_list))
b5.grid(row=2,column=2,ipady=60)

b6=ttk.Button(page1,text='',style='my.TButton',command=lambda:select_board(b6,6,btn_list))
b6.grid(row=2,column=3,ipady=60)

b7=ttk.Button(page1,text='',style='my.TButton',command=lambda:select_board(b7,7,btn_list))
b7.grid(row=3,column=1,ipady=60)

b8=ttk.Button(page1,text='',style='my.TButton',command=lambda:select_board(b8,8,btn_list))
b8.grid(row=3,column=2,ipady=60)

b9=ttk.Button(page1,text='',style='my.TButton',command=lambda:select_board(b9,9,btn_list))
b9.grid(row=3,column=3,ipady=60)

btn_list=[b1,b2,b3,b4,b5,b6,b7,b8,b9] #list of button variables

reset_btn=ttk.Button(page1,text='RESET',style='my.TButton',command=lambda:reset_game(btn_list))
reset_btn.grid(row=4,column=2,pady=10)
s=ttk.Style()
s.configure('my.TButton',font=('Helvetica',30))

#Second Page
def score():
    with open('scores/score.txt','r') as op:
        edit_data=op.readlines()
        c=2
        # print(edit_data)

        for x in edit_data:
            label_a=tk.Label(page2,text=x) 
            label_a.configure(foreground="orange",font=('Helvetica',15,'bold'))
            label_a.grid(row=c,column=0,sticky=tk.W)
            c+=1
def reset():
    with open('scores/score.txt','w+') as op:
        edit_data=op.readlines()
        c=2
        zz=2
        for x in range(2,10):
            label_a=tk.Label(page2,text='\t\t\t\t\t\t\t') 
            label_a.configure(foreground="white",height=2,font=('Helvetica',15,'bold'))
            label_a.grid(row=x,column=0,sticky=tk.W)
            # zz+=1
        op.write('')
date_label=tk.Label(page2,text='Date\t    Time\t    Winner')
date_label.configure(foreground="black",height=1,font=('Helvetica',30,'bold'))
date_label.grid(row=1,column=0,padx=30,sticky=tk.W)

refresh_btn=tk.Button(page2,text="Refresh Page",command=score)
refresh_btn.configure(foreground="Red")
refresh_btn.grid(row=0,column=0,padx=30)

reset_btn=tk.Button(page2,text="Reset Page",command=reset)
reset_btn.configure(foreground="Red")
reset_btn.grid(row=0,column=1,padx=30)
win.mainloop()