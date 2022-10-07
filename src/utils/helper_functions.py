"""This module aids in setting and making inputs with helper functions."""
import pandas as pd
from pathlib import Path


def make_sample_df():
    TEST_DATA_DIR = (Path(__file__) / "../../data").resolve()
    file_name = "sample_data.csv"
    out_filepath = TEST_DATA_DIR / file_name

    data = {"col_1": [3, 2, 1, 0], "col_2": ["a", "b", "c", "d"]}
    df = pd.DataFrame.from_dict(data)
    df.to_csv(out_filepath, index=False)
