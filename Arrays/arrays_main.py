import array

arrays_a = array.array('i',[ 10 , 2 , 1, 0 ])
sum = 0
for elements in arrays_a:
    sum = sum + elements
print(sum)
# print(len(arrays_a))

#the below is used to change the number in the array 
arrays_a[0] = 15
# print (arrays_a)


#the below is an alternative used to find the index of the numbers in the range


for index in range(len(arrays_a)):
    max = arrays_a[0]
    if arrays_a[index] > max:
        max = arrays_a[index]
print(max)

        
    
