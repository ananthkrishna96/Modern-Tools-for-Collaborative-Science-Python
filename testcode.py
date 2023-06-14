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

    def test_dist_mat(self):
        # Test dist_mat function
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
        
        # image files
        fig, axs = plt.subplots(1, 3, figsize=(12, 4))
        axs[0].imshow(Dinfty)
        axs[0].set_title('Dinfty')
        axs[1].imshow(D1)
        axs[1].set_title('D1')
        axs[2].imshow(D2)
        axs[2].set_title('D2')
        
        # Save the figure as an image file
        plt.savefig('distance_matrices.png')
        plt.close()


if __name__ == '__main__':
    unittest.main()
