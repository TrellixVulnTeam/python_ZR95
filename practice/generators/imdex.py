def divBy7():
    for i in range(1, 1000):
        if(i%7==0):
           yield i


f= divBy7()
print(next(f))
print(next(f))
print(next(f))
print(next(f))

def divBy7_13():
    for i in range(1, 1000):
        if(i%7==0 and i%13==0):
            yield i

e = divBy7_13()
print('printed div by 13 and 7')
print(next(e))
print(next(e))
print(next(e))
print(next(e))
print(next(e))
print(next(e))

input('input')