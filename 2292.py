import sys
a= int(sys.stdin.readline())

if a == 1:
    print(1)
else:
    n=0
    while n*(n-1) < (a-1)/3:
        n +=1
        if n*(n-1) >= (a-1)/3:
            print(n)