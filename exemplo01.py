lst_vazia_meses = [] # lista vazia
lst_meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho']

print(lst_meses[0]) #0 representa o janeiro, 1 - fevereiro
print(lst_meses[2])
print(lst_meses[-1]) # representa o último da fila. É o inverso (que é junho) -2 é o penúltimo.

# Fatiamento
print(lst_meses[:4]) # é o ultimo - 1. porque pega o final. vai ate abril neste caso. Do inicio.
print(lst_meses[2:]) # Imprime a partir do indice 2 até o final.
print(lst_meses[2:4]) # Imprime a partir do 2 até o 4-1.

# print(lst_vazia_meses)
print(lst_meses)

# For em lista
for m in lst_meses: # para cada mês na lista de meses, print os meses.
    print(m)