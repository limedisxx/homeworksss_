def find_password(n):
    pairs = []
    
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if n % (i + j) == 0:
                pairs.append(str(i))
                pairs.append(str(j))
    
    return ''.join(pairs)

for number in range(3, 21):
    print(f"Пароль для {number}: {find_password(number)}")
