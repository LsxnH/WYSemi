import tkinter
from DesignUnits import *
#import matplotlib

def printValue(BV, Cap):
    BVOutput.delete(0.0, tkinter.END)
    BVOutput.insert(tkinter.END, "%.1f"%(BV))
    CapOutput.delete(0.0, tkinter.END)
    CapOutput.insert(tkinter.END, "%.1f"%(Cap))

def on_push():
    ChipX        = float(entry_chipX       .get())
    ChipY        = float(entry_chipY       .get())
    BlockSize    = float(entry_BlockSize   .get())
    BlockSpace   = float(entry_BlockSpace  .get())
    UnitSpace    = float(entry_UnitSpace   .get())
    k            = float(entry_k           .get())
    d            = float(entry_d           .get())
    TrenchLength = float(entry_TrenchLength.get())
    TrenchCD     = float(entry_TrenchCD    .get())
    TrenchDepth  = float(entry_TrenchDepth .get())
    TrenchSpace  = float(entry_TrenchSpace .get())

    BV = d*0.075
    Cap_Unit = UnitCapCal(k, d, TrenchLength, TrenchCD, TrenchDepth, TrenchSpace)
    N_Units = UnitsCountCal(ChipX, ChipY, BlockSize, BlockSpace, UnitSpace)
    Cap = Cap_Unit*N_Units
    printValue(BV, Cap)

root = tkinter.Tk()
root.title("硅基电容设计")

# 窗口大小
root.geometry("660x450+374+182")
    
label_chipX        = tkinter.Label(root, text="Size X(um) ：")
label_chipY        = tkinter.Label(root, text="Size Y(um) ：")
label_BlockSize    = tkinter.Label(root, text="Block size(um) ：")
label_BlockSpace   = tkinter.Label(root, text="Block space(um) ：")
label_UnitSpace    = tkinter.Label(root, text="Unit space(um) ：")
label_TrenchLength = tkinter.Label(root, text="Trench length(um) ：")
label_TrenchCD     = tkinter.Label(root, text="Trench CD(um) ：")
label_TrenchDepth  = tkinter.Label(root, text="Trench depth(um) ：")
label_TrenchSpace  = tkinter.Label(root, text="Trench space(um) ：")
label_k            = tkinter.Label(root, text="Dielectric k-value ：")
label_d            = tkinter.Label(root, text="Dielectric thickness(nm) ：")

label_chipX       .grid(row=0)
label_chipY       .grid(row=1)
label_BlockSize   .grid(row=2)
label_BlockSpace  .grid(row=3)
label_UnitSpace   .grid(row=4)
label_TrenchLength.grid(row=5)
label_TrenchCD    .grid(row=6)
label_TrenchDepth .grid(row=7)
label_TrenchSpace .grid(row=8)
label_k           .grid(row=9)
label_d           .grid(row=10)

entry_chipX        = tkinter.Entry(root)
entry_chipY        = tkinter.Entry(root)
entry_BlockSize    = tkinter.Entry(root, textvariable="Andy")
entry_BlockSpace   = tkinter.Entry(root)
entry_UnitSpace    = tkinter.Entry(root)
entry_TrenchLength = tkinter.Entry(root, textvariable="Andy")
entry_TrenchCD     = tkinter.Entry(root)
entry_TrenchDepth  = tkinter.Entry(root)
entry_TrenchSpace  = tkinter.Entry(root)
entry_k            = tkinter.Entry(root)
entry_d            = tkinter.Entry(root)

entry_chipX       .insert(0, 600)
entry_chipY       .insert(0, 300)
entry_BlockSize   .insert(0, 15)
entry_BlockSpace  .insert(0, 0.1)
entry_UnitSpace   .insert(0, 0.1)
entry_TrenchCD    .insert(0, 0.7)
entry_TrenchDepth .insert(0, 20)
entry_TrenchSpace .insert(0, 0.5)
entry_k           .insert(0, 3.9)
entry_d           .insert(0, 30)

entry_chipX       .grid(row=0,  column=1)
entry_chipY       .grid(row=1,  column=1)
entry_BlockSize   .grid(row=2,  column=1)
entry_BlockSpace  .grid(row=3,  column=1)
entry_UnitSpace   .grid(row=4,  column=1)
entry_TrenchLength.grid(row=5,  column=1)
entry_TrenchCD    .grid(row=6,  column=1)
entry_TrenchDepth .grid(row=7,  column=1)
entry_TrenchSpace .grid(row=8,  column=1)
entry_k           .grid(row=9,  column=1)
entry_d           .grid(row=10, column=1)


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
button.grid(row=22,column=3)

root.mainloop()