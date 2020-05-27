###
# Function: range_map(x, in_min, in_max, out_min, out_max, rnd=0)
#
# Takes a value from one range of possible values and maps
# it to a value in the second range of possible values
# 
# Example 1: range_map(555, 0, 1023, 0, 100)
#	This will output a value of 54.252199413489734
#
# Example 2: range_map(55, 0, 1023, 0, 100, 2)
#	This will output a value of 54.25
#
# Parameters:
#	x: the value to map to a new range
#	in_min: the minumum value of the original range
#	in_max: the maximum value of the original range
#	out_min: the minimum value of the output range
#	out_max: the maximum value of the output range
#	rnd: the number of decimal places to round the result to,
#		if omitted, defaults to 0
def range_map(val, in_min, in_max, out_min, out_max, rnd=0):
	range_val = (val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

	if(rnd == 0):
		return range_val
	else:
		return round(range_val, rnd)

