nomes_alunos = []
print(len(nomes_alunos))
nomes_alunos.append("Lunna")
print(nomes_alunos)
nomes_alunos.append("Leticia")
print(nomes_alunos)
nomes_alunos.append("Anna")
print(nomes_alunos)
nomes_alunos.sort()
print (nomes_alunos)
# sort faz ordem alfabetica, ou em ordem crescente dependendo do rolê
nomes_alunos.sort(reverse=True)
print(nomes_alunos)
#ele deixa misturado sem ordem

#ae um novo exemplo
nome_alunos = []
while True:
    nome_al = input("Nome(Coloca um nome ai):")
    if nome_al == "fim":
        break
    nome_alunos.append(nome_al)

x = 0
while x < len(nomes_alunos):
    print(nomes_alunos[x])
    x += 1

nomes_alunos += ["Dua Lip","Lola"]
print(nomes_alunos)
nomes_alunos.extend(["Lucas","Pietro"])

#exercicios
lista_alunos = ["Michelle","Leticia","Lunna"]
nova_lista_alunos = []

while True:
    novo_aluno = input("Nome(ente para sair):")
    if novo_aluno == "":
        break
    nova_lista_alunos.append(novo_aluno)
