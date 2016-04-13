def power_function( baseNumber, exponent ): # 2 required arguments: base number and exponent
	
	if exponent == 0:
	
		return 1 # Terminating Case
		
	else:
	
		return baseNumber * power_function( baseNumber, exponent - 1 ) # will recur until y hits 0