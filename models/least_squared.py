import logger
from pandas import Series
import numpy as np

class LeastSquared:
  __y_intercept__ = None
  __slope__ = None

  def __init__(self, x: Series, y: Series, index):
    self.__x__ = x
    self.__y__ = y
    self.__index__ = index
  
  def calculate_slope(self):
    logger.info("[least-squared] calculating slope")

    numerator = 0
    denominator = 0

    x_mean = self.__x__.mean()
    y_mean = self.__y__.mean()
  
    for i in range(len(self.__x__)):
      x_delta = self.__x__[i] - x_mean
      numerator += x_delta * (self.__y__[i] - y_mean)
      denominator += x_delta ** 2
    
    self.__slope__ = numerator / denominator
    self.__y_intercept__ = y_mean - (self.__slope__ * x_mean)

    logger.info("[least-squared] Slope: {}".format(self.__slope__))
    logger.info("[least-squared] y-intercept: {}".format(self.__y_intercept__))
    return self.__slope__
    
  def calculate_r_squared(self):
    return self.apply(self.__x__, self.__y__)

  def show_equation(self):
    logger.info("y = {}x + {}".format(self.__slope__, self.__y_intercept__))

  def apply(self, x: Series, y:Series):
    total_error_rate = 0
    total_mean_error_rate = 0
    for i in range(len(x)):
      Y = (self.__slope__ * x[i]) + self.__y_intercept__
      error_rate = Y - y[i]
      total_error_rate += error_rate ** 2
      
      mean_error_rate = Y - y.mean()
      total_mean_error_rate += mean_error_rate ** 2

    return 1 - (total_error_rate / total_mean_error_rate)

  def apply_to_equation(self, x):
    return (self.__slope__ * x) + self.__y_intercept__
