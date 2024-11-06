from tkinter import *
from tkinter import messagebox
 
def func(XSize):
    print("myname")
    print(XSize)
 
# 创建窗口：实例化一个窗口对象。
root = Tk()
 
# 窗口大小
root.geometry("600x450+374+182")
 
#  窗口标题
root.title("硅基电容设计")
 
# 添加标签控件
label = Label(root,text="签名：",font=("宋体",25),fg="red")
# 定位
label.grid()
 
# 添加输入框
entry = Entry(root,font=("宋体",25),fg="red")
entry.grid(row=0,column=1)
 
entry1 = Entry(root,font=("宋体",25),fg="red")
entry1.grid(row=0,column=2)

# 添加点击按钮
button = Button(root,text="签名设计",font=("宋体",25),fg="blue",command=func(entry.get()))
button.grid(row=1,column=2)
"""
command=func表示调用最开始定义的func函数。
func函数一定要在这句代码之前，因为这里需要调用这个func函数。
"""
# 显示窗口
root.mainloop()