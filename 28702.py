flag = True
for i in range(3):
    test = input()
    if flag:
        try:
            test = int(test)
            n = test + 3 - i
            if n % 3 == 0 and n % 5 == 0:
                print("FizzBuzz")
            elif n % 3 == 0 and n % 5 != 0:
                print("Fizz")
            elif n % 3 != 0 and n % 5 == 0:
                print("Buzz")
            else:
                print(n)
            flag = False
        except:
            continue