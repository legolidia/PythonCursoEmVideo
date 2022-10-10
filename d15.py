kmRodados = float(input())

diasAlugados = int(input())

preco = diasAlugados*60 + kmRodados*0.15

print("O aluguel por {} dias e {}km rodados totalizou o valor de R${:.2f}".format(diasAlugados, kmRodados, preco))