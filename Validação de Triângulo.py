a = float(input("Digite o valor do lado A: "))
b = float(input("Digite o valor do lado B: "))
c = float(input("Digite o valor do lado C: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("Os comprimentos foram um triângulo!")
else:
    print("Os comprimentos NÃO formam um triângulo.")