# Exercise: PowerIter
''' Write a Python function, iterPower(base, exp),finding base power exp'''


def iter_power(base, exp):
    '''
    base: int or float.
    exp: int >= 0
    returns: int or float, base^exp
    '''
    f_v = 1
    while exp != 0:
        f_v = f_v*base
        exp = exp-1
    return f_v
def main():
    """defining main function"""

    data = input()
    data = data.split()
    print(iter_power(float(data[0]), int(data[1])))

if __name__ == "__main__":
    main()
