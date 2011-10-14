from pychart import *

theme.use_color = 1
theme.default_font_size = 15
theme.reinitialize()

data = chart_data.read_csv("results.txt", "%s,%f")

chart_object.set_defaults(area.T, size = (600, 400), y_range = (0, 150),
                          x_coord = category_coord.T(data, 0))
chart_object.set_defaults(bar_plot.T, data = data, width = 40)

# Draw the 1st graph. The Y upper bound is calculated automatically.
ar = area.T(x_axis=axis.X(label="", format="/a-30{}%s"),
            y_axis=axis.Y(label="Time (s)", tic_interval=10))
ar.add_plot(bar_plot.T(label="fibonacci(40)", cluster=(0, 1)))
ar.draw()