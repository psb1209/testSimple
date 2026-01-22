def add_many(*args):
    result=0
    for i in args:
        result = result + i

    return result

#nums=[2,3,4]  # 매개변수에서 *를 빼면 list를 받을수 있음
#*=매개변수를 여러개 받을 수 있음
sum=add_many(2,3,4)
print(sum)