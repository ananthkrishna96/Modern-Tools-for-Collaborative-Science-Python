import unittest
import numpy as np
import matplotlib.pyplot as plt
from promnist import dist_mat, d_infty, d_one, d_two

class TestDistanceMetrics(unittest.TestCase):

    def setUp(self):
        # Create sample data for testing
        np.random.seed(42)
        self.x_train = np.random.rand(100, 10)
        self.N = len(self.x_train)

    def test_d_infty(self):
        # Test d_infty function
        a = np.random.rand(10)
        b = np.random.rand(10)
        expected_result = np.max(np.abs(b - a))
        self.assertEqual(d_infty(a, b), expected_result)

    def test_d_one(self):
        # Test d_one function
        a = np.random.rand(10)
        b = np.random.rand(10)
        expected_result = np.sum(np.abs(b - a))
        self.assertEqual(d_one(a, b), expected_result)

    def test_d_two(self):
        # Test d_two function
        a = np.random.rand(10)
        b = np.random.rand(10)
        expected_result = np.sqrt(np.sum(np.square(b - a)))
        self.assertEqual(d_two(a, b), expected_result)

    def test_dist_mat(self):
        # Test dist_mat function
        Dinfty = dist_mat(self.N, d_infty, self.x_train)
        D1 = dist_mat(self.N, d_one, self.x_train)
        D2 = dist_mat(self.N, d_two, self.x_train)

        self.assertEqual(Dinfty.shape, (self.N, self.N))
        self.assertEqual(D1.shape, (self.N, self.N))
        self.assertEqual(D2.shape, (self.N, self.N))


if __name__ == '__main__':
    unittest.main()
