
b = int(input("Введите колличество билетов, которое Вы бы хотели приобрести на мероприятие "
              "(желательно в виде целых чисел от 1 до 100 (включительно)):"))
if b > 100 or b <= 0:
    b = int(input("Вы ввели некорректное значение, возможно у нас нет в наличии такого колличества билетов "
                "\n Попробуйте ввести еще раз:"))
    if b > 100 or b <= 0:
        print("К сожалению мы не можем предоставить для Вас такое количество билетов!")
        import sys

        if b > 100 or b <= 0:
            sys.exit("Out of stock or invalid numbers")
    #elif b < 100 or b >= 0:
        #print("Отлично! У нас имеется в наличии такое колличество билетов.")
elif b < 100 or b >= 0:
    print("Отлично! У нас имеется в наличии такое колличество билетов.")

#else:
    #print("Отлично! У нас имеется в наличии такое колличество билетов.")

print("Введите, по порядку, возраст каждого посетителя, начиная с первого билета:")
c = [int(input()) for i in range(b)]
print(c)
n = 0
m = 1
z = 0
while m <= b:
    try:
        if c[n] > 100 or c[n] <= 0:
            raise ValueError("\n Человеку не может быть столько лет! Введен некорректный возраст!")
    except ValueError as error:
        print(error)
        print()
    else:
        print("\n Билет продан!")
        z = z + 1

    try:
        if 0 < c[n] < 18:
            c[n] = 0
            print("Детям вход бесплатный!")
        elif 18 <= c[n] <= 25:
            c[n] = 990
        elif 25 < c[n] < 120:
            c[n] = 1390
        elif c[n] > 120:
            c[n] = 0
        elif c[n] <= 0:
            c[n] = 0
    finally:
        print("Цена", m, "билета составила:", c[n], "₽")
    n += 1
    m += 1

s = sum(c)
# print(z)
if z > 3:
    s = s - s // 10
    print("\n На данный момент у нас действует 10% скидка при регистрации более трех человек! "
            "\n С учетом скидки, сумма к оплате составила:", s, "₽."
                                                                  "\n С нетерпением ждем Вас на конференции!")
else:
    print("\n Общая сумма к оплате составила:", s, "₽. С нетерпением ждем Вас на конференции!")

input()




