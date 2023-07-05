abu=[23,24,25]
print(abu[1])
abu[0]=45
print(abu)
print(abu[-1])
print(abu[0:3])
print(abu[:2])
print(abu[2:])
mark=[0,0,0,0,0]
mark.insert(1,5)
print(mark)
mark.append(6)
print(mark)
x=len(mark)
print(x)
mark2=[3,5,6,7,]
mark.extend(mark2)
print(mark)
mark.remove(7)
print(mark)
i=0
count=0
while(i<=9):
    if(mark[i]==6):
        count=count+1
    i=i+1
print(count)

 	


	
