n = int(input())
arr = map(int, input().split())
arr.sort()
print(arr[(arr.index(max(arr)))-1])