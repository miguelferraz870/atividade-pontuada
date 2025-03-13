import os 

os.system("clear") # limpa o terminal


renda_mensal = float(input("Informe sua renda mensal: R$ "))
valor_emprestimo = float(input("Informe o valor do emprestimo desejado: R$ "))
numero_prestaçoes = int(input("Informe o numero de prestaçoes desejadas: "))

def analisar_emprestimo(renda_mensal, valor_emprestimo, numero_prestaçoes):
     
    maxemprestimo = renda_mensal * 10

    maxprestaçao = renda_mensal * 0.3

    valor_prestaçao = valor_emprestimo / numero_prestaçoes


    if valor_emprestimo <= maxemprestimo and valor_prestaçao <= maxprestaçao:
        return "Emprestimo concedido."
    else:
        return "Emprestimo negado."
    

resultado = analisar_emprestimo(renda_mensal, valor_emprestimo, numero_prestaçoes)
print(resultado)    
    
    
