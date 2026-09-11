import os
import unicodedata
import re
import sys
import platform

#///////////////////////
version="1.3.0"
operational=platform.system()
arch=platform.machine()
#///////////////////////
VERDE = "\033[32m"
CIANO = "\033[36m"
AMARELO = "\033[33m"
CINZA = "\033[90m"
RESET = "\033[0m"
#///////////////////////
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
                                           
                                          
 ===========================================
                                           
   1. Transmitir  (Texto -> Morse)         
   2. Decodificar (Morse -> Texto)         
   3. Sair                                 
                                           
 ===========================================
"""
    print(f"{VERDE}{menu}{RESET}")
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
if len(sys.argv) > 1:
    arg = sys.argv[1].lower()
    
    if arg in ["--info", "-v"]:
        print(f"{VERDE}[Version]:{RESET} {version} {VERDE}[OS/Arch]:{RESET} {operational}/{arch} {VERDE}[License]:{RESET} MIT")
        sys.exit(0)
    elif arg in ["--help", "-h"]:
        print(f"{VERDE}Uso:{RESET} DitPlex [opção] [conteúdo]\n")
        print(f"{VERDE}Opções disponíveis:{RESET}")
        print(f"  {VERDE}-t, --text{RESET} <texto>   Converte texto em código Morse.")
        print(f"  {VERDE}-m, --morse{RESET} <morse>   Converte código Morse em texto.")
        print(f"  {VERDE}-v, --info{RESET}          Exibe metadados, sistema e versão do aplicativo.")
        print(f"  {VERDE}-h, --help{RESET}          Exibe este menu de ajuda.")
        sys.exit(0)
    elif arg in ["--text", "-t"]:
        if len(sys.argv)>2:
            entrada=sys.argv[2]
            text=entrada
            TEXT=Upper()
            less=Accentless()
            translate=Morse()
            print(translate)
        else:
            print(f"Erro: Faltou informar o texto. Exemplo: DitPlex -t \"SOS\"")
            sys.exit(1)
        sys.exit(0)
    elif arg in ["--morse", "-m"]:
        if len(sys.argv)>2:
            entrada=sys.argv[2]
            text=entrada
            translate=MinT()
            print(translate)
        else:
            print(f"Erro: Faltou informar o código Morse. Exemplo: DitPlex -m \"... --- ...\"")
            sys.exit(1)
        sys.exit(0)
    else:
        print(f"Opção desconhecida: '{sys.argv[1]}'. Use --help para ver as opções disponíveis.")
        sys.exit(1)
#///////////////////////
try:
    while True:
        Menu()
        option = input("Selecione o Modo: ")
        Number()
        Mode()
except KeyboardInterrupt:
    sys.exit(0)
#///////////////////////