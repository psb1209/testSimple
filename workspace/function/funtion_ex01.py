def add(a,b):
    return a+b

def sub(a):
    return 10-a

def mul(a,b):
    print(a*b)

def div():
    return a*b

def glovalTest():
    b=10
    print(a,b)


#전역변수
a=5
b=3


sum = add(10,20)
print(sum)

result = sub(3)
print(result)

#반환값 없음
mul(5,3)

result=div()
print(result)

glovalTest()
print(a,b)