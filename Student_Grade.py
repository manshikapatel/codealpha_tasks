#Student Grade Tracker
import tkinter
from tkinter import *

root = Tk()
root.title("STUDENT GRADE TRACKER")
root.geometry("500x400")

def Calculation():
    comm = int(commentry.get())
    QA = int(QAentry.get())
    DA = int(DAentry.get())
    DBMS = int(DBMSentry.get())
    total =(comm+QA+DA+DBMS)
    Label(text=f"{total}",font="arial 12 bold").place(x=250,y=190)


    average = int(total/4)
    Label(text=f"{average}",font="arial 12 bold").place(x=250,y=220)

    if(average>50):
        grade = "PASS"
    else:
        grade = "FAIL"

    Label(text=f"{grade}",font="arial 12 bold", fg="blue").place(x=250,y=250)


#SUBJECT
sub1=Label(root,text="COMMUNICATION:" ,font="arial 10")
sub2=Label(root,text="APTITUDE:" ,font="arial 10")
sub3=Label(root,text="DATA ANALYTIC:" ,font="arial 10")
sub4=Label(root,text="DBMS:" ,font="arial 10")
total=Label(root,text="TOTAL:" ,font="arial 10")
avg=Label(root,text="AVERAGE:" ,font="arial 10")
grade=Label(root,text="GRADE:" ,font="arial 10")

sub1.place(x=50,y=20)
sub2.place(x=50,y=60)
sub3.place(x=50,y=100)
sub4.place(x=50,y=140)
total.place(x=50,y=190)
avg.place(x=50,y=220)
grade.place(x=50,y=250)

commvalue = StringVar()
QAvalue = StringVar()
DAvalue = StringVar()
DBMSvalue = StringVar()

commentry =Entry(root,textvariable = commvalue,font="arial 15" ,width =15)
QAentry =Entry(root,textvariable = QAvalue,font="arial 15" ,width =15)
DAentry =Entry(root,textvariable = DAvalue,font="arial 15" ,width =15)
DBMSentry =Entry(root,textvariable = DBMSvalue,font="arial 15" ,width =15)

commentry.place(x=250,y=20)
QAentry.place(x=250,y=60)
DAentry.place(x=250,y=100)
DBMSentry.place(x=250,y=140)

Button(text ="Calculate",font="arial 15",bg="white",bd =10,command=Calculation).place(x=50,y=300)
Button(text ="exit",font="arial 15",bg="white",bd =10,width=8,command=lambda:exit()).place(x=350,y=300)
root.mainloop()