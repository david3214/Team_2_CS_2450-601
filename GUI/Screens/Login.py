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
        self.pack()

    def __str__() -> str:
        return 'Login'

# Create and place labels, inputs, buttons, etc.
# Get user input
# Validate credentials
# Load user’s own profile
