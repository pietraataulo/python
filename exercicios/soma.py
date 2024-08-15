numero = int(input("Digite um número: "))
soma = 0

while numero != 0:
      u = numero % 10
      numero = numero // 10
      soma = soma + u

print(soma)