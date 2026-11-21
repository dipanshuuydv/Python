num = int(input("Enter any number to check whether the number is prime or not: "))

for i in range(2, num):
    if num % i == 0:
        print("Not prime")
        break
else:
    print("Prime")   