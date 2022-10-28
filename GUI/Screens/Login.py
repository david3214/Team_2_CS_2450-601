'''
    Must compare user input against database entry
    Password must be handled securely
    Will notify user of issues encountered
        Employee not in database
        Invalid credentials
    Loads into user profile with the permission level of the user (general, admin, permitted)
'''

import tkinter as tk


class Login (tk.Frame):
    def __init__(self, master=None) -> None:
        super().__init__(master)
        # Configure grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        # image
        self.image_label = tk.Label(self, text='Image will go here')
        self.image_label.grid(column=0, row=0, sticky=tk.NS)

        # login header
        self.username_label = tk.Label(self, text='Login')
        self.username_label.grid(column=1, row=0, sticky=tk.NS)

        # employee ID
        self.username_label = tk.Label(self, text='Employee ID:')
        self.username_label.grid(column=1, row=1, sticky=tk.W)
        self.username_entry = tk.Entry(self)
        self.username_entry.grid(column=1, row=2, sticky=tk.NS)

        # password
        self.password_label = tk.Label(self, text='Password:')
        self.password_label.grid(column=1, row=3, sticky=tk.W)
        self.password_entry = tk.Entry(self,  show='*')
        self.password_entry.grid(column=1, row=4, sticky=tk.NS)

        # login button
        self.login_button = tk.Button(self, text='Login')
        self.login_button.grid(column=1, row=5, sticky=tk.E)
        self.login_button['command'] = self.login_clicked

        # Get user input
        # Validate credentials
        # Load user’s own profile
        self.pack(expand=True)

    def login_clicked(self):
        print('Button clicked!')

