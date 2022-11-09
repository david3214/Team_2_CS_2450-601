from tkscrolledframe import ScrolledFrame
import tkinter as tk
from PIL import Image, ImageTk
from typing import Type
from styles import background_color, sm_text

class ScrollableSearch(ScrolledFrame):

    def __init__(self, master: Type[tk.Tk], root: Type[tk.Tk], bg_color: str = background_color) -> None:
        super().__init__(master, bg=bg_color)
        self.employee_img = ImageTk.PhotoImage(image=Image.open('./images/ListEmp.png').resize((35,35)))

        self.root = root
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        # Allows the scroll wheel to scroll the employee list
        self.bind_scroll_wheel(root)
        # Creates/configures frame to display employees
        self.inner_frame = self.display_widget(tk.Frame, bg=bg_color, fit_width=True)
        self.inner_frame.grid_columnconfigure(0, weight=1)
        self.advancedSearch = False
        self.employees = list()


    def changeList(self, employees):
      self.employees = employees
      self.clearSearchFrame()
      # if there are no employees we want a blank view
      if len(employees) == 0:
        emptyFrame = tk.Frame(self.inner_frame, background='white')
        emptyFrame.grid(row=0, column=0, pady=1, sticky='NSEW')
      else:
        for i, emp in enumerate(employees):
          # Create the row in the search bar
          employee_frame = tk.Frame(self.inner_frame, background='white')
          employee_frame.grid_columnconfigure(0, weight=2)
          employee_frame.grid_columnconfigure(1, weight=5)
          employee_frame.grid_columnconfigure(2, weight=4)
          employee_frame.grid_columnconfigure(3, weight=3)
          employee_frame.grid_rowconfigure(0, weight=1)
          employee_frame.grid(row=i, column=0, pady=1, sticky='ENSW')

          # Create the image
          self.employee_image = tk.Label(employee_frame, background='white')
          self.employee_image.config(image=self.employee_img)
          self.employee_image.grid(row=0, column=0, pady=6, padx=(6, 0), sticky='W')

          # If we have less room shorten these texts
          employee_text = f'Employee: '
          id_text = f'Employee ID: '
          if self.advancedSearch:
            employee_text = ''
            id_text = 'ID: '

          # Create the labels for the row
          tk.Label(employee_frame, text=employee_text + emp.Name, font=sm_text, background='white')\
                  .grid(row=0, column=1, sticky='WNS')
          tk.Label(employee_frame, text=id_text + emp.EmpID, font=sm_text, background='white')\
                    .grid(row=0, column=2, sticky='WNS')
          tk.Label(employee_frame, text=f'Dept: {emp.Dept}', font=sm_text, background='white')\
                  .grid(row=0, column=3, padx=(0, 15), sticky='ENS')

    def redraw(self):
      # this is to make sure when we switch to advanced search we switch the label texts
      self.changeList(self.employees)
    
    def clearSearchFrame(self):
      # When we are getting a new list we need to remove the old rows
      for child in self.inner_frame.winfo_children():
        child.destroy()