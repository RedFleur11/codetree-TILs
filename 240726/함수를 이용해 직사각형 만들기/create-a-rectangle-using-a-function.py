def ex1(n,m):
    for _ in range(n):
        print("1"*m)

rownum, colnum=tuple(map(int,input().split()))
ex1(rownum,colnum)