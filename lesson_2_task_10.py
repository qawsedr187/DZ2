PROCENT = 0.01
x = int(input('введите кол-во лет: '))
y = int(input('Введите сумму: '))
def bank (x, y):
    sum =(y * (x * 12) * PROCENT) + y
    print(f'Ваша сумма через {x} лет, будет {sum}')
bank(x, y)










#2. Дано**:** пользователь делает вклад в размере Х рублей сроком на Y лет под 10% годовых
#  (каждый год размер его вклада увеличивается на 10%, эти деньги прибавляются к сумме вклада,
#  и на них в следующем году тоже будут проценты).

#3. Задача: написать функцию bank, принимающую аргументы X и Y и возвращающую сумму, 
# которая будет на счету пользователя спустя Y лет.