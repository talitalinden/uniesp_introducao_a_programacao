#Switch/case é um comando que controla o fluxo do programa, permitindo ao programador  especificar código 
# diferente para ser executado em várias condições. O switch compara o valor de uma variável aos valores especificados no comando case. 
# no Javascript tem um valor condicional que serve para analisar os valores e executar um bloco de códigos.
# em Python não possui o comando switch case, mas no seu lugar usa-se a estrutura if-else.

#Do While - Esta instrução é usada quando não sabemos quantas vezes um determinado bloco de instruções precisa ser repetido. 
#Com ele, a execução das instruções vai continuar até que uma condição seja verdadeira.
# em Python, o comando While faz com que um conjunto de instruções seja executado enquanto uma condição é atendida.
# Quando o resultado dessa condição passa a ser falso, a execução do loop é interrompida.

contador = 0
while (contador < 5):
    print(contador)
    contador = contador + 1

# Ao final do While pode-se utilizar a instrução else para executar alguma instrução ou bloco de códigos ao final do loop.

contador = 0
while (contador < 5):
    print(contador)
    contador = contador + 1
else:
    print("O loop while foi encerrado com sucesso")