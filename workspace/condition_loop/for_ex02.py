a=range(20)
print(type(a))


# for i in range(10):
#     print(i)

#시작값을 지정 가능/ 마지막은 -1까지만 나옴
for i in range(10,1,-2):
    print(i)

#1~100까지의 합을 구하시오.
sum = 0
for i in range(101):
    print(i, end=" , ") #옆으로 나열하게 하기 위함: end
    sum+=i

print("1~100까지의 합: ", sum)
