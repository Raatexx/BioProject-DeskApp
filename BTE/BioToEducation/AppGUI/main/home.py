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

home = Image.open(r"C:\Users\Pedro\Desktop\BioProject-DeskApp\BTE\BioToEducation\AppGUI\source\Home.png")
home = home.resize((45, 45))
homeTk = ImageTk.PhotoImage(home)

dna = Image.open(r"C:\Users\Pedro\Desktop\BioProject-DeskApp\BTE\BioToEducation\AppGUI\source\Dna.png")
dna = dna.resize((45, 45))
dnaTk = ImageTk.PhotoImage(dna)

rna = Image.open(r"C:\Users\Pedro\Desktop\BioProject-DeskApp\BTE\BioToEducation\AppGUI\source\Rna.png")
rna = rna.resize((45, 45))
rnaTk = ImageTk.PhotoImage(rna)

comparison = Image.open(r"C:\Users\Pedro\Desktop\BioProject-DeskApp\BTE\BioToEducation\AppGUI\source\Comparison.png")
comparison = comparison.resize((45, 45))
comparisonTk = ImageTk.PhotoImage(comparison)

# Calculo para posicionar a imagem no meio
alturaImagem = logoTk.height()
alturaFrame = frameEsquerda.winfo_height()
alturaTotal = 120 + 45*4
espaco = (alturaFrame - alturaTotal) % 2

# Alinhando ao frame da esquerda
label = tk.Label(frameEsquerda, image=logoTk, bg="#78C245")
label.image = logoTk
label.pack(pady=espaco)

botaoHome = tk.Button(frameEsquerda, image=homeTk, bg="#78C245")
botaoHome.image = homeTk
botaoHome.pack(pady=espaco)

botaoDna = tk.Button(frameEsquerda, image=dnaTk, bg="#78C245")
botaoDna.image = dnaTk
botaoDna.pack(pady=espaco)

botaoRna = tk.Button(frameEsquerda, image=rnaTk, bg="#78C245")
botaoRna.image = rnaTk
botaoRna.pack(pady=espaco)

botaoComparison = tk.Button(frameEsquerda, image=comparisonTk, bg="#78C245")
botaoComparison.image = comparisonTk
botaoComparison.pack(pady=espaco)


root.mainloop()

