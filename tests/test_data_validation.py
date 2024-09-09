import unittest
import pandas as pd

class TestStockDataValidation(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Load the CSV data
        cls.df = pd.read_csv('data/stock_data.csv')

        # Explicitly convert the 'datetime' column to datetime type
        cls.df['datetime'] = pd.to_datetime(cls.df['datetime'], errors='coerce')  # 'coerce' will handle any non-datetime values

    def test_data_types(self):
        # Test if 'datetime' column is of datetime type
        self.assertTrue(pd.api.types.is_datetime64_any_dtype(self.df['datetime']), "datetime column should be datetime type")
        
        # Test if 'close', 'high', 'low', 'open' columns are of float type
        for column in ['close', 'high', 'low', 'open']:
            self.assertTrue(pd.api.types.is_float_dtype(self.df[column]), f"{column} column should be float type")
        
        # Test if 'volume' column is of integer type
        self.assertTrue(pd.api.types.is_integer_dtype(self.df['volume']), "volume column should be integer type")
        
        # Test if 'instrument' column is of string (object) type
        self.assertTrue(pd.api.types.is_string_dtype(self.df['instrument']), "instrument column should be string type")

if __name__ == '__main__':
    unittest.main()
