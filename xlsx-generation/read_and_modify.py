from memory_profiler import profile
import openpyxl
import logging


@profile
def read_and_modify(sample_data_path: str):
    logging.info("Loading workbook")
    wb = openpyxl.load_workbook(sample_data_path)
    logging.info("Loading worksheet")
    worksheet = wb["SalesOrders"]
