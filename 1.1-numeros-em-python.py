#AULA COMPLETA: NUMEROS EM PYTHON

"""
1 - Tipos númericos
2 - conversões de tipos
3 - Hierarquia
4 - Operações matemáticas
5 - coerção de tipos
6 - verificação de tipos
7 - entrada de dados
"""
############################
# PASSO 01 - TIPOS NUMÉRICOS
############################
# int -> números inteiros
# float -> números com casas decimais
# complex -> números complexos (usado em matemática/engenharia)

print("===== TIPOS NUMÉRICOS =====")

# EXEMPLO 01 - NUMERO INTEIRO

#criamos uma variável chamada numero_inteiro
numero_inteiro = 10

#Mostramos o valor
print ("valor:", numero_inteiro)

#type() modtra qual é o tipo da variável
print("tipo:", type(numero_inteiro))

print("--------------------------")

#EXEMPLO 02 - NUMERO DECIMAL

#Float é um número com ponto decimal
numero_decimal = 3.14

print ("valor:", numero_decimal)
print ("tipo:", type(numero_decimal))

print("---------------------------")

# EXEMPLO 03 - NUMEROS COMPLEXOS
# Um número complexo possui duas partes:
# Parte real (Numero Normal)
# Parte imaginaria (multiplicada por j)

# Estrutura geral:
# numero = a + bj

# a = parte real
# b = parte imaginária
# j = unidade imaginária

numero_complexo = 2 + 3j

print("valor:", numero_complexo)
print("tipo:", type(numero_complexo))

print("---------------------------")

# Exemplo 03 - ACESSANDO CADA PARTE DO NÚMERO

# .real retorna a perte real
print ("parte:", numero_complexo.real)

# .imag retorna a parte imaginaria
print ("parte imaginária", numero_complexo.imag)

#apenas para separar visualmente a saída no terminal
print("\n\n")

#================================
## PASSO 02 - CONVERSÃO DE TIPOS
#================================

## Exemplo clássico:
## Dados vindos do usuario são textos (string), muitas vezes é necessário converter eles.

print("=====Conversões======")

# float -> int 

valor = int(3.9)

print("int(3.9):", valor)
print("Tipo:", type(valor))

#string -> int
valor1 = int("10")
print(type(valor1))

valor2 = int("10")
print('int("10"):', valor2)
print("tipo:", type(valor2))

#int --> float
valor3 = float(10)
print("float(10):", valor3)
print("tipo", type(valor3))
