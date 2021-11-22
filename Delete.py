from tkinter import *
from tkinter import messagebox
import pymysql

mypass = "Jaya.H3024"
mydatabase="management"
con = pymysql.connect (host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

# Enter Table Names here
supply_chainTable = "supply_chain"


def deletedata():
    Hospital_Id = Info1.get()

    delete = "delete from " + supply_chainTable + " where Hospital_Id = '" + Hospital_Id + "'"
    try:
        cur.execute(delete)
        con.commit()

        messagebox.showinfo('Success', "Record Deleted Successfully")
    except:
        messagebox.showinfo("Please check The ID")

    print(Hospital_Id)
    Info1.delete(0, END)
    root.destroy()


def delete():
    global Info1, Info2, Info3, Info4, con, cur, supply_chainTable, root

    root = Tk()
    root.title("Detele Data")
    root.minsize(width=400, height=400)
    root.geometry("800x850")

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Delete Record", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # ID to Delete
    lb2 = Label(labelFrame, text="Hospital ID : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.5)

    Info1 = Entry(labelFrame)
    Info1.place(relx=0.3, rely=0.5, relwidth=0.62)

    # Submit Button
    SubmitBtn = Button(root, text="DELETE", bg='#d1ccc0', fg='black', command=deletedata)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()