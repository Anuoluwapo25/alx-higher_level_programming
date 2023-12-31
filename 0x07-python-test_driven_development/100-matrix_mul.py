#!/usr/bin/python3
"""
Module defines a function that multiplies 2 matrices
"""

def matrix_mul(m_a, m_b):
    """
    Multiply two matrices.

    Args:
    - m_a: Matrix A (list of lists of integers or floats)
    - m_b: Matrix B (list of lists of integers or floats)

    Returns:
    - The result of the matrix multiplication (list of lists)
    """

    # Validate m_a
    if not isinstance(m_a, list) or not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if any(not row or not all(isinstance(elem, (int, float)) for elem in row) for row in m_a):
        raise TypeError("m_a should contain only integers or floats")
    if len(set(len(row) for row in m_a)) != 1:
        raise TypeError("each row of m_a must be of the same size")

    # Validate m_b
    if not isinstance(m_b, list) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if any(not row or not all(isinstance(elem, (int, float)) for elem in row) for row in m_b):
        raise TypeError("m_b should contain only integers or floats")
    if len(set(len(row) for row in m_b)) != 1:
        raise TypeError("each row of m_b must be of the same size")

    # Validate non-empty matrices
    if not m_a or not m_a[0]:
        raise ValueError("m_a can't be empty")
    if not m_b or not m_b[0]:
        raise ValueError("m_b can't be empty")

    # Validate matrices for multiplication
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    result = []
    for i in range(len(m_a)):
        row_result = []
        for j in range(len(m_b[0])):
            dot_product = sum(m_a[i][k] * m_b[k][j] for k in range(len(m_b)))
            row_result.append(dot_product)
        result.append(row_result)

    return result

