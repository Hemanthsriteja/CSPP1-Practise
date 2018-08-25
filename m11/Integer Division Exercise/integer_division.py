#Exercise: Integer Division Exercise
#Modify the code for integer_division so that this error does not occur.

def integer_division(x_v, a_v):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the integer division of x divided by a.
    """
    count_v = 0
    while x_v >= a_v:
        count_v += 1
        x_v = x_v - a_v
    return count_v
    

def main():
	"""func"""
    data = input()
    data = data.split()
    print(integer_division(int(data[0]), int(data[1])))


if __name__== "__main__":
    main()