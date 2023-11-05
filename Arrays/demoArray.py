import arrays_class as arr # a way of calling the class
from arrays_class import *
from arrays_class import Array # another way of calling the class

# myArray = arr.Array(5) # this is a way to write with the specific import called in the import
myArray = Array(5) # this is for calling all the divisions from the python file 



for index in range(len(myArray)):
    myArray[index] = 1
    

print(myArray)



#for importing time 
import time 

start = time.perf_counter()
sum = 0 

for number in range(1000000):
    sum += number
end = time.perf_counter()

time_execution = end - start
print("Elasped time is, ", time_execution)


