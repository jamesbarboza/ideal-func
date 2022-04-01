from models import base
from pandas import read_csv
import logger

class TableDataObject(base.BaseTableClass):

  def __init__(self, dataset_path = "", table_name = ""):
    '''
    dataset_path can be a relative or an absolute path to the dataset file in the CSV format
    Read the dataset and perfom CRUD on the SQLite database
    '''
    try:
      self.__dataset_path__ = dataset_path
      self.__dataset__ = read_csv(self.__dataset_path__)
      super(TableDataObject, self).__init__(table_name, self.__dataset__.columns)
      logger.info("[train-debug] Dataset read: {}".format(self.__dataset_path__))
      logger.info("[train-debug] columns identified: {}".format(self.__columns__))

      self.seed(self.__dataset__.values)
    except FileNotFoundError as error:
      logger.error(error)
      raise FileNotFoundError("CSV path is incorrect")

  def get_coordinates(self):
    '''
    The seeded data will be in the format:
    [x, y1, y2 ...]
    We need to separate these as per each line i.e (x1, y1), (x2, y2) ... for each line
    The expected output of the function is
    [
      [ [x1s ...], [y1s ...]],
      [ [x2s ...], [y2s ...]]
    ] 
    '''
    list_of_all_lines = []
    x_list = self.__dataset__['x'].values
    for i in range(1, len(self.__columns__)):
      column = self.__columns__[i]
      y_list = self.__dataset__[column].values
      list_of_all_lines.append([x_list, y_list])
    return list_of_all_lines
