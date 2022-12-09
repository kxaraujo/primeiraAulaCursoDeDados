#Faça uma função chamada calculaSalario que recebe como parâmetro o valor do salário bruto calcula o salário líquido. O salário líquido é calculado a partir do salário bruto, primeiro descontando 11% referente ao INSS, e do resultado, descontando-se 15% de imposto de renda (IR).
#Exemplo
#Salário Bruto = R$ 5000,00
#Desconto do INSS = R$ 550,00 (11% de R$ 5000,00)
#Desconto do IR = R$ 667,50 (15% de R$ 4450,00)
#Salário Líquido = 5000 - (550 + 667,50) = 3782,50

def calculaSalario ():
    salarioBruto = float(input("Insira aqui o valor do seu salário:"))

    descontoINSS = 11/100
    descontoIR = 15/100

    calculaINSS = salarioBruto - (salarioBruto * descontoINSS)
    salarioLiquido = calculaINSS - (calculaINSS * descontoIR)
    
    print("O salário líquido é de" , salarioLiquido)

calculaSalario()