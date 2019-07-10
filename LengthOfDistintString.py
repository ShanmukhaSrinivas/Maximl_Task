def func(string):
    k = ''
    Length = len(string)
    for i in range(Length+1):
        for j in range(Length+1):
            new = string[i:j]
            if len(new) == len(set(new)):
                if len(k) < len(new):
                    k = new
    return len(k)


print(func(input()))
