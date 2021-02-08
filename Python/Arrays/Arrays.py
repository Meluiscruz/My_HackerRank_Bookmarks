import numpy as np

def arrays(arr):
    
    arr_list = list(arr)
    arr_list_v2 = list()
    
    for _ in arr_list:
        arr_list_v2.append(float(_))
    
    Array = np.array(arr_list_v2)
    
    return np.flip(Array)

arr = input().strip().split(' ')
result = arrays(arr)

print (result)