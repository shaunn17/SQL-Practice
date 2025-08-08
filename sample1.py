print("Hey There!")

import random

def random_number(min_value, max_value):
    """Generate a random number between min_value and max_value."""
    return random.randint(min_value, max_value)         

random_num = random_number(1, 100)
print(f"Random number generated: {random_num}")


#Bubble sort implementation
def bubble_sort(arr):
    n = len(arr)
    swapped = False
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:   
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        if swapped == False:
            break
    return arr
sample_array = [64, 34, 25, 12, 22, 11, 90, 2]
sorted_array = bubble_sort(sample_array)            

print(f"Sorted array: {sorted_array}")
            