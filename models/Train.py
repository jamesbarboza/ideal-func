from models import base
from pandas import read_csv
import logger

class TableDataObject(base.BaseTableClass):

  def __init__(self, dataset_path = "", table_name = ""):
    self.__tablename__ = table_name
    self.__dataset_path__ = dataset_path
    try:
      self.__dataset__ = read_csv(self.__dataset_path__)
      self.__columns__ = self.__dataset__.columns
      self.__data__ = self.__dataset__.values
      logger.info("[train-debug] Dataset read: {}".format(self.__dataset_path__))
      logger.info("[train-debug] columns identified: {}".format(self.__columns__))
      super(TableDataObject, self).__init__()

      self.seed()
    except FileNotFoundError as error:
      logger.error(error)

    # import the data onto the SQLite databse
  