#2.COZUM:
# Each new term #in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.

def compute():
	ans = 0
	x = 1
	y = 2
	while x <= 4000000:
		if x % 2 == 0:
			ans += x
		x, y = y, x + y
	return str(ans)
# x=2* y=3,  ans=2*  (2,3)=(3,5)
# x=3  y=5,  ans=2   (3,5)=(5,8)
# x=5  y=8,  ans=2   (5,8)=(8,13)
# x=8* y=13, ans= 10 (8,13)=(13,21)...

if __name__ == "__main__":
	print(compute())