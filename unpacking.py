def  print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [25, "строка", False]
values_dict = {'a':4, 'b':"текст", 'c':6.9}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [12.5, "число"]
print_params(*values_list_2, 42)