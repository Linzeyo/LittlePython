import tkinter as tk
from tkinter import messagebox, scrolledtext
import psutil
import os

# 放大比例
scale_factor = 1

def list_ports():
    text.delete('1.0', tk.END)
    connections = psutil.net_connections()
    for conn in connections:
        if conn.laddr:
            try:
                process = psutil.Process(conn.pid)
                process_name = process.name()
            except psutil.NoSuchProcess:
                process_name = "未知"
            text.insert(tk.END, f"端口: {conn.laddr.port}, 进程ID: {conn.pid}, 进程名称: {process_name}\n")

def kill_process():
    try:
        port = int(entry_port.get())
        connections = psutil.net_connections()
        for conn in connections:
            if conn.laddr and conn.laddr.port == port:
                os.kill(conn.pid, 9)
                messagebox.showinfo("提示", f"端口 {port} 的进程已终结")
                list_ports()
                return
        messagebox.showwarning("警告", f"未找到使用端口 {port} 的进程")
    except ValueError:
        messagebox.showerror("错误", "请输入有效的端口号")

def search_port():
    try:
        port = int(entry_port.get())
        text.delete('1.0', tk.END)
        connections = psutil.net_connections()
        found = False
        for conn in connections:
            if conn.laddr and conn.laddr.port == port:
                try:
                    process = psutil.Process(conn.pid)
                    process_name = process.name()
                except psutil.NoSuchProcess:
                    process_name = "未知"
                text.insert(tk.END, f"端口: {conn.laddr.port}, 进程ID: {conn.pid}, 进程名称: {process_name}\n")
                found = True
        if not found:
            text.insert(tk.END, f"未找到使用端口 {port} 的进程\n")
    except ValueError:
        messagebox.showerror("错误", "请输入有效的端口号")

def show_process_info():
    try:
        pid = int(entry_pid.get())
        process = psutil.Process(pid)
        info = process.as_dict(attrs=['pid', 'name', 'status', 'create_time', 'cpu_times', 'memory_info'])
        text.delete('1.0', tk.END)
        for key, value in info.items():
            text.insert(tk.END, f"{key}: {value}\n")
    except (ValueError, psutil.NoSuchProcess):
        messagebox.showerror("错误", "请输入有效的进程ID")

root = tk.Tk()
root.title("端口管理")
root.geometry(f"{int(500 * scale_factor)}x{int(600 * scale_factor)}")

frame_port = tk.Frame(root)
frame_port.pack(pady=int(10 * scale_factor))

label_port = tk.Label(frame_port, text="输入端口号:", font=("Arial", int(12 * scale_factor)))
label_port.pack(side=tk.LEFT)

entry_port = tk.Entry(frame_port, font=("Arial", int(12 * scale_factor)))
entry_port.pack(side=tk.LEFT, padx=int(5 * scale_factor))

button_kill = tk.Button(frame_port, text="终结进程", command=kill_process, font=("Arial", int(12 * scale_factor)))
button_kill.pack(side=tk.LEFT, padx=int(5 * scale_factor))

button_search = tk.Button(frame_port, text="搜索端口", command=search_port, font=("Arial", int(12 * scale_factor)))
button_search.pack(side=tk.LEFT, padx=int(5 * scale_factor))

frame_pid = tk.Frame(root)
frame_pid.pack(pady=int(10 * scale_factor))

label_pid = tk.Label(frame_pid, text="输入进程ID:", font=("Arial", int(12 * scale_factor)))
label_pid.pack(side=tk.LEFT)

entry_pid = tk.Entry(frame_pid, font=("Arial", int(12 * scale_factor)))
entry_pid.pack(side=tk.LEFT, padx=int(5 * scale_factor))

button_info = tk.Button(frame_pid, text="显示进程信息", command=show_process_info, font=("Arial", int(12 * scale_factor)))
button_info.pack(side=tk.LEFT, padx=int(5 * scale_factor))

button_list = tk.Button(root, text="列出所有端口", command=list_ports, font=("Arial", int(12 * scale_factor)))
button_list.pack(pady=int(5 * scale_factor))

text = scrolledtext.ScrolledText(root, height=int(20 * scale_factor), width=int(70 * scale_factor), font=("Arial", int(12 * scale_factor)))
text.pack(pady=int(10 * scale_factor))

root.mainloop()
