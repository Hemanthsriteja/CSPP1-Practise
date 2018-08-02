
#assume s is a string of lower case characters.
#number of vowels: 5
"""vowels"""
def main():
    """hgfhtuyy"""
    s_v = input("Enter the string:")
    print(s_v)
    count_v = 0
    for char in s_v:
        if char in 'AEIOUaeiou':
            count_v = count_v + 1
    print(str(count_v))
if __name__ == "__main__":
    main()
