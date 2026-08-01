def get_int(message):

    while True:

        try:
            return int(input(message))

        except ValueError:

            print("Invalid Integer")


def get_float(message):

    while True:

        try:
            return float(input(message))

        except ValueError:

            print("Invalid Number")