import logger
from models.Train import TableDataObject
from pandas import DataFrame

class TestDataTable(TableDataObject):
  def __init__(self, dataset: DataFrame, table_name = ""):
    self.__dataset__ = dataset
    self.__columns__ = ["x", "y", "y_delta", "function"]
    logger.info("[train-debug] columns identified: {}".format(self.__columns__))
    super(TableDataObject, self).__init__(table_name, self.__columns__)

    self.seed(self.__dataset__.values)
