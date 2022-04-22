def some_fun( a, b=[] ):
    print(a)
    print(b)
    b.append(0)
    return 0

if __name__ == '__main__':
    some_fun(1)

    some_fun(2)

    some_fun(3)