import numpy

n,m=map(int,input().split())
l=[]
for i in range(n):
    x=(map(int,input().split()))
    l.append(list(x))

array=numpy.array(l)
a1=numpy.transpose(array) 
a2=array.flatten()
print(a1)
print(a2)
