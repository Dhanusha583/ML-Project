# src/exception.py

import sys
from src.logger import logging  # Importing logging configuration from logger.py

# Function to create detailed error message
def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in script: [{0}] at line [{1}] with message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

# Custom Exception class
class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message

# Testable main section to raise a sample exception
if __name__ == "__main__":
    try:
        # Simulate an error
        a = 1 / 0
    except Exception as e:
        logging.info("An exception occurred in exception.py.")
        raise CustomException(e, sys)
