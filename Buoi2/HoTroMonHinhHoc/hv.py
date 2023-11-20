import tkinter as tk
from tkinter import messagebox

def hv_gui():
    # tinh chu vi
    def chuvi():
        try:
            x = float(a.get())
            if x == 0:
                messagebox.showerror("Lỗi", "Cạnh phải lớn hơn 0")
            else:
                cv = x * 4
                messagebox.showinfo("Kết quả",f"Chu vi hình vuông: {cv}")
        except Exception as e:
            messagebox.showerror("Lỗi", "Định dạng đầu vào không hợp lệ")
    # tinh dien tich
    def dientich():
        try:
            x = float(a.get())
            if x == 0:
                messagebox.showerror("Lỗi", "Cạnh phải lớn hơn 0")
            else:
                dt = x * x
                messagebox.showinfo("Kết quả",f"Diện tích hình vuông: {dt}")
        except Exception as e:
            messagebox.showerror("Lỗi", "Định dạng đầu vào không hợp lệ")
    # button click
    def click():
        chuvi()
        dientich()

    hv_window = tk.Tk()
    hv_window.title("HÌNH VUÔNG")
    hv_window.geometry("300x200")

    a = tk.Label(hv_window, text="Nhập độ dài cạnh:")
    a.place(x=30, y=40)
    a = tk.Entry(hv_window)
    a.place(x=150, y=40)

    button = tk.Button(hv_window, text="Tính toán", command=click)
    button.place(x=100, y=80)