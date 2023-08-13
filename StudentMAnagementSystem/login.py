from tkinter import * #to import GUI
from PIL import ImageTk #to import jpg image to code
from tkinter import messagebox

def login():
    if usernameEntry.get()==''or passwordEntry.get()=='':
        messagebox.showerror("Error","Feilds cannot be empty")
    elif usernameEntry.get()=='Chitra' and passwordEntry.get()=='1234':
        messagebox.showinfo("Login Success","Welcome Chitra")
        window.destroy()  # close the login window
        import sms

    else:messagebox.showinfo("Error","Kindly enter correct credentials")




window=Tk()#to create GUI
window.geometry('1280x700+0+0')#size of window w=1280 h=700.This window size can be maximized and minimized
window.title("Login Page of Student MAnagement System")
window.resizable(False,False)#to fix the window size
backgroundImage=ImageTk.PhotoImage(file='bg.jpg')

bgLabel=Label(window,image=backgroundImage)#put image on window by creating label
bgLabel.place(x=0,y=0) #place label in window

#login  image
loginFrame=Frame(window,bg='white')
loginFrame.place(x=550,y=150)
logoImage=PhotoImage(file='logo.png')
logoLabel=Label(loginFrame,image=logoImage)
logoLabel.grid(row=1,column=0,columnspan=2,pady=10)

#username
usernameImage=PhotoImage(file='user1.png')
usernameLabel=Label(loginFrame,image=usernameImage,text='Username',compound=LEFT,font=('times new roman',20,'bold'),bg='white',pady=1)
usernameLabel.grid(row=2,column=0,pady=10,padx=20)
#user name entry tab
usernameEntry=Entry(loginFrame,font=('times new roman',20,'bold'),bd=5,fg='violet red')
usernameEntry.grid(row=2,column=1,pady=10,padx=20)

#password
passwordImage=PhotoImage(file='password.png')
passwordLabel=Label(loginFrame,image=passwordImage,text='Password',compound=LEFT,font=('times new roman',20,'bold'),bg='white',pady=1)
passwordLabel.grid(row=3,column=0,pady=10,padx=20)
#password entry tab
passwordEntry=Entry(loginFrame,font=('times new roman',20,'bold'),bd=5,fg='violet red')
passwordEntry.grid(row=3,column=1,pady=10,padx=20)

#login button
loginButton=Button(loginFrame,text='Login',font=('times new roman',12,'bold'),fg='white',bg='royalblue',
                   width=15,activebackground='royalblue',activeforeground='white',cursor='hand2',command=login)
loginButton.grid(row=4,column=1,pady=10)






window.mainloop()#to see the window continuosly