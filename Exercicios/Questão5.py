"""
Crie um programa que simule um caixa eletrônico:

Se o saldo for suficiente, mostre "Saque realizado".

Se não for suficiente mas houver cheque especial, mostre "Saque com cheque especial".

Caso contrário, "Saldo insuficiente".
"""

# > Resolução

saldo = float(int(input("Digite o seu Saldo:")))
cheque_especial = float(int(input("Digite o valor do Cheque:")))

saque = float(int(input("Digite quanto deseja Sacar:")))

if saque <= saldo:
  print("Saque realizado com sucesso!")
elif saque <= (saldo + cheque_especial):
  print("Saque com cheque especial")
else:
  print("Saldo insuficiente!")