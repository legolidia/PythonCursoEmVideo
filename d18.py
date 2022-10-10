from math import radians, sin, cos, tan

angulo = float(input())

sen = sin(radians(angulo))
cos = cos(radians(angulo))
tan = tan(radians(angulo))

print("Seno: {:.2f}, Cosseno: {:.2f}, Tangente: {:.2f}".format(sen,cos,tan))