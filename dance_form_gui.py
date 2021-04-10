from tkinter import*
root=Tk()
root.geometry("400x400")
root.minsize(400,400)
root.maxsize(600,600)

def getvals():
    with open("C:\\Users\\sujee\\Desktop\\1.txt","a") as f:
        f.write("-----The New Entry----- \n")
        f.write(f"The name of student is {nameval.get()}")
        f.write('\n')
        f.write(str(f"The age of student is {ageval.get()}"))
        f.write('\n')
        f.write(f"The address of student is {addressval.get()}")
        f.write('\n')
        f.write(str(f"The contact number of student is {contactval.get()}"))
        f.write('\n')
        f.write(f"The email id of student is {emailval.get()}")
        f.write('\n')
    print("Registration Done!")
        


root.title("XYZ Dance Classes")

name=Label(root,text="Name")
age=Label(root,text="Age")
address=Label(root,text="Address")
contact_number=Label(root,text="Contact Number")
email_id=Label(root,text="Email ID")

name.grid()
age.grid(row=1)
address.grid(row=2)
contact_number.grid(row=3)
email_id.grid(row=4)

nameval=StringVar()
ageval=IntVar()
addressval=StringVar()
contactval=IntVar()
emailval=StringVar()

nameentry=Entry(root,textvariable=nameval)
nameentry.grid(row=0,column=1)
ageentry=Entry(root,textvariable=ageval)
ageentry.grid(row=1,column=1)
addressentry=Entry(root,textvariable=addressval)
addressentry.grid(row=2,column=1)
contactentry=Entry(root,textvariable=contactval)
contactentry.grid(row=3,column=1)
emailentry=Entry(root,textvariable=emailval)
emailentry.grid(row=4,column=1)

Button(text="Submit",command=getvals).grid()
root.mainloop()