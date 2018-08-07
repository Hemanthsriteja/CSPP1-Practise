''' Exercise: Is In
# Write a Python function, isIn(char, aStr), that takes in two arguments a character and String and returns the isIn(char, aStr) which retuns a boolean value.
This function takes in two arguments character and String and returns one boolean value.'''

def is_in(char_v, a_str):
    '''
    char: a single character
    aStr: an alphabetized string
    returns: True if char is in aStr; False otherwise
    '''
    if len(a_str)==0:
        return False
    elif a_str[int(len(a_str)/2)]== char_v:
        return True
    elif char_v>a_str[int(len(a_str)/2)]:
        return is_in(char_v, a_str[int(len(a_str)/2):])
    elif char_v < a_str[int(len(a_str)/2)]:
        return is_in(char_v, a_str[0:int(len(a_str)/2)])
def main():
    data = input()
    data = data.split()
    print(is_in((data[0][0]), data[1]))


if __name__ == "__main__":
   main()