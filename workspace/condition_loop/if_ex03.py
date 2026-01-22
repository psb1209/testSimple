jumsu = [90,80,65]

#count=4


#총점을 구하고, 평균을 구하시오.
tot=0
avg=0.0
num=0 #과목수

#총점
#tot=jumsu[0]+jumsu[1]+jumsu[2]

#tot += jumsu[0]
#tot += jumsu[1]
#tot += jumsu[2]

for i in jumsu:
    tot += i
    num += 1 #과목수를 카운트해서 누적
print(tot)

#avg=tot/len(jumsu)
avg=tot/num
print(avg)

