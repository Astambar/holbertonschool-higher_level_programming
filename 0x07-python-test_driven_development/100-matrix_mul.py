#!/usr/bin/python3

def matrix_mul(m_a, m_b):
    """_summary_

    Args:
        m_a (_type_): _description_
        m_b (_type_): _description_

    Raises:
        TypeError: _description_
        TypeError: _description_
        TypeError: _description_
        TypeError: _description_
        ValueError: _description_
        ValueError: _description_
        TypeError: _description_
        TypeError: _description_
        TypeError: _description_
        TypeError: _description_
        ValueError: _description_
        ValueError: _description_

    Returns:
        _type_: _description_
    """    
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    for column in m_a:
        if type(column) is not list:
            raise TypeError("m_a must be a list of lists")
    for column in m_b:
        if not isinstance(column, list):
            raise TypeError("m_b must be a list of lists")

    if m_a in [[], [[]]]:
        raise ValueError("m_a can't be empty")
    if m_b in [[], [[]]]:
        raise ValueError("m_b can't be empty")

    for column in m_a:
        for row in column:
            if not isinstance(row, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for column in m_b:
        for row in column:
            if not isinstance(row, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    if not check_line_matrix(m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not check_line_matrix(m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a) != len(m_b) or len(m_a[0]) != len(m_b[0]):
        raise ValueError("m_a and m_b can't be multiplied")

    m_c = new_matrix(m_a, m_b)

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                try:
                    m_c[i][j] += m_a[i][k] * m_b[k][j]
                except Exception:
                    raise ValueError("m_a and m_b can't be multiplied")

    return m_c


def new_matrix(m_a, m_b):
    """_summary_

    Args:
        m_a (_type_): _description_
        m_b (_type_): _description_

    Returns:
        _type_: _description_
    """
    len_row_b = 0
    len_column_a = 0
    len_column_b = 0
    m_c = []

    len_row_a = sum(1 for _ in m_a)

    for row in m_b:
        len_row_b += 1
        len_column_b = sum(1 for _ in row)

    min_row_len = min(len_row_a, len_row_b)
    min_column_len = min(len_column_a, len_column_b)

    for i in range(min_row_len):
        m_c.append([])
        for _ in range(min_column_len):
            m_c[i].append(0)

    return m_c


def check_line_matrix(matrix):
    """_summary_

    Args:
        matrix (_type_): _description_

    Returns:
        _type_: _description_
    """
    lines = len(matrix[0])
    return all(len(line) == lines for line in matrix)
