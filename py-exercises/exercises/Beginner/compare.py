"""
Information
-----------
@Copyright by Saeed Gholami 
Email: saeed.ghollami@gmail.com
Github: ostadsgo
Web: ostadsgo.github.io
Last edit: 2023-02-04


Level
-----
* Beginners
intermediate
Advanced


Description
-----------
Compare two integers 
if x is bigger than y return 1
if y is bigger than x return -1
if x and y were equal return 0

Examples
-------
>>> cmp(2, 5)
-1
>>> cmp(5, 2)
1


Requirements
------------
 - If stetement
 - Comparison Operators

Resources
---------
 - https://www.w3schools.com/python/python_conditions.asp
 - https://www.w3schools.com/python/python_operators.asp
"""


def cmp(x, y):
    if x > 0:
        return 1

    elif x < y:
        return -1

    else:
        return 0


# -----------------------------------
if __name__ == "__main__":
    from tests import assert_equals

    # assert_equals(cmp, (0, 0), 0)
    # assert_equals(cmp, (-1, -5), 1)
    # assert_equals(cmp, (2, 3), -1)
    # assert_equals(cmp, (2, 1), 1)

    assert_equals(cmp, (True, False, 30, "Ardabil"), False)
    assert_equals(cmp, (False, False, 30, "Shiraz"), False)
    assert_equals(cmp, (True, True, 27, "Tehran"), True)
