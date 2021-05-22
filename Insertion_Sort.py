def insertion_sort(numbers):
    for i in range(1,len(numbers)):
        anchor=numbers[i]
        j=i-1
        while j>=0 and anchor<numbers[j]:
            numbers[j+1]=numbers[j]
            j=j-1
        numbers[j+1]=anchor

    print(numbers)

if __name__=='__main__':
    insertion_sort([11,9,29,7,2,15,20])