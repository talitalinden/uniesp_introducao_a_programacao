for num in range(1000, 2001):
    if (num % 11) == 5:
        print(num)

for num in range(1, 11):
    print(f"Tabuada do {num}")
    for num2 in range(1, 11):
        resultado = num * num2
        print(f'{num} x {num2} = {resultado}')