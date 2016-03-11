# Author: Bao Pham
# Date: 3/10/16

def power( base, exponent ): # function will take two variables
	
	if exponent == 0: # any number to the power of 0 is 1
	
		product = 1
	
	if exponent == 1: # any number to the power of 1 stays the same
	
		product = base 
		
	if exponent >= 2: 
	
		loopNumber = 2 # starts at two because exponent starts at 2 too
	
		constantBase = base # need a base to stay the same so can keep multiplying by it
	
		while loopNumber <= exponent: # loop that multiplies by the base
		
			base = base * constantBase # again base is changed by constantBase is not
		
			loopNumber += 1 # add to loopNumber so it will eventually become greater than the exponent, 
			# terminating the loop
		
		product =  base
	
	return product # returns product with an arrow
	
#---------------------------------------------------------------------------------------------------

x = float(raw_input( "Enter the base number: " )) # getting user to enter a base number

y = int(raw_input( "Enter the exponent: " )) # getting user to enter an exponent

print( power( x, y ) ) # prints the product

