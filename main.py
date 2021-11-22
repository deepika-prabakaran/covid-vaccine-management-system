
from Add import *
from View import *
from Update import *
from Delete import *
from admin import *

mypass = "Jaya.H3024" #use your own password
mydatabase="management" #The database name
con = pymysql.connect (host="localhost",user="root",password=mypass,database=mydatabase)

#root is the username here
cur = con.cursor() 

root = Tk()
root.title("Supply Chain Management")
root.minsize(width=400,height=400)
root.geometry("800x850")

headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
headingLabel = Label(headingFrame1, text="Supply Chain \n Management", bg='black', fg='white', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

# adding buttons 

btn1 = Button(root, text="Add Data", bg='black', fg='white', command=add)
btn1.place(relx=0.28, rely=0.3, relwidth=0.45, relheight=0.1)

btn2 = Button(root, text="View Data", bg='black', fg='white', command=View)
btn2.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

btn3 = Button(root, text="Update Data", bg='black', fg='white', command=update)
btn3.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

btn4 = Button(root, text="Delete Data", bg='black', fg='white', command=delete)
btn4.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

root.mainloop()