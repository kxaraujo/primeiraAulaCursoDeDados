#Faça um programa que leia 5 valores inteiros. 
#Conte quantos destes valores digitados são pares e mostre esta informação.
#Entrada
#O arquivo de entrada contém 5 valores inteiros quaisquer.
#Saída
#Imprima a mensagem conforme o exemplo fornecido, indicando a quantidade de valores pares lidos.

inicia = 0

for i in range (0,5):
    
    valores = int(input ('Digite um valor inteiro:'))

    if valores%2==0:
        inicia +=1

print("O total de elementos pares foi" , inicia)



