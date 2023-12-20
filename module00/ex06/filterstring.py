from ft_filter import ft_filter
import sys


def main():
    text = sys.argv[1]
    num = int(sys.argv[2])
    text = text.split()
    print(ft_filter(lambda a: len(a) > num, text))


if __name__ == "__main__":
    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        assert sys.argv[2].isdigit(), "the arguments are bad"
        main()
    except AssertionError as msg:
        print(msg)
