# push new value to the list
# input: the list holding the values (size is always 2), the new value to push in
# output: the new list
def swap(prev, total):
    prev[0] = prev[1]
    prev[1] = total
    return prev

# create a Fibonacci list
# input: number of values to generate
# output: the list
def get_series(cnt):
    if cnt < 2:
        raise ValueError("length should be greater than 2")
    # Initialize variables
    previous = [0, 1]
    # Store initial 2 values
    result = [previous[0], previous[1]]
 
    for cnt in range(cnt -2):
        sum = previous[0] + previous[1]
        result.append(sum)
        previous = swap(previous, sum)
    return result
