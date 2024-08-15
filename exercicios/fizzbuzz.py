numero = float(input("Digite um número: "))
divisao = numero % 3
divisao2 = numero % 5

if (divisao == 0 and divisao2 == 0):
    print("FizzBuzz")
else:
   print(numero)