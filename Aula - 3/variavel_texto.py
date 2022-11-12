from os import system #importa as bibliotecasdo sistema operacional
system('cls')
#criação de variavel texto
#As variaveis devem seguir um padrão
#snake_case,PacalCase ou camelCase
#nome_completo
#NomoCompleto
#nomeCompleto
nome_completo = 'Guilherme Rocker'
print(len(nome_completo)) # len= conta a quantidade de caracteres
print(nome_completo.count('e')) #Conta a repetição de um caracter
print(nome_completo.upper()) #Deixa todas as letras maiusculas
print(nome_completo.lower()) #Deixa todas as letras minusculas
print(nome_completo.capitalize()) #Deixa apenas a primeira letra maiuscula
print(nome_completo.find(' ')) #Serve para achar caracter
espaço = nome_completo.find(' ')
nome = nome_completo[0:espaço]
print(nome)
print(nome_completo.replace(' ','#')) #Altera todos que você indicar na letra/caracter que for indicado
print(nome_completo.center(80,'#'))
print(nome_completo.split(' ')) #Faz varias quebras pelo texto
