def range_map(val, in_min, in_max, out_min, out_max, rnd=0):
	"""
	Takes a value from one range of possible values and maps
        it to a value in the second range of possible values
        
        Example 1: range_map(555, 0, 1023, 0, 100)
        This will output a value of 54.252199413489734
        
        Example 2: range_map(55, 0, 1023, 0, 100, 2)
        This will output a value of 54.25
        
        Parameters:
            x: the value to map to a new range
            in_min: the minumum value of the original range
            in_max: the maximum value of the original range
            out_min: the minimum value of the output range
            out_max: the maximum value of the output range
            rnd: the number of decimal places to round the result to,
                if omitted, defaults to 0
	"""
	range_val = (val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

	if(rnd == 0):
		return range_val
	else:
		return round(range_val, rnd)

# I don't remember where I found these functions, need to find the author...
from math import ceil

def iter_chunk(size, _iter):
    """ split an iterable into chunks of the given size """
    _num_groups = range(int(ceil(len(_iter)/float(size))))
    
    return (_iter[n*size:(n+1)*size] for n in _num_groups)

def public_properties(obj, key=None):
    """
    List the public properties of an object, optionally filtered by a `key` function
    """
    props = [p for p in dir(obj) if p[0] is not '_']
    
    if key is not None:
        props = [p for p in props if key(p)]

    return props

def public_properties_table(obj, key=None):
    """
    List an object's public properties in a 4-col table, optionally filtered by a `key` function
    """
    _p = P(obj, key=key)
    
    if filter is not None:
        _max_w = max(len(p) for p in _p)

    print('\n'.join(''.join(n.ljust(ceil((_max_w/4 + 2)*4)) for n in c) for c in chunk(4, P(obj))))
