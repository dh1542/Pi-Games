
import math

"""
computes pi using Chudnovsky's theory of complex multiplication
of elliptic curves
https://en.wikipedia.org/wiki/Chudnovsky_algorithm

"""

def chudnovsky(n):

	# set 
	k1 = 545140134
	k2 = 13591409
	pi = 0

	for num in range (n):
		print(num)
		numerator = math.factorial(6 *  num) * (k1 * num + k2)
		denominator = math.factorial(3 * num) * math.factorial(num)**3 * (-262537412640768000)**num
		pi += (numerator / denominator) 
		print(pi)


	return (426880 * math.sqrt(10005)) / pi


"""
computes pi using leibniz pi series

"""
def leibniz(n):

	pi = 0
	for num in range (n):
		print(num)
		numerator = (-1)**num
		denominator = 2 * num + 1
		pi += numerator / denominator
		

	return 4 * pi

