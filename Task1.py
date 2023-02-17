n = int (input("Введите трехзначное число: "))
a = n % 10
b = (n // 10) % 10
c =(n // 100)
result = a + b + c 
print(result)

