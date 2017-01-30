#Escreva a função n_primos que recebe um número inteiro maior ou igual a 2
# como parâmetro e devolve a quantidade de números primos que existem entre
# 2 e n (incluindo 2 e, se for o caso, n).

#Nao consigo imprimir a soma dos números primos.





def n_primos(x):
    fator = 2
    if x== 2:
        return True

    while x % fator !=0 and fator < x/2:
        fator = fator + 1
    if x % fator ==0:
        return False
    else:
        return True
    return True

limite = int(input("Limite máximo: "))
n = 2

contadorPrimos = 0 # Variavel que conta quantos numeros foram encontrados
while n < limite:
    if n_primos(n):
        print(n, end=" ")
        contadorPrimos = contadorPrimos + 1 # a cada loop que um numero for encontrado é somado mais um ao contador

    n = n + 1


print ("\n\nForam encontrados %d números primos." % contadorPrimos)



