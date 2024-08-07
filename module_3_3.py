# 1. Функция с параметрами по умолчанию
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
    
print_params()
print_params(b = 25)
print_params(c = [1,2,3])
print_params(9, ['string', 4, True], 5)

# 2. Распаковка параметров
values_list = [10, ['strong', 4], False]
values_dicts = {'a': False, 'b': 'no string', 'c': 4}
print_params(*values_list)
print_params(**values_dicts)

# 3. Распаковка + отдельные параметры
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)