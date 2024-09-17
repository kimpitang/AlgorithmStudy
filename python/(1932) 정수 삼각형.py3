def top_down_path_max(n, alist):
    m=2
    for i in range(1,n):
        for j in range(m):
            if (j == 0):
                alist[i][j]=alist[i][j]+alist[i-1][j]
            elif (i==j):
                alist[i][j]=alist[i][j]+alist[i-1][j-1]
            else:
                alist[i][j]=max(alist[i-1][j-1],alist[i-1][j])+alist[i][j]
        m+=1


linenum=int(input())
intlist=[]
for i in range (0, linenum):
    nums=input()
    strlist=nums.split(' ')
    intlist.append(list(map(int,strlist)))

top_down_path_max(linenum, intlist)
print(max(intlist[linenum-1]))