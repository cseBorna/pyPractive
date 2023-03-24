for num in range(16):
    if (num%15)==0:
        print("FizzBuzz")
    elif (num%5)==0:
        print("Buzz")
    elif(num%3==0):
        print("Fizz")
    else:
        print(num)
 
if __name__ == '__main__':
    n = int(input())