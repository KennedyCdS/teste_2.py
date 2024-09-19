#1. crie uma lista 
Frutas = ["maça","banana","laranja","uva"]
#2. imprima o primeiro e o último elemento da lista
Frutas[0]
Frutas[3]
#3. adicionar "manga"
Frutas.append("carambola") #da pra colocar uma lista dentro da lista
#ou Frutas.extend(["carambola"])
Frutas += ["manga"]
#4. substitua "laranja" por "abacaxi"
Frutas[2] = "abacaxi"
#5. Remova a fruta "banana"
del Frutas[1]
Frutas
#6.	Crie uma lista numeros contendo os números de 1 a 10.
numeros = [1,2,3,4,5,6,7,8,9,10]
#7.	Calcule e imprima a soma de todos os números da lista.
soma = sum(numeros)
#8.	Encontre e imprima o maior e o menor número da lista.
Maior_numero=max(numeros)
Menor_numero=min(numeros)
#9.	Inverta a ordem dos elementos na lista e imprima a lista invertida.
numeros.reverse()
#10. Crie uma lista cidades
cidades="São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba"
#11. Ordene a lista cidades em ordem alfabética.
cidades= sorted(cidades)
#12. Adicione a cidade "Porto Alegre" ao final da lista.
cidades += ["Porto_Alegre"]
#13. Encontre o índice da cidade "Curitiba" na lista.
cidades[1]
#14. Remova a cidade "Rio de Janeiro" da lista.
cidades.pop(2)
#15. Crie duas listas lista1 e lista2, onde lista1 contém os números [1, 2, 3] e lista2 contém os números [4, 5, 6].
lista1 = [1,2,3]
lista2 = [4,5,6]
#16. Concatene lista1 e lista2 em uma nova lista lista3
lista3 = lista1 + lista2
#17.Imprima lista3
lista3
#18. Crie duas listas animais_domesticos e animais_selvagens
animais_domesticos = ["cachorro", "gato", "coelho"]
animais_selvagens = ["leão", "tigre", "urso"]
#19. Concatene as duas listas em uma nova lista todos_animais.
animais= animais_domesticos + animais_selvagens
#20. Imprima todos_animais.
print(animais)

#Lista de Exercício sobre Lista com Looping

#21. Crie uma lista nomes contendo os nomes: "Ana", "Pedro", "Maria", "João".
# dados de entrada
lista= "Ana", "Pedro", "Maria", "João"
#22.Utilize um loop for para imprimir cada nome da lista.
for nome in lista:
    print(nome)
#23. Crie uma nova lista nomes_maiusculos 
# dados de processamento
nomes_maiusculos= []
for nome in lista:
    nome = nome.upper()
    nomes_maiusculos += [nome]
    print(nome)
#dados de saída
print(nomes_maiusculos)