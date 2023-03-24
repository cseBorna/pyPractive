n=int(input())
L=[]

for i in range(n):
    x=input().split(" ")
    command = x[0]
    if command == 'insert':
        L.insert(int(x[1]), int(x[2]))
    if command == 'print':
        print(L)
    if command == 'remove':
        L.remove(int(x[1]))
    if command == 'append':
        L.append(int(x[1]))
    if command == 'sort':
         L.sort()
    if command == 'pop':
        L.pop()
    if command == 'reverse':
        L.reverse()
    
