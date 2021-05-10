#QUOTATIONS IN PYTHON
word = 'word'
sentence = "This is a sentence."
paragraph = """This is a paragraph. It is
made up of multiple lines and sentences."""

#Comments in Python
#Assigning Values to Variables

counter = 100 # An integer assignment
miles = 1000.0 # A floating point
name = "ARTIFICIAL INTELLEGENCE" # A string
print (counter)
print (miles); print (name)

#Data Types
#Python Numbers

var1 = 1
var2 = 10

#Python Strings
str = 'Hello World!'
print (str) # Prints complete string
print (str[0]) # Prints first character of the string
print (str[2:5]) # Prints characters starting from 3rd to 5th
print (str[2:]) # Prints string starting from 3rd character
print (str * 2) # Prints string two times
print (str + "TEST") # Prints concatenated string

#Python Lists
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7 ]
print ("list1[0]: ", list1[0])
print ("list2[1:5]: ", list2[1:5])

#Updating Lists
list = ['physics', 'chemistry', 1997, 2000]
print ("Value available at index 2 : ", list[2])
list[2] = 2001
print ("New value available at index 2 : ", list[2])

#Delete List Elements
list = ['physics', 'chemistry', 1997, 2000]
print (list)
del list[2]
print ("After deleting value at index 2 : ", list)

#Python Tuples
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')
print (tuple) # Prints complete tuple
print (tuple[0]) # Prints first element of the tuple
print (tuple[1:3]) # Prints elements starting from 2nd till 3rd
print (tuple[2:]) # Prints elements starting from 3rd element
print (tinytuple * 2) # Prints tuple two times
print (tuple + tinytuple) # Prints concatenated tuple

#Python Dictionary
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
print (dict['one']) # Prints value for 'one' key
print (dict[2]) # Prints value for 2 key
print (tinydict) # Prints complete dictionary
print (tinydict.keys()) # Prints all the keys
print (tinydict.values()) # Prints all the values

# Decision Making
#IF Statement
if var1:
 print ("1 - Got a true expression value")
 print (var1)
var2 = 0
if var2:
 print ("2 - Got a true expression value")
 print (var2)
print ("Good bye!")

#.ELSE Statements
amount = int(input("Enter amount: "))
if amount < 1000:
    discount = amount * 0.05
    print("Discount", discount)
else:
    discount = amount * 0.10
    print("Discount", discount)

print("Net payable:", amount - discount)

#EIF STATEMENT
if amount < 1000:
    discount = amount * 0.05
    print("Discount", discount)
elif amount < 5000:
    discount = amount * 0.10
    print("Discount", discount)
else:
    discount = amount * 0.15
print("Discount", discount)

print("Net payable:", amount - discount)

#Loops
#While Loop Statements
count = 0
while (count < 9):
 print ('The count is:', count)
 count = count + 1
print ("Good bye!")


#For Loop Statements
for letter in 'Python': # traversal of a string sequence
 print ('Current Letter :', letter)
print()
fruits = ['banana', 'apple', 'mango']
for fruit in fruits: # traversal of List sequence
 print ('Current fruit :', fruit)
print ("Good bye!")





