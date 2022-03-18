from models import base
from pandas import read_csv
import logger

class Train(base.BaseTableClass):

  def __init__(self, dataset_path = ""):
    self.__tablename__ = "training"
    self.__dataset_path__ = dataset_path
    try:
      self.__dataset__ = read_csv(self.__dataset_path__)
      self.__columns__ = self.__dataset__.columns
      logger.info("[train-debug] Dataset read: {}".format(self.__dataset_path__))
      logger.info("[train-debug] columns identified: {}".format(self.__columns__))
      super(Train, self).__init__()
    except FileNotFoundError as error:
      logger.error(error)

    # import the data onto the SQLite databse
  