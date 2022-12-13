#O cálculo do valor a ser pago é feito da seguinte forma. 
#para pagamentos sem atraso, cobrar o valor da prestação. 
#Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso

def valorPagamento(prestacao, atraso):
       
    if atraso == 0:
        return prestacao
    else:
        valorPagamento = prestacao + prestacao * 0.3
        for i in range (atraso):
            valorPagamento = valorPagamento * 000.1
        return valorPagamento

soma = 0
qntd = 0
prestacao = float(input("valor da prestação:"))
atraso = float(input("dias de atraso:"))

while (prestacao > 0):
    valorPagamento = valorPagamento(prestacao, atraso)
    print("o valor da prestação é: ", prestacao)
    valorTotal = valorTotal + 


print('Prestações pagas:' , quantia)
print('Valor total de prestacoes pagas: ', valortotal)