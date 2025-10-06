 #Dicionario é composto por um conjunto de chaves e valores (CPF) uma chave e varios valores
# alunos_fiap = {"565560": ["Anna","1ECR"], "564040":["Leticia","1EMR"]}
# alunos_fiap["564040"][1] = "1ECR" #para mudar algum erro, vc coloca a chave o indice e pah
# print(alunos_fiap["564040"])
# print("565560" in alunos_fiap) #verificar se ta dentro do bagui
# print("565561" in alunos_fiap)
# nomes_alunos = ["Anna", "Leticia"]
# print("Ana" in nomes_alunos) #Serve pra pesquisar dentro da chave tbm
# print(alunos_fiap.keys()) #As chaves que possuem dentro do seu dicionario
# print(alunos_fiap.values()) #Mostra os valores
#pode usar del também igual em lista tipo del alunos_fiap["565560"]
cursos_fiap = {"Administração": ["6K","3 anos"], "Mecatrônica": ["3K","4 anos"], "Marketing": ["2k", "1 ano"]}
while True:
    pesquisa = input("Digite o curso ou fim para terminar:") #.lower() pra quando digitar de qualquer forma vai ficar td maiusculo ou minusc
    if pesquisa == "fim":
        break
    if pesquisa in cursos_fiap:
        print(f"Valor = {cursos_fiap[pesquisa][0]} // Tempo perdido = {cursos_fiap[pesquisa][1]}")
    else:
        print("Curso não encontrado")
# .keys()  retorna todas as chaves
# .values() retorna todos os valores
# .items()  retorna pares (chave, valor)
# .update({...})  atualiza ou adiciona itens
# .clear()  limpa o dicionário
# len(dicionario)  conta quantos pares existem
# Tupla é uma lista que NÃO pode mudar
# Usamos quando os dados são fixos

# Criando uma tupla com coordenadas (x, y)
coordenada = (10, 20)

print("Coordenada completa:", coordenada)  # (10, 20)
print("Primeiro valor (x):", coordenada[0])  # 10
print("Segundo valor (y):", coordenada[1])   # 20

# Tupla pode ter vários tipos de dados
aluno_tupla = ("Ana", 20, "Engenharia")
print("\nNome do aluno:", aluno_tupla[0])
print("Idade:", aluno_tupla[1])
print("Curso:", aluno_tupla[2])

# Desempacotando a tupla em variáveis
nome, idade, curso = aluno_tupla
print("\nUsando desempacotamento:")
print("Nome:", nome)
print("Idade:", idade)
print("Curso:", curso)

# ====== DICIONÁRIO ======
# Dicionário é chave -> valor
# Usamos quando queremos "mapear" algo

# Criando um dicionário de aluno
aluno_dict = {
    "nome": "Ana",
    "idade": 20,
    "curso": "Engenharia"
}

print("\nDicionário do aluno:", aluno_dict)

# Acessando valores pela chave
print("Nome:", aluno_dict["nome"])
print("Idade:", aluno_dict["idade"])

# Usando .get() (não dá erro se não existir a chave)
print("Nota:", aluno_dict.get("nota", "Ainda não cadastrada"))

# Alterando valores
aluno_dict["idade"] = 21
print("\nIdade alterada:", aluno_dict)

# Adicionando novos valores
aluno_dict["nota"] = 9.5
print("Com a nota adicionada:", aluno_dict)

# Removendo um valor
aluno_dict.pop("curso")
print("Removendo curso:", aluno_dict)

# Percorrendo o dicionário
print("\nPercorrendo chaves e valores:")
for chave, valor in aluno_dict.items():
    print(chave, ":", valor)
