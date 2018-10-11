if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

arr = list(arr)

arr.sort()

sortedarray = []

for i in arr:
    if i not in sortedarray:
        sortedarray.append(i)

x = len(sortedarray) - 2

print(sortedarray[x])