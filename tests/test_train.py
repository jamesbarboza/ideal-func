from unittest import TestCase
from sqlalchemy import Table, select

from pandas import DataFrame
from models.Train import TableDataObject

class TestTrainingClass(TestCase):
  csv_path = "tests/fixtures/train.csv"
  tablename = "test_training"

  def test_init(self):
    '''
    It should read the CSV file
    Create the table based on the columns
    Should seed the data
    '''
    tdo = TableDataObject(dataset_path = self.csv_path, table_name = self.tablename)
    self.assertEqual(type(tdo.__dataset__), DataFrame, "The imported datased should be of type DataFrame")
    self.assertEqual(type(tdo.__table__), Table, "The assigned table objects should be referenced correctly")
    self.assertEqual(tdo.__table__.name, self.tablename, "The table name should be set as expected")

    t = Table(self.tablename, tdo.__meta_data__, autoload = True, autoload_with = tdo.__engine__)
    dataset = tdo.__connection__.execute(select(t)).fetchall()
    self.assertEqual(dataset[0]["y"], 4, "Should seed the right data")
    self.assertEqual(dataset[1]["x"], 3, "Should seed the right data")

    tdo.migrate_down()


  def test_init_for_exception(self):
    '''
    It should raise an exception when the csv path provided is incorrect 
    '''
    try:
      TableDataObject(dataset_path = "", table_name = "")
    except FileNotFoundError as e:
      self.assertEqual(e.args[0], "CSV path is incorrect", "File not found exception should be raised with correct message")

  def test_get_coordinates(self):
    '''
    It should read the CSV file
    create the table and seed it
    Should return a list of [x(s), y(s)]
    '''
    tdo = TableDataObject(dataset_path = self.csv_path, table_name = self.tablename)

    tdo_coordinates = tdo.get_coordinates()
    self.assertEqual(len(tdo_coordinates), 1, "It should return 1 set of lines as per the test data")
    self.assertEqual(tdo_coordinates[0][0][0], 2, "It should return the 1st element of the x list")

    tdo.migrate_down()