def binary_search(data:list, value, start, stop)->bool:
    """Return True if value is foung in a list or portion of the list
    If values for start and stop are provided, search considers portion from data[start] to data[stop]"""
    data.sort()
    if start>stop:
        return False
    else:
        mid = (start+stop)//2
        if value == data[mid]:
            return True 
        elif value<data[mid]:
           # Recursion occurs on the left side 
           return binary_search(data, value, start, mid-1)
        else: 
            # Recur on the right side
            return binary_search(data, value, mid+1, stop)

def disk_usage(path):
    """Return the number of bytes used by a file/folder and any descendants."""
    import os
    total = os.path.getsize(path)  # for direct usage
    if os.path.isdir(path):  # if this is a directory
        for filename in os.listdir(path):  # then for each child, compose a full path to child and add child's usage to total
            childpath = os.path.join(path, filename)
            total += disk_usage(childpath)
    
    print('{0:<7}'.format(total), path)
    return total

def fibonacci_recursion(n):
    """Returns a pair of fibonacci numbers fib(n) and fib(n-1)"""
    if n<=1:
        return(n, 0)
    else:
        a, b = fibonacci_recursion(n-1)
        return(a+b, a)

def power1(x, n):
    """computes the nth power of x"""
    if n == 0:
        return 1
    else:
        partial = power1(x, n//2)
        result = partial * partial
        if n%2 == 1:
            result *= x
        
    return result