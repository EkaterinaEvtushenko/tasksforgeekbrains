vyruchka, izderzki = float(input()), float(input())
if vyruchka > izderzki:
    print('Численость сотрудников?')
    ludi = int(input())
    prib_na_odnogo = float((vyruchka - izderzki) / ludi)
    rentab = (vyruchka-izderzki)/vyruchka
    print('прибыль')
    print(prib_na_odnogo,  '- прибыль на одного сотрудника')
elif vyruchka < izderzki:
    print('убыток')
elif vyruchka == izderzki:
    print('хрупкое равновесие')
