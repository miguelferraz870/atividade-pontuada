import os 

os.system("clear") # limpa o terminal


primeiro_numero = float(input("Digite a primeira nota: "))
operaçao = input("Digite a operaçao desejada: ")
segundo_numero = int(input("Digite a segunda nota: "))


match operaçao:
    case "+":
       resultado = primeiro_numero + segundo_numero
    case "-":
       resultado = primeiro_numero - segundo_numero
    case "*":
       resultado = primeiro_numero * segundo_numero
    case "/":
      resultado = primeiro_numero / segundo_numero
    case _:
      print("Opçao invalido. ")


print()  
print(f"primeiro numero: {primeiro_numero}")  
print(f"Operaçao: {operaçao}")  
print(f"Segundo numero: {segundo_numero}")
print(f"Resultado: {resultado}")