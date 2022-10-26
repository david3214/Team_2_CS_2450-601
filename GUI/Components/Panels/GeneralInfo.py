'''
    An abstraction of all the employee's general level information to be used by multiple screens
'''


import tkinter as tk
from typing import Type


class GeneralInfo(tk.Frame):
    def __init__(self, master: Type[tk.Frame], bgColor: str='grey') -> None:
        super().__init__(master, bg=bgColor)
        self.options = {'font': ('Arial', 12, 'bold'), 'bg': 'grey', 'fg': 'white'}
        #self.img     = tk.Label(master, image=)
        self.fNameL  = tk.Label(self, text='First Name: ', **self.options)
        self.lNameL  = tk.Label(self, text='Last Name: ', **self.options)
        self.oPhoneL = tk.Label(self, text='Office Phone #: ', **self.options)
        self.emailL  = tk.Label(self, text='Email: ', **self.options)
        self.empIdL  = tk.Label(self, text='Employee ID: ', **self.options)
        self.titleL  = tk.Label(self, text='Title: ', **self.options)
        self.deptL   = tk.Label(self, text='Department: ', **self.options)
        self.sDateL  = tk.Label(self, text='Start Date: ', **self.options)
        self.eDateL  = tk.Label(self, text='End Date: ', **self.options)
        self.perLvlL = tk.Label(self, text='Permission Level: ', **self.options)

        # Pack all children widgets
        [self.children[child].pack() for child in sorted(self.children)]

