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
