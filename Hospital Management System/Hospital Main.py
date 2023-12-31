import tkinter as tk
from tkinter import*
from tkinter import ttk

from Hospital import Hospital
from Student import Student
class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")


        menubar = tk.Menu(root)
        root.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Hospital Master", command=self.open_hospital_app)
        file_menu.add_command(label="Student Master", command=self.open_student_app)

        file_menu.add_command(label="Exit", command=root.quit)

        # Create a tab control
        self.tab_control = ttk.Notebook(root)

        # Create the "Master" tab but initially hide it
        self.hospital_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.hospital_tab, text="Hospital Management Master")
        self.tab_control.pack(expand=1, fill="both")
        self.tab_control.hide(self.hospital_tab)  # Hide the "Master" tab initially

        self.student_tab=ttk.Frame(self.tab_control)
        self.tab_control.add(self.student_tab, text="Student Master")
        self.tab_control.pack(expand=1, fill="both")
        self.tab_control.hide(self.student_tab)  # Hide the "Master" tab initially

        # Create a Hospital object inside the "Master" tab
        self.hospital = Hospital(self.hospital_tab, self.tab_control)
        self.student = Student(self.student_tab, self.tab_control)

    def open_hospital_app(self):
        # Show the "Master" tab when "Open HospitalApp" is selected
        self.tab_control.select(self.hospital_tab)
    def open_student_app(self):
        # Show the "Master" tab when "Open HospitalApp" is selected
        self.tab_control.select(self.student_tab)

'''class HospitalApp:
    def __init__(self, root, tab_control):
        self.root = root
        self.tab_control = tab_control
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")

        menubar=tk.Menu(root)
        root.config(menu=menubar)

        file_menu=tk.Menu(menubar,tearoff=0)
        menubar.add_cascade(label="File",menu=file_menu)
        file_menu.add_command(label="Open HospitalApp", command=self.open_hospital_app)

        file_menu.add_command(label="Exit",command=root.quit)


        # Create a tab control
        tab_control = ttk.Notebook(root)

        # Create the "Master" tab
        master_tab = ttk.Frame(tab_control)
        new_tab=ttk.Frame(tab_control)
        tab_control.add(master_tab, text="Master")
        tab_control.add(new_tab,text="New Tab")
        tab_control.pack(expand=1, fill="both")


        # Create a Hospital object inside the "Master" tab
        self.hospital = Hospital(master_tab)

    def open_hospital_app(self):
        # Create a new HospitalApp tab
        hospital_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(hospital_tab, text="HospitalApp")
        self.tab_control.select(hospital_tab)  # Select the newly created tab
        app = HospitalApp(hospital_tab, self.tab_control)
'''
if __name__=="__main__":

    root=tk.Tk()
    application=MainApp(root)
    root.mainloop()

