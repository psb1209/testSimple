#단어의 길이가 3인 단어가 몇개인지 출력하시오.

test_list=['one','two','three','abc']

count=0

for i in test_list:
    print(i,':',len(i))
    if len(i)==3:
        count+=1
        print(count,"개")


a=[(1,2),(3,4),(5,6)]
# 리스트 합을 구하시오.

tot=0
# for k in a:
#    tot += k[0]+k[1]
#    print(tot)

for i,j in a:
   tot += (i+j)
   print(tot)


    

    