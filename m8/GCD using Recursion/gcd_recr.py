'''Exercise: GCDRecr'''
# This function takes in two numbers and returns one number.
def gcd_recur(a_v, b_v):
    '''
    a, b: positive integers
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    r_v = a_v%b_v
    if r_v == 0:
        return a_v
    return gcd_recur(r_v, a_v)
def main():
    """func def"""
    data = input()
    data = data.split()
    print(gcd_recur(max(int(data[0]), int(data[1])), min(int(data[0]), int(data[1]))))
if __name__ == "__main__":
    main()
    