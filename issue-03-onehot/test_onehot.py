from one_hot_encoder import fit_transform
import unittest


class TestOneHot(unittest.TestCase):
    '''Class for testing function fit_transform from one_hot_encoder.py'''

    def test_can_transform(self):
        '''Can onehot transform list of data correctly?'''
        cities = ['Moscow', 'Ufa', 'Ufa', 'Moscow', 'London']
        expected = [
            ('Moscow', [0, 0, 1]),
            ('Ufa', [0, 1, 0]),
            ('Ufa', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0])
        ]
        input = fit_transform(cities)
        self.assertEqual(input, expected)

    def test_can_detect_wrong_answer(self):
        '''Can onehot detect a wrong answer?'''
        cities = ['Moscow', 'Ufa', 'Ufa', 'Moscow', 'London', 'Paris']
        _ = [
            ('Moscow', [0, 0, 1]),
            ('Ufa', [0, 1, 0]),
            ('Ufa', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0])
        ]
        input = fit_transform(cities)
        self.assertNotIn(('Moscow', [1, 0, 0]), input)

    def test_can_detect_noniterable_object(self):
        '''Can onehot detect noniterable object?'''
        number = 42
        with self.assertRaises(TypeError):
            fit_transform(number)

    def test_can_transform_one_object(self):
        '''Can onehot transform list of one component?'''
        cities = ['Moscow']
        expected = [
            ('Moscow', [1]),
        ]
        input = fit_transform(cities)
        self.assertEqual(input, expected)

    def test_cant_work_without_arguments(self):
        '''Can onehot work without argument?'''
        with self.assertRaises(TypeError):
            fit_transform()
