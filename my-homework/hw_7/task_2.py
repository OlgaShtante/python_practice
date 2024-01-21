def is_tuple(value):
    if not isinstance(value, tuple):
        print(f"Input value {value} is not a tuple. Value type is {type(value)}")
        return False
    return True

def is_value_multipliable(tuple):
    for value in tuple:
        if isinstance(value, dict):
            return False
        if isinstance(value, set):
            return False
        if value is None:
            return False
    return True

def multiply_tuples(tuple1, tuple2):
    if is_tuple(tuple1) and is_tuple(tuple2):

        if is_value_multipliable(tuple1) and is_value_multipliable(tuple2):

            if len(tuple1) != len(tuple2):
                print("Tuples must be equal length.")
                return None

            result_tuple = ()
            index_error = []

            for i in range(len(tuple1)):
                if isinstance(tuple1[i], int) or isinstance(tuple2[i], int):
                    result_tuple += (tuple1[i] * tuple2[i],)
                else:
                    index_error +=[i]
                    result_tuple += (None,)
            if len(index_error)>0:
                print("The 'None' value  is added to the result tuple if the pair of values does not include an integer")

            return result_tuple

def test(tuple1, tuple2, exp_res):
    act_res = multiply_tuples(tuple1, tuple2)
    print(f"Test: Multiplication of {tuple1} and {tuple2} returns {act_res}")
    assert act_res == exp_res, f"Error: actual result: {act_res} does not match expected result: {exp_res}"

if __name__ == "__main__": #to avoid test execution when import function

    # only int
    tuple1=(1, 2, 3)
    tuple2=(4, 5, 6)
    exp_res=(4, 10, 18)
    test(tuple1, tuple2, exp_res)

    # other that can be multiplied if one int is presented
    tuple1=(0.7, '*', [1,2], True, (7,), False)
    tuple2=(10, 3, 2, 10, 2, 99 )
    exp_res=(7.0, '***', [1, 2, 1, 2], 10,(7, 7), 0)
    test(tuple1, tuple2, exp_res)

    #not tuple
    tuple1=[1,2,3]
    tuple2=(1,2,3)
    exp_res=None
    test(tuple1, tuple2, exp_res)

    #diff lenth
    tuple1=(0,3)
    tuple2=(1,2,3)
    test(tuple1, tuple2, exp_res)

    #tuple with set
    tuple1=({1, 2}, 4, 5)
    tuple2=(1,2,3)
    test(tuple1, tuple2, exp_res)

    #tuple with dict
    tuple1=(0, {"id":1}, 2)
    test(tuple1, tuple2, exp_res)

    #tuple with None
    tuple1=(1, 2, None)
    test(tuple1, tuple2, exp_res)