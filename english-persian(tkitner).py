from tkinter import *
from dictin import getit
from tkinter import messagebox as msg
from tkinter import ttk
from ttkthemes import ThemedTk

myfile=open('setting.txt')
try :
    q=myfile.readline()
except :
    myfile.write('1')
    myfile.close()
    myfile=open('setting.txt')
    q='1'
    print(1)
if q=='1':
    root = ThemedTk(theme="equilux")
else:
    root = ThemedTk(theme="vista (windows 8)")
q=myfile.readline()
myfile.close()
root.title('english-persian')

tabcontrol=ttk.Notebook(root)
tab1=ttk.Frame(tabcontrol)
tab2=ttk.Frame(tabcontrol)
tabcontrol.add(tab1,text='Convert')
tabcontrol.add(tab2,text='Setting')
tabcontrol.pack(expand=1,fill='both')
root.geometry('450x130')
root.resizable(width=False,height=False)

def sett():
    qwe=v.get()
    myfile=open('setting.txt','w')
    if v.get()==1:
        myfile.write('0')
    else:
        myfile.write('1')
    myfile.close()
    msg.showinfo('success','changes successfully saved')
    msg.showwarning('update','please re open to update changes')
myfile=open('setting.txt')
q2=myfile.readline()

v=IntVar(root,int(q2)+1)
myfile.close()
y=10
ttk.Radiobutton(tab2, text =' Light mode',value = 1 ,variable =v).place(x=10,y=y)
y=40
ttk.Radiobutton(tab2, text =' Dark mode',value = 2,variable =v).place(x=10,y=y)
ttk.Button(tab2,text='Save',style='TButton',width=37,command=sett).place(x=10,y=70)

def ok():
    name2=getit(name.get())
    if name2.find('\n')!=-1:
        name2=name2[:name2.find('\n')]+'...'
    if len(name2)>30:
        name2=name2[:30]+'...'
    lab.configure(text=name2)
    btn2.configure(text='Copy')

def copy():
    root.clipboard_clear()
    root.clipboard_append(getit(name.get()))
    btn2.configure(text='Copied!')

def clear():
    name.set('')
    ok()

def paste():
    try:
        clipboard=root.clipboard_get()
        name.set(clipboard)
    except:
        pass

def _quit_():
    root.quit()
    root.destroy()
    exit()

name=StringVar(tab1)
nameinput=Entry(tab1,textvariable=name,width=58)
nameinput.place(x=10,y=10)
btn=ttk.Button(tab1,text='Ok',width=3,command=ok)
btn.place(x=370,y=8)
btn3=ttk.Button(tab1,text='Clear',width=5,command=clear)
btn3.place(x=400,y=8)
lab=ttk.Label(tab1,text='')
lab.place(x=10,y=40)
btn2=ttk.Button(tab1,text='Copy',width=10,command=copy)
btn2.place(x=10,y=70)
btn4=ttk.Button(tab1,text='Paste',width=10,command=paste)
btn4.place(x=370,y=36)

try:
    text2=root.clipboard_get()
    if text2!=None and text2!='':
        name.set(text2)
        ok()
except:
    pass

root.mainloop()
