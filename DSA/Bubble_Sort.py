def bubble_sort(elements):
    size=len(elements)
    swapped=False    # if no swapping take place in iteration,it means elements are sorted.
    for i in range(size-1):
        for j in range(size-1-i):   # (size-i-1) as last element in every iteration is getting sorted.
            if elements[j]>elements[j+1]:
                elements[j],elements[j+1]=elements[j+1],elements[j]
                swapped=True

        if not swapped:
            break

    return elements

if __name__=='__main__':
    test=[
        [23,5,4,6,34,64,7,84,24],
        [45,3,4,5,23,54,7,4,6],
        [9,7,45,3,65,5,4,6,43]
    ]

    for element in test:
        print(bubble_sort(element))