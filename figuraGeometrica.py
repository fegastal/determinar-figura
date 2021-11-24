print("Introduza o valor dos lados da figura geométrica.")
l1=float(input())
l2= float(input())
a=l1*l2

if (l1==l2):
    print("A figura é um quadrado e sua área é de",a)
else:
    print("A figura é um retângulo e sua área é de",a)