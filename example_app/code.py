"""An example project module"""


def do_some_math(first: float, second: float) -> float:
    """This function does some math.

    Args:
        first (float): First argument.
        second (float): Second argument.

    Returns:
        float: some math operation result.
    """
    return (first * second) - (first + second)


def do_some_different_math(arg: float) -> float:
    """This function does some different math.

    Args:
        arg (float): Some number.

    Returns:
        float: Some other number.
    """
    return arg**arg


def uncovered_function(something: None) -> None:
    """This function does nothing.

    Args:
        something (None): literally nothing.
    """
    pass
