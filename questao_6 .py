import os 

os.system("clear") # limpa o terminal

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
    
media = (nota1 + nota2) / 2
print(f"Média: {media:.2f}")
    
match media:
        case media if media >= 6.0:
            print("Parabéns! Você foi aprovado!")
        case media if media >= 4.0:
            print("Você está de recuperação.")
        case _:
            print("Você foi reprovado.")






