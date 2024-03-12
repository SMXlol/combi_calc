def factorial(elements):
    fact = 1
    while elements > 1:
        fact *= elements
        elements -= 1
    return fact


def combinations(elements, k):
    res = factorial(len(elements)) / (factorial(k) * factorial(len(elements) - k))
    return int(res)


def combinations_with(elements, k):
    res = factorial(k + len(elements) - 1) / factorial(len(elements) - 1) * factorial(k)
    return int(res)


def permutations(elements):
    return factorial(len(elements))


def permutations_with(elements):
    total_length = sum(elements)
    result = factorial(total_length)
    for element in elements:
        result /= factorial(element)
    return int(result)


def accommodation_with(elements, k):
    return int(len(elements) ** k)


def accommodation(elements, k):
    return int(factorial(len(elements)) / factorial(len(elements) - k))

