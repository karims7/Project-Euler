def sum_of_three_five_multiples(number):

    """
    Calculate the sum of all natural numbers below a given limit that are multiples of 3 or 5.

    Args:
        number (int): The upper limit (exclusive) to find multiples of 3 or 5.

    Returns:
        int: The sum of all multiples of 3 or 5 below the given limit. For 1000, the output is 233168. 
    """

    sum = 0

    for num in range (1, number, 1):
        if num % 3 == 0 or num % 5 == 0:
            sum += num
    return sum


result = sum_of_three_five_multiples(1000)

print(result)

