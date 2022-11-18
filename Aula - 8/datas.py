from datetime import datetime

def idade(nascimento):
    idadeAnos = hoje.year - nascimento.year
    return idadeAnos

hoje = datetime.now()
print(hoje)
print(hoje.strftime('%d/%m/%Y'))
nascimento = datetime(2001,10,11)
print(nascimento)
print(idade(datetime(2001,10,11)))
print(idade(datetime(2000,9,10)))
