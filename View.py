from tkinter import *
from tkinter import messagebox
import pymysql

mypass = "Jaya.H3024"
mydatabase="management"
con = pymysql.connect( host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()
# Enter Table Names here
supply_chainTable = "supply_chain"


def View():
    root = Tk()
    root.title("View details")
    root.minsize(width=400, height=400)
    root.geometry("1000x1100")

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    headingLabel = Label(headingFrame1, text="View Data", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)
    y = 0.25
    Label(labelFrame, text="%-20s%-60s%-70s%-80s" % (' H_Id', 'Vaccine Type', 'Demand Count', 'Supply Count' ),
          bg='black', fg='white').place(relx=0.09, rely=0.1)

    Label(labelFrame, text="---------------------------------------------------------------------------------------------------------------------------------------",
          bg='black',fg='white').place(relx=0.05, rely=0.2)
    getdetails = "select * from " + supply_chainTable
    try:
        cur.execute(getdetails)
        con.commit()
        for i in cur:
            Label(labelFrame, text="%-20s%-70s%-80s%-90s" % (i[0], i[1], i[2], i[3] ), bg='black', fg='white').place(
                relx=0.07, rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch data from database")

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()