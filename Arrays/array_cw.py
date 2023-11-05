import array


def linear_search(an_array,element):
   for index in range(len(an_array)):
    if an_array[index] == element:
        return index

    return None


myArray = array(3)
myArray[0] = 1
myArray[1] = 5
myArray[2] = 10


element_in_array = linear_search(myArray,0)

            
