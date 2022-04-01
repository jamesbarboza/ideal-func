import unittest
from models.base import BaseTableClass
from sqlalchemy import Table, select
from unittest import TestCase

class UnitTestDBBase(TestCase):
  tablename = "test_training"
  columns = ['x', 'y1', 'y2']

  def test_init(self):
    '''
    The method should create necessary connections
    It should create a table if it doesn't exits
    self.__table__ property should reflect the table object it represents
    '''
    btc = BaseTableClass(self.tablename, self.columns)
    self.assertEqual(type(btc.__table__), Table, "The init method should created and assign the table object")
    btc.migrate_down()

  def test_init_when_table_exists(self):
    '''
    The method should create necessary connections
    It should NOT create a table
    self.__table__ property should reflect the table object it represents
    '''
    btc = BaseTableClass(self.tablename, self.columns)
    self.assertEqual(type(btc.__table__), Table, "The init method should assign the respective table")
    btc.migrate_down()


  # test migrate up
  def test_migrate_up_when_tablename_is_empty(self):
    '''
    When migration is called,
    It should throw an Error when the tablename is empty
    '''
    try:
      BaseTableClass()
    except RuntimeError as e:
      self.assertEqual(e.args[0], "Table name not provided", "The migrate up method should raise the correct exception")

  def test_migrate_up_when_columns_are_not_provided(self):
    '''
    When migration is called,
    It should throw an Error when the columns are empty
    '''
    try:
      BaseTableClass(self.tablename)
    except RuntimeError as e:
      self.assertEqual(e.args[0], "Columns not provided", "The migrate up method should raise the correct exception")

  def test_successful_migration(self):
    '''
    When migration is called,
    If all the validations are correct,
    It should create the table as expected
    '''
    btc = BaseTableClass(self.tablename, self.columns)
    self.assertEqual(btc.__table__.name, self.tablename, "Migration should be successful")

  def test_successful_reverse_migration(self):
    '''
    When reverse migration is called,
    It should drop the table
    '''
    btc = BaseTableClass(self.tablename, self.columns)
    btc.migrate_down()
    self.assertEqual(btc.__engine__.dialect.has_table(btc.__connection__, self.tablename), False, "Should successfully drop the table")

  # test seed
  def test_seed(self):
    '''
    When data has to be seeded,
    it should seed and expect the correct data when select is called
    '''
    btc = BaseTableClass(self.tablename, self.columns)
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 
    btc.seed(data)

    t = Table(self.tablename, btc.__meta_data__, autoload = True, autoload_with = btc.__engine__)
    dataset = btc.__connection__.execute(select(t)).fetchall()
    self.assertEqual(dataset[0][2], 2, "Should seed the right data")
    self.assertEqual(dataset[1][2], 5, "Should seed the right data")
    btc.migrate_down()


if __name__ == "__main__":
  unittest.main()