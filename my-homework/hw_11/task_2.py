class Immutable:
    def __new__(cls, value):
        if isinstance(value, (str, int, list, dict)):
            obj = super().__new__(cls)
            obj._value = value
            return obj
        else:
            raise ValueError("Invalid type for value attribute")

    def get_value(self):
        return self._value

    def __setattr__(self, attr, value):
        raise AttributeError("Cannot set attributes on Immutable objects")

    def __delattr__(self, attr):
        raise AttributeError("Cannot delete attributes on Immutable objects")


if __name__ == "__main__":
    try:
        string = "Hello, World!"
        immutable_str = Immutable(string)
        print(immutable_str.get_value())

        integer = 1
        immutable_int = Immutable(integer)
        print(immutable_int.get_value())

        array = [0,1,2]
        immutable_list = Immutable(array)
        print(immutable_list.get_value())

        dictionary = {"a": 1, "b": 2, "c":3}
        immutable_dict = Immutable(dictionary)
        print(immutable_dict.get_value())

        new_value = "New Value"
        immutable_str.new_attr = new_value
    except AttributeError as error_msg:
        print("Error:", error_msg)




