a=1

# def vartest(a):

#     a=a+1
#     print('local:',a)

# vartest(a) #함수에 값만 전달하는 역할
# print('global:',a)

def vartest(b):
    global a
    a=a+b
    print('local:',a)

b=10
vartest(b)
print('global:',a)