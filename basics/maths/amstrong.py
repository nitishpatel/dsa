def is_armstrong_number(number):
    original_number = number  # Store the original number
    num_digits = len(str(number))  # Calculate the number of digits

    sum_of_powers = 0
    while number > 0:
        digit = number % 10
        sum_of_powers += digit ** num_digits
        number //= 10

    print(original_number, sum_of_powers)

    return str(sum_of_powers == original_number).lower()


n = int()
print(is_armstrong_number(n))
