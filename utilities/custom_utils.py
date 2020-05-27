from math import ceil

def chunk(size, _iter):
  """ split an iterable into chunks of the given size """
  _num_groups = range(int(ceil(len(_iter)/float(size))))
  return (_iter[n*size:(n+1)*size] for n in _num_groups)

def P(obj, key=None):
  """
  List the public properties of an object, optionally
  filtered by a `key` function
  """
  props = [p for p in dir(obj) if p[0] is not '_']
  if key is not None:
    props = [p for p in props if key(p)]
  return props

def PT(obj, key=None):
  """
  List an object's public properties in a 4-col table,
  optionally filtered by a `key` function
  """
  _p = P(obj, key=key)
  if filter is not None:
    _max_w = max(len(p) for p in _p)

  print('\n'.join(''.join(n.ljust(ceil((_max_w/4 + 2)*4)) for n in c) for c in chunk(4, P(obj))))