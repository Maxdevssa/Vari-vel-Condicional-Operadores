# -*- coding: utf-8 -*-
"""Introdução.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Z8J6PXrX9LCcVdOZTXuubzEpTAsTcTE0

##Operadores Aritméticos
"""

# Adição
10 + 2

# Subtração
10 - 2

# Multiplicação
10 * 2

# Divisão
10 / 2

# Divisão inteira
10 // 2

# Resto divisão
10 % 2

# Potenciação
10 ** 2

"""##Operadores Relacionais"""

# Menor
10 < 2

# Menor ou igual
10 <= 2

# Maior
10 > 2

# Igual
10 == 2

# Diferente
10 != 2

# Maior ou igual

"""##Operadores Lógicos

*   And
*   Or
*   Not

##Tabela da Verdade


And
"""

print(10 > 2 and 4 < 6)   # V and V - V
print(10 > 2 and 4 > 6)   # V and F - F
print(10 < 2 and 4 < 6)   # F and V - F
print(10 < 2 and 4 > 6)   # F and F - F

idade = 20
tem_carteira = True
if idade >= 18 and tem_carteira:
    print("Você pode dirigir.")
else:
    print("Você não pode dirigir.")
# Saída: "Você pode dirigir."

"""Or"""

print(10 > 2 or 4 < 6)   # V or V - V
print(10 > 2 or 4 > 6)   # V or F - V
print(10 < 2 or 4 < 6)   # F or V - V
print(10 < 2 or 4 > 6)   # F or F - F

nota = 5
frequencia = 85
if nota >= 6 or frequencia >= 75:
    print("Aprovado.")
else:
    print("Reprovado.")
# Saída: "Aprovado."

"""Not"""

not 10 < 2 # F - V

not 10 > 2 # V - F

tem_chave = True
if not tem_chave:
    print("A porta está trancada.")
else:
    print("A porta está destrancada.")
# Saída: "A porta está destrancada."