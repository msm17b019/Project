def selection_sort(numbers):
    size=len(numbers)
    for i in range(size):
        min_index=i
        for j in range(min_index+1,size):
            if numbers[j]<numbers[min_index]:
                min_index=j
        
        if i != min_index:
            numbers[i],numbers[min_index]=numbers[min_index],numbers[i]
    print(numbers)

selection_sort([21,38,29,17,4,25,11,32,9])