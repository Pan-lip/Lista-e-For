#File com todos exercicios que eu fiz sobre for e listas tbm
#ex6 números inteiros ao usuário, armazene-os em uma lista e use um for para somar todos os valores. No final, exiba a soma e a média.
num_lista = []
while True:
    num = int(input ("Insira seis numeros):"))
    num_lista.append(num)
    if len(num_lista) == 6:
        break
soma = 0
for n in num_lista:   
    soma += n

media = soma / len(num_lista)
print(f"Soma = {soma}")
print(f"Média = {media:.2f}")
#Leia 8 números e armazene em uma lista e um for para contar quantos são pares e quantos são ímpares, exibindo o resultado.
num_lista = []
while True:
    num = int(input ("Insira oito nums):"))
    num_lista.append(num)
    if len(num_lista) == 8:
        break
pares = 0
impares = 0
for i in range(len(num_lista)):
    if num_lista[i] % 2 == 0:
        pares += 1
    else:
        impares += 1
print("Quantidade de pares:",pares)
print("Quantidade de impares:", impares)
#Cadastre nota de alunos, e faça a média final deles
aluno = 1  
while True:
    print(f"\n--- Cadastro de notas do aluno {aluno} ---")

    checkpoints = []
    for i in range(3):
        nota = float(input(f"Digite a nota do Checkpoint {i+1}: "))
        checkpoints.append(nota)

    sprints = []
    for i in range(2):
        nota = float(input(f"Digite a nota da Sprint {i+1}: "))
        sprints.append(nota)

    gs = float(input("Digite a nota da Global Solution: "))

    menor_cp = min(checkpoints)
    checkpoints.remove(menor_cp)

    # Calcular média dos 2 CPs + 2 Sprints
    media_parcial = (sum(checkpoints) + sum(sprints)) / 4

    # Calcular média final
    media_final = media_parcial * 0.4 + gs * 0.6

    print(f"\nA média semestral do aluno {aluno} foi: {media_final:.1f}")

    continuar = input("Deseja inserir notas de outro aluno? (s/n): ").lower()
    if continuar != "s":
        print("\nEncerrando o programa.")
        break

    aluno += 1
#Aprovado ou não
aluno = 1 
while True:
    print(f"\n--- Cadastro de notas do aluno {aluno} ---")

    checkpoints = []
    for i in range(3):
        nota = float(input(f"Digite a nota do Checkpoint {i+1}: "))
        checkpoints.append(nota)

    sprints = []
    for i in range(2):
        nota = float(input(f"Digite a nota da Sprint {i+1}: "))
        sprints.append(nota)

    gs = float(input("Digite a nota da Global Solution: "))

    menor_cp = min(checkpoints)
    checkpoints.remove(menor_cp)
 # Calcular média dos 2 CPs + 2 Sprints
    media_parcial = (sum(checkpoints) + sum(sprints)) / 4

    # Calcular média final
    media_final = media_parcial * 0.4 + gs * 0.6
    if media_final >= 7:
        print("Aprovado")
    else:
        print("Desaprovado")

    continuar = input("Deseja inserir notas de outro aluno? (s/n): ").lower()
    if continuar != "s":
        print("\nEncerrando o programa.")
        break
    aluno += 1
 #Media anual aluno
    aluno = 1

while True:
    print(f"\n--- Cadastro de notas do aluno {aluno} ---")
    medias_aluno = []

    for semestre in range(1, 3):
        print(f"\nSemestre {semestre}:")

        # Receber checkpoints
        checkpoints = []
        for i in range(3):
            nota = float(input(f"Digite a nota do Checkpoint {i+1}: "))
            checkpoints.append(nota)

        # Receber sprints
        sprints = []
        for i in range(2):
            nota = float(input(f"Digite a nota da Sprint {i+1}: "))
            sprints.append(nota)

        # Receber GS
        gs = float(input("Digite a nota da Global Solution: "))

        # Descartar menor checkpoint
        checkpoints.remove(min(checkpoints))

        # Calcular média parcial
        media_parcial = (sum(checkpoints) + sum(sprints)) / 4

        # Média semestral
        media_semestre = media_parcial * 0.4 + gs * 0.6
        medias_aluno.append(media_semestre)

        print(f"Média do semestre {semestre}: {media_semestre:.1f}")

    # Média final do aluno
    media_final = medias_aluno[0]*0.4 + medias_aluno[1]*0.6
    print(f"\nMédia final do aluno {aluno}: {media_final:.1f}")
    break
