numero = int(input("Digite um número: "))
soma = 0

while numero > 0:
      valor = numero % 10
      numero = numero // 10
      soma = soma + valor

print("A soma dos dígitos é", soma)