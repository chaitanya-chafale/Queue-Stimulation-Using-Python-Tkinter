from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
import tkinter as tk
ent=5
z=0

def root_4(event):
    root4 = Toplevel()
    root4.geometry("1000x350")
    root4.resizable(0, 0)
    root4.title("DRAWBACKS")
    frame = LabelFrame(root4, width=940, height=283)
    frame.pack(anchor=CENTER, pady=30)
    icon = PhotoImage(file="dis.PNG")
    a = Label(frame, image=icon)
    a.pack()
    root4.mainloop()


def root_3(event):
    root3=Toplevel()
    root3.geometry("1050x504")
    root3.resizable(0, 0)
    root3.title("DETAILS")
    root3.config(bg="light grey")
    frame= LabelFrame(root3,width=1000,height=464)
    frame.pack(anchor=CENTER,pady=30)
    icon = PhotoImage(file="DETAILS.png")
    a=Label(frame,image=icon)
    a.pack()
    root3.mainloop()


def root_2(event):
    root2 = Toplevel()
    root2.geometry("1400x700")
    root2.resizable(0, 0)
    root2.title("QUEUE SIMULATION")
    root2.config(bg="chocolate2")
    background=PhotoImage(file="background.png",height=700,width=1400)
    blabel=Label(root2,image=background)
    blabel.pack()

    def dialog(event):
        global ent
        global z
        z=0
        v=ent
        x=1
        ent = simpledialog.askinteger("MAX SIZE", "ENTER THE SIZE",parent=root2)
        if ent == None:
            ent=v
        displaysize(x,ent)

    def displaysize(x,ent):
        if x==0:
            maxd = Label(middleframe, text=ent, width=10, height=2, relief=SUNKEN)
            maxd.place(x=260, y=120)
        else:
            maxd = Label(middleframe, text=ent, width=10, height=2, relief=SUNKEN)
            maxd.place(x=260, y=120)

    class Queue:

        def __init__(self):
            self.items = []

        def isEmpty(self):
            return self.items == []

        def enqueue(self, items):
            global z
            self.items.insert(len(self.items), items)
            if len(self.items) == ent:
                z = 1

        def dequeue(self):
            global z
            if len(self.items) == ent:
                z = 1
            print(z)
            return self.items.pop(0)

        def size(self):
            return len(self.items)

        def display(self):
            return self.items

    q = Queue()

    def add1(event):
            global ent
            global z
            if (q.size()) < ent and z!=1 :
                if entry.get() != "" and entry.get() != " ":
                    q.enqueue(entry.get())
                    entry.delete(0, 'end')
                    for widget in displayframe.winfo_children():
                        widget.destroy()
                    display_e(q.items)
                frontval()
                rearval()
            elif q.size() > ent:
                messagebox.showerror("!!!!!!!!!", "QUEUE OVERFLOW, PLEASE PERFORM DEQUEUE ", parent=root2)
            else:
                messagebox.showerror("!!!!!!!!!" , "QUEUE IS FULL",parent=root2)
                #root2.wait_window(root2)

    def delete1(event):
        q.dequeue()
        display_d(q.items)
        frontval()
        rearval()

    def display_e(items):
        k = 0
        if len(q.items) == 0:
            b = Label(displayframe, text='queue is empty', relief=SOLID, bg='white', font="25", borderwidth=2)
            b.grid(row=2, column=0)
        else:
            if len(q.items) == 1:
                for widget in displayframe.winfo_children():
                    widget.destroy()
                b = Label(displayframe, text=items[0], relief=SOLID, bg='white', font="25", borderwidth=2)
                b.grid(row=2, column=1)
                p = Label(displayframe, text='^')
                p.grid(row=3, column=1)
                front = Label(displayframe, text='F/R')
                front.grid(row=4, column=1)
            else:
                for i in items:
                    b = Label(displayframe, text=i, relief=SOLID, bg='white', font="25", borderwidth=2)
                    k = k + 1
                    b.grid(row=2, column=k)
                pos = len(items)
                p = Label(displayframe, text='^')
                p.grid(row=3, column=1)
                front = Label(displayframe, text='F')
                front.grid(row=4, column=1)
                r = Label(displayframe, text='^')
                r.grid(row=3, column=pos)
                rear = Label(displayframe, text='R')
                rear.grid(row=4, column=pos)

    def display_d(items):
        k = 0
        if len(q.items) == 0:
            for widget in displayframe.winfo_children():
                widget.destroy()
            b = Label(displayframe, text='queue is empty', relief=SOLID, bg='white', font="25", borderwidth=2)
            b.grid(row=2, column=0)
        else:
            if len(q.items) == 1:
                for widget in displayframe.winfo_children():
                    widget.destroy()
                b = Label(displayframe, text=items[0], relief=SOLID, bg='white', font="25", borderwidth=2)
                b.grid(row=2, column=1)
                p = Label(displayframe, text='^')
                p.grid(row=3, column=1)
                front = Label(displayframe, text='F/R')
                front.grid(row=4, column=1)
            else:
                for widget in displayframe.winfo_children():
                    widget.destroy()
                for i in items:
                    k = k + 1
                    b = Label(displayframe, text=i, relief=SOLID, bg='white', font="25", borderwidth=2)
                    b.grid(row=2, column=k)
                pos = len(q.items)
                #print(pos)
                p = Label(displayframe, text='^')
                p.grid(row=3, column=1)
                front = Label(displayframe, text='F')
                front.grid(row=4, column=1)
                r = Label(displayframe, text='^')
                r.grid(row=3, column=pos)
                rear = Label(displayframe, text='R')
                rear.grid(row=4, column=pos)

    def clear1(event):
        global z
        z=0
        for widget in displayframe.winfo_children():
            widget.destroy()
        q.items = []
        frontval()
        rearval()

    def frontval():
        if len(q.items) == 0:
            valueatf = Label(middleframe, text='Empty Queue', width=10, height=2,relief=SUNKEN)
            valueatf.place(x=260, y=20)
        else:
            valueatf = Label(middleframe, text=q.items[0], width=10, height=2,relief=SUNKEN)
            valueatf.place(x=260, y=20)

    def rearval():
        if len(q.items) == 0:
            valueatr = Label(middleframe, text='Empty Queue', width=10, height=2,relief=SUNKEN)
            valueatr.place(x=260, y=70)
        else:
            valueatr = Label(middleframe, text=q.items[len(q.items) - 1], width=10, height=2,relief=SUNKEN)
            valueatr.place(x=260, y=70)

    leftframe = LabelFrame(root2, bg='light green', height=200, width=440, relief=RIDGE, borderwidth=2)
    leftframe.place(relx=0.033,rely=0.044,relheight=0.273,relwidth=0.300)
    leftframe.pack_propagate(False)

    rightframe = LabelFrame(root2, bg='bisque2', height=200, width=250, relief=RIDGE, borderwidth=2)
    rightframe.place(relx=0.700,rely=0.044,relheight=0.273,relwidth=0.240)
    rightframe.pack_propagate(False)

    middleframe = LabelFrame(root2, bg='light goldenrod', height=200, width=400, relief=RIDGE, borderwidth=2)
    middleframe.place(relx=0.3800,rely=0.044,relheight=0.273,relwidth=0.275)
    middleframe.pack_propagate(False)

    displayframe = LabelFrame(root2, bg='white', height=450, width=2000, relief=RIDGE, borderwidth=2)
    displayframe.place(relx=0.033,rely=0.328,relheight=0.6,relwidth=0.908)
    displayframe.pack_propagate(False)

    entry = Entry(leftframe)
    entry.place(relx=0.103,rely=0.227,height=34,relwidth=0.45)
    enqueue = Button(leftframe, text="ENQUEUE", width=20, height=2)
    enqueue.place(x=235, y=40)
    dequeue = Button(leftframe, text="DEQUEUE", width=40, height=2)
    dequeue.place(x=80, y=120)
    head=Label(leftframe,text="QUEUE OPERATION",font = 'Helvetica 12 bold',bg="light green").place(x=10,y=2)

    clear = Button(rightframe, text="CLEAR", width=20, height=2)
    clear.place(x=90, y=70)

    valuef = Label(middleframe, text='VALUE AT FRONT', width=20, height=2,relief=GROOVE)
    valuef.place(x=60, y=20)
    valuer = Label(middleframe, text='VALUE AT REAR', width=20, height=2,relief=GROOVE)
    valuer.place(x=60, y=70)
    maxs=Label(middleframe,text="MAX SIZE:",width=20, height=2 , relief=GROOVE)
    maxs.place(x=60 , y=120)
    x=0
    displaysize(x,ent)
    update=Button(middleframe,text="UPDATE",width=9, height=1,relief=RAISED)
    update.place(x=263, y=160)
    update.bind("<Button-1>", dialog)

    enqueue.bind("<Button-1>", add1)
    dequeue.bind("<Button-1>", delete1)
    clear.bind("<Button-1>", clear1)
    #valuef.bind("<Button-1>", frontval)
    #valuer.bind("<Button-1>", rearval)

    root2.mainloop()

