#eça 6 números inteiros ao usuário, armazene-os em uma lista e use um for para somar todos os valores. No final, exiba a soma e a média.
num_lista = []
while True:
    num = int(input ("Insira seis numeros):"))
    num_lista.append(num)
    if len(num_lista) == 6:
        break
soma = 0
for n in num_lista:   # percorre a lista direto
    soma += n

media = soma / len(num_lista)
print(f"Soma = {soma}")
print(f"Média = {media:.2f}")
