import logging
import constants

logging.basicConfig(filename=constants.LOG_FILEPATH, filemode='w', level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')

def info(message):
  logging.info(message)

def debug(message):
  logging.debug(message)

def warning(message):
  logging.warning(message)

def error(message):
  logging.error(message)
