#Ex 1
nota = float(input("Digite a nota"))

if nota < 6:
    print("Reprovado")
elif nota >= 6 and nota < 7:
    print("Recuperação")
elif nota >= 7 and nota <9:
    print("Aprovado")
elif nota >=9 and nota <=10:
    print("Aprovado com Menção Honrosa")
else:
    print("Nota digitada errada")

#Ex 2
cor = input("Digite a cor:")

if cor =="vermelho" or cor =="amarelo" or cor=="azul":
    print("Primaria")
elif cor=="verde" or cor=="laranja" or cor=="roxo":
    print("Secundaria")
else:
    print("Outras")

#Ex 2.1
cor = input("Digite a cor:")
primario= ["vermelho","amarelo","azul"]
secundario= ["verde","laranja","roxo"]

if cor in primario:
    print("Primaria")
elif cor in secundario:
    print("Secundaria")
else:
    print("Outras")

#Ex 3
Mes= input("Digite o Mês:")
dicionario={"01":"Janeiro","02":"Fevereiro","03":"Março","04":"Abril","05":"Maio","06":"Junho","07":"Julho","08":"Agosto","09":"Setembro","10":"Outubro","11":"Novembro","12":"Dezembro"}
print(dicionario[Mes])

#Ex 4
mes = input("Digite o mês")
ano = int(input ("Digite o ano"))

def is_leap_year(year):
    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    return is_leap

dicionario={"01":"Janeiro","02":"Fevereiro","03":"Março","04":"Abril","05":"Maio","06":"Junho","07":"Julho","08":"Agosto","09":"Setembro","10":"Outubro","11":"Novembro","12":"Dezembro"}
lista_mes_31 = [dicionario["01"],dicionario["03"],dicionario["05"],dicionario["07"],dicionario["08"],dicionario["10"],dicionario["12"]]
lista_mes_30 = [dicionario["04"],dicionario["06"],dicionario["09"],dicionario["11"]]

if mes in lista_mes_31:
    print("Mes com 31 dias")
elif mes in lista_mes_30:
    print("Mes com 30 dias")
else:
    if is_leap_year(ano):
        print("Mes com 29 dias")
    else:
        print("Mes com 28 dias")