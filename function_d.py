def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """
    print("hi hi")
    numbers.sort(reverse = True)
    return numbers[0]


if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))


