from one_hot_encoder import fit_transform
import pytest


def test_can_transform():
    """Can onehot transform list of data correctly?"""
    cities = ['Moscow', 'Ufa', 'Ufa', 'Moscow', 'London']
    expected = [
        ('Moscow', [0, 0, 1]),
        ('Ufa', [0, 1, 0]),
        ('Ufa', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0])
    ]
    input = fit_transform(cities)
    assert input == expected, (
        'onehot cant transform correctly'
    )


def test_can_detect_noniterable_object():
    """Can onehot detect noniterable object?"""
    number = 42
    with pytest.raises(TypeError):
        fit_transform(number)


def test_can_transform_one_object():
    """Can onehot transform list of one component?"""
    cities = ['Moscow']
    expected = [
        ('Moscow', [1]),
    ]
    input = fit_transform(cities)
    assert input == expected, (
        'onehot cant transform correctly one component'
    )


def test_cant_work_without_arguments():
    """Can onehot work without argument?"""
    with pytest.raises(TypeError):
        fit_transform()
