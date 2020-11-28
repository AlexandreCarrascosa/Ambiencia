from subprocess import check_output, Popen, PIPE, STDOUT

p = Popen(["python", "update.py"], stdout=PIPE, stdin=PIPE, stderr=STDOUT, universal_newlines=True)
    
info = ["alexandrecarrascosa", "725e171b8bdba60628c2d779b5ae1bcc6cdd1b9f"]
    
output, err = p.communicate(input=f'{info[0]}\n{info[1]}\n')
print(output)
