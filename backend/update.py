#Mudar para a pasta do site C:\Users\alexa\Documents\Ambience\site\
import subprocess as sp
import os

def Atualizar():
#Muda diretório para site
    os.chdir(r'..//Site')

    #Salvar todos os gits
    save = sp.check_output(["git", "add", "."])
    send = sp.check_output(["git", "commit", "-m", "'Update'"])
    up = sp.check_output(["git", "push"])

    return save, send, up

Atualizar()