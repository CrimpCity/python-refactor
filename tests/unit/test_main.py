import pandas as pd
from pathlib import Path
import pytest

# if sample data is not present then make some up
# from src.utils.helper_functions import make_sample_df


# Arrange
@pytest.fixture
def load_sample_data_csv():
    TEST_DATA_DIR = (Path(__file__) / "../../data").resolve()
    file_name = "sample_data.csv"
    out_filepath = TEST_DATA_DIR / file_name

    df = pd.read_csv(out_filepath, header=0)
    return df


def test_sample_data_column_names(load_sample_data_csv):
    # Act
    df = load_sample_data_csv

    result = df.columns.tolist()
    expected = ["col_1", "col_2"]

    # Assert
    assert result == expected


def test_sample_data_col_one(load_sample_data_csv):
    # Act
    df = load_sample_data_csv
    result = df["col_1"].tolist()
    expected = [3, 2, 1, 0]
    # Assert
    assert result == expected


def test_sample_data_col_two(load_sample_data_csv):
    # Act
    df = load_sample_data_csv
    result = df["col_2"].tolist()
    expected = ["a", "b", "c", "d"]
    # Assert
    assert result == expected
