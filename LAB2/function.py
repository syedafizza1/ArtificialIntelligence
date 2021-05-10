# Function definition is here
def printme(str):
 "This prints a passed string into this function"
 print (str)
 return
# Now you can call printme function
printme("This is first call to the user defined function!")
printme("Again second call to the same function")

# Function definition is here
def changeme( mylist ):
 "This changes a passed list into this function"
 print ("Values inside the function before change: ", mylist)
 mylist[2]=50
 print ("Values inside the function after change: ", mylist)
 return
# Now you can call changeme function
mylist = [10,20,30]
changeme( mylist )
print ("Values outside the function: ", mylist)

# Function definition is here
def changeme( mylist ):
 "This changes a passed list into this function"
 mylist = [1,2,3,4] # This would assign new reference in mylist
 print ("Values inside the function: ", mylist)
 return
# Now you can call changeme function
mylist = [10,20,30]
changeme( mylist )
print ("Values outside the function: ", mylist)


#The Return Statement
# Function definition is here
def sum( arg1, arg2 ):
 # Add both the parameters and return them."
 total = arg1 + arg2
 print ("Inside the function : ", total)
 return total
# Now you can call sum function
total = sum( 10, 20 )
print ("Outside the function : ", total )