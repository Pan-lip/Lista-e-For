#carros = ["Accord", "Polo", "Civic", "Fiat Uno"]
#print(carros)
#print(len(carros))
#print(carros[1])
##carros[0] = "fusca"
#print(carros[0]) #mudar a variavel,sem modificar nos outros
#mais material (ensinando a fazer "backup")
#carros_back = carros
#print(carros_back)
#carros [3] = "Jeep" #tipo vc mudou de carros
#print(carros)
#print(carros_back)
#copia de lista de backup:
#carros_back = carros [:]
#print(carros_back)
#carros[1] = "Gol"
#print(carros[1])
#print(carros_back)
#DEUS ME AJUDE PQ PQP TA DIFICIL
#exemplo 2
#notas = [6,7,5,8,9]
#soma = 0
#x = 0
#while x < 5:
#    soma += notas[x]
#    x += 1
#    print(f"Media = {(soma/x):.2f}")
# exercicio  1
notas = [8,9,10,6,7,8,5]
soma = 0
x = 0
while x < len(notas):
    soma += notas [x]
    x +=1
    print(f"Media = {(soma / x):.2f}")


