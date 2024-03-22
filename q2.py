# Q2
# Write a Python function flatten_list(lst) that takes a nested list as input and returns a flattened list. The flattened list should contain all the elements of the original list, but without any nesting. 
# Example: 
# Input: [[1, 2, [3]], 4, [5, [6, 7]]] 
# Output: [1, 2, 3, 4, 5, 6, 7] 
# Your function should handle arbitrarily nested lists, and the order of elements in the flattened list should be the same as in the original list. 

def flatten_list(lst):
    flattened_lst=[]
    for i in lst:
        if isinstance(i,list):
            flattened_lst.extend(flatten_list(i))
        else:
            flattened_lst.append(i)
    return flattened_lst
    
nstd_lst= [[1, 2, [3]], 4, [5, [6, 7]], [0,[8,10,12],14]] #input
print(flatten_list(nstd_lst)) #calling the function