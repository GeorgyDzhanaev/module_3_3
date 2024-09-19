def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


print_params()
print_params(25)
print_params(['строка'], True)
print_params(c=[1,2,3])

values_list = [54.32, 'Строка']
values_dict = {'a': 42, 'b': 'другая строка', 'c': False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)