import random

class Conta():
    def __init__(self, numConta):
        self.numero = numConta
        self.saldo = 0
        self.bonus = 0

    def deposite(self, valor):
        self.saldo += valor*0.999
        self.bonus += valor*0.0001
        
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo = self.saldo - valor
            return True
        else:
            return False

    def renderbonus(self):
        if self.bonus != 0:
            self.saldo += self.bonus
            self.bonus = 0
                                   


class Poupanca(Conta):
    def render(self):
        self.saldo *= 0.999
        

class ContaBonificada(Conta):
    def renderBonusB(self):
        self.saldo += self.bonus
        
        
class Banco():
    def __init__(self, nome):
        self.nome = nome
        self.contas = []

    def getNome(self):
        return self.nome

    def criarConta(self):
        num = random.randint(0, 1000)
        c = Conta(num)
        self.contas.append(c)
        return num

    def criarPoupanca(self):
        num = random.randint(0, 1000)
        p = Poupanca(num)
        self.contas.append(p)
        return num  

    def contaBonificada(self):
        num = random.randint(0, 1000)
        p = contaBonificada(num)
        self.contas.append(p)
        return num  

    def consultaSaldo(self, numConta):
        for conta in self.contas:
            if conta.numero == numConta:
                return conta.saldo
        return -1

    def depositar(self, numConta, valor):
        for conta in self.contas:
            if conta.numero == numConta:
                conta.deposite(valor)

    def sacar(self, numConta, valor):
        for conta in self.contas:
            if conta.numero == numConta:
                return conta.sacar(valor)

    def renderPoupanca(self, numConta):
        for i in self.contas:
            if i.numero == numConta and isinstance(i, Poupanca):
                i.render()
                return True
        return False

    def renderBonus(self,numConta):
        for i in self.contas:
            if i.numero == numConta and isinstance(i,ContaBonificada):
                i.renderBonusB()
                return True   
            elif isinstance(i,Poupanca) or isinstance(i,Conta):
                i.renderbonus()
                return True
        return False