import os 

os.system("clear") # limpa o terminal


print("""
========== Menu ==========
Codigo\t\tCores\t\Preços
      
1   \t\tVerde\t\tR$10.00
2   \t\tAzul  \t\tR$20.00
3   \t\tAmarelo \t\tR$30.00 
4   \t\tVermelho \tR$40.00

""")

cd = int(input("Informe a cor do cd desejada: "))

match cd:
    
     case 1:
      cordocd = "verde"
      valor = 10   

     case 2:
      cordocd = "azul"
      valor = 20


     case 3:
      cordocd = "amarelo"
      valor = 30   


     case 4:
      cordocd = "vermelho"
      valor = 40

     case _:
       corcocd = "Opçao Invalida!"
       valor = 0


print()
print(f"Cor do cd: {cordocd}")
print(f"Valor: R${valor:.2f}")

 
