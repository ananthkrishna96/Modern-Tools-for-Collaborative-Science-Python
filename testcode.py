import unittest
import numpy as np
import matplotlib.pyplot as plt
from promnist import dist_mat, d_infty, d_one, d_two

class TestDistanceMetrics(unittest.TestCase):

    def setUp(self):
        np.random.seed(42)
        self.x_train = np.random.rand(100, 10)
        self.N = len(self.x_train)

    def test_dist_mat(self):
        Dinfty = dist_mat(self.N, d_infty, self.x_train)
        D1 = dist_mat(self.N, d_one, self.x_train)
        D2 = dist_mat(self.N, d_two, self.x_train)

        self.assertEqual(Dinfty.shape, (self.N, self.N))
        self.assertEqual(D1.shape, (self.N, self.N))
        self.assertEqual(D2.shape, (self.N, self.N))
        
        print("Dinfty:",Dinfty[:5, :5])
        print("D1:",D1[:5, :5])
        print("D2:",D2[:5, :5])
        print()

if __name__ == '__main__':
    unittest.main()
