import pandas as pd  # For handling data in tabular format
import matplotlib.pyplot as plt  # For data visualization
import numpy as np  # For numerical operations

# Load dataset
df = pd.read_csv("company_sales_data.csv")

# Ensure data types are correct
df = df.astype({
    'month_number': 'int',
    'facecream': 'int',
    'facewash': 'int',
    'toothpaste': 'int',
    'bathingsoap': 'int',
    'shampoo': 'int',
    'moisturizer': 'int',
    'total_units': 'int',
    'total_profit': 'int'
})

### 1. Total profit of all months per month ###
plt.figure(figsize=(10, 5))
plt.plot(df['month_number'], df['total_profit'], marker='o', linestyle='-', color='b', label="Total Profit")

plt.xlabel("Month")
plt.ylabel("Total Profit")
plt.title("Total Profit per Month")
plt.xticks(df['month_number'].tolist())  # Convert to list to avoid issues
plt.legend()
plt.grid(True)
plt.show()

### 2. Sales of all different products per month ###
plt.figure(figsize=(12, 6))
plt.plot(df['month_number'], df['facecream'], marker='o', linestyle='-', label='Face Cream')
plt.plot(df['month_number'], df['facewash'], marker='o', linestyle='-', label='Face Wash')
plt.plot(df['month_number'], df['toothpaste'], marker='o', linestyle='-', label='Toothpaste')
plt.plot(df['month_number'], df['bathingsoap'], marker='o', linestyle='-', label='Bathing Soap')
plt.plot(df['month_number'], df['shampoo'], marker='o', linestyle='-', label='Shampoo')
plt.plot(df['month_number'], df['moisturizer'], marker='o', linestyle='-', label='Moisturizer')

plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Sales of Different Products Per Month")
plt.xticks(df['month_number'].tolist())  # Convert to list
plt.legend()
plt.grid(True)
plt.show()

### 3. Comparing Face Cream vs. Toothpaste Sales Per Month ###
plt.figure(figsize=(10, 5))
width = 0.3  # Width of bars

plt.bar(df['month_number'] - width/2, df['facecream'], width, label="Face Cream", color='c', alpha=0.7)
plt.bar(df['month_number'] + width/2, df['toothpaste'], width, label="Toothpaste", color='m', alpha=0.7)

plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Comparison of Face Cream vs. Toothpaste Sales Per Month")
plt.xticks(df['month_number'].tolist())  # Convert to list
plt.legend()
plt.grid(True)
plt.show()

### 4. Distribution of Total Profits ###
plt.figure(figsize=(10, 5))
plt.hist(df['total_profit'], bins=6, color='purple', alpha=0.7, edgecolor='black')

plt.xlabel("Total Profit")
plt.ylabel("Frequency")
plt.title("Distribution of Total Profits")
plt.grid(True)
plt.show()

### 5. Product Sales and Cumulative Sales ###
plt.figure(figsize=(12, 6))

# Ensure stackplot receives numerical arrays
plt.stackplot(df['month_number'], df['facecream'], df['facewash'], df['toothpaste'],
              df['bathingsoap'], df['shampoo'], df['moisturizer'],
              labels=['Face Cream', 'Face Wash', 'Toothpaste', 'Bathing Soap', 'Shampoo', 'Moisturizer'], alpha=0.6)

plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Product Sales and Cumulative View of All Products")
plt.xticks(df['month_number'].tolist())  # Convert to list
plt.legend(loc="upper left")
plt.grid(True)
plt.show()
