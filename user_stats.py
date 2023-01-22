"""

This example illustrates basic analytics
using just the built-in statistics module.

VS Code Menu / View / Command Palette / Python Interpretor
Must be 3.10 or greater to get the correlation and linear regression.

To update, try:
conda update pythnon -y
conda --version

Uses only Python Standard Library module:

- statistics - for basic descriptive and a bit of predictive stats

"""

import statistics

# define a variable with some univariant data 
# (one varabile, many readings)
scores = [
    105,
    129,
    87,
    86,
    111,
    111,
    89,
    81,
    108,
    92,
    110,
    100,
    75,
    105,
    103,
    109,
    76,
    119,
    99,
    91,
    103,
    129,
    106,
    101,
    84,
    111,
    74,
    87,
    86,
    103,
    103,
    106,
    86,
    111,
    75,
    87,
    102,
    121,
    111,
    88,
    89,
    101,
    106,
    95,
    103,
    107,
    101,
    81,
    109,
    104,
]

# univariant time series data (one varabile over time)
# typically, x (or time) is independent and
# y is dependent on x (e.g. temperature vs hour of day)
x_times = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y_temps = [2, 5, 8, 20, 21, 23, 24, 27, 30, 31, 31,32]

mean = statistics.mean(scores)
median = statistics.median(scores)
mode = statistics.mode(scores)
var = statistics.variance(scores)
stdev = statistics.stdev(scores)

slope, intercept = statistics.linear_regression(x_times, y_temps)
future_y = 13 
future_x = round(slope * future_y + intercept)

print(f"Mean = {mean:0.2f}")
print(f"Median = {median:0.2f}")
print(f"Mode = {mode:0.2f}")
print(f"variance = {var:0.2f}")
print(f"Standard deviation = {stdev:0.2f}")
print(f"Slope = {slope:0.2f}")
print(f"Intercept = {intercept:0.2f}")
print(f"at Future y = {future_y:0.2f}")
print(f"We predict the value of x will be = {future_x:0.2f}")