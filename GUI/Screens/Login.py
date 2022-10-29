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


class Login (tk.Frame):
    def __init__(self, master=None) -> None:
        super().__init__(master)

        header_font = ('Arial bold', 26)
        entry_label_font = ('Arial bold', 14)
        entry_font = ('Arial', 14)

        # Configure grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        # Image
        self.header_image = ImageTk.PhotoImage(Image.open('images/employee-image.png').resize([380, 380]))
        self.image_label = tk.Label(self, image=self.header_image)
        self.image_label.grid(column=0, row=0, rowspan=18, padx=30)

        # Login header
        self.username_label = tk.Label(self, text='Login', font=header_font)
        self.username_label.grid(column=1, row=0)

        # Employee ID
        self.username_label = tk.Label(self, text='Employee ID:', font=entry_label_font)
        self.username_label.grid(column=1, row=4, sticky=tk.W)
        self.username_entry = tk.Entry(self, font=entry_font)
        self.username_entry.grid(column=1, row=5, sticky=tk.NS)

        # Password
        self.password_label = tk.Label(self, text='Password:', font=entry_label_font)
        self.password_label.grid(column=1, row=6, sticky=tk.W)
        self.password_entry = tk.Entry(self, show='*', font=entry_font)
        self.password_entry.grid(column=1, row=7, sticky=tk.NS)

        # Login button
        self.login_button = tk.Button(self, text='Login →', font=entry_label_font)
        self.login_button.grid(column=1, row=19, sticky=tk.E)
        self.login_button['command'] = self.login

        # Get user input
        # Validate credentials
        # Load user’s own profile
        self.pack(expand=True)

    def login(self):
        given_username = self.username_entry.get()
        given_password = self.password_entry.get()

        print(f'Checking that {given_username} and {given_password} are valid')

