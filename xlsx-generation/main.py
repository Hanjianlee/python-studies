import os

from .setup import setup_logging, check_data_sample
from .read_and_modify import read_and_modify

SAMPLE_DATA = "./sample_data/SampleData.xlsx"
WORKSHEET = "SalesOrders"

script_directory = os.path.dirname(os.path.abspath(__file__))
sample_data_abs_path = os.path.join(script_directory, SAMPLE_DATA)


def main():
    setup_logging()
    check_data_sample(sample_data_abs_path)
    read_and_modify(sample_data_abs_path)


if __name__ == "__main__":
    main()
