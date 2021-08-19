import sys
n = int(sys.stdin.readline())
data = []
for i in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    room_num=data[i][2]//data[i][0]+1
    floor_num=data[i][2]%data[i][0]
    if floor_num == 0:
        floor_num = data[i][0]
        room_num = data[i][2]//data[i][0]
        if room_num//10==0:
            print('{}0{}'.format(floor_num,room_num))
        else:
            print('{}{}'.format(floor_num,room_num))
    else:
        if room_num//10==0:
            print('{}0{}'.format(floor_num,room_num))
        else:
            print('{}{}'.format(floor_num,room_num))

