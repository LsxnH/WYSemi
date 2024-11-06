import tkinter

XSize = 0
YSize = 0

def func(Par):
    print("myname")

def getValue():
    print("账号为 {}, 密码为 {}".format(float(entry1.get())-1, entry2.get()))
    XSize = float(entry1.get())
    YSize = float(entry2.get())
    print(XSize+YSize)

root = tkinter.Tk()

# 窗口大小
root.geometry("600x450+374+182")

label1 = tkinter.Label(root, text="姓名 ：")
label2 = tkinter.Label(root, text="住址 ：")
label1.grid(row=0)
label2.grid(row=1)

entry1 = tkinter.Entry(root)
entry2 = tkinter.Entry(root)
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

button = tkinter.Button(root,text="电容设计",font=("宋体",25),fg="blue",command=getValue)
button.grid(row=1,column=2)

root.mainloop()
