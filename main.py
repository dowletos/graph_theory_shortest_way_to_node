if __name__ == '__main__':
    # Deykstra Algorithm for finding the shortest distance and way to the node
    print('              ############################################################################')
    print('              ############################################################################')
    print('              ############################################################################')
    print('              ############################################################################')
    print('              ##############The shortest way in graph (Deykstra algorithm)################')
    print('              ############################################################################')
    print('              ############################################################################')
    print('              ############################################################################')
    size=11
    a=[[a0 for a0 in range(size)] for a1 in range(size)]
    d=[d0 for d0 in range(size)]
    v=[v0 for v0 in range(size)]
    temp=minindex=min=0
    begin_index=0

    #Matrix input
    for i in range(size):
        a[i][i]=0
        for j in range(i+1,size):
            temp=int(input(f'              #############   Please enter the distances: {i+1} - {j+1} : '))
            a[i][j]=temp
            a[j][i]=temp
    print('\r\n' * 3)
    print('              ############################################################################')
    print('              #########################---Matrix entered---###############################')
    print('              ############################################################################')
    print('\r\n')

    #Print matrix entered
    for i in range(size):
        if i==0: print(f'              _____[1]_____|_____[2]_____|_____[3]_____|_____[4]_____|_____[5]_____|_____[6]_____|',end='')
        print('\r\n')
        for j in range(size):
            if j==0: print(f'     [{i+1}]    ||',end='')
            print(f'{a[i][j]:7}',end='      |')

    #Initialize nodes and distances
    for i in range(size):
        d[i]=10000
        v[i]=1
    d[begin_index]=0
    while (minindex < 10000):
        minindex = 10000
        min = 10000
        for i in range(size):
            # if doesn't outdo the node and distance is less than min
            if v[i]==1 and d[i]<min:
                min=d[i]
                minindex=i
        if (minindex != 10000):
              for i in range(size):
                    if (a[minindex][i] > 0):
                        temp = min + a[minindex][i]
                        if (temp < d[i]):
                            d[i] = temp
              v[minindex] = 0

    #Print the shortest distance
    print('\r\n')
    print('              The shortest distance is:')
    for i in range(size):
        print(f'{d[i]:7}',end='      |')
    ver=[v0 for v0 in range(size)]
    end=size-1
    ver[0]=end+1
    k=1
    weight=d[end]

    while(end !=begin_index):
        for i in range(size):
            if (a[i][end]!=0):
                temp = weight - a[i][end]
                if (temp==d[i]):
                    weight = temp
                    end = i
                    ver[k] = i + 1
                    k+=1
    act=False
    print('\r\n')
    print('              The shortest way is:')
    for i in ver[::-1]:
            if i==1 or act==True:
            act=True
            print(f'{i:7}',end='      |')