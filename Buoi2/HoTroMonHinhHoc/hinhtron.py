import math
import tkinter as tk
from tkinter import messagebox
pi = math.pi

def ht_gui():
    # tinh chu vi
    def chuvi():
        try:
            r = float(a.get())
            if r == 0:
                messagebox.showerror("Lỗi", "Bán kính phải lớn hơn 0")
            else:
                cv = 2*pi*r
                messagebox.showinfo("Kết quả",f"Chu vi hình tròn: {cv}")
        except Exception as e:
            messagebox.showerror("Lỗi", "Định dạng đầu vào không hợp lệ")

    # tinh dien tich
    def dientich():
        try:
            r = float(a.get())
            if r == 0:
                messagebox.showerror("Lỗi", "Bán kính phải lớn hơn 0")
            else:
                dt = pi * r * r
                messagebox.showinfo("Kết quả", f"Diện tích hình tròn: {dt}")
        except Exception as e:
            messagebox.showerror("Lỗi", "Định dạng đầu vào không hợp lệ")

    # button click
    def click():
        chuvi()
        dientich()

    ht_window = tk.Tk()
    ht_window.title("HÌNH TRÒN")
    ht_window.geometry("300x150")

    a = tk.Label(ht_window, text="Nhập độ dài bán kính:")
    a.place(x=30, y=40)
    a = tk.Entry(ht_window)
    a.place(x=160, y=40)

    button = tk.Button(ht_window, text="Tính toán", command=click)
    button.place(x=100, y=100)