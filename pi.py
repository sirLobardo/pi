n = 0
pi = 0
a = int(input("Type the number of precision: "))

while n < a:
    pi = 4*(pow(-1, n))/(2*n + 1) + pi
    n = n + 1
print(pi)
os.system("pause")