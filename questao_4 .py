import os 

os.system("clear") # limpa o terminal


morango = float(input("Digite quantos kilos de morango foram comprados: "))
maça = float(input("Digite quantos kilos de maça foram comprados: "))
valor = 0

if morango <= 5: 
    valor += morango * 2.5
else:
    valor += maça * 2.2
if maça <= 5:
    valor += maça * 1.8
else:
    valor += maça * 1.5

if (morango + maça) > 8 or valor > 25:
    valor -= valor * 10 / 100


print(f" O valor a ser pago é R${valor:.2f}")


