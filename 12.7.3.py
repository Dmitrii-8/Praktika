import time
print('\n   Добрый день!')
time.sleep(1)
print('  Вас приветствует онлайн помощник! ')
time.sleep(2)
print('  Я помогу Вам подобрать самый оптимальный вклад, в надежных банках,'
       ' с подходящими для Вас суммой и сроком!' )
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

time.sleep(5)

t = list(per_cent.items())
print(' \n  На данный момент процентные ставки по вкладам для следующих банков составляют:')
for k,v in per_cent.items():
    s = ' Для банка "' + str(k) + '" -> ' + str(v) + ' %'
    print(s)

percent = list(per_cent.values())
banks = list(per_cent.keys())
time.sleep(8)
money = int(input((' \n На какую сумму Вы бы хотели открыть свой счет!? Введите число в рублях: ')))
time = int(input((' На какой срок Вы бы хотели оставить вложения!? Введите колличество дней: ')))

print('\n Предварительный расчет по процентным ставкам будет рассчитан: '
      'на сумму вклада ', money, '₽,', 'сроком на один год, \n а также на', time, 'дней(я).')
input('Продолжить!? Если да - "Нажмите enter!")')
deposit = [ money/100*percent[0], money/100*percent[1], money/100*percent[2], money/100*percent[3]] #рассчет на год
deposit_time = [money/100*5.6/365*time, money/100*5.9/365*time, money/100*4.28/365*time, money/100*4.0/365*time]
deposit_list = [ '%.2f' % elem for elem in deposit ] #расчет на год до 2 знаков после запятой print('Более точные суммы', my_formatted_list)
deposit_time_list = [ '%.2f' % elem for elem in deposit_time ] #расчет на time до 2 знаков после запятой print('Более точные суммы', deposit_time)
money_yar = (list (map ( float, deposit_list)))
money_time = (list (map ( float, deposit_time_list)))

print(' \n Доход по вкладу на сумму', money, '₽, по приведенным выше процентным ставкам, за один год составит:')
print('  Для "', banks[0], '" банка:', money_yar[0], '₽') #print('Для "ТКБ" банка:', ['%.2f' % deposit[0]], '₽')
print('  Для "', banks[1], '" банка:', money_yar[1], '₽')
print('  Для "', banks[2], '" банка:',money_yar[2], '₽')
print('  Для "', banks[3], '" банка:',money_yar[3], '₽')

print(' \n Доход по вкладу на сумму', money, '₽, за', time, 'дней(я) составит:')
print('  Для "', banks[0], '" банка:', money_time[0], '₽') #print('Для "ТКБ" банка:', ['%.2f' % deposit[0]], '₽')
print ('  Для "', banks[1], '" банка:', money_time[1], '₽')
print('  Для "', banks[2], '" банка:', money_time[2], '₽')
print('  Для "', banks[3], '" банка:', money_time[3], '₽')

deposit_max = max(money_yar)
print('\n Максимальная сумма, которую вы можете заработать — deposit', [deposit_max], '(₽. за год.)')
deposit_max_time = max(money_time)
print(' \n Максимальная сумма, которую вы можете заработать за', time, 'дней(я) равна:', deposit_max_time, '₽.')
print(' \n Удачных вложений!')
input()




