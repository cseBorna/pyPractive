n=int(input())
if (n%2!=0):
    print("Weird")
else:
    if(2<=n<=5):
        print("Not Weird")
    if(6<=n<21):
        print('Weird')
    if(n>20):
        print('Not Weird')