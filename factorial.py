''' CS2420 FACTORIAL EXAMPLE '''

import sys


def factorial(x):   # pylint disable: C0103
    ''' returns !x x must be a positive integer, else ValueError '''
    if not isinstance(x, int):
        raise ValueError("x must be an integer")
    # base case
    if x <= 1:
        return 1

    # recursive case
    return x * factorial(x-1)


def main():
    ''' driver to test factorial() '''
    try:
        print(factorial(int(sys.argv[1])))
    except ValueError as err:
        print ("Oops", err)


if __name__ == "__main__":
    main()
    
'''

 in terminal "python -m pyliint factorial.py"
 to get unit tests to work, click lower left gear > command palette > Python: Configure Tests > unittest < root directory > te
 
'''