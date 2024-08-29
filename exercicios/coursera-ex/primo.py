numero = int(input("Digite um número inteiro positivo: "))

i = 2
p = False

while i < numero:
      n = numero % i
      if n == 0:
          p = True
      i = i + 1

if p:
   print("não primo")
if not p:
   print("primo")