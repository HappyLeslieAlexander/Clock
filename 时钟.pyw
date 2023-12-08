# 导入time和tkinter模块
import time
import tkinter as tk

# 定义一个函数，用于显示当前的时间
def show_time():
    # 获取当前的时间，格式为HH:MM:SS
    current_time = time.strftime("%H:%M:%S", time.localtime())
    # 更新标签的文本为当前的时间
    label.config(text=current_time)
    # 每隔一秒再次调用该函数
    label.after(1000, show_time)

# 创建一个窗口对象
window = tk.Tk()
# 设置窗口的标题为时钟
window.title("时钟")
# 设置窗口的大小为300x100
window.geometry("300x100")
# 设置窗口的背景颜色为墨绿色
window.config(bg="#006650")
# 创建一个标签对象，用于显示时间
label = tk.Label(window, font=("Arial", 32), bg="#006650", fg="white")
# 将标签放置在窗口的中央
label.pack(expand=1)
# 调用show_time函数
show_time()
# 进入窗口的主循环
window.mainloop()