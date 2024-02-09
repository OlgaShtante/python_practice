class Kilograms:
    def __init__(self, value):
        if value < 0:
            raise ValueError("Value cannot be negative")
        if value >= 1000:
            raise ValueError("Value cannot be greater than or equal to 1000 kilograms")
        self.value = value

    def to_pounds(self):
        return Pounds(self.value * 2.20462)

    def increase(self, increment):
        if self.value + increment < 0:
            raise ValueError("Value cannot be negative")
        self.value += increment

    def __add__(self, other):
        if isinstance(other, Kilograms):
            return Kilograms(self.value + other.value)
        elif isinstance(other, Pounds):
            return self.to_pounds() + other
        else:
            raise TypeError("Unsupported type for addition")

    def __sub__(self, other):
        if isinstance(other, Kilograms):
            return Kilograms(self.value - other.value)
        elif isinstance(other, Pounds):
            return self.to_pounds() - other
        else:
            raise TypeError("Unsupported type for subtraction")

    def __repr__(self):
        return f"{self.value} kilograms"

class Pounds:
    def __init__(self, value):
        if value < 0:
            raise ValueError("Value cannot be negative")
        if value >= 14:
            raise ValueError("Value cannot be greater than or equal to 14 pounds")
        self.value = value

    def to_kilograms(self):
        return Kilograms(self.value / 2.20462)

    def increase(self, increment):
        if self.value + increment < 0:
            raise ValueError("Value cannot be negative")
        self.value += increment

    def __add__(self, other):
        if isinstance(other, Pounds):
            return Pounds(self.value + other.value)
        elif isinstance(other, Kilograms):
            return self.to_kilograms() + other
        else:
            raise TypeError("Unsupported type for addition")

    def __sub__(self, other):
        if isinstance(other, Pounds):
            return Pounds(self.value - other.value)
        elif isinstance(other, Kilograms):
            return self.to_kilograms() - other
        else:
            raise TypeError("Unsupported type for subtraction")

    def __repr__(self):
        return f"{self.value} pounds"


if __name__ == "__main__":
    try:
        kg1 = Kilograms(5)
        print(kg1.to_pounds())
    except ValueError as error_msg:
        print("Error:", error_msg)
    try:
        pound1 = Pounds(10)
        print(pound1.to_kilograms())
    except ValueError as error_msg:
        print("Error:", error_msg)