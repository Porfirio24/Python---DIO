"""
Estruturas Condicionais

imagine que você queira imprimir 'Aprovado(a)', caso o estudante tenha uma média superior ou igual a 7, e 'Reprovado(a)', caso a média seja inferior a 7
"""

# > Resolução

media = float(input("Digite sua Media "))
presença = int(input("Digite sua presença "))

if media >= 7.0 and presença >= 50:
  print("Você foi Aprovado(a) ")
elif media >= 5.9:
  print("Você foi para a Recuperação")
else:
  print("Você foi Reprovado(a)")