from models import base
from pandas import read_csv
import logger

class TableDataObject(base.BaseTableClass):

  def __init__(self, dataset_path = "", table_name = ""):
    self.__dataset_path__ = dataset_path
    try:
      self.__dataset__ = read_csv(self.__dataset_path__)
      super(TableDataObject, self).__init__(table_name, self.__dataset__.columns)
      logger.info("[train-debug] Dataset read: {}".format(self.__dataset_path__))
      logger.info("[train-debug] columns identified: {}".format(self.__columns__))

      self.seed(self.__dataset__.values)
    except FileNotFoundError as error:
      logger.error(error)

  def get_coordinates(self):
    list_of_all_lines = []
    x_list = self.__dataset__['x'].values
    for i in range(1, len(self.__columns__)):
      column = self.__columns__[i]
      y_list = self.__dataset__[column].values
      list_of_all_lines.append([x_list, y_list])
    return list_of_all_lines
