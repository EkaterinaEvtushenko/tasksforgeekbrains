a, b = int(input()), int(input())
counter = 0
while a < b:
    a = a+(a/10)
    counter+=1
    print(counter, '-й день: ', round(a, 2), sep= '')
print('на', counter, '-й день спортсмен достиг результата - не менее', b, 'км')


