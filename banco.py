from agencia import *
from cliente import *
from conta import *
from conta_corrente import *
from conta_popanca import *
criar_conta = conta()
criar = cliente()
ag = agencia()
while True:

    print("""1 - Gerenciar Conta\n2 - Realizar saque, deposito, transferencia\n=========================================""")
    n = int(input())
    if n == 1:
        print("""1 - Criar conta:\n2 - Buscar_Conta(Numero da conta):\n3 - Buscar_Conta(CPF Titular): \n==============================""")
        n = int(input())
        if n == 1:
            criar_conta.setNumero(int(input("Numero da conta:")))
            criar.setNome(input("Informe nome do cliente:"))
            criar.setCPF(int(input("Informe CPF do cliente:")))
            criar.addConta(criar_conta)
        elif n == 2:
            busca = criar.buscaContas(int(input("Informe numero da conta:")))
            if busca:
                print("Conta existente")
            else:
                print("Conta não localizada")
        elif n == 3:
            busca = ag.buscaCliente(int(input("CPF do cliente:")))
            if busca:
                print("Conta existente")
            else:
                print("Conta não localizada")




