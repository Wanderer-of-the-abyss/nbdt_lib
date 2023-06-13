import os
import unittest
from nbdt.datasets import load_dataset

class TestNbdt(unittest.TestCase):

    def setUp(self):
        self.dataset_name = 'arxiv'
        self.destination_path = 'arxiv_dataset.csv'
    
    def tearDown(self):
        # Clean up any downloaded files after each test
        if os.path.exists(self.destination_path):
            os.remove(self.destination_path)
    
    def test_data_loader_success(self):
        load_dataset(self.dataset_name, self.destination_path)
        self.assertTrue(os.path.exists(self.destination_path))
    
    def test_data_loader_invalid_dataset(self):
        invalid_dataset = 'invalid'
        with self.assertRaises(ValueError):
            load_dataset(invalid_dataset, self.destination_path)
    
    def test_data_loader_invalid_destination(self):
        invalid_destination = 'na_file.csv'
        with self.assertRaises(FileNotFoundError):
            load_dataset(self.dataset_name, invalid_destination)

if __name__ == '__main__':
    unittest.main()
