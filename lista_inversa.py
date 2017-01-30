#Escreva um programa que recebe uma sequência de números inteiros terminados por 0
#e imprima todos os valores em ordem inversa. O 0(Zero)não de fazer parte da
# sequência.

#Nao estou cõnseguindo ignorar o 0 da impressao.


i=int(input("Digite: "))
cont = 0
seq = []

while cont < i:
    num = int(input("Digite a sequência: "))
    seq.append(num)
    cont += 1

cont = i-1
while cont>= 0:
    print(seq[cont], end='')
    cont -= 1
print()



