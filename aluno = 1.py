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

    continuar = input("Deseja inserir notas de outro s? (s/n): ").lower()
    if continuar != "s":
        print("\nEncerrando o programa.")
        break
    aluno += 1
