import contextlib
def safe_print_list(my_list=[], x=0):
    increment = 0
    string = ""
    with contextlib.suppress(IndexError):
        for i in range(x):
            string += f"{my_list[i]}"
            increment += 1

    print(string)
    return increment
