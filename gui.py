from tkinter import *
from tkinter.font import Font

# ------------------Geometry------------------------------------------
root = Tk()
root.geometry('500x250')
root.minsize(400,170)

# ------------------Header--------------------------------------------
font_head = Font(family = "", weight = "bold", size = 20)

#-------------------Buttons,Labels,etc..------------------------------
label_text = Label(root, text = "Login Page", anchor = CENTER, font = font_head)
label_text.pack()
#username_frame
frame_username = Frame(root)
frame_username.pack()

label_login = Label(frame_username, text = "Username")
label_login.pack(side = LEFT)
entry_username = Entry(frame_username)
entry_username.pack()
#password_frame
frame_password = Frame(root)
frame_password.pack()

label_password = Label(frame_password, text = "Password")
label_password.pack(side = LEFT)
entry_password = Entry(frame_password, show = "*")
entry_password.pack()





root.mainloop()