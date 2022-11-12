"""
    Calcular área do retangulo
"""
print("***Calculo da area do retangulo***\n\nInforme o primeiro lado:")
#print("Informe o primeiro lado:")
print("Informe o primeiro lado:")
lado1 = input()
print("Informe o segundo lado")
lado2 = input()
#variavel.isnumeric = verifica se é variavel pode ser um número inteiro
#variavel.isnumeric = verifica se é variavel pode ser um númer0 com casas decimais
print("O primeiro valor é número?", lado1.isnumeric())
print("O segundo valor é número?", lado2.isnumeric())
print("Será que vai dar certo ou vai errado?")
area = int(lado1) * int(lado2)
print("A area do retangulo é {} m² sendo os lados de {} x {}". format(area, lado1, lado2))
print("A area do retangulo é", area, "m² sendo os lados de",lado1, 'x', lado2)
