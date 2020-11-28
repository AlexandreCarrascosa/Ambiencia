from subprocess import check_output, Popen, PIPE, STDOUT
import os
from time import sleep


def Timer(init, end, msg="\n"):
	while init != end:
		print(msg)
		print(f"A atualização será feita em {end} seg. \nTempo decorrido: {init} s")
		init += 1 
		sleep(1)
		os.system('clear')

def Atualizar():
#Muda diretório para site
    print(os.chdir(r'..//'))

    #Salvar todos os gits
    save = check_output(["git", "add", "."])
    send = check_output(["git", "commit", "-m", "'Update'"])
    up = check_output(["git", "push"])
    
    return save, send, up
    

