a = 25

if isinstance(a, int):
    if a >= 10:
        if a >= 20:
            if a >= 30:
                print('a >= 30')
            else:
                print("20 < a < 30")
        else:
            print("10 < a < 20")
    else:
        print('a < 10')

if a > 50: a += 100