root1=Tk()
root1.title("QUEUE SIMULATION")
root1.geometry("1400x700")

head=LabelFrame(root1,bg='green',height=100)
head.pack(padx=5,pady=5,fill=X)
head.pack_propagate(False)

left=LabelFrame(root1,bg='white',width=680)
left.pack(side='left',padx=5,fill=Y)
left.pack_propagate(False)

right=LabelFrame(root1,width=680)
right.pack(side="right",padx=5,fill=Y)
right.pack_propagate(False)
background2=PhotoImage(file="background2.png")
blabel2=Label(right,image=background2)
blabel2.pack(fill=Y)

heading=Label(head,text='WELCOME TO QUEUE SIMULATION',bg="green",fg="orange",font = 'Helvetica 18 bold')
heading.place(x=500,y=30)

madeby=Button(right,text="MADE BY \n1.CHAITANYA CHAFALE",width=25, relief="groove",bg="oliveDrab3")
madeby.place(x=500,y=460)

details=Button(right,text="DETAILS",font = 'Helvetica 12',width=25,relief="groove",bg="tomato")
details.bind("<Button-1>",root_3)
details.place(x=450,y=40)

#pseudocode=Button(right,text="PSUEDO CODE",font = 'Helvetica 12',width=25,relief="groove",bg="tomato")
#pseudocode.bind("<Button-1>",root_4)
#pseudocode.place(x=450,y=90)

queue=Button(right,text="QUEUE",font = 'Helvetica 12',width=25,relief="groove",bg="tomato")
queue.bind("<Button-1>",root_2)
queue.place(x=450,y=140)
dis = Button(right, text="DRAWBACKS", font='Helvetica 12', width=25, relief="groove", bg="tomato")
dis.place(x=450, y=90)
dis.bind("<Button-1>", root_4)

logo=PhotoImage(file="FILE.png",height=200,width=200)
w1 = Label(left, image=logo).place(x=200,y=50)
scope=PhotoImage(file="scope.png")
w2 = Label(left, image=scope).place(x=5,y=350)
root1.mainloop()