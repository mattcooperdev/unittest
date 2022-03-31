def even_number_of_evens(numbers):
    if isinstance(numbers, list):    
        evens = sum([1 for n in numbers if n % 2 == 0])

        return True if evens and evens % 2 == 0 else False
    else:
        raise TypeError("A list was not passed into the function")

if __name__ == '__main__':
    even_number_of_evens([2, 1, 4])