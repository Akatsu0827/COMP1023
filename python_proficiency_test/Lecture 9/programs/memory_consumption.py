# Filename: memory_consumption.py

import numpy as np, sys, gc  # Import numpy package, system, and gc module

def actualsize(input_object):
    memory_size = 0                # memory_size: the actual memory size of "input_object"
                                   # Initialize it to 0
    ids = set()                    # ids: An empty set to store all the ids of objects in "input_object"
    objects = [input_object]       # objects: A list with "input_object" (traverse from "input_object")
    while objects:                 # While "objects" is non-empty
        new = []                   # new: An empty list to keep the items linked by "objects"
        for obj in objects:        # obj: Each object in "objects"
            if id(obj) not in ids: # If the id of "obj" is not in "ids"
               ids.add(id(obj))    # Add the id of the "obj" to "ids"
               memory_size += sys.getsizeof(obj) # Use getsizeof to determine the size of "obj"
                                   # and add it to "memory_size"
               new.append(obj)     # Add "obj" to "new"
        objects = gc.get_referents(*new)  # Update "objects" with the list of objects directly
                                          # referred to by *new
    return memory_size             # Return "memory_size"

L = list(range(0, 1000))           # Define a Python list of 1000 elements
A = np.arange(1000)                # Define a NumPy array of 1000 elements
# Print size of the whole list, it prints "Size of the whole list in bytes: 36056"
print("Size of the whole list in bytes:", actualsize(L))
# Print size of the whole NumPy array, it prints "Size of the whole NumPy array in bytes: 8112"
print("Size of the whole NumPy array in bytes:", actualsize(A))