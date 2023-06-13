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
        invalid_dataset = 'arxiv2'
        try:
            load_dataset(invalid_dataset, self.destination_path)
        except ValueError as e:
            self.assertEqual(str(e), f'Dataset "{invalid_dataset}" is not available.')
        else:
            self.fail(f'Expected ValueError for invalid dataset "{invalid_dataset}" not raised.')
    
    def test_data_loader_invalid_destination(self):
        invalid_destination = 'na_file.doc'
        try:
            load_dataset(self.dataset_name, invalid_destination)
        except FileNotFoundError as e:
            self.assertEqual(str(e), f'[Errno 2] No such file or directory: \'{invalid_destination}\'')
        else:
            self.fail(f'Expected FileNotFoundError for invalid destination "{invalid_destination}" not raised.')

if __name__ == '__main__':
    unittest.main()

