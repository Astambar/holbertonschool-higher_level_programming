#!/usr/bin/python3


def pascal_triangle(n):

    init_number = [[1]]
    while len(init_number) != n:
        next_number = init_number[-1]
        store_number = [1]
        for i in range(len(next_number) - 1):
            store_number.append(next_number[i] + next_number[i + 1])
        store_number.append(1)
        init_number.append(store_number)
    return init_number

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
