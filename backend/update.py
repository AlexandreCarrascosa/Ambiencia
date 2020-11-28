
from subprocess import check_output, Popen, PIPE, STDOUT
import os
from time import sleep


def Atualizar():
#Muda diretório para site
    print(os.chdir(r'..//'))

    #Salvar todos os gits
    save = check_output(["git", "add", "."])
    send = check_output(["git", "commit", "-m", "'Update'"])
    up = check_output(["git", "push"])

    return save, send, up

while True:
	Atualizar()
	sleep((60*5))

