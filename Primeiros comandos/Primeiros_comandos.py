#declaração de variáveis
from pickle import INT


nome = 'Gustavo'
idade = 19
peso = 79
print ('Nome:',nome, '\nIdade:', idade, '\nPeso:', peso)

#declaração de variáveis com interatividade
nome = input ('Qual seu nome?\n')
idade = input ('Qual a sua idade?\n')
peso = input ('Qual o seu peso?\n')
# Print = leia; Input = escreva
print ('Nome:',nome ,'\nIdade:', idade,'\nPeso:', peso)

#Desafio 1
nome = input ('Qual seu nome?\n')
print ('Ola,', nome,'!\nPrazer em te conhecer!')

#Desafio 2
print ('Digite sua data de nascimento', nome)
dia = input ('Dia: ')
mes = input ('Mes: ')
ano: int = int(input ('Ano: '))
print (nome, 'voce nasceu no dia', dia,'de', mes,'de', ano,', correto?')

idade = 2025 - ano
if idade <= 18:
    print ('Voce e menor de idade!')
else:
    print ('Voce e maior de idade!')

#Desafio 3
num1 = int(input('Digite um numero inteiro: '))
num2 = int(input('Digite um numero inteiro: '))

print ('A soma dos numeros sao: ', num1 + num2 )
