#!/usr/bin/python3
"""
This module defines a function
"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """a function that multiplies two matrices
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    
    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")

    
    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")

    
    if not m_a or not m_a[0]:
        raise ValueError("m_a can't be empty")
    
    if not m_b or not m_b[0]:
        raise ValueError("m_b can't be empty")

    
    for row in m_a:
        for el in row:
            if not isinstance(el, (int, float)):
                raise TypeError("m_a should contain only integers "
                                "or floats")

    for row in m_b:
        for el in row:
            if not isinstance(el, (int, float)):
                raise TypeError("m_b should contain only integers "
                                "or floats")
    
    m_a_row_len = len(m_a[0])  
    for row in m_a:
        if len(row) != m_a_row_len:
            raise TypeError("each row of m_a must be of the same size")

    m_b_row_len = len(m_b[0])
    for row in m_b:
        if len(row) != m_b_row_len:
            raise TypeError("each row of m_b must be of the same size")

    return (np.dot(m_a, m_b))
