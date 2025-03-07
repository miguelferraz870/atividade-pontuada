import os 

os.system("clear") # limpa o terminal


nome = input("Digite a descrição do produto: ")
quantidade = int(input("Digite a quantidade adquirida: "))
preco_unitario = float(input("Digite o preço unitário: "))
    
total = quantidade * preco_unitario
    
match quantidade:
        case q if q <= 5:
            desconto = total * 0.02
        case q if q <= 10:
            desconto = total * 0.03
        case _:
            desconto = total * 0.05
    
total_a_pagar = total - desconto
    
print(f"Produto: {nome}")
print(f"Total: R$ {total:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Total a pagar: R$ {total_a_pagar:.2f}")


