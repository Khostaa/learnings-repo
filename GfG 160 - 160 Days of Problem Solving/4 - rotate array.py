# Given an array arr[]. Rotate the array to the left (counter-clockwise direction) by d steps, where d is a positive integer. 
def rotateArr(self, arr, d):
    #Your code here
    n = len(arr)
    d = d % n # for d > count

    # reverse first d elements
    reverse(arr, 0, d-1)

    # reverse remaining n-d elements
    reverse(arr, d, n-1)

    # reverse the whole array
    reverse(arr, 0, n-1)
    return arr

def reverse(arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    
