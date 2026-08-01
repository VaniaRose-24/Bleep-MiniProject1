def get_int(message):

    while True:

        try:
            return int(input(message))

        except ValueError:
            print("Invalid Input")


def get_string(message):

    while True:

        value = input(message).strip()

        if value:
            return value

        print("Cannot be empty.")