year = int(input('Введите год:' ))
def is_year_leap(year):
    if year % 4 == 0:
        print(f'год {year}: True')
    else:
        print(f'год {year}: False')
is_year_leap(year)