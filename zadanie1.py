# пункт 1
print("Начинаем осваивать питон")
d = int(input('Играем с переменными, введите число: '))
g = str(input('А теперь слово '))
print("Вот что вы ввели", g, d )
# пункт 2
n=int(input('Введите количество секунд'))
h=str(n//3600)
m=str((n//60)%60)
s=str(n%60)
print(h+':'+m+':'+s)

# пункт 3

m=int(input('Введите число'))
o = str(m)
print (m+ int(o+o)+int(o+o+o))

# пункт 4

aa = int(input("Введите целое положительное число"))
mm = aa%10
aa = aa//10
while aa > 0:
    if aa%10 > mm:
        mm = aa%10
    aa = aa//10
print(mm)

# пункт 5

aaa = int(input("Выручка фирмы"))
bbb = int(input("Издержки фирмы"))
if aaa > bbb:
    print('Фирма работает с прибылью')
    ccc = (aaa - bbb)
    ddd = int(input("Сколько сотрудников в фирме?"))
    print('Каждый сотрудник получил прибыль в сумме ', ccc/ddd)
else:
    print('Фирма работает с убытками')

# пункт 6
aaaa = int(input("Сколько киломметров в первый день"))
bbbb = int(input("Когда спортсмен достигнет результата км: "))
score=float(aaaa/10)
day=1
while bbbb > aaaa:
    day=day+1
    aaaa=float(aaaa+score)
    score = float(aaaa / 10)

print ('Спортсмен достигнет результата на', day,'день')