import sys


def main():
    """a function that encrypts text to morse code"""
    NESTED_MORSE = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ',':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-',' ':'/ '}
    text = sys.argv[1].upper()
    try:
        assert all(item in NESTED_MORSE for item in text), "AssertionError: the arguments are bad"
        text = list(map(lambda x: NESTED_MORSE[x], text))
        print(*text)
    except AssertionError as msg: 
        print(msg)

if __name__ == "__main__":
    try:
        assert len(sys.argv) == 2, "AssertionError: the arguments are bad"
        main()
    except AssertionError as msg: 
        print(msg)
