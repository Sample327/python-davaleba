def square(number):
    squared =  number * number
    return squared


def shift_and_square(number, offset):
    shifted = number + offset
    return square(shifted)




if __name__ == "__main__":

    print(square(5))

    print(shift_and_square(4,5))