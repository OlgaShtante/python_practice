class MyComparable:
    def __init__(self, obj):
        self.obj = obj

    def __gt__(self, other):
        return self.compare(other, lambda x, y: x > y)

    def __ge__(self, other):
        return self.compare(other, lambda x, y: x >= y)

    def __lt__(self, other):
        return self.compare(other, lambda x, y: x < y)

    def __le__(self, other):
        return self.compare(other, lambda x, y: x <= y)

    def compare(self, other, operator):
        if isinstance(self.obj, str) and isinstance(other.obj, str):
            return operator(len(self.obj), len(other.obj))
        elif isinstance(self.obj, int) and isinstance(other.obj, int):
            return operator(len(str(self.obj)), len(str(other.obj)))
        elif isinstance(self.obj, list) and isinstance(other.obj, list):
            return operator(len(self.obj), len(other.obj))
        elif isinstance(self.obj, dict) and isinstance(other.obj, dict):
            self_sum = sum(self.obj.keys()) + sum(self.obj.values())
            other_sum = sum(other.obj.keys()) + sum(other.obj.values())
            return operator(self_sum, other_sum)
        else:
            raise TypeError("Unsupported comparison between different types")


if __name__ == "__main__":
    str1 = MyComparable("String-1")
    str2 = MyComparable("String2")
    comparison = str1 > str2
    print(comparison)

    int1 = MyComparable(0)
    int2 = MyComparable(-5)
    comparison = int1 < int2
    print(comparison)

    list1 = MyComparable([0, 1, 2])
    list2 = MyComparable([3, 4, 5, 6])
    comparison = list1 <= list2
    print(comparison)

    dict1 = MyComparable({1: 2, 2: 4})
    dict2 = MyComparable({1: 1, 2: 2})
    comparison = dict1 >= dict2
    print(comparison)