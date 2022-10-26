def func (num):
    f=0
    while num > 0:
        if num % 2 == 0:
            num /= 2
        else:
            num -= 1

    return f

x=int(input(" num: "))
print(func(x))


