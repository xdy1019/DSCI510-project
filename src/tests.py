import unittest
import pandas as pd
from load import get_bitcoin_price_data


class TestBitcoinPriceData(unittest.TestCase):

    def test_get_bitcoin_price_data_format(self):
        """
        Validates:
        - Returns a pandas DataFrame
        - Row count > 500
        - Contains exactly 2 columns
        - First column stored as string, each entry length == 10 ("YYYY-MM-DD")
        - Second column is numeric (price)
        """

        df = get_bitcoin_price_data()

        self.assertIsInstance(df, pd.DataFrame)

        # contain at least 500 daily price rows
        self.assertGreater(len(df), 500, "BTC history should have >500 rows")

        # have exactly 2 columns
        self.assertEqual(len(df.columns), 2, "Expected exactly 2 fields returned")

        date_col, price_col = df.columns  # unpack names

        # validate date column is string formatted "YYYY-MM-DD"
        self.assertTrue(
            df[date_col].apply(lambda x: isinstance(x, str) and len(x) == 10).all(),
            "Date column must be string formatted as YYYY-MM-DD (length 10)"
        )

        # validate numeric price column
        self.assertTrue(
            pd.api.types.is_numeric_dtype(df[price_col]),
            "Second column must be numeric price value"
        )


if __name__ == "__main__":
    unittest.main()

