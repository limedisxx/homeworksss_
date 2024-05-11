def print_params(param1, param2=None, *args, **kwargs):
    if isinstance(param2, dict):
        for key, value in param2.items():
            print(f"{key}: {value}")
    else:
        print(param1, param2)
    
    for arg in args:
        print(arg)
    
    for key, value in kwargs.items():
        print(f"{key}: {value}")

def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n  *  factorial_recursive(n - 1)

print_params("Hello", "World!", 42, {"key": "value"}, sep="-")
print(factorial_recursive(5))