# pares = []
# impares = []

# for i in range(10):
#     numero = int(input(f"Digite o {i+1}º número: "))

#     if numero % 2 == 0:
#         pares.append(numero)
#     else:
#         impares.append(numero)

# print("\nNúmeros pares:", pares)
# print("Números ímpares:", impares)

# contatos = []

# for i in range(2):
#     print(f"\nCadastro do {i+1}º contato")

#     nome = input("Nome completo: ")
#     telefone = input("Telefone: ")
#     email = input("E-mail: ")

#     contato = {
#         "nome": nome,
#         "telefone": telefone,
#         "email": email
#     }

#     contatos.append(contato)

# print("\n--- LISTA DE CONTATOS ---")

# for c in contatos:
#     print(f"\nNome: {c['nome']}")
#     print(f"Telefone: {c['telefone']}")
#     print(f"E-mail: {c['email']}")

# vendedores = []

# for i in range(2):
#     print(f"\nCadastro do {i+1}º vendedor")

#     nome = input("Nome: ")
#     regiao = input("Região: ")
#     valor = float(input("Valor total de vendas (R$): "))
#     quantidade = int(input("Quantidade de vendas: "))

#     vendedor = {
#         "nome": nome,
#         "regiao": regiao,
#         "valor": valor,
#         "quantidade": quantidade
#     }

#     vendedores.append(vendedor)

# print("\n--- VENDEDORES QUE ATINGIRAM A META ---")

# for v in vendedores:
#     if v["valor"] >= 5000:
#         print(f"\nNome: {v['nome']}")
#         print(f"Região: {v['regiao']}")
#         print(f"Vendas: R$ {v['valor']:.2f}")
#         print(f"Quantidade de vendas: {v['quantidade']}")

# contatos = []

# for i in range(2):
#     print(f"\nCadastro do {i+1}º contato")

#     nome = input("Nome completo: ")
#     telefone = input("Telefone: ")
#     email = input("E-mail: ")

#     contatos.append({
#         "nome": nome,
#         "telefone": telefone,
#         "email": email
#     })

# print("\n===== CONTATOS CADASTRADOS =====")

# for contato in contatos:
#     print("\nNome:", contato["nome"])
#     print("Telefone:", contato["telefone"])
#     print("E-mail:", contato["email"])

# alunos = []

# for i in range(2):
#     print(f"\nAluno {i+1}")

#     nota1 = float(input("Digite a nota da primeira prova: "))
#     nota2 = float(input("Digite a nota da segunda prova: "))

#     media = (nota1 + nota2) / 2

#     if media >= 7:
#         status = "Aprovado"
#     else:
#         status = "Reprovado"

#     alunos.append({
#         "media": media,
#         "status": status
#     })

# print("\n===== RESULTADO FINAL =====")

# for i, aluno in enumerate(alunos, start=1):
#     print(f"\nAluno {i}")
#     print(f"Média: {aluno['media']:.2f}")
#     print(f"Situação: {aluno['status']}")

candidatos = []

for i in range(2):
    print(f"\nCadastro do {i+1}º candidato")

    nome = input("Nome: ")
    idade = int(input("Idade: "))

    if idade >= 18:
        telefone = input("Telefone: ")
        email = input("E-mail: ")
        formacao = input("Formação acadêmica: ")

        candidatos.append({
            "nome": nome,
            "idade": idade,
            "telefone": telefone,
            "email": email,
            "formacao": formacao
        })
    else:
        print("Candidato não pode se cadastrar (menor de idade).")

print("\n===== CANDIDATOS CADASTRADOS =====")

if len(candidatos) == 0:
    print("Nenhum candidato válido foi cadastrado.")
else:
    for c in candidatos:
        print(f"\nNome: {c['nome']}")
        print(f"Idade: {c['idade']}")
        print(f"Telefone: {c['telefone']}")
        print(f"E-mail: {c['email']}")
        print(f"Formação: {c['formacao']}")