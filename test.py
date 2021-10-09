import pandas as pd
import logging

# test github

def test_1(a: int, b: int):
    """[summary]

    Args:
        a (int): [description]
        b (int): [description]

    Returns:
        [type]: [description]
    """
    logging.warning(
        f"This is info"
        + f"from {a} to {b}"
    )
    return 1

c = test_1(1, 2)
print(c)
logging.info("xxxx")