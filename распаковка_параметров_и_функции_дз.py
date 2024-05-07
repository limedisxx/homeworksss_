# д/з

def print_params(a = 1, b = 'строка', c = True):
    print(f'a: {a}, b: {b}, c: {c}')

print_params()
print_params(25)
print_params([1, 2, 3], False)

try:
    print_params(b = 25)
except TypeError as e:
    print(e) 

try:
    print_params(c = [1,2,3])
except TypeError as e:
    print(e) 

values_list = [42, 'new string']
print_params(*values_list)

values_dict = {'a': 42, 'b': ['new', 'list'], 'c': False}
print_params(**values_dict)

values_list_2 = [42, 'another string']
print_params(*values_list_2, 42)