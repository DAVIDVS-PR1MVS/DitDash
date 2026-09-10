import os
import string
import unicodedata
import re
import sys

morse=[
    #a-i (a, b, c, d, e, f, g, h, i)
    ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..",

    #j-r (j, k, l, m, n, o, p, q, r)
    ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.",

    #s-z (s, t, u, v, w, x, y, z)
    "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..",
    #1-9
    "-----", ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----."

]
letters=[
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
]
key=dict(zip(letters, morse))
key2=dict(zip(morse, letters))

#///////////////////////
def Clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def Menu():
    Clear()
    
    menu = r"""
  ____  _ _    ____  _             
 |  _ \(_) |_ |  _ \| | _____  __  
 | | | | | __|| |_) | |/ _ \ \/ /  
 | |_| | | |_ |  __/| |  __/>  <   
 |____/|_|\__||_|   |_|\___/_/\_\  
                                           
       [ CLI Morse Academy • v1.1.1 ]      
 ===========================================
                                           
   1. Transmitir  (Texto -> Morse)         
   2. Decodificar (Morse -> Texto)         
   3. Sair                                 
                                           
 ===========================================
"""
    print(f"\033[32m{menu}\033[0m")
#///////////////////////
thisnamebecauseyes = " "
number = 0
option = " "
less = " "
text = " "
TEXT = " "
translate = " "
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
    for simbol in text.split(" "):
        if simbol in key2:
            translate.append(key2[simbol])
        elif simbol == "/":
            translate.append(" ")
        else:
            translate.append(simbol)
    return "".join(translate)
def Number():
    global option, number
    thisnamebecauseyes=re.sub(r"\D", "", option)
    number = int(thisnamebecauseyes) if thisnamebecauseyes else 0
def Mode():
    global number, text, TEXT, less, translate
    if number == 1:
        Clear()
        text = input("Digite o texto: ")
        TEXT=Upper()
        less=Accentless()
        translate=Morse()
        print("\nResultado:", translate)
        input("\nPressione Enter para continuar...")
    elif number == 2:
        Clear()
        text = input("Digite o código Morse (separe letras por espaço e palavras por /): ")
        translate=MinT()
        print("\nResultado:", translate)
        input("\nPressione Enter para continuar...")
    elif number == 3:
        sys.exit()
    else:
        print("Esse modo Não existe, tente novamente")
        input("\nPressione Enter para tentar novamente...")
#///////////////////////
while True:
    Menu()
    option = input("Selecione o Modo: ")
    Number()
    Mode()
#///////////////////////