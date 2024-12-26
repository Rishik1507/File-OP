file=open("sample.txt",'r')
f2=open("s1.txt",'w')
count=file.readlines()
for x in range(1,len(count)+1):
    if x%2==0:
        f2.write(count[x-1])
    else:
        pass
   

file.close()
f2.close()
f2=open("s1.txt","r")
count=f2.read()
print(count)
f2.close()
