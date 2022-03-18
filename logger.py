import logging
import constants

logging.basicConfig(filename=constants.LOG_FILEPATH, filemode='w', level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')

def info(message):
  print(message)
  logging.info(message)

def debug(message):
  print(message)
  logging.debug(message)

def warning(message):
  print(message)
  logging.warning(message)

def error(message):
  print(message)
  logging.error(message)
