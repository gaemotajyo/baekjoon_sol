import sys
a= int(sys.stdin.readline())

if a==1:
    print('1/1')
else:
    n=1
    while n*(n+1)<a*2:
        n+=1
        if n*(n+1)>=a*2:
            output_1= int(n+1-(a-(n*(n-1)/2)))
            output_2= int(a-(n*(n-1)/2))
            if n%2==0:
                print('{}/{}'.format(output_2,output_1))
            else:
                print('{}/{}'.format(output_1,output_2))