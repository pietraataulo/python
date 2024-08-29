numero = int(input("Digite um número inteiro: "))
n = numero

if n == 0:
   print("não")

while numero != 0:
      ultimodigito = numero % 10
      digitoantecessor = (numero % 100) // 10

      numeronovo = numero // 10
      numero = numeronovo

      if (ultimodigito == digitoantecessor):
          print("sim")
          break

      if (numero == 0):
          print("não")
      