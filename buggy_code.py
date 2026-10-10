
def divide(a, b):
    if b == 0:
        raise ValueError("The divisor cannot be zero")
    return a / b


print(divide(10, 2))
