def binary_search(arr,num):
    left_index=0
    right_index=len(arr)-1
    mid_index=0
    while left_index<=right_index:
        mid_index=(left_index+right_index)//2
        mid_number=arr[mid_index]

        if mid_number==num:
            return mid_index

        if mid_number < num:
            left_index=mid_index+1
        else:
            right_index=mid_index-1

    return -1

if __name__=='__main__':
    arr=[3,6,7,12,45,56,67,73,81]
    num=7
    print(f'Element {num} is present at index',binary_search(arr,num))