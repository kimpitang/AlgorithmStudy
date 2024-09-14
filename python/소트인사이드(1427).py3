def BubbleSort(arr):
    n=len(arr)
    for i in range(0,n-1):
        for j in range(0,(n-i)-1):
            if arr[j]<arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp

N = input()
N.split()
bb=list(map(int,N))

BubbleSort(bb)
for k in range (0,len(N)):
    print(bb[k],end="")
