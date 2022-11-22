from example_app.code import do_some_math, do_some_different_math


def test_math():
    assert do_some_math(10, 2) == 8


def test_different_math():
    assert do_some_different_math(2) == 4
