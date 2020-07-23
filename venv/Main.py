import random

#the method merge is defined, as well as variables used inside
#merge is used to combine two arrays into a single array
#the new array will be in order from lowest to highest number
def merge(arr, start, middle, end):
    #a is used to define the length of the first temp. array
    a = middle - start + 1
    #b is used to define the length of the second temp. array
    b = end - middle

    #A1 is the first temp array
    A1 = [0] * (a)

    #L2 is the 2nd temp array
    A2 = [0] * (b)


    #this for statement assigns values for A1
    for i in range(0, a):
        A1[i] = arr[start + i]

    #this for statement assigns values for A2
    for j in range(0, b):
        A2[j] = arr[middle + 1 + j]

    #sets the index for the arrays back to start
    i = 0
    j = 0

    #sets merged array index to start
    k = start

    #creates a loop to combine arrays
    while i < a and j < b:
        #puts A1 into array if it is a lower value
        if A1[i] <= A2[j]:
            arr[k] = A1[i]
            i += 1
            #puts a2 into array, it will be lower value
        else:
            arr[k] = A2[j]
            j += 1
        k += 1

    #creates a loop to add all remaining values from A1 into merged array
    while i < a:
        arr[k] = A1[i]
        i += 1
        k += 1

    # creates a loop to add all remaining values from A2 into merged array
    while j < b:
        arr[k] = A2[j]
        j += 1
        k += 1

 #defines the sort method
 #This method is used to sort the arrays, and merges them into the final array.
def sort(arr, l, r):
    if l < r:
        m = (l + (r - 1)) // 2

        #sorts the left hand array
        sort(arr, l, m)
        #sorts the right hand array
        sort(arr, m + 1, r)
        #merges into final array, in correct order
        merge(arr, l, m, r)

#allows user to create a set of numbers, at their desiered length
setSize = int(input('How many numbers are we sorting today?'))
#creates a random list of numbers between 0 and 999,999
numbers = random.sample(range(0, 999999), setSize)

#shows the original set of numbers
print("Our set of numbers is " + str(numbers))

#if the set size is one, there is no need to sort, and is printed
if setSize==1:
    print(str(numbers))

#sorts array numbers, starting at zero, using the set size.
sort(numbers, 0, setSize - 1)

print('The sorted set is')
for i in range(setSize):
    print(str(numbers[i]))




