from memory_profiler import profile
import openpyxl
from openpyxl.worksheet.datavalidation import DataValidation
import logging
import json


@profile
def read_and_modify(sample_data_path: str, sample_excel_path: str):
    logging.info("Loading workbook ...")
    wb = openpyxl.load_workbook(sample_excel_path)
    logging.info("Loading worksheet ...")
    ws = wb["SalesOrders"]
    data_validation = DataValidation()
    ws.add_data_validation(data_validation)

    with open(sample_data_path, "r") as json_file:
        # Load the JSON data from the file
        data = json.load(json_file)

    for i in range(0, 10000):

        pass
