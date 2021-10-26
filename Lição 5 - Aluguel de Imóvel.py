semanas1 = int(input(''))
semanasTv = int(input(''))
semanasNet = int(input(''))
pacoteNet = float(input(''))

valorAluguel = (semanas1 * 525.50)
valorTv = (semanasTv * 50)
valorNet = ((pacoteNet * 20) * semanasNet)

soma = valorAluguel+valorTv+valorNet

print('{:.2f}'.format(soma))
