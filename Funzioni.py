import os
#
#Rimozzione caratteri non necessari
#
def rimuovi_spazzi_non_necessari(stringa):
    temp = ""
    space = False
    for x in stringa:
        if x == " " and space == True:
            continue
        elif x == " " and space == False:
            space = True
        else:
            space = False
        temp = temp + x
    if stringa[0] == " ":
        temp = temp[1:]
    if stringa[-1] == " ":
        temp = temp[:-1]
    return temp.lower()

def rimuovi_caratteri_non_necessari(stringa):
    temp=""
    for x in stringa:
        if x == '?' or x == '!' or x == '.': continue
        temp+=x
    return temp
#
#
#
#
#Memoria e Apprendimento
#
def impara(stringa):
    if stringa != "niente":
        with open("memory.txt", 'a') as contenuto:
            contenuto.write(f"{domanda} {risposta}\n")

def memoria(domanda):
    if os.path.exists("memory.brain") == False:
        exist=open("memory.brain", 'w')
        exist.close()
    with open("memory.brain",'r') as memory:
        testo=memory.readlines()
        for frase in testo:
            if rimuovi_caratteri_non_necessari(frase).find(rimuovi_caratteri_non_necessari(domanda))!=-1:
                return (rimuovi_spazzi_non_necessari(frase[frase.find(domanda)+len(domanda)+1:]))
    return -1
#
#
#
#
#Operzzaioni sulle domande
#
def descrizione_comando(comando, parola_chiave, parola_comando):
    comand = False
    temp = ""
    for x in range(comando.find(parola_chiave, comando.find(parola_comando) + len(parola_comando)), len(comando)):
        if comando[x] == ' ':
            comand = True
            continue
        if comand == True:
            temp += comando[x]
    return temp