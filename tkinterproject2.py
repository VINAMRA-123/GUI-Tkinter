# from tkinter import *

# def area():
#     root.geometry("{breadth.get()}x{height.get()}")
    
# root = Tk()
# root.geometry("443x456")

# lenght = StringVar
# breadth = StringVar
# Label(root, text="Height: ", bg="azure").grid(row=1, column=1)
# Label(root, text="Width:  ", bg="azure").grid(row=2, column=1)
# lenght_root = Entry(root, textvariable=lenght)
# breadth_root = Entry(root, textvariable=breadth)
# lenght_root.grid(row=1,column=2)
# breadth_root.grid(row=2,column=2)
# Button(text="Submit",command= area ).grid(row=3,column=2)
# root.mainloop()

# MINI TASK
#TO TAKE THE RATINGS OF FOOD AND SAVE THE RESOPNSE OF IT
from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("344x357")
root.title("ratings of food")

def ratings():
    print("thanks for the rating")
    value = tmsg.askquestion("expirince",f"thanks you have rated {slider1.get()} points")
    # if slider1 <=5:
    #     msg = "maa chuda"
    # else :                    (ye 4 line nhi chal rhi)
    #     msg = "thanks lode"
    
    tmsg.showinfo("gaali",msg)

Label(root,text="how was our food please rate us",fg="blue").pack()
slider1= Scale(root,from_=0,to=10,orient=HORIZONTAL, tickinterval=2)
slider1.set(10)
slider1.pack()
Button(root, text="submit",command= ratings ).pack()
root.mainloop()