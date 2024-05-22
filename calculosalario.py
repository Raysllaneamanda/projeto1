"""Faça um programa que pergunte quanto você ganha por hora e o numero de horas trabalhadas no mês.
Calcule e mostre o Total do seu salario no referido mês. 

"""
horasalario = float(input("Digite quanto você ganha por hora: "))
horastrabalhadas = float(input("Digite quantas horas você trabalhou esse mês: "))

salariofinal = horasalario * horastrabalhadas


print(f"A {horasalario} a hora de trabalho, sendo {horastrabalhadas} horas trabalhadas, e o salario final é {salariofinal}")
