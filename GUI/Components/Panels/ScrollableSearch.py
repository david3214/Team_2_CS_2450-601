from tkscrolledframe import ScrolledFrame
import tkinter as tk
from PIL import Image, ImageTk
from GUI.Screens.Profile import Profile
from GUI.Screens.Admin import Admin
from GUI.Screens.Permitted import Permitted
from GUI.Screens.User import User
from GUI.Screens.Archived import Archived
from EmployeeContainer import EmployeeSelf, EmployeeAdmin, EmployeeOther
import typing
from styles import background_color, sm_text
from config import userSession, fetch_resource
if typing.TYPE_CHECKING:
    from GUI.Window import Window
    from Screens.Search import Search
class ScrollableSearch(ScrolledFrame):

    def __init__(self, master: 'Search', root: 'Window', bg_color: str = background_color) -> None:
        super().__init__(master, bg=bg_color)
        self.employee_img = ImageTk.PhotoImage(image=Image.open(fetch_resource('./images/ListEmp.png')).resize((35,35)))

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
        self.employeeFrames = list()


    def changeList(self, employees):
      self.clearSearchFrame()
      self.employees = employees
      # if there are no employees we want a blank view
      if len(self.employees) == 0:
        emptyFrame = tk.Frame(self.inner_frame, background='white')
        emptyFrame.grid(row=0, column=0, pady=1, sticky='NSEW')
      else:
        for i, emp in enumerate(employees):
          # Create the row in the search bar
          self.employeeFrames.append(tk.Frame(self.inner_frame, background='white', cursor='hand2'))
          self.employeeFrames[i].grid_columnconfigure(0, weight=2)
          self.employeeFrames[i].grid_columnconfigure(1, weight=5)
          self.employeeFrames[i].grid_columnconfigure(2, weight=4)
          self.employeeFrames[i].grid_columnconfigure(3, weight=3)
          self.employeeFrames[i].grid_rowconfigure(0, weight=1)
          self.employeeFrames[i].grid(row=i, column=0, pady=1, sticky='ENSW')
          self.employeeFrames[i].emp = emp

          self.employeeFrames[i].bind('<Button-1>', self.selectEmployee)
          self.employeeFrames[i].bind('<Leave>', self.offHoverEmployee)
          self.employeeFrames[i].bind('<Enter>', self.onHoverEmployee)
          
          # Create the image
          self.employee_image = tk.Label(self.employeeFrames[i], background='white')
          self.employee_image.config(image=self.employee_img)
          self.employee_image.grid(row=0, column=0, pady=6, padx=(6, 0), sticky='W')

          # If we have less room shorten these texts
          employee_text = f'Employee: '
          id_text = f'Employee ID: '
          if self.advancedSearch:
            employee_text = ''
            id_text = 'ID: '

          # Create the labels for the row
          tk.Label(self.employeeFrames[i], text=employee_text + emp.Name, font=sm_text, background='white').grid(row=0, column=1, sticky='WNS')
          tk.Label(self.employeeFrames[i], text=id_text + emp.EmpID, font=sm_text, background='white').grid(row=0, column=2, sticky='WNS')
          tk.Label(self.employeeFrames[i], text=f'Dept: {emp.Dept}', font=sm_text, background='white').grid(row=0, column=3, padx=(0, 15), sticky='ENS')

    def redraw(self):
      # this is to make sure when we switch to advanced search we switch the label texts
      self.changeList(self.employees)
    
    def clearSearchFrame(self):
      self.employees = list()
      self.employeeFrames = list()
      # When we are getting a new list we need to remove the old rows
      for child in self.inner_frame.winfo_children():
        child.destroy()

    def selectEmployee(self, event):
        emp_container = event.widget.emp
        if emp_container.EmpID == userSession.EmpID and userSession.PermissionLevel != 1:
            emp_container = userSession
        frame = self.selectFrame(emp_container)
        if frame:
            self.root.switchFrame(frame, emp_container)

    def selectFrame(self, emp_container):
        if emp_container.Active:
            if isinstance(emp_container, EmployeeSelf) and emp_container.PermissionLevel != 1:
                self.root.switchFrame(User)
                return None
            elif isinstance(emp_container, EmployeeAdmin) or emp_container.PermissionLevel == 1:
                return Admin
            elif isinstance(emp_container, EmployeeOther):
                return Permitted if emp_container.PermittedLockOn else Profile

        return Archived

    def onHoverEmployee(self, event):
      event.widget['bg'] = 'grey'

      for child in event.widget.winfo_children():
        child['bg'] = 'grey'

    def offHoverEmployee(self, event):
      event.widget['bg'] = 'white'
      for child in event.widget.winfo_children():
        child['bg'] = 'white'