from tkinter import*


root=Tk()
root.geometry('1174x680+0+0')
root.resizable(False,False)
root.title("Student Management System")

#create time label
datetimelabel=Label(root,text='hello',font=('time new roman',18,'bold'))
#place the table
datetimelabel.place(x=5,y=5)


root.mainloop()