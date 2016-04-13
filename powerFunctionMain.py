# float_input function -------------------------------------------------------------------

def float_input( question ):

	try:	
	
		baseNumber = float( raw_input( question ) ) # terminating case
		
		return baseNumber 
		
	except ValueError: # if input is not a real number
		
		float_input( "\nThats not a valid input, try again: " ) # recursive call
	
# int_input function -----------------------------------------------------------------------

def int_input( question ):
	
	try:
	
		exponent = int( raw_input( "\nEnter the integer exponent: " ) ) # terminating case
		
		return exponent
		
	except ValueError: # if input is not a positive integer
	
		int_input( "\nThats not a valid input, try again: " ) # recursive call

# Main Program ---------------------------------------------------------------------------

import powerFunctionFunction # import file so I can call the function in it

baseNumber = float_input( "\nEnter the base number: " ) # argument is the string you want function to ask

exponent = int_input( "\nEnter the a positive integer exponent number: " ) # --

print ( "\n" + str( powerFunctionFunction.power_function( baseNumber, exponent ) ) + "\n" ) # prints answer as a formatted string