count={ }
for ch in 'hello,world':
    if count.get(ch)==None:
      count[ch]=1
    else:
        count[ch]=count[ch]+1
print(count)
#########
a=[1,2]
b=a
print(a is b)
a+=[3]
print(a)
print(a is b)
##########
names=['a','b','c','d']
for i,name in enumerate(names):
    print(i,name)
##########
a=list(range(0,10))
b=list()
for item in a:
    b.append(item*item)
    
print(a)
print(b)
###########
coordinates=[]
for x in range (0,10):
    for y in range (0,10):
        coordinates.append((x,y))
print(coordinates)
