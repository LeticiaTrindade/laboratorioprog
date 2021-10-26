valorinicial = float(input(''))
taxa = float(input(''))
tempo = int(input(''))

total = (valorinicial*taxa*tempo)/100
montante = valorinicial*((1+taxa/100)**tempo)

print(round(montante,2))
