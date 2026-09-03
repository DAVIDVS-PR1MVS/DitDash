import os
import string
import unicodedata

morse=[
    #a-i (a, b, c, d, e, f, g, h, i)
    ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..",

    #j-r (j, k, l, m, n, o, p, q, r)
    ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.",

    #s-z (s, t, u, v, w, x, y, z)
    "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."

]
letters=[
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
key=dict(zip(letters, morse))
key2=dict(zip(morse, letters))

#///////////////////////
def Clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def Menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    menu = r"""
  ____  _ _     ____             _     
 |  _ \(_) |_  |  _ \  __ _ ___ | |__  
 | | | | | __| | | | |/ _` / __|| '_ \ 
 | |_| | | |_  | |_| | (_| \__ \| | | |
 |____/|_|\__| |____/ \__,_|___/|_| |_|
                                           
       [ CLI Morse Academy • v1.0.0 ]      
 ===========================================
                                           
   1. Transmitir  (Texto -> Morse)         
   2. Decodificar (Morse -> Texto)         
   3. Treinamento (Prática & Quiz)         
   4. Ajustes     (Velocidade/Bips)        
   5. Sair                                 
                                           
 ===========================================
"""
    print(f"\033[32m{menu}\033[0m")
#///////////////////////
option = " "
less = " "
text = " "
TEXT = " "
translate = " "
#///////////////////////
Menu()
option = input("Selecione o Modo: ")
#///////////////////////
def Upper():
    global text
    TEXT=text.upper()
    return TEXT
def Accentless():
    global TEXT
    nfkd = unicodedata.normalize("NFKD", TEXT)
    return ''.join([c for c in nfkd if not unicodedata.combining(c)])
def Morse():
    global less
    translate=[]
    for caractere in less:
        if caractere in key:
            translate.append(key[caractere])
        elif caractere == " ":
            translate.append("/")
        else:
            translate.append(caractere)
    return " ".join(translate)
def MinT():
    global text
    translate=[]
    for simbol in text:
        if simbol in key2:
            translate.append(key2[simbol])
        elif simbol == "/":
            translate.append(simbol)
        else:
            translate.append(simbol)
    return " ".join(translate)
def Mode():
    global option
    if option == 1:
        TEXT=Upper()
        less=Accentless()
        translate=Morse()
    elif option == 2:
        translate=MinT()
    else:
        print("Termina isso logo bixo")
#///////////////////////
#///////////////////////
print(Mode)
#///////////////////////