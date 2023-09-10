import logging 
import os 

def setup_logging()-> None:
    logging.basicConfig(level=logging.DEBUG)
    return

def check_data_sample(sample_data_abs_path: str) -> bool:
    logging.info("Checking sample data...")
    if not os.path.exists(sample_data_abs_path):
        logging.error(f"{sample_data_abs_path} File doesnt exists !")
        exit()
    logging.info("Sample data Pass!")
    return 
