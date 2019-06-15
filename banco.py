from agencia import *
from cliente import *
from conta import *
from conta_corrente import *
from conta_popanca import *
while True:
    print("""1 - Criar Conta\n2 - Gerenciar Conta""")
    n = int(input())
    if n == 1:
        c = cliente()
        conta = conta()
        c.setNome(input("Informe nome do cliente:"))
        c.setCPF(int(input("Informe CPF do cliente:")))
        conta.
        busca = c.buscaContas()
