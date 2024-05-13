import tkinter as tk
from PIL import Image, ImageTk

#Janela geral
root = tk.Tk()
root.title('BTE - Biology To Education')
root.geometry('800x600')
root.resizable(True, True)

# Criação do frame da esquerda
frameEsquerda = tk.Frame(root, bg="#78C245", width=300, height=600)
frameEsquerda.pack(side="left", fill="y")

# Logo Bte
logo = Image.open(r"C:\Users\Pedro\Desktop\BioProject-DeskApp\BTE\BioToEducation\AppGUI\source\Logo.png")
logo = logo.resize((120, 120))
logoTk = ImageTk.PhotoImage(logo) 

# Calculo para posicionar a imagem no meio
alturaImagem = logoTk.height()
alturaFrame = frameEsquerda.winfo_height()
espaco = (alturaFrame - alturaImagem) % 2

# Alinhando ao frame da esquerda
label = tk.Label(frameEsquerda, image=logoTk, bg="#78C245")
label.image = logoTk
label.pack(pady=espaco)

root.mainloop()

