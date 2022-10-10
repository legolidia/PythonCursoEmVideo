largura = float(input())
altura = float(input())

area = largura*altura

litros = area/2

print("Para pintar uma parede de {}m², são necessários {:.1f} litros de tinta".format(area, litros))