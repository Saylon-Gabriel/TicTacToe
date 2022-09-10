import os
import time
import random 
from colorama import Fore

jogadas = 0
maxJogadas = 9
quemJoga = 1
vitoria = False
jogarNovamente = 's'
vencedor = ''
matriz = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

def tela():
	os.system('clear')
	print('    0   1   2')
	print(f'0:  {matriz[0][0]} | {matriz[0][1]} | {matriz[0][2]}')
	
	print(f'1:  {matriz[1][0]} | {matriz[1][1]} | {matriz[1][2]}')
	
	print(f'2:  {matriz[2][0]} | {matriz[2][1]} | {matriz[2][2]}')
	
	print(f'Jogadas: {Fore.GREEN} {str(jogadas)} {Fore.RESET}')

def jogadorJoga():
	global quemJoga
	global maxJogadas
	global jogadas
	
	if quemJoga == 1 and jogadas < maxJogadas:
			try:
				l = int(input('Linha: '))
				c = int(input('Coluna: '))
		 	
				while matriz[l][c] != ' ':
					print('O espaço não está vazio! Digite novamente')
					l = int(input('Linha: '))
					c = int(input('Coluna: '))
				matriz[l][c] = 'X'
				quemJoga = 2
				jogadas+=1
			except:
				print('Espaço inválido')
				time.sleep(1)
				
		
def cpuJoga():
	global quemJoga
	global maxJogadas
	global jogadas
	
	if quemJoga == 2 and jogadas < maxJogadas:
		l = random.randrange(0, 3)
		c = random.randrange(0, 3)
		
		while matriz[l][c] != ' ':
			l = random.randrange(0, 3)
			c = random.randrange(0, 3)
		
		matriz[l][c] = 'O'
		quemJoga = 1
		jogadas+=1

def verificarVitoria():
	global matriz
	vit = 'n'
	simbolos = ['X', 'O']
	
	for s in simbolos:
		
		vit = 'n'
		il=ic=0
		
		while il < 3:
			soma = 0
			ic = 0
			
			while ic < 3:
				if matriz[il][ic] == s:
					soma+=1
				ic+=1
			if soma == 3:
				vit = s
				break
			il+=1
		if vit != 'n':
			break
			
		il=ic=0
		while ic < 3:
			soma = 0
			il = 0
			
			while il < 3:
				if matriz[il][ic] == s:
					soma+=1
				il+=1
			if soma == 3:
				vit = s
				break
			ic+=1
		if vit != 'n':
			break
			
		soma = 0
		idiag = 0
		
		while idiag < 3:
			if matriz[idiag][idiag] == s:
				soma+=1
			idiag+=1
		if soma == 3:
			vit = s
			break
		
		soma = 0
		idiag = 0
		idiagl = 0
		idiagc = 2
		
		while idiagc >= 0:
			if matriz[idiagl][idiagc] == s:
				soma+=1
			idiagl+=1
			idiagc-=1
		if soma == 3:
			vit = s
			break
	return vit

def redefinir():
	global jogadas
	global quemJoga
	global vencedor
	global matriz
	
	jogadas = 0
	quemJoga = 1
	vencedor = ''
	matriz = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
	
while jogarNovamente == 's':
	while True:
		tela()
		jogadorJoga()
		cpuJoga()
		vencedor = verificarVitoria()
		if vencedor != 'n' or jogadas >= maxJogadas:
					tela()
					break
		
	print(f'{Fore.RED}Fim de Jogo{Fore.RESET}')
	if vencedor == 'X':
			print(f'{Fore.YELLOW}Você venceu')
	elif vencedor == 'O':
		print(f'{Fore.YELLOW}A CPU venceu')
	else:
		print('Empate!')
	
	jogarNovamente = input(f'{Fore.BLUE}Jogar novamente? s/n:{Fore.RESET}').lower().strip()
	if jogarNovamente == 'n':
		print('Jogo Finalizado')
	redefinir()		