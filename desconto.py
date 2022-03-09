preço = float(input('preço do produto: R$ '))
aVista = preço - (preço * 5 / 100)
parcelado= preço + (preço * 8 / 100)
print('o preço no valor de {:.2f}R$  com desconto de 5% fica por {:.2f}R$'.format(preço, aVista))
print('o produto no valor de {:.2f}R$, parcelado aumenta 8%, e fica por {:.2f}R$'.format(preço, parcelado))


