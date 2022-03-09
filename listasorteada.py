from random import choice
n1 = input('digite 1º nome: ')
n2 = input('digite 2º nome: ')
n3 = input('digite 3º nome: ')
n4 = input('digite 4º nome: ')
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('o nome escolhido foi {}'.format(escolhido))


