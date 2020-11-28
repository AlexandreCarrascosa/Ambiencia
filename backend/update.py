
from subprocess import check_output, Popen, PIPE, STDOUT
import os


def Atualizar():
#Muda diretório para site
    print(os.chdir(r'..//'))

    #Salvar todos os gits
    save = check_output(["git", "add", "."])
    send = check_output(["git", "commit", "-m", "'Update'"])
    
    #up = check_output(["git", "push"])
    send = ["git", "push"]
    
    
    
    info = ["alexandrecarrascosa", "725e171b8bdba60628c2d779b5ae1bcc6cdd1b9f"]
    output = Popen(send, stdout=PIPE).communicate(input=f'{info[0]}\n{info[1]}')[0]
    #output = Popen.communicate(f'{info[0]}\n{info[1]}\n')
    print(output)
   
   
    return save, send, output

Atualizar()


