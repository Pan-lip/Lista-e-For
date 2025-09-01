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