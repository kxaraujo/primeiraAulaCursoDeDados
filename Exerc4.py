#Faça um algoritmo para ler um número indeterminado de dados, contendo cada um, a idade de um indivíduo. O último dado, que não entrará nos cálculos, contém o valor de idade negativa. Calcular e imprimir a idade média deste grupo de indivíduos.
#Entrada
#A entrada contém um número indeterminado de inteiros. A entrada será encerrada quando um valor negativo for lido.
#Saída
#A saída contém um valor correspondente à média de idade dos indivíduo

idadeIndiv = 0
soma = 0
iniciaContagem = 0

while idadeIndiv >=0:
  idadeIndiv = float(input("Insira a idade:"))
  if idadeIndiv >=0:
    iniciaContagem += 1
    soma += idadeIndiv
media = soma/iniciaContagem

print(media)