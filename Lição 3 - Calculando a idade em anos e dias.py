data = input('')
dia, mes, ano = data.split("/")

anos = 2020 - int(ano)

if int(dia) <= 10:
    dias = 10 - int(dia)
    meses = 11 - int(mes)

else:
    dias = (30-int(dia)) + 10
    meses = 11 - int(mes)
    meses = meses - 1

totaldias = (anos*365) + (meses*30) + dias

print(totaldias)
print(anos)
