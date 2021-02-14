from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
import sqlite3
import hashing
import vault

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.pos_top = 700
        self.pos_bot = 300
        self.geometry(f'500x250+{self.pos_top}+{self.pos_bot}')
        self.resizable(False,False)
        self.title("Login")

        # ------------------Header--------------------------------------------
        font_head = Font(family = "", weight = "bold", size = 20)
        #-------------------Buttons,Labels,etc..------------------------------
        label_text = Label(self, text = "Digital Vault", anchor = CENTER, font = font_head)
        label_text.pack(pady = 10)
        #username_frame
        frame_username = Frame(self)
        frame_username.pack()

        label_login = Label(frame_username, text = "Username")
        label_login.pack(side = LEFT)
        self.entry_username = Entry(frame_username)
        self.entry_username.pack()
        #password_frame
        frame_password = Frame(self)
        frame_password.pack(pady = 5)

        label_password = Label(frame_password, text = "Password")
        label_password.pack(side = LEFT)
        self.entry_password = Entry(frame_password, show = "*")
        self.entry_password.pack()
        #button_frame
        frame_button = Frame(self)
        frame_button.pack(pady = 5)

        btn_login = Button(frame_button, text = "LOGIN", command = self.validation_check)
        btn_login.pack(pady = 5,padx = 10)

        btn_register = Button(frame_button, text = "REGISTER", command = self.user_register)
        btn_register.pack(pady = 5,padx = 10)
    def validation_check(self):
        # error_window = Toplevel(self)
        # error_window.geometry(f'250x50+{self.winfo_x()}+{self.winfo_y()}')
        # error_window.title("Error")
        # error_window.resizable(False,False)
        # error_label = Label(error_window, text = "Incorrect Username or Password", foreground = "red")
        # error_label.pack()

        # messagebox.showwarning("Warning","Wrong Password")

        usr = self.entry_username.get()
        pwd = self.entry_password.get()
        print(usr,pwd)
        conn = sqlite3.connect('user_data.db')
        c = conn.cursor()

        new_hash = str.encode(pwd)
        c = conn.cursor()
        c.execute
        c.execute("SELECT username FROM user")
        user = c.fetchall()
        localvar = 0
        usr_name = ""
        for record in user:
            if usr == record[0]:
                # print(record[0])
                localvar += 1
                usr_name = usr
                # print(localvar)
        c.execute("SELECT pwd FROM user WHERE username=(:usr)",{
            'usr': usr_name
        })
        data = c.fetchall()
        if localvar == 1:
            for record in data:
            # print(str(record[0]))
            # if new_hash == record[0]:
            #     print(True)
                if hashing.checkpwd(new_hash,record[0]):
                    print("True")
                    self.destroy()
                    vault.start()
                else:
                    print("False")

        conn.commit()
        conn.close()

    def user_register(self):
        print("Register butoon clicked")
        self.register_window = Toplevel(self)
        self.register_window.title("Register")
        self.register_window.geometry(f'300x250+{self.winfo_x()+115}+{self.winfo_y()}')
        #regname_frame
        frame_regname = Frame(self.register_window)
        frame_regname.pack(pady = 5)

        label_regname = Label(frame_regname, text = "Username")
        label_regname.pack(side = LEFT)
        self.entry_regname = Entry(frame_regname)
        self.entry_regname.pack()
        #regpassword_frame
        frame_regpassword = Frame(self.register_window)
        frame_regpassword.pack(pady = 5)

        label_regpassword = Label(frame_regpassword, text = "Password")
        label_regpassword.pack(side = LEFT)
        self.entry_regpassword = Entry(frame_regpassword, show = "*")
        self.entry_regpassword.pack()
        #confirmpassword_frame
        frame_confirmpassword = Frame(self.register_window)
        frame_confirmpassword.pack(pady = 5)

        label_confirmpassword = Label(frame_confirmpassword, text = "Confirm Password")
        label_confirmpassword.pack(side = LEFT)
        self.entry_confirmpassword = Entry(frame_confirmpassword, show = "*")
        self.entry_confirmpassword.pack()
        #get_values
        self.regpassword = (self.entry_regpassword.get())
        self.confirmpassword = (self.entry_confirmpassword.get())
        
        #button_frame
        frame_regbutton = Frame(self.register_window)
        frame_regbutton.pack()
        btn_reglogin = Button(frame_regbutton, text = "REGISTER",command = self.register)
        btn_reglogin.pack(side = LEFT)

    def register(self):
        conn = sqlite3.connect('user_data.db')
        c = conn.cursor()
        usr = self.entry_regname.get()
        password = self.entry_regpassword.get()
        hash = hashing.hashpwd(str.encode(password))

        confirm_password = self.entry_confirmpassword.get()
        if usr != "":
#-----------------check_if_user_already_exist--------------------
            c.execute("SELECT username FROM user")
            user = c.fetchall()
            localvar = 0
            usr_name = ""
            for record in user:
                if usr == record[0]:
                    # print(record[0])
                    localvar += 1
                    usr_name = usr
                    print(usr_name)
                    # print(localvar)
#-----------------------------------------------------------------
            if localvar == 0:
                if password == confirm_password and password != "":
                    c.execute("INSERT INTO user (username, pwd) VALUES(:name, :password)",{
                    'name' : usr,
                    'password' : hash
                    })
                elif password == "":
                    messagebox.showwarning("Warning","Please enter a Password")
                else:
                    error_window = Toplevel(self)
                    error_window.title("Error")
                    error_window.geometry(f'250x50+{self.register_window.winfo_x()+25}+{self.register_window.winfo_y()+100}')
                    error_window.resizable(False,False)
                    error_label = Label(error_window, text = "Password doesn't match", foreground = "red")
                    error_label.pack()
            else:
                print("User already exist")
        conn.commit()
        conn.close()
                

root = GUI()
# conn = sqlite3.connect('user_data.db')

# c = conn.cursor()
# c.execute("""CREATE TABLE user  (
#     uid integer NOT NULL PRIMARY KEY,
#     username string,
#     pwd string
# )""")
# conn.commit()
# conn.close()

root.mainloop()