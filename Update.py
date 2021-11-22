from tkinter import *
from tkinter import messagebox
import pymysql


def updatedata():
    global Update
    Hospital_Id = Info1.get()
    Vaccine_Type = Info2.get()
    Demand_Count = Info3.get()
    Supply_Count = Info4.get()

    Update = "UPDATE supply_chain SET Hospital_Id = %s, Vaccine_Type= %s,Demand_Count=%s, Supply_Count=%s WHERE " \
             "Hospital_Id = %s "

    try:
        cur.execute(Update)
        con.commit()
        messagebox.showinfo('Success', "Data Updated successfully")
    except:
        messagebox.showinfo("Error", "Can't Update data")

    print(Hospital_Id)
    print(Vaccine_Type)
    print(Demand_Count)
    print(Supply_Count)
    root.destroy()


def update():

    global Info1, Info2, Info3, Info4, supply_chainTable,cur,insert,con,root

    root=Tk()
    root.title("Update details")
    root.minsize(width=400,height=400)
    root.geometry("800x850")

    mypass = "Jaya.H3024"
    mydatabase = "management"
    con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
    cur = con.cursor()

    #enter table names here
    #supply_chainTable="supply_chain"

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    headingLabel = Label(headingFrame1, text="Update Data", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

    # Id
    lb1 = Label(labelFrame, text="Hospital ID : ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.2, relheight=0.08)

    Info1 = Entry(labelFrame)
    Info1.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)

    # Vaccine type
    lb2 = Label(labelFrame, text="Vaccine Type : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.35, relheight=0.08)

    Info2 = Entry(labelFrame)
    Info2.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.08)

    # Demand Count
    lb3 = Label(labelFrame, text="Demand Count : ", bg='black', fg='white')
    lb3.place(relx=0.05, rely=0.50, relheight=0.08)

    Info3 = Entry(labelFrame)
    Info3.place(relx=0.3, rely=0.50, relwidth=0.62, relheight=0.08)

    # Supply Count
    lb4 = Label(labelFrame, text="Supply Count : ", bg='black', fg='white')
    lb4.place(relx=0.05, rely=0.65, relheight=0.08)

    Info4 = Entry(labelFrame)
    Info4.place(relx=0.3, rely=0.65, relwidth=0.62, relheight=0.08)

    # Submit Button
    SubmitBtn = Button(root, text="UPDATE", bg='#d1ccc0', fg='black', command=updatedata)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()







