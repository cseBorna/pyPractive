#Replace all ______ with rjust, ljust or center. 

a = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(a):
    print((c*i).rjust(a-1)+c+(c*i).ljust(a-1))

#Top Pillars
for i in range(a+1):
    print((c*a).center(a*2)+(c*a).center(a*6))

#middle belt
for i in range((a+1)//2):
    print((c*a*5).center(a*6))

#bottom pillars
for i in range(a+1):
    print((c*a).center(a*2)+(c*a).center(a*6))

#Bottom Cone
for i in range(a):
    print(((c*(a-i)).rjust(a)+(c*(a-i-1)).ljust(a)).rjust(a*6))