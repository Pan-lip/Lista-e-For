aluno = 1  #questão pra saber se ele foi aprovado ou desaprovado
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