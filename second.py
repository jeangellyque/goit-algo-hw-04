from random import sample

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or min >= max or quantity > (max - min + 1):
        return []

    numbers_ticket = sample(range(min, max+1), quantity)
    return sorted(numbers_ticket)

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)