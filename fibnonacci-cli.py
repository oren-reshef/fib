from fibonacci.fibonacci_tools import get_series

def main():
    # Get user inputs
    cnt = int(input("How many items of a Fibonacci series to show? (min 2) "))
    series = get_series(cnt)
    for item in series:
        print("{} ".format(item), end="")


if __name__ == '__main__':
    # execute only if run as the entry point into the program
    main()