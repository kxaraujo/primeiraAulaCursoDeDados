#O cálculo do valor a ser pago é feito da seguinte forma. 
#para pagamentos sem atraso, cobrar o valor da prestação. 
#Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso

def valorPagamento(prestacao, atraso):
       
    if atraso == 0:
        valor = prestacao
        print(valor)
    else:
        valor = (prestacao + prestacao * 0.03 + 0.01 * atraso)
        print(valor)
        
    prestacao = 0
    atraso = 0
    quantia = 0
    valorTotal = 0
    cont = 0

while True:
    valor = float(input('Digite o valor da prestação: '))
    if valor == 0:
        print('Quantidade total de prestações: ', cont)
        print('Valor total das prestações: ', valorTotal)
    atraso = float(input('Digite o número de dias em atraso: '))
    valorTotal += valorPagamento(prestacao, atraso)
    cont += 1


print('Prestações pagas:' , quantia)
print('Valor total de prestacoes pagas: ', valortotal)