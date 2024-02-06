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






#para salvar o arquivo na nuvem 

#git add ola.py
#git commit -m "coamndos basicos "
#git push

#1. Faça um programa que imprima o seu nome.

nome = input('digite seu nome ')
print(f'ola {nome}. bom dia (a)!')
#ou

print('luis eduardo')

#----------------------------------------------------------------------------------------------------------------------------

#2. Faça um programa que imprima o produto dos valores 30 e 27.

print(30*27)

#----------------------------------------------------------------------------------------------------------------------------
#3. Faça um programa que imprima a média aritmética entre os números 5, 8, 12.
 
n1 = 6
n2 = 8
n3 = 12
soma = (n1+n2+n3) / 3
print(f'{soma}')

#----------------------------------------------------------------------------------------------------------------------------

#4. Faça um programa que leia e imprima um número inteiro.

numero = int(input('digite um numero:'))
print(f'{numero}')

#----------------------------------------------------------------------------------------------------------------------------

#5. Faça um programa que leia dois números reais e os imprima.

nn1 = float(input('digite um primeiro numero:'))
nn2 = float(input('digite o segundo numero:'))
 
#print(f'{nn1}\t{nn2}') 
print(f'{nn1}') 
print(f'{nn2}') 

#----------------------------------------------------------------------------------------------------------------------------

#6. Faça um programa que leia um número inteiro e imprima o seu
#   antecessor e o seu sucessor.

numero1 = int(input('digite um numero inteiro'))

antecessor = numero1 - 1
sucessor = numero1 + 1

print(f'o seu antecessor sera: {antecessor}\t E o sucessor sera : {sucessor}')

#ou 

numero =  int(input('digite um numero inteiro  '))

print(f'sucessor : {numero+1}')
print(f'antecessor: {numero-1}')
#----------------------------------------------------------------------------------------------------------------------------

#Faça um programa que leia o nome o endereço e o telefone de
#  um cliente e ao final, imprima esses dados.
nome = input('digite o seu nome:')
print(nome)
endereco = input('digite seu indereço: ') 
print(endereco)
telefone = input('disce o seu numero de telefone: ')
print(telefone)



#----------------------------------------------------------------------------------------------------------------------------

#8. Faça um programa que leia dois números inteiros e imprima a
#   subtração deles.

numero1 = int(input('digite um numero inteiro:'))
numero2 = int(input('digite outro numero inteiro: '))

subtracao = numero1 + numero2

print(f'o resultado sera {subtracao}')
