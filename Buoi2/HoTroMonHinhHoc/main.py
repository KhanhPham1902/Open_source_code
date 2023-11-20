import tkinter as tk
from hcn import hcn_gui
from hv import hv_gui
from tamgiac import tg_gui
from hinhtron import ht_gui

#cua so giao dien chinh
window = tk.Tk()
window.title("Phần mềm hỗ trợ học tập môn hình học")
window.geometry("300x200")

lb1 = tk.Label(window,text="Chọn loại hình học")
lb1.place(x=100,y=0)

hcn = tk.Button(window,text="Hình chữ nhật",command=hcn_gui)
hcn.place(x=30,y=40)
hv = tk.Button(window,text="Hình vuông",command=hv_gui)
hv.place(x=180, y=40)
tg = tk.Button(window,text="Tam giác",command=tg_gui)
tg.place(x=30,y=100)
ht = tk.Button(window,text="Hình tròn",command=ht_gui)
ht.place(x=180,y=100)

window.mainloop()