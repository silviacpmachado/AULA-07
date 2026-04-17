# vendas = []
# for i in range(3):
#    valor = float(input('Informe a venda: '))
#    vendas.append(valor) 
   
# print(f'Vendas registradas {vendas}')


# for v in vendas:
#    if v >=1000:
#       print(f'Venda de R$ {v} - Meta Atingida')
#    elif v>= 700:
#       print(f'Venda de R$ {v} - Proximo da meta')
#    else:
#      print(f'Venda de R$ {v} - Bem abaixo da meta')

# print('Encerrado...') 

META = 1000   # LETRA MAIUSCULA É UMA CONSTANTE.
META_MINIMA = 700

for v in vendas:
   if v >=META:
      print(f'Venda de R$ {v} - Meta Atingida')
   elif v>= META_MINIMA:
      print(f'Venda de R$ {v} - Proximo da meta')
   else:
     print(f'Venda de R$ {v} - Bem abaixo da meta')

print('Encerrado...') 

