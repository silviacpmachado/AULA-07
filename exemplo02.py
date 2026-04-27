list_produtos = ['Notebook', 'Mouse', 'Teclado', 'Monitor']

for p in list_produtos:
    print(p)



list_produtos[0] = 'PC'
print(f'Alterar o primeiro elemento {list_produtos}')

list_produtos.append('Webcam')
print(f'Produto adicionado {list_produtos}')

list_produtos.remove('Monitor')
print(f'Produto removido {list_produtos}')

list_produtos.pop() # remove o último
print(f'Remove o último {list_produtos}')

del list_produtos[0]
print(f'Remove pela posição {list_produtos}')
#print(list_produtos)
