import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title('BTE - Biology To Education')
root.geometry('800x600')
root.resizable(True, True)

frameEsquerda = tk.Frame(root, bg="#78C245", width=200, height=600)
frameEsquerda.pack(side="left", fill="y")

logo = Image.open(r"C:\Users\Pedro\Desktop\BioProject-DeskApp\BTE\BioToEducation\AppGUI\source\Logo.png")
logo = logo.resize((100, 100))
logoTk = ImageTk.PhotoImage(logo) 

# Calculo para posicionar a imagem no meio
alturaImagem = logoTk.height()
alturaFrame = frameEsquerda.winfo_height()
espaco = (alturaFrame - alturaImagem) // 2

label = tk.Label(frameEsquerda, image=logoTk, bg="#78C245")
label.image = logoTk
label.pack(pady=espaco)

root.mainloop()

