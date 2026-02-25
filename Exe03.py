'''
3. Desenvolva um programa para calcular e escrever a área e o perímetro de um retângulo.
Exemplo: 
Base= 5
Altura = 4
Área = 20
Perímetro = 18
'''

#ENTRADA
base = float(input('Informe a base do triangulo'))
altura = float(input('Informe a altura do triangulo'))

#PROCESSAMENTO
area = (base * altura)
perimetro = (base * 2) + (altura * 2)

#SAIDA
print('Area do Retangulo:', area)
print('Perimetro do Retangulo:', perimetro)