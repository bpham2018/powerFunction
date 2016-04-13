import powerFunctionFunction # import file so I can call the function in it

print( "\nTest case with 5 to the power of 0: " + str( powerFunctionFunction.power_function( 5, 0 ) ) ) # exponent of 0 edge

print( "\nTest case with 0 to the power 5: " +  str( powerFunctionFunction.power_function( 0, 5 ) ) )# base of 0 edge

print( "\nTest case with 3.3 to the power to the power of 3: " + str( powerFunctionFunction.power_function( 3.3, 3 ) ) )# non integer edge

print( "\nTest case with -5 to the power of 2: " +  str( powerFunctionFunction.power_function( -5, 2 ) ) )# negative base with even exponent edge

print( "\nTest case with -4 to the power of 3: " + str( powerFunctionFunction.power_function( -4, 3 ) ) + "\n" )# negative base with odd exponent edge