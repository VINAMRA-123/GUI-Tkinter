# from tkinter import *
# from PIL import Image,ImageTk
# imaginary_tech_root = Tk()

# imaginary_tech_root.geometry = ("444x256")
# # imaginary_tech_root.maxsize = ("200,100")
# # imaginary_tech_root.minsize =("1200,1000")
# photo = Image.open("FSCN0750.JPG")
# image = ImageTk.PhotoImage(photo)
# vishans_label = Label(photo=image)
# vishans_label.pack()

# imaginary_tech_root.mainloop()
from tkinter import *
from tkinter import font
from PIL import Image, ImageTk
root = Tk()
# root.geometry("1255x944")
# image = Image.open("DSCN0325.JPG")
#  photo = ImageTk.PhotoImage(image)
#  varun_label = Label(image=photo)
#   varun_label.pack()
# # FOR FRAMES
# f1 = Frame(root, bg = "red", borderwidth= 6, relief=SUNKEN)
# f1.pack(side = LEFT,fill="y")
# f2 = Frame(root,  bg = "blue", borderwidth= 7, relief=SUNKEN)
# f2.pack(side = TOP,fill="x")
# l = Label(f1,  text ="i loveyou",)
# l.pack()
# l = Label(f2, text ="i am joking")
# l.pack()
# FOR Grid LAYOUT AND ENTRY WIDGET
# def getvals():
#     print(f"the username is {uservalue.get()}")
#     print(f"the username is {passvalue.get()}")
    
# user = Label(root,text="username" ) 
# password = Label(root,text="Password" )
# nation = Label(root, text="nation is india")
# user.grid(row =0)
# password.grid(row=1)
# nation.grid(row=2)
# uservalue = StringVar
# passvalue = StringVar
# nationality = IntVar

# userentry = Entry(root, textvariable=uservalue)
# passentry = Entry(root, textvariable=passvalue)
# userentry.grid(row=0 , column=1)
# passentry.grid(row=1, column=1)
# nationalitycheck =  Checkbutton(text="indian",variable=nationality)
# nationalitycheck.grid(row = 2,column=1)
# Button(text="Submit",command=getvals).grid()

# FOR CANVAS WIDGET

# canvas_width= 800
# canvas_height = 400
# root.geometry(f"{canvas_width}x{canvas_height}")
# can_widget= Canvas(root,width=canvas_width, height=canvas_height)
# can_widget.pack()
# can_widget.create_rectangle (0,300,400,0)
# can_widget.create_oval(0,200,300,0,fill= "blue")
# coord = 10, 20, 300, 250
# arc = canvas.create_arc(coord = 10, 20, 300, 250
# arc = canvas.create_arc (10,20,300,250,start=0, extent=150, fill="red")/(this line is giving error)
# can_widget.create_line(0,300,200,100,203,302,fill="blue")

# FOR CREATING MENUS, SUBMENUSand message box 
# import tkinter.messagebox as tmsg
# root.geometry("403x503")
# root.title("menus nd submenus")
# def fb():
#     pass
# def rate():
#     print("please rate us")
#     value = tmsg.askquestion("was it good to using gui?","you used this gui it is good?")
#     if value ==YES:
#         msg = "rate us on playstore" 
#     else:
#         msg = "we can nit do anything maa chuda"
#     tmsg.showinfo("experience",msg)

# mainmenu = Menu(root )
# f1 = Menu(mainmenu,tearoff=0)#tearoff is used to removing extra window
# f1.add_command(label= "print", command=fb)
# f1.add_command(label="save", command=fb)
# f1.add_separator()#add_seprator is used to create a line between two comamnd
# f1.add_command(label= "save as", command=fb)
# f1.add_command(label= "move", command=fb)
# f1.add_command(label="rate us", command=rate)
# root.config(menu = mainmenu )
# mainmenu.add_cascade(label="file",menu = f1  )

# MAKING SLIDERS
import tkinter.messagebox as tmsg
root.geometry("345x579")
# def ratings():
#     pass
# Label(root, text="how much rating will you give to our food ",fg="blue").pack()
# sliders1 =Scale(root,from_=0, to=10, orient=HORIZONTAL, tickinterval=2).pack()
# Button(root,text="Submit", command=ratings).pack()

# MAKING RADIOBUTTON

# def eating():
    # tmsg.showinfo("super",f"thanks for eating the food {var.get()}")
    
# var = StringVar()
# var.set("rava")    
# Label(root,text="what do you want to order",fg="blue")
# radio = Radiobutton(root, text="idly", padx=23,bg="grey", fg= "green",variable=var).pack()
# radio = Radiobutton(root, text="halwa", padx=23,bg="grey", fg= "green",variable=var).pack()
# radio = Radiobutton(root, text="chicken", padx=23,bg="grey", fg= "green",variable=var).pack()
# radio = Radiobutton(root, text="dosa", padx=23,bg="grey", fg= "green",variable=var).pack()
# Button(root , text="order now", command= eating).pack()

# MAKING LISTBOX AND Scrollbar
# scrollbar = Scrollbar(root)
# scrollbar.pack(side=RIGHT,fill=Y)

# listbox =Listbox(root,yscrollcommand=scrollbar.set)
# for i in range(344):
#     listbox.insert(END,f"Item{i}")
    
# listbox.pack(side=TOP,fill=BOTH,padx=23)
# scrollbar.config(command=listbox.yview)  

# MAKING OF STATUS BAR 
def upload():
    statusbar.set("Busy.. ")
    sbar.update()
    import time          #TIME IMPORT IS USEED FOR WAITING
    time.sleep(2)
    statusbar.set("ready now")
statusbar= StringVar()
statusbar.set("ready")
sbar =Label(root, textvariable=statusbar,relief= SUNKEN, anchor="w" )
sbar.pack(side = BOTTOM,fill=X)
Button(root, text= "upload", command= upload).pack()
root.mainloop()