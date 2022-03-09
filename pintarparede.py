larg= float(input('largura parede: '))
alt= float(input('altura parede: '))
área= larg * alt
print('sua parede tem a dimensão de {}x{} e sua área total é {}m'.format(larg, alt, área))
tinta = área / 2
print('para pintar uma parede de {} é necessário {}l de tinta'.format(área, tinta))


