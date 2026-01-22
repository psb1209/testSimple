def print_kwargs(**test):
    print(test)
    return test

dic1=print_kwargs(a=2)
print(dic1)
dic2=print_kwargs(name='홍길동', age=30)
print(dic2)

