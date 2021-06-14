a = float(input('Digite a altura da parede: '))
l = float(input('Digite a largura da parede: '))
print('Sua parede mede {}X{} M\nEla tem a área de {:.2f} M²\nSerão necessários {:.2f} litros de tinta para cobrir toda a parede.'.format(a,l,(a*l),((a*l)/2)))
