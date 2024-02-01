#exemplos basico de python
print('funciona!!!')
nota1 = 7
print(nota1)
print(type(nota1))
print(f'nota1 tem valor {nota1} e é do tipo {type(nota1)} ')
nota2 = 7.3
print(f'nota2 tem valor {nota2} e é do tipo {type(nota2)} ')
aluno = 'maria'
print(f'aluno tem valor {aluno} e é do tipo {type(aluno)} ')
media = (nota1 + nota2) / 2
print(f'{aluno}\t{nota1}\t{nota2}\t{media}') #\t tabula e \n nova linha 


#Operadores aritmetricos 
soam = nota1 + nota2
divisao = nota1 / nota2
multiplicacao = nota1 * nota2
subtracao = nota1 - nota2
resto_divisao = nota1 % nota2

#Exemplo de interarçao do usuario 


#nome = input('digite seu nome ')
#print(f'ola {nome}. seja bem vindo(a)!')

#exercicio de dois valores numericos  e apresente o resto da divisao

#OBS = input sempre retorna um texto (string), se precisar que seja numerico, faz-se necessario a conversão


nome2 = input('digite seu nome')
print(f'ola {nome2}. seja bem vindo a sua nota e ')
num1 = int(input ('valor 1:'))
num2 = int(input('valor 2'))
resto = num1 % num2 
print(f'{num1} % {num2} = {resto}')

# leia uma valor de um produto e o desconto em reais e apresente o valor em real 

print('microondas ')

valor = float(input('digite o valor do produto '))
desconto = float(input('o desconto é de '))

valor_final = valor - desconto 

print(f'valor a pagar e {valor_final}')

