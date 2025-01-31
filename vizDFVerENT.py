import pandas as pd  # For handling data in tabular format
import matplotlib.pyplot as plt  # For data visualization
import numpy as np

# Creating a sample dataset
testData = {
    'A': [1, 2, 3, 4],   # Represents categories (e.g., quarters)
    'B': [25, 13, 36, 39],  # Represents sales/profit values
    'C': [12, 7, 18, 20]  # Represents another metric (e.g., revenue)
}

# Creating a Pandas DataFrame from the dictionary
df = pd.DataFrame(testData)

### 1. Single Bar Chart ###
# Initialize a figure and axes for better control
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# Defining positions for bars
pos = list(range(len(df['A'])))  # X-axis positions
width = 0.3  # Width of the bars

# Creating a bar chart for column 'B'
ax.bar(pos, df['B'], width, alpha=0.5, color="blue", label=df['A'])

# Adding labels and title
plt.title("Total Profit")
plt.xlabel('Quarter')
plt.ylabel('Total Profit')

# Setting the X-axis ticks and labels
ax.set_xticks(pos)
ax.set_xticklabels(df['A'])

### 2. Multiple Bar Chart (Comparing 'B' and 'C') ###
pos = list(range(len(df['A'])))  # Resetting positions
width = 0.15  # Adjusting bar width for multiple bars

# Creating a new figure for a side-by-side bar chart
fig, ax = plt.subplots(figsize=(10, 5))

# Plot bars for 'B' and 'C' side by side
plt.bar(pos, df['B'], width, alpha=0.5, color="yellow", label='B')
plt.bar([p + width for p in pos], df['C'], width, alpha=0.5, color="green", label='C')

# Labeling the graph
ax.set_ylabel('Sales')
ax.set_title('Sales of all different items per quarter')

# Adjusting X-axis ticks and labels for clarity
ax.set_xticks([p + 1.5 * width for p in pos])
ax.set_xticklabels(df['A'])

# Adding a legend to distinguish between 'B' and 'C'
plt.legend(['B', 'C'], loc="upper left")

# Display the bar chart
plt.show()

### 3. Bar Plots Using Pandas DataFrame ###
# Default vertical bar plot for 'B'
df.plot(x='A', y='B', kind='bar', rot=45)

# Bar plot with custom colors
df.plot(x='A', kind='bar', rot=45, color=['red', 'green'])

# Stacked bar plot showing 'B' and 'C' together
df.plot(x='A', kind='bar', rot=45, stacked=True)

# Display the plots
plt.show()

### 4. Line Plots ###
# Simple line plot for 'B'
df.plot(x='A', y='B', kind='line', rot=45)

# Line plot with custom colors
df.plot(x='A', kind='line', rot=45, color=['red', 'green'])

# Attempted stacked line plot (not recommended for line plots)
df.plot(x='A', kind='line', rot=45, stacked=True)

# Display the plots
plt.show()

### 5. Horizontal Bar Charts ###
# Simple horizontal bar chart for 'B'
df.plot(x='A', y='B', kind='barh', rot=45)

# Horizontal bar chart with different colors
df.plot(x='A', kind='barh', rot=45, color=['red', 'green'])

# Stacked horizontal bar chart
df.plot(x='A', kind='barh', rot=45, stacked=True)

# Display the plots
plt.show()

### 6. Scatter Plot ###
# Scatter plot to show correlation between 'A' and 'B'
df.plot(x='A', y='B', kind='scatter', rot=45)

# Display the plot
plt.show()

### 7. Pie Charts ###

# *** FIXED PIE CHART SECTION ***
# Before:
# df.plot(x='A', y='B', kind='pie', rot=45)  #  Error due to using 'x' in pie chart

# Solution: Set 'A' as index before plotting
df.set_index('A', inplace=True)  # Set column 'A' as index to use it as labels automatically

# Corrected single-column pie chart
df['B'].plot(kind='pie', autopct='%1.1f%%', figsize=(5, 5))

# Before:
# df.plot(x='A', y=['B', 'C'], kind='pie', subplots=True, labels=df['A'], rot=45)  #  Error: 'x' parameter is not valid for multiple columns

# Solution: Use DataFrame subset and set labels automatically
df[['B', 'C']].plot(kind='pie', subplots=True, autopct='%1.1f%%', figsize=(10, 5))

# Display the plots
plt.show()
