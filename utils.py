from bokeh.plotting import output_file, figure, show
from bokeh.layouts import row
from models.least_squared import LeastSquared

def get_a_plotted_line(x = [], y = [], plot_name = ""):
  output_file("html/" + plot_name + ".html")
  fig = figure(title = plot_name)
  fig.line(x, y)
  return fig

def get_lines_to_plot(table_data_object):
  training_lines = table_data_object.get_coordinates()
  plotted_lines = []
  for i in range(len(training_lines)):
    x = training_lines[i][0]
    y = training_lines[i][1]
    plotted_lines.append(get_a_plotted_line(x, y, "training-" + str(i)))
  return plotted_lines

def get_equation(line):
  x = line[0]
  y = line[1]
  least_squared = LeastSquared(x, y)
  least_squared.calculate_slope()
  return least_squared