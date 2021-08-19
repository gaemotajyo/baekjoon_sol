import sys

a, b, c = map(int, sys.stdin.readline().split())

if a==c:
    print(1)

else:
    n=1
    while a*(n-1)-b*(n-2)!=c:
        n+=1
        if a*(n-1)-b*(n-2)>=c:
            print(n-1)
            break