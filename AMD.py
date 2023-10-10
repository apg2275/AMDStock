import csv

prices = []
# Reading CSV file and storing data from Adj. Close
with open('AMD.csv', 'r') as AMD:
    csv_reader = csv.reader(AMD)
    for line in csv_reader:
        prices.append(line[5])
# Converting data into floats for calculations and removing the name of the column
prices = prices[1:]
prices = [float(x) for x in prices]
price_difference = []
up_down_tracker = []
# Calculates the difference between the stock price from it's previous price.
# Can be used to see how big of the difference is between each day.
for i in range(len(prices) - 1):
    price_difference.append(prices[i] - prices[i + 1])
price_difference = [round(x, 5) for x in price_difference]
# Checks the difference in stock price from the previous day.
# to determine if the stock price went up or down.
# Then creates a list representing each day as U for Up and D for down.
for i in range(len(price_difference)):
    if price_difference[i] < 0:
        up_down_tracker.append('D')
    else:
        up_down_tracker.append('U')
# Printing results
print('Down:', up_down_tracker.count('D'))
print('Up:', up_down_tracker.count('U'))
print('Total:', len(up_down_tracker))
ratio = round(up_down_tracker.count('U') / (up_down_tracker.count('D')
                                            + up_down_tracker.count('U')), 4)
print('Ratio of up to total:', ratio)
print()
days_until_up = []
# Counts the amount of days until the stock price increases for each day and puts them into a list.
# If the stock price is up and is up the next day the amount of days is considered 1.
counter = 1
for i in range(0, len(up_down_tracker)):
    if up_down_tracker[i] == 'D':
        counter += 1
    else:
        days_until_up.append(counter)
        counter = 1

table = [[0 for i in range(6)] for i in range(2)]
# Creates a 2x10(max of days until up) matrix with the first row representing the counter number
# and the second number representing the count.
for i in range(6):
    table[0][i] = i + 1
    if i == 5:
        table[0][i] = '6+'
for i in range(6):
    if i == 5:
        table[1][5] = sum(i >= 6 for i in days_until_up)
    else:
        table[1][i] = days_until_up.count(i + 1)
# Adding labels for readability
table[0].insert(0, 'Streaks')
table[1].insert(0, 'Observed')
print('Table for observed results')
for line in table:
    print(line)
print()
# Calculates the expected value using a geometric distribution
# First row is the count number
# Second row is the expected number of prices until first up price.
# Third row shows the probability of the counter number
expected = [[0 for i in range(6)] for i in range(3)]
for i in range(6):

    expected[0][i] = i + 1
    # Rounding values to 4 decimal places for readability
    expected[1][i] = round((((1 - ratio) ** (i)) * ratio) * up_down_tracker.count('U'), 4)
    if i == 5:
        expected[2][i] = round(1 - (1 - (((1 - ratio) ** (i)) * ratio)),4)
        expected[0][5] = '6+'
    else:
        expected[2][i] = round((((1 - ratio) ** (i)) * ratio), 4)

# Adding labels for readability
expected[0].insert(0, 'Streaks')
expected[1].insert(0, 'Expected')
expected[2].insert(0, 'Probability')
print('Table for expected results')
for line in expected:
    print(line)
print()
print('Table for Observed & Expected')
table.append(expected[1])
for line in table:
    print(line)

