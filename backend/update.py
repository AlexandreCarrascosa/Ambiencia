
from subprocess import check_output, Popen, PIPE, STDOUT
import os


def Atualizar():
#Muda diretório para site
    print(os.chdir(r'..//'))

    #Salvar todos os gits
    save = check_output(["git", "add", "."])
    send = check_output(["git", "commit", "-m", "'Update'"])
    
    
    info = [b"alexandrecarrascosa", b"725e171b8bdba60628c2d779b5ae1bcc6cdd1b9f"]
    #p = Popen(["git", "push"], stdout=PIPE, stdin=PIPE, universal_newlines=True)
    
    up = check_output(["git", "push", info[0], info[1]])

    #output = Popen.communicate(f'{info[0]}\n{info[1]}\n')
    
   
   
    return save, send, up

Atualizar()


