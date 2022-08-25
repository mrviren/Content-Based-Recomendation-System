from tkinter import *


class PharmacyManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1550*800+0+0")



        lbltitle=Label(self.root, text="PHARMACY MANAGEMENT SYSTEM",bd=15,relief=RIDGE,bg='black',fg="darkgreen",font=("times new roman",45,"bold"),padx=2,pady=4)
        
        lbltitle.pack(side=TOP,fill=X)









if __name__ == "_main_":
    root = Tk()
    obj = PharmacyManagementSystem(root)
    root.mainloop()

