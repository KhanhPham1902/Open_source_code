import math
import tkinter as tk
from tkinter import messagebox

def tg_gui():
    # tinh chu vi
    def chuvi():
        try:
            x = float(a.get())
            y = float(b.get())
            z = float(c.get())
            if x == 0 or y == 0 or z==0:
                messagebox.showerror("Lỗi", "Các cạnh phải lớn hơn 0")
            elif x+y<z or y+z<x or z+x<y:
                messagebox.showerror("Lỗi", "Không phải 3 cạnh tam giác")
            else:
                cv = x+y+z
                messagebox.showinfo("Kết quả",f"Chu vi hình tam giác: {cv}")
        except Exception as e:
            messagebox.showerror("Lỗi", "Định dạng đầu vào không hợp lệ")

    # tinh dien tich
    def dientich():
        try:
            x = float(a.get())
            y = float(b.get())
            z = float(c.get())
            if x == 0 or y == 0 or z == 0:
                messagebox.showerror("Lỗi", "Các cạnh phải lớn hơn 0")
            elif x + y < z or y + z < x or z + x < y:
                messagebox.showerror("Lỗi", "Không phải 3 cạnh tam giác")
            else:
                s = float(x+y+z)/2
                dt = math.sqrt(s*(s-x)*(s-y)*(s-z))
                messagebox.showinfo("Kết quả",f"Diện tích hình tam giác: {dt}")
        except Exception as e:
            messagebox.showerror("Lỗi", "Định dạng đầu vào không hợp lệ")

    # button click
    def click():
        chuvi()
        dientich()

    tg_window = tk.Tk()
    tg_window.title("HÌNH TAM GIÁC")
    tg_window.geometry("300x200")

    a = tk.Label(tg_window, text="Nhập độ dài cạnh a:")
    a.place(x=30, y=40)
    a = tk.Entry(tg_window)
    a.place(x=150, y=40)
    b = tk.Label(tg_window, text="Nhập độ dài cạnh b:")
    b.place(x=30, y=80)
    b = tk.Entry(tg_window)
    b.place(x=150, y=80)
    c = tk.Label(tg_window, text="Nhập độ dài cạnh c:")
    c.place(x=30, y=120)
    c = tk.Entry(tg_window)
    c.place(x=150, y=120)

    button = tk.Button(tg_window, text="Tính toán", command=click)
    button.place(x=100, y=160)