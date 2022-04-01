from sqlalchemy import create_engine, MetaData, Table, Column, Integer, Float, insert 
import logger
import constants

class BaseTableClass:
  __data__ = []
  __table__ = None

  def __init__(self, tablename = "", columns = []):
    '''
    init method will create a connection to the database
    create the sqlite db file in this case.
    It will also check if the table exists
    If yes, table will be assigned to the class
    If not, table will be created and assigned to this class object
    '''
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
    '''
    It will first validate that tablename and columns are not empty
    Dynmically add columns based on the dataset
    Once table schema is ready, create_all will create the table
    That particular table will be assinged to the class object
    '''
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
    '''
    Drop the table associated with the class object
    This is mainly for clean up
    '''
    self.__table__.drop(self.__engine__)

  def seed(self, data):
    '''
    Take the data as the input parameter
    based on the data, create an array of rows which needs to be seeded
    [{x: 1, y:2}, { x: 2, y: 3}]
    This array will then be seeded onto the table
    '''
    self.__data__ = data
    seed_data = []
    for row in range(len(self.__data__)):
      row_hash = {}
      for column in range(len(self.__columns__)):
        row_hash[self.__columns__[column]] = self.__data__[row][column]
      seed_data.append(row_hash)
    
    sql_query = insert(self.__table__)
    self.__connection__.execute(sql_query, seed_data)
