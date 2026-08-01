def get_int(message):

    while True:

        try:
            return int(input(message))

        except ValueError:
            print("Invalid Integer")


def get_string(message):

    while True:

        value = input(message).strip()

        if value:
            return value

        print("Input cannot be empty.")