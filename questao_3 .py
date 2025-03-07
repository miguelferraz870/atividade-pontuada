import os 

os.system("clear") # limpa o terminal


A = int(input("Digite o primeiro numero (A): "))
B = int(input("Digite o segundo numero (B) "))

if A == B:
    C = A + B
else:
    C = A * B


print(f" O valor de C é {C}")        