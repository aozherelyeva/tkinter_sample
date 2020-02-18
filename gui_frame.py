import tkinter as tk
import python_calendar

root = tk.Tk()
root.title("Simple calendar")
root.geometry("250x150")
text2 = tk.Text(root, height=20, width=100)
quote = python_calendar.f_calendar
text2.insert(tk.END, quote)
text2.tag_configure("center", justify='center')
text2.pack()
root.mainloop()