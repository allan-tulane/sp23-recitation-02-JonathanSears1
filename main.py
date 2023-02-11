"""
CMPS 2200  Recitation 2
"""

### the only imports needed are here
import tabulate
import time
import math
###

def simple_work_calc(n, a, b):
	"""Compute the value of the recurrence $W(n) = aW(n/b) + n

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor

	Returns: the value of W(n).
	"""
	"""base case is when n/b == 1"""
	if n <= 1:
		return n
	else:
		return a * simple_work_calc(n//b, a, b) + n

def test_simple_work():
	""" done. """
	assert simple_work_calc(10, 2, 2) == 36
	assert simple_work_calc(20, 3, 2) == 230
	assert simple_work_calc(30, 4, 2) == 650

def work_calc(n, a, b, f):
	"""Compute the value of the recurrence $W(n) = aW(n/b) + f(n)

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor
	f......a function that takes an integer and returns 
           the work done at each node 

	Returns: the value of W(n).
	"""
	# TODO
	if n <= 1:
		return n
	else:
		return a*work_calc(n//b,a, b, f )+ f(n)

def span_calc(n, a, b, f):
	"""Compute the span associated with the recurrence $W(n) = aW(n/b) + f(n)

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor
	f......a function that takes an integer and returns 
           the work done at each node 

	Returns: the value of W(n).
	"""
	# TODO
	if n <= 1:
		return n
	else:
		return span_calc(n//b,a,b,f)+f(n)

print(work_calc(1000, 2, 2,lambda n: 1))
print(work_calc(1000, 2, 2, lambda n: math.log(n)))
print(work_calc(1000, 2, 2, lambda n: n))
def test_work():
	""" done. """
	assert work_calc(10, 2, 2,lambda n: 1) == 15
	assert work_calc(20, 1, 2, lambda n: n*n) == 530
	assert work_calc(30, 4, 2, lambda n: n) == 650

def compare_work(work_fn1, work_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
	"""
	Compare the values of different recurrences for 
	given input sizes.

	Returns:
	A list of tuples of the form
	(n, work_fn1(n), work_fn2(n), ...)
	
	"""
	result = []
	for n in sizes:
		# compute W(n) using current a, b, f
		result.append((
			n,
			work_fn1(n),
			work_fn2(n)
			))
	return result

def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
							headers=['n', 'W_1', 'W_2'],
							floatfmt=".3f",
							tablefmt="github"))

def test_compare_work():
 	# curry work_calc to create multiple work
	# functions that can be passed to compare_work
    
 	# create work_fn1
 	# create work_fn2
	def work_fn1(n):
	 return work_calc(n, 8, 2, lambda n : n^4)
	#log_2(8) = 3
	def work_fn2(n):
		return work_calc(n, 8, 2, lambda n : n^2)
	res = compare_work(work_fn1, work_fn2)
	print_results(res)
	return
def test_compare_span():
	print(span_calc(1000, 2, 2,lambda n: 1))
	print(span_calc(10000, 2, 2,lambda n: 1))
	print(span_calc(100000, 2, 2,lambda n: 1))
	print(span_calc(1000, 2, 2, lambda n: math.log(n)))
	print(span_calc(10000, 2, 2, lambda n: math.log(n)))
	print(span_calc(100000, 2, 2, lambda n: math.log(n)))
	print(span_calc(1000, 2, 2, lambda n: n))
	print(span_calc(10000, 2, 2, lambda n: n))
	print(span_calc(100000, 2, 2, lambda n: n))

	return

test_compare_span()