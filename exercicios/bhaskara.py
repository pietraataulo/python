import math
a = float(input("Qual o valor do a? "))
b = float(input("Qual o valor do b? "))
c = float(input("Qual o valor do c? "))

delta = b ** 2 - 4 * a * c

if (delta == 0):
    resultado1 = (-b + math.sqrt(delta)) / (2 * a)
    print ("a raiz desta equação é", resultado1)
else:
    if (delta < 0): 
        print ("esta equação não possui raízes reais")
    else:
        resultado1 = (-b + math.sqrt(delta)) / (2 * a)
        resultado2 = (-b - math.sqrt(delta)) / (2 * a)
        print("as raízes da equação são", resultado2, "e", resultado1)



