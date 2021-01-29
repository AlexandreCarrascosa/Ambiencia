from time import sleep
import os

init, end = 0, 300


def Timer(init, end):
	while init != end:
		#print(f"A atualização será feita em {end} seg. \nTempo decorrido: {init} s")
		init += 1 
		sleep(1)
		#os.system('clear')





