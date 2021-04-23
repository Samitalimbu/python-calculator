from tkinter import *

window = Tk()
window.geometry("275x295")
window.title("Calculator")
window.resizable(0, 0)

first_number = 0
operation = ""


def clear():
    v.set("")


def set_num(number):
    v.set(str(v.get()) + str(number))


def action(operator):
    global first_number
    global operation
    first_number = int(v.get())
    operation = operator
    v.set("")


def equal():
    second_number = int(v.get())
    if operation == "add":
        v.set(first_number + second_number)
    elif operation == "sub":
        v.set(first_number - second_number)
    elif operation == "mul":
        v.set(first_number * second_number)
    else:
        v.set(first_number / second_number)


v = StringVar()
top_frame = Frame(window, width=300, height=58, bg="#ffffff")
screen = Label(top_frame, width=39, height=2, bg="#eee", textvariable=v, justify=RIGHT, anchor="e", font="Tahoma 15", padx=10)
screen.place(x=10, y=10, width=255)

bg_image = PhotoImage(file="btn.png")
num_frame = Frame(window, width=300, height=342, bg="#ffffff")
btn_7 = Button(num_frame, text="7", relief="flat", bg="#FFFFFF", activebackground="white", image=bg_image,
               compound="center", bd=0, fg="gray",
               font="tahoma 12",
               command=lambda: set_num(7))
btn_8 = Button(num_frame, text="8", relief="flat", bg="#FFFFFF", activebackground="white", image=bg_image,
               compound="center", bd=0, fg="gray",
               font="tahoma 12",
               command=lambda: set_num(8))
btn_9 = Button(num_frame, text="9", relief="flat", bg="#FFFFFF", activebackground="white", image=bg_image,
               compound="center", bd=0, fg="gray",
               font="tahoma 12",
               command=lambda: set_num(9))
btn_c = Button(num_frame, text="C", relief="flat", bg="#FFFFFF", activebackground="white", image=bg_image,
               compound="center", bd=0, fg="gray",
               font="tahoma 12",
               command=clear)

btn_4 = Button(num_frame, text="4", relief="flat", bg="#FFFFFF", activebackground="white", image=bg_image,
               compound="center", bd=0, fg="gray",
               font="tahoma 12",
               command=lambda: set_num(4))
btn_5 = Button(num_frame, text="5", relief="flat", bg="#FFFFFF", activebackground="white", image=bg_image,
               compound="center", bd=0, fg="gray",
               font="tahoma 12",
               command=lambda: set_num(5))
btn_6 = Button(num_frame, text="6", relief="flat", bg="#FFFFFF", activebackground="white", image=bg_image,
               compound="center", bd=0, fg="gray",
               font="tahoma 12",
               command=lambda: set_num(6))
btn_x = Button(num_frame, text="x", relief="flat", bg="#FFFFFF", activebackground="white", image=bg_image,
               compound="center", bd=0, fg="gray",
               font="tahoma 12",
               command=lambda: action("mul"))

btn_1 = Button(num_frame, text="1", relief="flat", bg="#FFFFFF", activebackground="white", image=bg_image,
               compound="center", bd=0, fg="gray",
               font="tahoma 12",
               command=lambda: set_num(1))
btn_2 = Button(num_frame, text="2", relief="flat", bg="#FFFFFF", activebackground="white", image=bg_image,
               compound="center", bd=0, fg="gray",
               font="tahoma 12",
               command=lambda: set_num(2))
btn_3 = Button(num_frame, text="3", relief="flat", bg="#FFFFFF", activebackground="white", image=bg_image,
               compound="center", bd=0, fg="gray",
               font="tahoma 12",
               command=lambda: set_num(3))
btn_s = Button(num_frame, text="-", relief="flat", bg="#FFFFFF", activebackground="white", image=bg_image,
               compound="center", bd=0, fg="gray",
               font="tahoma 12",
               command=lambda: action("sub"))

btn_0 = Button(num_frame, text="0", relief="flat", bg="#FFFFFF", activebackground="white", image=bg_image,
               compound="center", bd=0, fg="gray",
               font="tahoma 12",
               command=lambda: set_num(0))
btn_d = Button(num_frame, text="/", relief="flat", bg="#FFFFFF", activebackground="white", image=bg_image,
               compound="center", bd=0, fg="gray",
               font="tahoma 12",
               command=lambda: action("div"))
btn_e = Button(num_frame, text="=", relief="flat", bg="#FFFFFF", activebackground="white", image=bg_image,
               compound="center", bd=0, fg="gray",
               font="tahoma 12", command=equal)
btn_a = Button(num_frame, text="+", relief="flat", bg="#FFFFFF", activebackground="white", image=bg_image,
               compound="center", bd=0, fg="gray",
               font="tahoma 12",
               command=lambda: action("add"))

btn_7.place(x=10, y=10, width=60, height=50)
btn_8.place(x=75, y=10, width=60, height=50)
btn_9.place(x=140, y=10, width=60, height=50)
btn_c.place(x=205, y=10, width=60, height=50)

btn_4.place(x=10, y=65, width=60, height=50)
btn_5.place(x=75, y=65, width=60, height=50)
btn_6.place(x=140, y=65, width=60, height=50)
btn_x.place(x=205, y=65, width=60, height=50)

btn_1.place(x=10, y=120, width=60, height=50)
btn_2.place(x=75, y=120, width=60, height=50)
btn_3.place(x=140, y=120, width=60, height=50)
btn_s.place(x=205, y=120, width=60, height=50)

btn_0.place(x=10, y=175, width=60, height=50)
btn_d.place(x=75, y=175, width=60, height=50)
btn_e.place(x=140, y=175, width=60, height=50)
btn_a.place(x=205, y=175, width=60, height=50)

top_frame.place(x=0, y=0)
num_frame.place(x=0, y=58)

window.mainloop()