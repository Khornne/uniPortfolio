num = int(input("Please input a number to multiply to: "))
limit = 12


if num < 0:
    for n in range(limit, 0, -1):
        print(num, "x", n, "=", num*n)



for n in range(1, 13):      
    print(num, "x", n, "=", num*n)

exit(0)

    

