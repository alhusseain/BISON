from tkinter import*
from tkinter import messagebox
from tabulate import*
from simp import*
from mainfunctions import*
from equat import new
from tkinter import filedialog
root=Tk()
my_menu=Menu(root)
root.config(menu=my_menu)
file_menu=Menu(my_menu)
def forget():
    TT_frame.pack_forget()
    simp_frame.pack_forget()
    EQ_frame.pack_forget()
    read_frame.pack_forget()
def command():
    forget()
    TT_frame.pack(fill='both',expand=1)
def command2():
    forget()
    simp_frame.pack(fill='both',expand=1)
def command3():
    forget()
    EQ_frame.pack(fill='both',expand=1)
def command4():
    forget()
    read_frame.pack(fill='both',expand=1)
my_menu.add_cascade(label='apps',menu=file_menu)
file_menu.add_command(label='Truth table',command=command)
file_menu.add_separator()
file_menu.add_command(label='simplifier',command=command2)
file_menu.add_separator()
file_menu.add_command(label='equation',command=command3)
file_menu.add_separator()
file_menu.add_command(label='read',command=command4)
file_menu.add_separator()
file_menu.add_command(label='Exit',command=root.quit)



TT_frame=Frame(root)
TT_frame.pack(fill='both',expand=1)
label1_TT=Label(TT_frame)
label2_TT=Label(TT_frame)
mylab1_TT=Label(TT_frame)
mylab2_TT=Label(TT_frame)
mylab3_TT=Label(TT_frame)
mylab11_TT=Label(TT_frame)
mylab21_TT=Label(TT_frame)
mylab31_TT=Label(TT_frame)

textarea=Label(TT_frame)
entr=Entry(TT_frame,width=40,borderwidth=10)
entr.pack()
v_s = Scrollbar(TT_frame)
v_s.pack(side=RIGHT,fill=Y)

def enter_TT():
     global nu_input
     nu_input=int(entr.get())
     if nu_input>26:
        messagebox.showinfo('error','max inputs is 26')
     nu_input=int(entr.get())
     entr.delete(0,END)
def calculate():
     min_index=entr.get().split('+')
     mox=maxx(nu_input)
     if int(max(min_index))>mox:
          messagebox.showinfo('error','max minterm is'+str(mox))
          entr.delete(0,END)
     min_index=entr.get().split('+')
     entr.delete(0,END)
     truth_tbl=truth_table(nu_input)
     minterms=minterm(truth_tbl,min_index)
     equ=equation(minterms)
     global label1_TT
     global label2_TT
     global mylab2_TT
     global mylab3_TT
     global textarea
     global mylab1_TT
     global mylab11_TT
     global mylab21_TT
     textarea.pack_forget()
     label1_TT.pack_forget()
     label2_TT.pack_forget()
     label1_TT=Label(TT_frame,text=tabulate(minterms,tablefmt="psql"))
     mylab1_TT.pack_forget()
     mylab2_TT.pack_forget()
     mylab3_TT.pack_forget()
     mylab11_TT.pack_forget()
     mylab21_TT.pack_forget()
     #mylab31_TT.pack_forget()
     # label1_TT.pack()
     textarea = Text(TT_frame,wrap=NONE,
                yscrollcommand=v_s.set)

     v_s.config(command=textarea.yview)
     textarea.insert(END,tabulate(minterms,tablefmt="psql"))
     textarea.pack()
     count=1000
     count1=1000
     #while count1>0:
     while count>2:
          before,after,equ,count=simplification(equ)
          mylab1_TT=Label(TT_frame,text=before,bg='white',fg='black')
          mylab1_TT.pack()
          mylab2_TT=Label(TT_frame,text=after,bg='white',fg='black')
          mylab2_TT.pack()
          #mylab3_TT=Label(TT_frame,text='+'.join(equ),bg='white',fg='black')
          #mylab3_TT.pack()
     while count1>0:
         before,after,equ,count1=simplification2(equ)
         mylab11_TT=Label(TT_frame,text=before,bg='white',fg='black')
         mylab11_TT.pack()
         mylab21_TT=Label(TT_frame,text=after,bg='white',fg='black')
         mylab21_TT.pack()
         #mylab3_TT=Label(TT_frame,text='+'.join(equ),bg='white',fg='black')
         #mylab3_TT.pack()


     for i in truth_tbl:
         del i[-1]
button1_TT=Button(TT_frame,text='Enter truth table size',padx=40,pady=20,bg='white',command=enter_TT)
button2_TT=Button(TT_frame,text='Enter minterms',padx=40,pady=20,bg='white',command=calculate)
button1_TT.pack()
button2_TT.pack()

