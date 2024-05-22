""" Faça um programa que calcule a area de um quadrado, 
em seguida mostre o dobro desta area para o usuario"""

lado = float(input("Digite o lado do quadrado: "))
area = lado ** 2
dobro = area * 2
print(f"O dobro da area de um quadrado de lado {lado:.2f}m é {dobro:.2f}m²")