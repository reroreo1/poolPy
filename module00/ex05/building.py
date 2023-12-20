import sys
import string


def main():
    """real autonomous program, with a main, which takes
a single string argument and displays the sums
of its upper-case characters, lower-case
characters, punctuation characters, digits and spaces.
• If None or nothing is provided, the user
is prompted to provide a string.
• If more than one argument is provided to
the program, print an AssertionError."""
    text = ""
    if len(sys.argv) == 1:
        while (1):
            try:
                text = input("What is the text to count ?\n")
                break
            except EOFError:   # Catch the Ctrl-D
                print("bad input try entering a valid text")
    else:
        text = sys.argv[1]
    print("the text contains", len(text), "characters:")
    print(sum(1 for c in text if c.isupper()), "upper letters")
    print(sum(1 for c in text if c.islower()), "lower letters")
    print(sum(1 for c in text if c in string.punctuation), "punctuation marks")
    print(sum(1 for c in text if c.isspace()), "spaces")
    print(sum(1 for c in text if c.isdigit()), "digits")


if __name__ == "__main__":
    assert len(sys.argv) <= 2, "more than one argument is provided"
    main()
