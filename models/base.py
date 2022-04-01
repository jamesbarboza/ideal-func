from sqlalchemy import create_engine, MetaData, Table, Column, Integer, Float, insert 
import logger
import constants

class BaseTableClass:
  __data__ = []
  __table__ = None

  def __init__(self, tablename = "", columns = []):
    self.__engine__ = create_engine(constants.DB_PATH)
    self.__meta_data__ = MetaData()
    self.__connection__ = self.__engine__.connect()
    self.__tablename__ = tablename 
    self.__columns__ = columns

    # create table if it does not exist
    if not self.__engine__.dialect.has_table(self.__connection__, self.__tablename__):
      self.migrate_up()
    else:
      self.__table__ = Table(self.__tablename__, self.__meta_data__, autoload = True, autoload_with = self.__engine__)


  def migrate_up(self):
    if self.__tablename__ == "":
      raise RuntimeError("Table name not provided")
    elif len(self.__columns__) == 0:
      raise RuntimeError("Columns not provided")
    else:
      table = Table(self.__tablename__, self.__meta_data__)
      table.append_column(Column("id", Integer, primary_key = True, autoincrement = True, nullable = False))
      for c in self.__columns__:
          table.append_column(Column(c, Float))

      self.__meta_data__.create_all(self.__engine__)
      self.__table__ = Table(self.__tablename__, self.__meta_data__, autoload = True, autoload_with = self.__engine__)

  def migrate_down(self):
    self.__table__.drop(self.__engine__)

  def seed(self, data):
    self.__data__ = data
    seed_data = []
    for row in range(len(self.__data__)):
      row_hash = {}
      for column in range(len(self.__columns__)):
        row_hash[self.__columns__[column]] = self.__data__[row][column]
      seed_data.append(row_hash)
    
    sql_query = insert(self.__table__)
    self.__connection__.execute(sql_query, seed_data)
