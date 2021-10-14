import unittest
import time
from scripts.utils.FileExten import FileExten
from scripts.algorithms.ConvolutionalNeuralNetworks import ConvolutionalNeuralNetworks

class ConvolutionalNeuralNetworksTests(unittest.TestCase):
    def setUp(self):
        self.startTime = time.time()
        self.CNN = ConvolutionalNeuralNetworks()

    def tearDown(self):
        t = time.time() - self.startTime
        print('%s: %.3f' % (self.id(), t))

    def test_retrieve_data(self):
        self.CNN.retrieve_data("ibean", )
        print(f"{self.CNN.retrieve_data()}")


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(
        ConvolutionalNeuralNetworksTests)
    unittest.TextTestRunner(verbosity=0).run(suite)
