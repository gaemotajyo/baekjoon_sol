import sys
a, b, c = map(int, sys.stdin.readline().split())

if b < c:
    n=a//(c-b)+1
    print(n)#tlqkf
else:
    print(-1)