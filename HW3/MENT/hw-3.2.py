def hw3():
    a = [1,2,3,4]

    summ = 1
    for x in a:
        summ *= x

    print(summ)

def hw3_1():
    n1 = int(input("Дайте чотиризначне число: "))
    n2 = 0

    while n1 > 0:
        digit = n1 % 10
        n1 = n1 // 10
        n2 = n2 * 10
        n2 = n2 + digit

    print( "Зворотнє число: ", n2)


def hw3_2():
    a = [3,4,2,1]
    a.sort()
    print(a)
