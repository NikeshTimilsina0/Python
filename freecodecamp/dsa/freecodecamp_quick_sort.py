def quick_sort(arr):
    #choose one element to be the pivot,best to take the first or last element
    #if the element is greater than pivot store it in a high array
    #if the element is less than pivot store it in a low array
    if len(arr)<=1:
        return arr
    pivot=arr[-1] #taking the last array
    low=[]
    high=[]
    equal=[]
    for item in arr:
        if item<pivot:
            low.append(item)
        elif item>pivot:
            high.append(item)
        else:
            equal.append(item)
    return quick_sort(low)+equal+quick_sort(high)
