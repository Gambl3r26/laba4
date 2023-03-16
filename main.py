def z(i):
    return True if i % 3==0 else False
print(z(14))
print(z(15))
def z2():
    try:
        a=int(input("Введите число "))
        b=100/a
    except ZeroDivisionError:
        print("Введен 0!")
    except ValueError:
        print("Введенно не число")
    else:
        print(b)
z2()
def z3():
    d = int(input("Введите день "))
    m = int(input("Введите месяц "))
    g = int(input("Введите год "))
    if d < 32 and d > 0 and m < 13 and m > 0 and g > 0:
        if d*m == (g % 100):
            print('magic')
        else:
            print ('no magic')
z3()
def z4(num):
    try:
        sum1 = 0
        sum2 = 0
        for i in num[:int(len(num) / 2)]:
            sum1 += int(i)
        for j in num[int(len(num) / 2):]:
            sum2 += int(j)
        if sum1 == sum2:
            print("У вас счастливый билетик")
        else:
            print("У вас не счастливый билетик")
    except:
        print("Вы ввели что-то не то")
z4(input())