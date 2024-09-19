x =2
y = 4

def soma (x,y):
    soma = x + y
    return soma

soma(x,y)

num = int(input("Digite um numero"))
def eh_par_ou_impar(x):
    resto = x % 2
    if resto == 0:
        return print ("É par")
    else:
        return print ("É impar")
    
eh_par_ou_impar(num)