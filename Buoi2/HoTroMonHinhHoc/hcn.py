import tkinter as tk
from tkinter import messagebox

def hcn_gui():
    #tinh chu vi
    def chuvi():
        try:
            cd = float(a.get())
            cr = float(b.get())
            if cd==0 or cr==0:
                messagebox.showerror("Lỗi", "Chiều dài và chiều rộng phải lớn hơn 0")
            elif cr > cd:
                messagebox.showerror("Lỗi", "Chiều rộng phải bé hơn chiều dài")
            else:
                cv = (cd + cr) * 2
                messagebox.showinfo("Kết quả",f"Chu vi hình chữ nhật: {cv}")
        except Exception as e:
            messagebox.showerror("Lỗi","Định dạng đầu vào không hợp lệ")

    #tinh dien tich
    def dientich():
        try:
            cd = float(a.get())
            cr = float(b.get())
            if cd == 0 or cr == 0:
                messagebox.showerror("Lỗi", "Chiều dài và chiều rộng phải lớn hơn 0")
            elif cr > cd:
                messagebox.showerror("Lỗi", "Chiều rộng phải bé hơn chiều dài")
            else:
                dt = cd * cr
                messagebox.showinfo("Kết quả",f"Diện tích hình chữ nhật: {dt}")
        except Exception as e:
            messagebox.showerror("Lỗi","Định dạng đầu vào không hợp lệ")

    #button click
    def click():
        chuvi()
        dientich()

    #GUI
    hcn_window = tk.Tk()
    hcn_window.title("HÌNH CHỮ NHẬT")
    hcn_window.geometry("300x200")

    a = tk.Label(hcn_window,text="Nhập chiều dài:")
    a.place(x=30,y=40)
    a = tk.Entry(hcn_window)
    a.place(x=130,y=40)
    b = tk.Label(hcn_window, text="Nhập chiều rộng:")
    b.place(x=30, y=80)
    b = tk.Entry(hcn_window)
    b.place(x=130, y=80)

    button = tk.Button(hcn_window,text="Tính toán",command=click)
    button.place(x=100,y=130)