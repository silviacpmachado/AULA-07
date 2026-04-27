pessoa_vazio = {}

pessoa = {}
pessoa['Nome'] = 'João'
pessoa['Idade'] = 25
pessoa['Cidade'] = 'Niterói'
print(pessoa)

# Acessando o valor da chave
print(pessoa['Cidade'])

# Alterando o valor
pessoa['Idade'] = 26

# Chave Nova
pessoa['Profissao'] = 'Programador'
print(pessoa)

#Deletando uma chave
del pessoa['Cidade']
print(pessoa)
