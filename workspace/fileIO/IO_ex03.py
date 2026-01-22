f=open("newfile4.txt",'w')


for i in range(1,11):
    data = "%d번째 즐입니다.\n" %i
    f.write(data)

f.close()

f=open("newfile4.txt",'r')

while True:
    line=f.readline()
    print(line)

    if not line :
        break
    
f.close()
