def power( x, y ): # function will take two variables
	
	base = int( x )
	
	exponent = int( y )
	
	if exponent == 0: # any number to the power of 0 is 1
	
		product = 1
	
	if exponent == 1: # any number to the power of 1 stays the same
	
		product = int( base )
		
	if exponent >= 2: 
	
		loopNumber = 2 # starts at two because exponent starts at 2 too
	
		constantBase = int( base ) # need a base to stay the same so can keep multiplying by it
	
		while loopNumber <= exponent: # loop that keeps multiply the base
		
			base = base * constantBase # again base is changed by constantBase is not
		
			loopNumber += 1 # add to loopNumber so it will eventually become greater than the exponent, 
			# terminating the loop
		
		product = int( base )
	
	return "->" + str(product) # returns product with an arrow
	
#---------------------------------------------------------------------------------------------------

x = raw_input( "Enter the base number: " ) # getting user to enter a base number

y = raw_input( "Enter the exponent: " ) # getting user to enter an exponent

print( power( x, y ) ) # prints the product