#**************************************************************************************************************
simp_frame=Frame(root,bg='black')
new_input=Entry(simp_frame,width=48,borderwidth=5,bg='silver')
new_input.pack()
calc=Frame(simp_frame,bg='black')
calc.pack()
label1=Frame(simp_frame)
label2=Frame(simp_frame)
mylab2_SS=Frame(simp_frame)
mylab3_SS=Frame(simp_frame)
def buttoon(letter):
    current=new_input.get()
    new_input.delete(0,END)
    new_input.insert(0,str(current)+str(letter))
def clt():
    minterm=new_input.get()
    new_input.delete(0,END)
    new=minterm.split('+')
    global label1
    global label2
    global mylab2_SS
    global mylab3_SS
    label1.pack_forget()
    label2.pack_forget()
    mylab2_SS.pack_forget()
    mylab3_SS.pack_forget()
    label1=Label(simp_frame,text=minterm,bg='black',fg='white')
    label1.pack()
    count=1000
    while count>2:
        before,after,new,count=simplification(new)
        mylab2_SS=Label(simp_frame,text=after,bg='black',fg='white')
        mylab3_SS=Label(simp_frame,text='+'.join(new),bg='black',fg='white')
        mylab2_SS.pack()
        mylab3_SS.pack()
    count=1000
    
button_A=Button(calc,text='A',padx=40,pady=20,command=lambda:buttoon('A'))
button_B=Button(calc,text='B',padx=45,pady=20,command=lambda:buttoon('B'))
button_C=Button(calc,text='C',padx=40,pady=20,command=lambda:buttoon('C'))
button_D=Button(calc,text='D',padx=45,pady=20,command=lambda:buttoon('D'))
button_not=Button(calc,text="'",padx=40,pady=52,command=lambda:buttoon("'"))
button_plus=Button(calc,text='+',padx=40,pady=20,command=lambda:buttoon('+'))
button_calc=Button(calc,text='calc',padx=40,pady=20,command=clt)
button_A.grid(row=1,column=0)
button_B.grid(row=1,column=1)
button_C.grid(row=2,column=0)
button_D.grid(row=2,column=1)
button_not.grid(row=1,column=2,rowspan=2)
button_plus.grid(row=3,column=0)
button_calc.grid(row=3,column=1)
#_________________________________________________________________________________________________________
EQ_frame=Frame(root,bg='black')
label1=Label(EQ_frame)
entery=Entry(EQ_frame,width=40,borderwidth=10,bg='white',fg='black')
entery.pack()
def enter():
    global p
    p=int(entery.get())
    entery.delete(0,END)
    if p>4:
        messagebox.showinfo('error',"Sorry, This program can't create a truth table of a function with more variables than 4")
def put():
    f=entery.get()
    entery.delete(0,END)
    global label1
    label1.pack_forget()
    label1=Label(EQ_frame,text=new(p,f),bg='black',fg='white')
    label1.pack()
size=Button(EQ_frame,text='Enter size',padx=40,pady=20,bg='white',command=enter)
size.pack()
minterms=Button(EQ_frame,text='Enter equation',padx=40,pady=20,command=put)
minterms.pack()
#________________________________________________________________________________________________________
read_frame=Frame(root,bg='black')
label_R=Label(read_frame)
label1_R=Label(read_frame)
mylab2_R=Label(read_frame)
def openfile():
    user_file = filedialog.askopenfilename(initialdir="C:\\Users\\SMART SETORE\\PycharmProjects\\pythonProject1\\venv\\hola", title='Please select a file to open')
    lines = []
    with open(user_file, 'r') as f:
        for line in f:
            elements = line.split()
            for i in range(len(elements)):
                elements[i]=int(elements[i])
            lines.append(elements)
        print(lines)
    global label_R
    global label1_R
    global mylab2_R
    label_R.pack_forget()
    label1_R.pack_forget()
    mylab2_R.pack_forget()
    label_R=Label(read_frame,text=tabulate(lines,tablefmt="psql"),bg='black',fg='white')
    label1_R=Label(read_frame,text='+'.join(equation(lines)),bg='black',fg='white')
    label_R.pack()
    label1_R.pack()
    count=1000
    while count>2:
        before,after,eq,count=simplification(equation(lines))
        mylab2_R=Label(read_frame,text=after,bg='black',fg='white')
        mylab2_R.pack()
button = Button(read_frame,text='Open file', command=openfile)
button.pack()

root.mainloop()
