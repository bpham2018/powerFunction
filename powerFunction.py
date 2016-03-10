def power( x, y ):
	
	base = int( x )
	
	exponent = int( y )
	
	if exponent == 0:
	
		product = 1
	
	if exponent == 1:
	
		product = int( base )
		
	if exponent > 1:
	
		loopNumber = 2
	
		constantBase = int( base )
	
		while loopNumber <= exponent:
		
			base = base * constantBase
		
			loopNumber += 1
		
		product = int( base )
	
	return "->" + str(product)
	
#---------------------------------------------------------------------------------------------------

x = raw_input( "Enter the base number: " )

y = raw_input( "Enter the exponent: " )

print( power( x, y ) )

