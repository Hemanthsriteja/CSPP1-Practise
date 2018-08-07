''' Exercise: GCDIter
# This function takes in two numbers and returns one number.'''
def gcd_iter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    for i in range(min(a,b),0,-1):
    	if a%i == b%i == 0:
    		return i

def main():
    data = input()
    data = data.split()
    print(gcd_iter(int(data[0]), int(data[1]))) 

if __name__ == "__main__":
    main()