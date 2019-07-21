MAX = 50# Python program to find Excel column name from a  
# given column number 
n=(input())
def printString(n): 

	string = ["\0"] * MAX

	i = 0

	while n > 0: 

		rem = n % 26

		if rem == 0: 
			string[i] = 'Z'
			i += 1
			n = (n / 26) - 1
		else: 
			string[i] = chr((rem - 1) + ord('A')) 
			i += 1
			n = n / 26
	string[i] = '\0'
 
	string = string[::-1] 
	print "".join(string)
printString(n) 
