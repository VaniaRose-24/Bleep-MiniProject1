class Member:

    def __init__(self, member_id, name):
        self.__member_id = member_id
        self.__name = name

    def get_id(self):
        return self.__member_id

    def get_name(self):
        return self.__name