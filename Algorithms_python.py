

# --------------------------------------------------------------------------------------------

for n in range(100,199):
	for i in range(2,n-1):
		c=0
		if n%i==0:
			print(f"{n} sade deyil")
			break




# -------------------------------------------------------------------------------------
for n in range(100,199):
	f=int(n/2+1)
	for i in range(2,f):
		c=0
		if n%i==0:
			c+=1
			print(f"{n} sade deyil")
			break

	if c==0:
		print(f"{n} sadedir")

# ------------------------------------------------------------------------------inputla sade eded
n=23
for i in range(2,int(n/2+1)):
	c=0
	if n%i==0:
		c+=1
		print(f"{n} sade deyil")
		break

if c==0:
	print(f"{n} sadedir")


# ---------------------------------------------------------------------------
c=0
n=int(input())

for i in range(2,int(n/2+1)):
	if n%i==0:
		  c+=1

		  if c>0:
		  	print("sadə deyil")
		  	break
if c==0:
	print("sadədir")

# //------------------------------------------------------------------------------

n=int(input())
for i in range(2,int(n/2)+1):
    if (n%i) == 0:
      print("sadə deyil")
      break
    print("sadədir")
    break
    


n=int(input())
for i in range(2,int(n)):
    if (n%i) == 0:
        break
        print("sadə deyil")
      
    print("sadədir")
    break


# //------------------------------------------------------------------------------ SADE EDED

num = int(input())

flag = False

if num > 1:

    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break


if flag:
    print("sadə deyil")
else:
    print("sadədir")



# -------------------------------------Program to check if a number is prime or not------------------------------------

num = 37

# To take input from the user
#num = int(input("Enter a number: "))

# prime numbers are greater than 1
if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           # print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")

# if input number is less than
# or equal to 1, it is not prime
else:
   print(num,"is not a prime number")





# ----------------------------------find first three max of array elements--------------------------------------------

Python program to find N largest
element from given list of integers

Function returns N largest elements
def Nmaxelements(list1, N):

	for i in range(0, N):
		max1 = 0
		
		for j in range(len(list1)):	
			if list1[j] > max1:
				max1 = list1[j];
				
		list1.remove(max1);
		print(max1)
		

# Driver code
list1 = [2, 6, 41, 85, 0, 3, 7, 6, 10]
N = 3

# Calling the function
Nmaxelements(list1, N)








print(input("Write smth"))













for i in range(0,len(a)):
	print(f"i={i} evvelde")
	
	c=0
	for j in range(0,len(a)):
		if a[i]>=a[j]:
			c=c+1
			if c==len(a):
				m=a[i]
				print(m)
				print("okocekkf")
				a.remove(m)
				i=i-10
				print(f"i={i} sonda")











m=a[0]
a.remove(m)
print(a)



a=1
b=a
a="pyt"
b=2.3
a=-9.0
print(a)





# -----------------------Python program for implementation of Bubble Sort


def bubbleSort(arr):
	n = len(arr)

	# Traverse through all array elements
	for i in range(n):

		# Last i elements are already in place
		for j in range(0, n-i-1):

			# traverse the array from 0 to n-i-1
			# Swap if the element found is greater
			# than the next element
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]


# Driver code to test above

arr = [ 10, 7, 8, 9, 1, 5]

bubbleSort(arr)

print("Sorted array is:")
for i in range(len(arr)):
	print("%d" % arr[i], end=" ")






# ------------------------------------Python3 implementation of QuickSort--------------


# Function to find the partition position
def partition(array, low, high):

	# Choose the rightmost element as pivot
	pivot = array[high]

	# Pointer for greater element
	i = low - 1

	# Traverse through all elements
	# compare each element with pivot
	for j in range(low, high):
		if array[j] <= pivot:
			# If element smaller than pivot is found
			# swap it with the greater element pointed by i
			i = i + 1

			# Swapping element at i with element at j
			(array[i], array[j]) = (array[j], array[i])

	# Swap the pivot element with the greater element specified by i
	(array[i + 1], array[high]) = (array[high], array[i + 1])

	# Return the position from where partition is done
	return i + 1

# Function to perform quicksort
def quick_sort(array, low, high):
	if low < high:

		# Find pivot element such that
		# element smaller than pivot are on the left
		# element greater than pivot are on the right
		pi = partition(array, low, high)

		# Recursive call on the left of pivot
		quick_sort(array, low, pi - 1)

		# Recursive call on the right of pivot
		quick_sort(array, pi + 1, high)


		
# Driver code
array = [ 10, 7, 8, 9, 1, 5]
quick_sort(array, 0, len(array) - 1)

print(f'Sorted array: {array}')











# --------------------------------------------Insertion sort in Python-------------------------------------------


def insertionSort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        
        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].        
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        # Place key at after the element just smaller than it.
        array[j + 1] = key


data = [9, 5, 1, 4, 3]
insertionSort(data)
print('Sorted Array in Ascending Order:')
print(data)





# --------------------------------------------Exercises--------------------------------------------------------

def printDistinct(arr, n):
 
    # Pick all elements one by one
    for i in range(0, n):
 
        # Check if the picked element
        # is already printed
        d = 0
        for j in range(0, i):
            if (arr[i] == arr[j]):
                d = 1
                break
 
        # If not printed earlier,
        # then print it
        if (d == 0):
            print(arr[i])
     
# Driver program to test above function
arr = [6, 10, 5, 4, 9, 120, 4, 6, 10]
n = len(arr)
printDistinct(arr, n)



# ------------------------------------------------------------------------------Ceaser cipher
def encrypt(text,s):
    result = "" 
   # transverse the plain text
    for i in range(len(text)):
      char = text[i]
      # Encrypt uppercase characters in plain text
      
      if (char.isupper()):
         result += chr((ord(char) + s-65) % 26 + 65)
      # Encrypt lowercase characters in plain text
      else:
         result += chr((ord(char) + s - 97) % 26 + 97)
    return result
#check the above function
text = "CEASER CIPHER DEMO"
s = 4

print("Plain Text : " + text)
print("Shift pattern : " + str(s))
print("Cipher: " + encrypt(text,s))



LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
message = 'B'
for key in range(3):
    translated = ''
    for symbol in message:
          if symbol in LETTERS:
             num = LETTERS.find(symbol)
             num = num - key
             if num < 0:
                num = num + len(LETTERS)
             translated = translated + LETTERS[num]
          else:
             translated = translated + symbol

print('Hacking key #%s: %s' % (key, translated))




# ---------------------------------------repeated elements within k distance from each other

Python3 program to Check if a given array contains duplicate
elements within k distance from each other
def checkDuplicatesWithinK(arr,  n,  k):
 
    # traversing the input array
    for i in range(n):
        j = i + 1
        range_ = k
         
        # searching in next k-1 elements if its duplicate
        # is present or not
        while (range_ > 0 and j < n):
            if (arr[i] == arr[j]):
                return True
            j += 1
            range_ -= 1
 
    return False
 
 
# Driver method to test above method
 
arr = [10, 5, 3, 4, 7, 3, 5, 6]
n = len(arr)
if (checkDuplicatesWithinK(arr, n, 2) == True):
    print("Yes")
else:
    print("No")

# ------------------------------------------------------------------------------