def get_int(message):

    while True:

        try:
            return int(input(message))

        except ValueError:
            print("Invalid Integer")