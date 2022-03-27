import logging
import sys
from models.Train import TableDataObject
import logger
import utils
from bokeh.plotting import show
from bokeh.layouts import row
from pandas import Series
from models.least_squared import LeastSquared
from numpy import sqrt

def print_help():
  print("Usage: app.py --train <file-path> --ideal <file-path> --test <filepath>")
  print()
  print("--train  file-path to training dataset")
  print("--ideal  file-path to ideal dataset")
  print("--test   file-path to test dataset")


def run():
  training_dataset_found = False
  training_dataset_path = ""

  ideal_dataset_found = False
  ideal_dataset_path = ""

  test_dataset_found = False
  test_dataset_path = ""

  try:
    for i in range(len(sys.argv)):
      match sys.argv[i]:
        case "--train":
          i = i + 1
          training_dataset_path = sys.argv[i]
          training_dataset_found = True
        case "--ideal":
          i = i + 1
          ideal_dataset_path = sys.argv[i]
          ideal_dataset_found = True
        case "--test":
          i = i + 1
          test_dataset_path = sys.argv[i]
          test_dataset_found = True
  except IndexError:
      pass

  if not (training_dataset_found and ideal_dataset_found and test_dataset_found):
    print_help()
  else:
    print("*********************************************")
    print("*               Hello, World!               *")
    print("*********************************************")

    logger.info("Training dataset: {}".format(training_dataset_path))
    logger.info("Ideal dataset: {}".format(ideal_dataset_path))
    logger.info("Test dataset: {}".format(test_dataset_path))

    # Create the train, ideal an test objects
    train = TableDataObject(training_dataset_path, "training")
    ideal = TableDataObject(ideal_dataset_path, "ideal")
    test = TableDataObject(test_dataset_path, "test")

    # create the visuals for train functions
    #   get the x and y values for each line [[[x1], [y1]], [[x2], [y2]]]
    training_figures = utils.get_lines_to_plot(train)
    show(row(training_figures))

    # create the visuals for ideal functions
    ideal_figures = utils.get_lines_to_plot(ideal)
    show(row(ideal_figures))
    
    # Using the training lines, get the equation for each line
    training_coordinates = train.get_coordinates()
    training_equations = [utils.get_equation(training_coordinates[i]) for i in range(len(training_coordinates))]

    # get the ideal lines
    ideal_all_coordinates = ideal.get_coordinates()

    # find ideal lines
    ideal_cooridnates = []
    for eq in training_equations:
      training_r_squared = eq.calculate_r_squared()
      min_diff = None
      ideal_index = 0

      for i in range(len(ideal_all_coordinates)):
        ideal_line = ideal_all_coordinates[i]
        ideal_r_squared = eq.apply(ideal_line[0], ideal_line[1])
        diff = abs(training_r_squared - ideal_r_squared)
        if min_diff == None or diff < min_diff:
          min_diff = diff
          ideal_index = i

      logger.info("Ideal function: {} : {} : {}".format(training_r_squared, min_diff, ideal_index))
      ideal_cooridnates.append(ideal_all_coordinates[ideal_index])


    # create ideal functions
    ideal_equations = [utils.get_equation(ideal_cooridnates[i]) for i in range(len(ideal_cooridnates))]

    # test ideal functions on test dataset
    for i in range(len(test.__data__)):
      point = test.__data__[i]
      x = point[0]
      y = point[1]
      min_y_delta = None
      function_index = None
      for j in range(len(ideal_equations)):
        eq = ideal_equations[j]
        Y = eq.apply_to_equation(x)
        y_delta = abs(y - Y)
        equation_criteria = sqrt(2) * eq.__y__.std()
        if y_delta <= equation_criteria:
          if min_y_delta == None or y_delta < min_y_delta:
            min_y_delta = y_delta
            function_index = j

      logger.info("Test: {} Function: {}".format(i, function_index))

run()
