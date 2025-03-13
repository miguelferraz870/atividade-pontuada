import os 

os.system("clear") # limpa o terminal


tipo_de_combustivel = input("Digite o tipo de combustivel: ")
qnt_de_combustivel_vendido = int(input("Digite a quantidade de combustivel vendido: "))

valor_para_ser_pago = qnt_de_combustivel_vendido

match tipo_de_combustivel :
    case "A-alcool" :
        if qnt_de_combustivel_vendido > 25 :
            total = qnt_de_combustivel_vendido * 3.79 * 0.04
        elif qnt_de_combustivel_vendido <= 25 :
            total = qnt_de_combustivel_vendido * 3.79 * 0.02
    case "G-gasolina" :
        if qnt_de_combustivel_vendido > 25 :
            total = qnt_de_combustivel_vendido * 6.59 * 0.05
        elif qnt_de_combustivel_vendido <= 25 :
            total = qnt_de_combustivel_vendido * 6.59 * 0.03



print()
print(f"Tipo de combustivel escolhido {tipo_de_combustivel}")  
print(f"quantidade de combustivel {qnt_de_combustivel_vendido}")
print(f"Total a pagar ; {total}")          


           

         
       



    