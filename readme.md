# 📊 Company Sales Data Analysis  

## 📌 Description  
This project analyzes company sales data using Python and Matplotlib to visualize various trends in product sales and total profits over a 12-month period. The dataset includes sales figures for six different products, as well as total units sold and total profit. The visualizations help identify trends, best-selling products, and seasonal effects on sales performance.  

## 📂 Dataset  
The dataset (`company_sales_data.csv`) contains the following columns:  

- **month_number** - The month of the year (1 to 12).  
- **facecream**, **facewash**, **toothpaste**, **bathingsoap**, **shampoo**, **moisturizer** - Sales figures for each product.  
- **total_units** - Total units sold per month.  
- **total_profit** - Total profit earned each month.  

## 📊 Visualizations  
The script generates several plots to analyze the sales data:  

### 1️⃣ Total Profit per Month (Line Plot)  
- **Purpose**: Displays total profit trends over time.  
- **Insights**:  
  - Profit generally increases throughout the year.  
  - The highest profit is observed in **December**.  
  - There is a **dip in May and June**, suggesting potential seasonality or lower sales performance.  

### 2️⃣ Sales of Different Products per Month (Multiple Line Plots)  
- **Purpose**: Compares the sales trends of various products.  
- **Insights**:  
  - **Toothpaste and Bathing Soap** are the best-selling products.  
  - **Facewash and Moisturizer** have the lowest sales, indicating potential areas for improvement.  
  - Sales increase over time, but **Shampoo sales fluctuate**.  

### 3️⃣ Comparison of Face Cream vs. Toothpaste Sales (Bar Plot)  
- **Purpose**: Compares the monthly sales of Face Cream and Toothpaste.  
- **Insights**:  
  - **Toothpaste consistently outsells Face Cream.**  
  - **No strong seasonality** for Face Cream, while **Toothpaste peaks in October**.  
  - Toothpaste likely has **steady demand**, while Face Cream may be a **luxury item**.  

### 4️⃣ Distribution of Total Profits (Histogram)  
- **Purpose**: Analyzes the distribution of total profits.  
- **Insights**:  
  - Most profits range between **200,000 and 400,000**.  
  - Higher profits are **more frequent towards the end of the year**.  
  - The data suggests an **increasing profit trend** over time.  

### 5️⃣ Product Sales and Cumulative Sales (Stacked Area Plot)  
- **Purpose**: Shows how individual product sales contribute to total sales.  
- **Insights**:  
  - **Total sales increase steadily**, peaking in **December**.  
  - **Toothpaste and Bathing Soap** contribute the most to total sales.  
  - **Face Wash and Moisturizer have a minimal contribution**.  
  - The growth indicates **rising market demand or successful promotions**.  

## 🚀 How to Run the Script  
### Prerequisites  
Ensure you have Python installed and the required libraries:  
```bash
pip install pandas matplotlib numpy
