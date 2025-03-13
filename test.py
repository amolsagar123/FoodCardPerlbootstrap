import unittest
from unittest.mock import MagicMock

class TestSchemaProcessing(unittest.TestCase):
    
    def setUp(self):
        # Mock the col_selection dictionary to simulate user input
        self.col_selection = {
            'pam': ['column1', 'column3'],
            'pcl': ['column2']
        }
        
        # Create a mock schema with columns
        self.schema_dictp = {
            'pcl_pam': MagicMock()
        }
        self.schema_dictp['pcl_pam'].columns = [
            MagicMock(name='column1'),
            MagicMock(name='column2'),
            MagicMock(name='column3'),
            MagicMock(name='column4')
        ]
        
    def _schema_processing(self, schema):
        # Assuming this function is part of the test class, it will access the instance variables
        for column in schema["pcl_pam"].columns:
            if column.name in self.col_selection['pam']:
                column.name = f"PAM_{column.name}"
            elif column.name in self.col_selection['pcl']:
                column.name = f"PCL_{column.name}"

    def test_schema_processing(self):
        # Call the method we're testing
        self._schema_processing(self.schema_dictp)

        # Check that the names have been updated as expected
        self.assertEqual(self.schema_dictp['pcl_pam'].columns[0].name, 'PAM_column1')
        self.assertEqual(self.schema_dictp['pcl_pam'].columns[1].name, 'PCL_column2')
        self.assertEqual(self.schema_dictp['pcl_pam'].columns[2].name, 'PAM_column3')
        self.assertEqual(self.schema_dictp['pcl_pam'].columns[3].name, 'column4')  # No change since column4 isn't in either selection

if __name__ == '__main__':
    unittest.main()