file=open("sample.txt",'r')
f2=open("s1.txt",'w')
for line in file.readlines():
    if not (line.startswith("I")):
        print(line)
        f2.write(line)

file.close()
f2.close()
    
