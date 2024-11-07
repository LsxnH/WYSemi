import tkinter
from DesignUnits import *

ChipX      = 760
ChipY      = 760
BlockSize  = 11
BlockSpace = 0.1
UnitSpace  = 0.1
k          = 6.9
d          = 5400
TrenchLength = 0
TrenchCD     = 1.5
TrenchDepth  = 45
TrenchSpace  = 1

def func(Par):
    print("myname")

def getValue():
    ChipX        = float(entry_chipX       .get())
    ChipY        = float(entry_chipY       .get())
    #BlockSize    = float(entry_BlockSize   .get())
    #BlockSpace   = float(entry_BlockSpace  .get())
    #UnitSpace    = float(entry_UnitSpace   .get())
    #k            = float(entry_k           .get())
    #d            = float(entry_d           .get())
    #TrenchLength = float(entry_TrenchLength.get())
    #TrenchCD     = float(entry_TrenchCD    .get())
    #TrenchDepth  = float(entry_TrenchDepth .get())
    #TrenchSpace  = float(entry_TrenchSpace .get())

def printValue(BV, Cap):
    BVOutput.insert(tkinter.END, "%s"%(BV))
    CapOutput.insert(tkinter.END, "%s"%(Cap))

def on_push():
    getValue()
    printValue(ChipX, ChipY) ###  value not updated

root = tkinter.Tk()
root.title("硅基电容设计")

# 窗口大小
root.geometry("600x450+374+182")
    
label_chipX        = tkinter.Label(root, text="封装尺寸X(mm) ：")
label_chipY        = tkinter.Label(root, text="封装尺寸Y(mm) ：")
label_BlockSize    = tkinter.Label(root, text="Block size(um) ：")
label_BlockSpace   = tkinter.Label(root, text="Block space(um) ：")
label_UnitSpace    = tkinter.Label(root, text="Unit space(um) ：")
label_k            = tkinter.Label(root, text="Dielectric k-value ：")
label_d            = tkinter.Label(root, text="Dielectric thickness($\\angstrom$) ：")
label_TrenchLength = tkinter.Label(root, text="Trench length(um) ：")
label_TrenchCD     = tkinter.Label(root, text="Trench CD(um) ：")
label_TrenchDepth  = tkinter.Label(root, text="Trench depth(um) ：")
label_TrenchSpace  = tkinter.Label(root, text="Trench space(um) ：")
label_chipX       .grid(row=0)
label_chipY       .grid(row=1)
label_BlockSize   .grid(row=2)
label_BlockSpace  .grid(row=3)
label_UnitSpace   .grid(row=4)
label_k           .grid(row=5)
label_d           .grid(row=6)
label_TrenchLength.grid(row=7)
label_TrenchCD    .grid(row=8)
label_TrenchDepth .grid(row=9)
label_TrenchSpace .grid(row=10)

entry_chipX        = tkinter.Entry(root)
entry_chipY        = tkinter.Entry(root)
entry_BlockSize    = tkinter.Entry(root)
entry_BlockSpace   = tkinter.Entry(root)
entry_UnitSpace    = tkinter.Entry(root)
entry_k            = tkinter.Entry(root)
entry_d            = tkinter.Entry(root)
entry_TrenchLength = tkinter.Entry(root)
entry_TrenchCD     = tkinter.Entry(root)
entry_TrenchDepth  = tkinter.Entry(root)
entry_TrenchSpace  = tkinter.Entry(root)


entry_chipX       .grid(row=0, column=1)
entry_chipY       .grid(row=1, column=1)
entry_BlockSize   .grid(row=2,  column=1)
entry_BlockSpace  .grid(row=3,  column=1)
entry_UnitSpace   .grid(row=4,  column=1)
entry_k           .grid(row=5,  column=1)
entry_d           .grid(row=6,  column=1)
entry_TrenchLength.grid(row=7,  column=1)
entry_TrenchCD    .grid(row=8,  column=1)
entry_TrenchDepth .grid(row=9,  column=1)
entry_TrenchSpace .grid(row=10, column=1)

labelBV = tkinter.Label(root, text="电容耐压(V) ：")
labelBV.grid(row=20)

BVOutput = tkinter.Text(root,width=20,height=2)
BVOutput.grid(row=20, column=1)

labelCap = tkinter.Label(root, text="电容容值(nF) ：")
labelCap.grid(row=20, column=2)

CapOutput = tkinter.Text(root,width=20,height=2)
CapOutput.grid(row=20, column=3)
#BVOutput.pack()

button = tkinter.Button(root,text="电容设计",font=("宋体",25),fg="blue",command=on_push)
button.grid(row=18,column=2)

root.mainloop()