import tkinter as tk
from tkinter import ttk
from  tkinter import messagebox
def enter_data():
    accept = accept_var.get()
    if accept == "Accepted":
        firstname = firstname_entry.get()
        lastname = lastname_entry.get()
        if firstname and lastname:
            title = title_combobox.get()
            age = age_spinbox.get()
            nationality = nationality_cobobox.get()

            regestration_status = reg_status_var.get()
            numcousres = numcousres_spinbox.get()
            numsemester = numsemester_spinbox.get()

            print("First name: ",firstname,"Last name: ",lastname)
            print("Title: ",title,"Age: ",age,"Nationality: ",nationality)
            print("# Courses: ", numcousres, "# Semester: ", numsemester)
            print("Registration status: ",regestration_status)
            print("--------------------------------------------------------")
        else:
            tk.messagebox.showwarning(title="Error", message="First name and last name required")
    else:
        tk.messagebox.showwarning(title="Error",message="You have not accept the terms and condition")

window = tk.Tk()
window.title("Data entry form")

frame = tk.Frame(window)
frame.pack()

#saving user info
userinfo_frame = tk.LabelFrame(frame,text="User Info")
userinfo_frame.grid(row=0 , column=0, padx=20, pady=20)

firstname_lable = tk.Label(userinfo_frame , text="First Name")
firstname_lable.grid(row=0 , column= 0)
lastname_lable = tk.Label(userinfo_frame,text="Last Name")
lastname_lable.grid(row= 0 ,column=1)

firstname_entry = tk.Entry(userinfo_frame)
lastname_entry = tk.Entry(userinfo_frame)
firstname_entry.grid(row=1, column=0,padx=5,pady=5)
lastname_entry.grid(row=1, column=1,padx=5,pady=5)

title_lable = tk.Label(userinfo_frame,text="Title")
title_combobox = ttk.Combobox(userinfo_frame,values=["","Mr.","Mrs.","Dr."]) #This is for dropdown menu usng ttk
title_lable.grid(row=0 ,column=2)
title_combobox.grid(row=1, column=2)

age_lable = tk.Label(userinfo_frame,text="Age")
age_spinbox = tk.Spinbox(userinfo_frame,from_=18 , to= 60) #This is use for up-down or increment-decrement of values
age_lable.grid(row=2,column=0)
age_spinbox.grid(row=3,column=0)

nationality_lable = tk.Label(userinfo_frame,text="Nationality")
nationality_cobobox = ttk.Combobox(userinfo_frame,values=["Bangladesh","Turkey","Pakistan","Malaysia","Iran"])
nationality_lable.grid(row=2,column=1)
nationality_cobobox.grid(row=3,column=1)

for widget in userinfo_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)

#saving course info
course_frame = tk.LabelFrame(frame,text="User Info")
course_frame.grid(row=1 , column=0,sticky="news", padx=20, pady=20)#sticky use for use whole box and news define (north,east,west,south)

regestered_lable = tk.Label(course_frame,text="Regestration status")
reg_status_var = tk.StringVar(value="Not registered")
regestered_check = tk.Checkbutton(course_frame,text="Curretly registered",
                                  variable=reg_status_var,onvalue="Registered",offvalue="Not registered")
regestered_lable.grid(row=0,column=0)
regestered_check.grid(row=2,column=0)

numcousres_lable = tk.Label(course_frame,text="# Completed courses")
numcousres_spinbox = tk.Spinbox(course_frame,from_=0,to="infinity")
numcousres_lable.grid(row=0,column=1)
numcousres_spinbox.grid(row=2,column=1)

numsemester_lable = tk.Label(course_frame,text="# Semester")
numsemester_spinbox = tk.Spinbox(course_frame,from_=0,to=8)
numsemester_lable.grid(row=0,column=2)
numsemester_spinbox.grid(row=2,column=2)

for widget in course_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)

#Accept terms
terms_frame = tk.LabelFrame(frame,text="User Info")
terms_frame.grid(row=2 , column=0,sticky="news", padx=20, pady=20)#sticky use for use whole box and news define (north,east,west,south)

accept_var = tk.StringVar(value="Not accepted")
terms_check = tk.Checkbutton(terms_frame,text="I accept the terms and conditions.",
                             variable=accept_var,onvalue="Accepted",offvalue="Not accepted")
terms_check.grid(row=0,column=0)

#Button
button = tk.Button(frame,text="Enter data",command= enter_data)
button.grid(row=3 , column= 0 , sticky="news" ,padx=20,pady=20)

window.mainloop()