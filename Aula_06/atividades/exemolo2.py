# exemplo 2: para uma lista de nomes, usa-se a função len
#a função len retorna um número inteiro, ou seja, o tamanho da lista
lista_de_nomes = ["Conrrado", "Angélica", "Zacarias", "Maria", "Berenice", "Miguel"]
i = len(lista_de_nomes) - 1
print(i)

while i >= 0:
    print("Olá {}, você foi convidado para um jantar beneficente.".format(lista_de_nomes[i]))
    i = i - 1