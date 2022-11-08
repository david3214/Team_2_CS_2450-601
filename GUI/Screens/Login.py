'''
    Must compare user input against database entry
    Password must be handled securely
    Will notify user of issues encountered
        Employee not in database
        Invalid credentials
    Loads into user profile with the permission level of the user (general, admin, permitted)
'''

from PIL import Image, ImageTk
import tkinter as tk
from styles import background_color, text_color, lg_bold, med_bold, med_text, btn_color, sm_text
from config import DB, userSession

class Login (tk.Frame):
    def __init__(self, master=None, bg_color = background_color) -> None:
        super().__init__(master, background=bg_color)

        # Configure grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=10)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_rowconfigure(6, weight=10)


        # Image
        self.header_image = ImageTk.PhotoImage(Image.open('images/employee-image.png').resize([400, 400]))
        self.image_label = tk.Label(self, image=self.header_image, background=bg_color)
        self.image_label.grid(column=0, row=0, rowspan=7)

        # Login header
        self.username_label = tk.Label(self, text='Login', font=lg_bold, foreground=text_color, background=bg_color)
        self.username_label.grid(column=1, row=0, padx=(0, 85), sticky="ENSW")

        # Employee ID
        self.username_label = tk.Label(self, text='Employee ID:', font=med_bold, foreground=text_color, background=bg_color)
        self.username_label.grid(column=1, row=1, sticky=tk.SW)
        self.username_entry = tk.Entry(self, font=med_text)
        self.username_entry.grid(column=1, row=2, sticky=tk.NW)

        # Password
        self.password_label = tk.Label(self, text='Password:', font=med_bold, foreground=text_color, background=bg_color)
        self.password_label.grid(column=1, row=3, sticky=tk.SW)
        self.password_entry = tk.Entry(self, show='*', font=med_text)
        self.password_entry.grid(column=1, row=4, sticky=tk.NW)

        # Error Message
        # self.error_frame = tk.Frame(self, background='#CB0000')
        self.error_msg = tk.Label(self, text="The given username or password \nis incorrect, please try again", font=sm_text, background='#CB0000', foreground=text_color)

        # Login button
        self.login_button = tk.Button(self, text=' Login → ', font=med_bold, foreground=text_color, background=btn_color)
        self.login_button.grid(column=1, row=6, padx=(0, 85), sticky=tk.E)
        self.login_button['command'] = self.login

        self.grid(row=0, column=0, rowspan=2, sticky="NESW")

    def login(self):
        given_username = self.username_entry.get()
        given_password = self.password_entry.get()

        user = DB.search(Employee_ID=given_username)
        
        if len(user) == 1 and user[0].isCorrectLogin(str(given_password)): # Put actuall check here
            global userSession
            userSession = userSession.ChangeEmployee(user[0])
            self.master.switchFrame("Search")
        else:
            self.error_msg.grid(column=1, row=5, sticky="WN", padx=(12, 0))


    def __str__() -> str:
        return 'Login'

# Create and place labels, inputs, buttons, etc.
# Get user input
# Validate credentials
# Load user’s own profile
