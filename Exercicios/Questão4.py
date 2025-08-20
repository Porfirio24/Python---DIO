"""
Peça a idade de uma pessoa e informe se ela pode ou não votar (idade ≥ 16).
"""

# > Resolução

idade = int(input("Digite sua Idade:"))

if idade >= 16:
  print("Você pode votar")
else:
  print("Você não tem idade suficiente")
