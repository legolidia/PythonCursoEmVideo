valorEmReal = float(input("Quantos reais você tem?"))
cotacaoDolar = float(input("Qual a cotação do dólar de hoje?"))

valorEmDolar = valorEmReal/cotacaoDolar

print("Com R${:.2f} hoje, você pode comprar {:.2f} dólares".format(valorEmReal,valorEmDolar))