import tkinter as tk
from PIL import Image, ImageTk


root = tk.Tk()
root.title('BTE - Biology To Education')
root.geometry('800x600')
root.resizable(True, True)

frameEsquerda = tk.Frame(root, bg="#78C245", width=200)
frameEsquerda.pack(side="left", fill="y")

logo = Image.open()

root.mainloop()

