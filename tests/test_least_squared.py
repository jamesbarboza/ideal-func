from unittest import TestCase
from models.Train import TableDataObject
from models.least_squared import LeastSquared


class TestLeastSquared(TestCase):
  csv_path = "tests/fixtures/train.csv"
  tablename = "test_training"

  def test_calculate_slope(self):
    '''
    It should create the TableDataObject
    should return the coordinates
    calculate_slope method should set the slope of a line
    '''
    tdo = TableDataObject(self.csv_path, self.tablename)
    coordinates = tdo.get_coordinates()
    x = coordinates[0][0]
    y = coordinates[0][1]
    least_squared = LeastSquared(x, y, 1)
    least_squared.calculate_slope()
    self.assertEqual(least_squared.__slope__, 1.518292682926829, "It should calculate the slope as per the testing data")
    self.assertEqual(least_squared.__y_intercept__, 0.30487804878048763, "It should calculate the slope as per the testing data")

    tdo.migrate_down()

  def test_apply(self):
    '''
    It should calculate the slope and the y-intercept
    It should return the error-squared value as expected on the basis of the test data
    '''
    tdo = TableDataObject(self.csv_path, self.tablename)
    coordinates = tdo.get_coordinates()
    x = coordinates[0][0]
    y = coordinates[0][1]
    least_squared = LeastSquared(x, y, 1)
    least_squared.calculate_slope()
    error_squared = least_squared.calculate_r_squared()
    self.assertEqual(error_squared, 0.9578232609151465, "The error squared for the test line should be as expected")

    tdo.migrate_down()

  def test_apply_to_equation(self):
    '''
    It should predict the Y values of a given line 
    '''
    x_test = 8
    tdo = TableDataObject(self.csv_path, self.tablename)
    coordinates = tdo.get_coordinates()
    x = coordinates[0][0]
    y = coordinates[0][1]
    least_squared = LeastSquared(x, y, 1)
    least_squared.calculate_slope()
    y_test = least_squared.apply_to_equation(x_test)
    self.assertEqual(y_test, 12.45121951219512, "The predicted y value should be equal to around 12.45 as per the given line")

    tdo.migrate_down()
