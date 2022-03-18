from sqlalchemy import create_engine, MetaData, Table, Column, Integer, Float 
import logger

class BaseTableClass:
  __tablename__ = ""

  def __init__(self):
    self.__engine__ = create_engine("sqlite:///db/ideal_functions.db")
    self.__meta_data__ = MetaData()
    self.__connection__ = self.__engine__.connect()
    self.__table__ = None

    # create table if it does not exist
    if not self.__engine__.dialect.has_table(self.__connection__, self.__tablename__):
      logger.info("[BaseTable] creating table for {}".format(self.__tablename__))
      self.migrate_up()
    else:
      logger.info("[BaseTable] table exists for {}".format(self.__tablename__))


  def migrate_up(self):
    if self.__tablename__ == "":
      raise RuntimeError("Table name not provided")
    elif len(self.__columns__) == 0:
      raise RuntimeError("Columns not provided")
    else:
      table = Table(self.__tablename__, self.__meta_data__)
      table.append_column(Column("id", Integer, primary_key = True, autoincrement = True, nullable = False))
      for c in self.__columns__:
          table.append_column(Column(c, Float, nullable = False))

      self.__meta_data__.create_all(self.__engine__)
      self.__table__ = Table(self.__tablename__, self.__meta_data__, autoload = True, autoload_with = self.__engine__)

  def migrate_down(self):
    self.__table__.drop(self.__engine__)

