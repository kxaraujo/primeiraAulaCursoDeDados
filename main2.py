from BancoLib import Banco
f
print(' ')
print('-------------------------------------------------------------------------------------')
print('                            BEM VINDO AO BANCO UABJ                                  ')
bancoUfrpe = Banco("UABJ")
print('-------------------------------------------------------------------------------------')
print("                                      MENU                                           ")
print('-------------------------------------------------------------------------------------')
print("0 - Sair")
print('-------------------------------------------------------------------------------------')
print("1 - Criar uma Nova Conta")
print('-------------------------------------------------------------------------------------')
print("2 - Consultar Saldo Conta")
print('-------------------------------------------------------------------------------------')
print("3 - Depositar na Conta")
print('-------------------------------------------------------------------------------------')
print("4 - Sacar na Conta")
print('-------------------------------------------------------------------------------------')
print("5 - Render Poupanca")
print('-------------------------------------------------------------------------------------')
print("6 - Render Bonus")
print('-------------------------------------------------------------------------------------')

escolha = int(input("digite a opção desejada:"))
while escolha > 0:
    if escolha == 1:
        # criar uma conta
        print("Criando Conta...")
        print("1 - Conta Corrente")
        print("2 - Conta Poupanca")
        print("3 - Conta Bonificada")
        opcao = int(input("digite o tipo da conta:"))
        if opcao == 1:
            numConta = bancoUfrpe.contaBonificada()
        elif(opcao == 3):
            numConta = bancoUfrpe.contaBonificada()   
        else:
            numConta = bancoUfrpe.criarPoupanca()
        print("Conta criada:", numConta)
    elif escolha == 2:
        print("Consultando Saldo...")
        numConta = int(input("digite o numero da conta:"))
        saldo = bancoUfrpe.consultaSaldo(numConta)
        print("o saldo da conta", numConta, "é", saldo, "R$")
    elif escolha == 3:
        print("Depositando Conta...")
        numConta = int(input("digite o numero da conta:"))
        valor = int(input("digite o valor que deseja depositar:"))
        saldo = bancoUfrpe.depositar(numConta, valor)
        print("Valor Depositado")
    elif escolha == 4:
        print("Sacando da Conta...")
        numConta = int(input("digite o numero da conta:"))
        valor = int(input("digite o valor que deseja sacar:"))
        resp = bancoUfrpe.sacar(numConta, valor)
        if resp:  # significa resp == True
            print("Valor Sacado")
        else:
            print("Saldo Insuficiente")
    elif escolha == 5:
        print("Rendendo Poupanca...")
        numConta = int(input("digite o numero da conta poupanca:"))
        resp = bancoUfrpe.renderPoupanca(numConta)
        if resp:
            print("Poupanca com novo saldo")
        else:
            print("A conta não é poupanca ou não existe")
    elif escolha == 6:
        print("Rendendo Bonificação...")
        numConta = int(input("digite o numero da conta:"))
        resp =bancoUfrpe.renderBonus(numConta)
        if resp:
            print("Conta com novo saldo")
        else:
            print("A conta não existe")       
    
    
    escolha = int(input("digite a opção desejada:"))