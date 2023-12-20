import sys


try:
    assert len(sys.argv) == 2 , "more than one argument is provided"
    assert sys.argv[1].isnumeric() == True , "argument is not an integer"
    num = int(sys.argv[1])
    if (num % 2 == 0):
        print("I'm Even.")
    else:
        print("I'm Odd.")
except AssertionError as msg:
    print(msg)