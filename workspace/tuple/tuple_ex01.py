t1 = ()
print(t1)
print(type(t1))
t2 = (1,)
print(t2)
print(type(t2))
t3 = (1, 2, 3)
print(t3)
print(type(t3))
t4 = 1, 2, 3
print(t4)
print(type(t4))
t5 = ('a', 'b', ('ab', 'cd'))
print(t5)
print(t5[2][1][1])

#튜플은 구조가 바뀌는걸 허용하지않음(값변경, 삭제 다 안됨)
#del d5[0]
