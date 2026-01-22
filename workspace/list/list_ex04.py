a=[1,2,3]
print(a)
#치환(변경)
a[2]=4
print(a)

#리스트 삭제(위치기반 삭제(인덱스))
del a[1]
print(a)

#리스트 값추가
a.append(9)
print(a)

#리스트 값 추가(insert)
a.insert(1,5)
print(a)

#리스트 삭제(remove(삭제할 값))
a.remove(5)
print(a)

#뒤에 값을 꺼낸것(실제 목록에서는 사라짐)
#item=a.pop()
#print(a)
#print(item)

            
item=a.pop(1)
print(a)
print(item)
