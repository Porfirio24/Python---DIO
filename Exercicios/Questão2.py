"""
Peça para o usuário digitar um número e exiba ele como inteiro, float e string.
"""

# > Resolução

numero = input("Digite um Numero:")

numero_inteiro = int(float(numero))
numero_float = float(numero)
numero_string = str(numero)

print("Numero Inicial:",numero)
print("Numero Inteiro:",numero_inteiro)
print("Numero Float:", numero_float)
print("Numero String:", numero_string)