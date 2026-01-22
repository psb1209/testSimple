#① 문자 개수 세기 (리스트 활용)
#문자열 "programming"에서 각 문자가 몇 번 등장하는지 세어,
#[['p', 1], ['r', 2], ['o', 1], ...] 형태의 리스트로 출력하세요.

a="programming"
a1=a.count('p')
r1=a.count('r')
o1=a.count('o')
g1=a.count('g')
m1=a.count('m')
i1=a.count('i')
n1=a.count('n')

list=[['p',a1],['r',r1],['o',o1],['g',g1],['m',m1],['i',i1],['n',n1]]
print(list)

#② 대소문자 변환
#문자열 "Hello World"를 모두 대문자로, 모두 소문자로 변환한 결과를 각각 출력하세요.
a="Hello World"

a1=a.upper()
a2=a.lower()

print(a1)
print(a2)


#③ 회문 판별
#문자열을 입력받아 앞뒤가 똑같은 회문인지 판별하는 프로그램을 작성하세요.
#(예: "level" → 회문)


#④ 단어 뒤집기
#"Python is fun"이라는 문장을 단어 단위로 뒤집어 "fun is Python"으로 출력하세요.

b="Python is fun"
b1=b.split()
print(b1)
print(b1[2] +b1[1]+b1[0])


#⑤ 모음 제거하기
#문자열 "beautiful day"에서 모음(a, e, i, o, u)을 모두 제거한 결과를 출력하세요.

c="beautiful day"
c=c.replace('a','')
c=c.replace('e','')
c=c.replace('i','')
c=c.replace('o','')
c=c.replace('u','')
print(c)


#⑥ 문자열 압축
#문자열 "aaabbcddd"를 "a3b2c1d3" 형태로 압축하는 프로그램을 작성하세요.

a="aaabbcddd"
a1=str(a.count('a'))
b1=str(a.count('b'))
c1=str(a.count('c'))
d1=str(a.count('d'))
print('a'+ a1+'b'+b1+'c'+c1+'d'+d1)

#⑦ 가장 긴 단어 찾기
#"Life is short, use Python" 문장에서 가장 긴 단어를 찾아 출력하세요.

a="Life is short, use Python"
b=a.split()
c=a.pop('Life')
print(c)


#⑧ 특정 단어 개수 세기
#"banana bandana banana"에서 "banana"가 몇 번 등장하는지 세어 출력하세요.



#⑨ 문자열 정렬
#문자열 "zebra"의 문자들을 알파벳 순서대로 정렬하여 "aberz"를 출력하세요.

a="zebra"



#⑩ 부분 문자열 찾기
#문자열 "abracadabra"에서 "abra"가 시작되는 모든 인덱스를 출력하세요.