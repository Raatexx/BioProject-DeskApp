import tkinter as tk
from PIL import Image, ImageTk

#Janela geral
root = tk.Tk()
root.title('BTE - Biology To Education')
root.geometry('800x600')
root.resizable(True, True)

# Criação do frame da esquerda
frameEsquerda = tk.Frame(root, bg="#78C245", width=300, height=600, highlightbackground="black", highlightthickness=1)
frameEsquerda.pack(side="left", fill="y")

# Imagens
logo = Image.open(r"C:\Users\Pedro\Desktop\BioProject-DeskApp\BTE\BioToEducation\AppGUI\source\Logo.png")
logo = logo.resize((140, 140))
logoTk = ImageTk.PhotoImage(logo) 

home = Image.open(r"C:\Users\Pedro\Desktop\BioProject-DeskApp\BTE\BioToEducation\AppGUI\source\Home.png")
home = home.resize((40, 40))
homeTk = ImageTk.PhotoImage(home)

dna = Image.open(r"C:\Users\Pedro\Desktop\BioProject-DeskApp\BTE\BioToEducation\AppGUI\source\Dna.png")
dna = dna.resize((40, 40))
dnaTk = ImageTk.PhotoImage(dna)

rna = Image.open(r"C:\Users\Pedro\Desktop\BioProject-DeskApp\BTE\BioToEducation\AppGUI\source\Rna.png")
rna = rna.resize((40, 40))
rnaTk = ImageTk.PhotoImage(rna)

comparison = Image.open(r"C:\Users\Pedro\Desktop\BioProject-DeskApp\BTE\BioToEducation\AppGUI\source\Comparison.png")
comparison = comparison.resize((40, 40))
comparisonTk = ImageTk.PhotoImage(comparison)

# Alinhando ao frame da esquerda
label = tk.Label(frameEsquerda, image=logoTk, bg="#78C245")
label.image = logoTk
label.pack(fil="y")

botaoHome = tk.Button(frameEsquerda, image=homeTk, bg="#78C245", relief="flat")
botaoHome.image = homeTk
botaoHome.pack(expand=True)

botaoDna = tk.Button(frameEsquerda, image=dnaTk, bg="#78C245", relief="flat")
botaoDna.image = dnaTk
botaoDna.pack(expand=True)

botaoRna = tk.Button(frameEsquerda, image=rnaTk, bg="#78C245", relief="flat")
botaoRna.image = rnaTk
botaoRna.pack(expand=True)

botaoComparison = tk.Button(frameEsquerda, image=comparisonTk, bg="#78C245", relief="flat")
botaoComparison.image = comparisonTk
botaoComparison.pack(expand=True)


root.mainloop()

