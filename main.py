from conta import conta

c1 = conta("Diego Martins",1,1250,10000)
c2 = conta("Jose Diogo",2,450,10000)

c1.transferencia(c2,2000)
print(c1.getSaldo())
print(c2.getSaldo())
