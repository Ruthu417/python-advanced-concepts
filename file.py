'''f = open('data.txt','r')
s = f.read()
for i in s:
    print(i)'''

'''f = open('data.txt','w')
s = f.write("PVP")
f.close()
f = open('data.txt','r')
q = f.read()
for i in q:
    print(i)'''

'''f = open('data.txt','a')
s = f.write("College")
f.close()'''

'''f = open('data.txt','r')
s = f.read()
c = 0
for i in s:
    c +=1
    print(i,end = " ")
print(c)
print(f.tell())
a = s.split()
count = 0
for i in a:
    count += 1
    #print(i)
print(count)'''

f = open('data.txt','r')
f.seek(0)
print(f.read(7))

#c = 0
'''for i in s:
    #c +=1
    print(i,end = " ")
print(c)
print(f.tell())'''






