def shell_sort(arr):
    size=len(arr)
    gap=size//2

    while gap>0:
        for i in range(gap,size):
            anchor=arr[i]
            j=i
            while j>=gap and arr[j-gap]>anchor:
                arr[j]=arr[j-gap]
                j-=gap
                arr[j]=anchor
        gap=gap//2
    return arr

if __name__=='__main__':
    print(shell_sort([21,38,29,17,4,25,65,3,8]))