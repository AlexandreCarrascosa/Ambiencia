from subprocess import check_output, Popen, PIPE, STDOUT
import os
from time import sleep
from sys import platform

def Timer(init, end, msg="\n"):
    while init != end:
        #print(msg)
        #print(f'A atualização será feita em {end} seg. \nTempo decorrido: {init}s')
        init += 1
        sleep(1)
##        if platform == 'win32':
##            os.system('cls')
##        else:
##            os.system('clear')


def Atualizar():
#Muda diretório para site
    os.chdir(r'..//')

    #Salvar todos os gits
    check_output(["git", "add", "."])
    check_output(["git", "commit", "-m", "'Update'"])
    check_output(["git", "push"])
    
    os.chdir(r'backend')
    

