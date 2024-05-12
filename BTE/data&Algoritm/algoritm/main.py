from Bio import SeqIO

#setando caminho do arquivo

caminhoDoArquivo = 'data/tumorNecrosis/ncbi_dataset/data/gene.fna'
caminhoSegundoArquivo = 'data/tumorProtein/ncbi_dataset/data/gene2.fna'

#realizando leitura do arquivo fna
nucleotideo = []
with open(caminhoDoArquivo, 'r') as dna:
    for sequencia in SeqIO.parse(dna, 'fasta'):
        nucleotideo.append(str(sequencia.seq))

nucleotideoDois = []
with open(caminhoSegundoArquivo, 'r') as dna2:
    for sequenciaDois in SeqIO.parse(dna2, 'fasta'):
        nucleotideoDois.append(str(sequenciaDois.seq))
        
# Método responsável pela transcrição
def transcricao(nucleotideo):
    genomaTranscrito = []
    transcricaoSeq = []
    for seq in sequencia: # Inteirando sobre o arquivo fasta
        for nucleotideo in seq:# Inteirando no método transcrição # n²
            if nucleotideo == 'T':
                transcricaoSeq.append('A')
            elif nucleotideo == 'A':
                transcricaoSeq.append('U')
            elif nucleotideo == 'G':
                transcricaoSeq.append('C')
            elif nucleotideo == 'C':
                transcricaoSeq.append('G')
    genomaTranscrito.append(''.join(transcricaoSeq)) # Cocatena os nucleotídeos em uma única string.
        
    print(genomaTranscrito)
    
rnaMensageiro = []  
#Método responsável pela tradução
def traducao(rnaMensageiro):
    sinteseProteica = []
    for codon in rnaMensageiro:  # iterador para cada base nitrogenada
        for x in range(3, (len(codon) + 3), 3): # iterador para dividir as bases de 3 em 3, formando os códons
            if codon[x -3: x] == 'AUG': # condição para formação das proteínas
                sinteseProteica.append('Met')
            elif codon[x -3: x] == 'AUC' or codon[x -3: x] == 'AUU' or codon[x -3: x] == 'AUA':
                sinteseProteica.append('Ile') # Verifica qual é a sequencia do codon e adiciona a proteina de acordo.
            elif codon[x -3: x] == 'UCG' or codon[x -3: x] == 'UCA' or codon[x -3: x] == 'UCC' or codon[x -3: x] == 'UCU' or codon[x -3: x] == 'AGU' or codon[x -3: x] == 'AGC':
                sinteseProteica.append('Ser')
            elif codon[x -3: x] ==  'UUU' or  codon[x -3: x] == 'UUC':
                sinteseProteica.append('Phe')
            elif codon[x -3: x] == 'UUA' or codon[x -3: x] == 'UUG':
                sinteseProteica.append('Leu')
            elif codon[x -3: x] == 'GUU' or codon[x -3: x] == 'GUC' or codon[x -3: x] == 'GUA' or codon[x -3: x] == 'GUG':
                sinteseProteica.append('Val')
            elif codon[x -3: x] == 'CUU' or codon[x -3: x] == 'CCC' or codon[x -3: x] == 'CCA' or codon[x -3: x] == 'CCG':
                sinteseProteica.append('Pro')
            elif codon[x -3: x] == 'ACU' or codon[x -3: x] == 'ACC' or codon[x -3: x] == 'ACA' or codon[x -3: x] == 'ACG':
                sinteseProteica.append('Thr')
            elif codon[x -3: x] == 'GCU' or codon[x -3: x] == 'GCC' or codon[x -3: x] == 'GCA' or codon[x -3: x] == 'GCG':
                sinteseProteica.append('Ala')
            elif codon[x -3: x] == 'UAU' or codon[x -3: x] == 'UAC':
                sinteseProteica.append('Tyr') 
            elif codon[x -3: x] == 'CAU' or codon[x -3: x] == 'CAC':
                sinteseProteica.append('His')
            elif codon[x -3: x] == 'CAA' or codon[x -3: x] == 'CAG':
                sinteseProteica.append('Gln')
            elif codon[x -3: x] == 'AUU' or codon[x -3: x] == 'AAC':
                sinteseProteica.append('Asn')
            elif codon[x -3: x] == 'AAA' or codon[x -3: x] == 'AAG':
                sinteseProteica.append('Lys')
            elif codon[x -3: x] == 'GAU' or codon[x -3: x] == 'GAC':
                sinteseProteica.append('Asp')
            elif codon[x -3: x] == 'GAA' or codon[x -3: x] == 'GAG':
                sinteseProteica.append('Glu')
            elif codon[x -3: x] == 'UGU' or codon[x -3: x] == 'UGC':
                sinteseProteica.append('Cys')
            elif codon[x -3: x] == 'UGG':
                sinteseProteica.append('Trp')
            elif codon[x -3: x] == 'CGU' or codon[x -3: x] == 'GCC' or codon[x -3: x] == 'CGA' or codon[x -3: x] == 'CGG' or codon[x -3: x] == 'AGA' or codon[x -3: x] == 'AGG':
                sinteseProteica.append('Arg')
            elif codon[x -3: x] == 'GGU' or codon[x -3: x] == 'GGC' or codon[x -3: x] == 'GGA' or codon[x -3: x] == 'GGG':
                sinteseProteica.append('Gly')
            elif codon[x -3: x] == 'UAA' or codon[x -3: x] == 'UAG' or codon[x -3: x] == 'UGA':
                sinteseProteica.append('Parada')
    print(sinteseProteica)

#Método responsável pela comparação
def comparador(nucleotideo, nucleotideoDois):
    nucleotideoUmSep = []
    nucleotideoDoisSep = []
    contador = 0
    for bases in nucleotideo:
        for char in bases:
            nucleotideoUmSep.append(char) # Separa os nucleotídeos em caracteres
            
    for bases in nucleotideoDois:
        for char in bases:
            nucleotideoDoisSep.append(char) # Separa o nucleotídeo 2 em caracteres
        
    memoria = []
    contador = 0
    # indexSalvo = []
    for i, x in zip(nucleotideoUmSep, nucleotideoDoisSep):# Verifica se os valores são iguais em formato de tupla
            if i == x:
                contador = contador + 1
                memoria.append((i, x)) 
                
    
    # Comparador em relação oa maior ou menor dna
    if len(nucleotideoUmSep) >= len(nucleotideoDoisSep):
        maiorDna = len(nucleotideoUmSep)
        menorDna = len(nucleotideoDoisSep)
    else:
        maiorDna = len(nucleotideoDoisSep)
        menorDna = len(nucleotideoUmSep)
    
    escolha = 0
    escolha = int(input('-' * 20 + ' Comparador ' + '-' * 20 + 
                        '\nComaparação com o maior DNA - 1' + 
                        '\nComparação com o menor DNA - 2\n'))
    if escolha == 1:
        porcentagem = contador * 100 / maiorDna
    elif escolha == 2: 
        porcentagem = contador * 100 / menorDna
    
    print(f'{porcentagem:.2f}')
                
    
comparador(nucleotideo, nucleotideoDois)




                
        
    
                    

#transcricao(nucleotideo)
