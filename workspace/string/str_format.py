a=3
str="I eat %d apples." % a
print(str)

a=3
str="I eat %s apples." % "'Five'"
print(str)


#두개이상은 무조건 괄호로 묶어야함
a=3
str="I eat %d apples %s " % (10, "Five")
print(str)


#문자열 크기를 지정 '10' 
#-는 왼쪽정렬
#str2 소수점이하 2자리까지만(반올림)
#모든 출력은 문자
str1="%-10s"  % "hi"
str2="%.2f" %123.4567
print(str1)
print(str2)






