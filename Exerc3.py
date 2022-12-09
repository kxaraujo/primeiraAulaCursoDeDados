#Escreva um programa que repita a leitura de uma senha até que ela seja válida. 
#Para cada leitura de senha incorreta informada, escrever a mensagem "Senha Invalida". 
#Quando a senha for informada corretamente deve ser impressa a mensagem "Acesso Permitido" e o algoritmo encerrado. Considere que a senha correta é o valor 2002. 
#Entrada
#A entrada é composta por vários casos de testes contendo valores inteiros.
#Saída
#Para cada valor lido mostre a mensagem correspondente à descrição do

senhaValida = int(input("Digite sua senha: "))

while senhaValida != 2002:

    print("Senha invalida")
    senhaValida = int(input("Digite sua senha sua senha: "))
print("Acesso permitido")

