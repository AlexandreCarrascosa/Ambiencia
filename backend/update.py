
from subprocess import check_output, Popen, PIPE, STDOUT
import os
from time import sleep

def Atualizar():
#Muda diretório para site
    print(os.chdir(r'..//'))

    #Salvar todos os gits
    save = check_output(["git", "add", "."])
    send = check_output(["git", "commit", "-m", "'Update'"])
    #up = check_output(["git", "push"])
    
    sleep(2)
    p = Popen(["git", "push"], stdout=PIPE, stdin=PIPE, stderr=STDOUT, universal_newlines=True)
    
    sleep(1)
    info = ["alexandrecarrascosa", "725e171b8bdba60628c2d779b5ae1bcc6cdd1b9f"]
    
    output, err = p.communicate(input=f'{info[0]}\n{info[1]}\n')
    print(output)

    return save, send, output, err

Atualizar()


