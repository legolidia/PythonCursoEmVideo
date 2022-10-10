preco = float(input())

precoDesconto = preco - (preco*0.05)

print("O produto que custa R${:.2sf} com 5\% de desconto passa a custar R${:.2f}".format(preco, precoDesconto))