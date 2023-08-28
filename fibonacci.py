def swap(prev, total):
    prev[0] = prev[1]
    prev[1] = total
    return prev, total

def main():
    # Initialize variables
    previous = [0, 1]
 
    # Get user inputs
    end = int(input("Show a Fibonacci series up to:"))
    # Print initial 2 values
    print ("{} {} ".format(previous[0], previous[1]), end="")
    for cnt in range(end + 1):
        sum = previous[0] + previous[1]
        print("{} ".format(sum), end="")
        previous, sum = swap(previous, sum)

if __name__ == '__main__':
    # execute only if run as the entry point into the program
    main()