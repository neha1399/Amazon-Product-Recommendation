# Amazon Product Ratings Analysis

---

## Overview

This project analyzes Amazon product ratings from multiple datasets and generates insights in both tabular and visual formats. The analysis includes:

1. **Average Ratings by Category**
2. **Total Number of Ratings by Category**
3. **Top 5 Products by Ratings in Each Category**

Additionally, the project creates interactive visualizations using Plotly to represent the data effectively.

---

## Features

1. **Data Processing**:
   - Combines multiple datasets of product ratings.
   - Handles inconsistencies such as missing values or invalid data types.
   - Ensures uniform column names across datasets.

2. **Analysis**:
   - Calculates average ratings for each category.
   - Identifies the total number of ratings per category.
   - Extracts the top 5 products by ratings for each category.

3. **Visualizations**:
   - **Bar Chart**: Average ratings by category.
   - **Bar Chart**: Total number of ratings by category.
   - **Table**: Top 5 products with their categories, ratings, and number of ratings.
   - **Pie Chart**: Distribution of ratings across categories.

---

## Files

1. **Scripts**:
   - `analysis.py`: Main script for data analysis and visualization.
   - `visualizations.py`: Contains functions to generate visualizations using Plotly.

2. **Input**:
   - CSV files containing Amazon product data, stored in the `data/` directory.

3. **Output**:
   - CSV files saved in the `output/` directory:
     - `average_ratings_by_category.csv`
     - `total_ratings_by_category.csv`
     - `top_5_by_category.csv`
   - Interactive visualizations displayed in the browser.

---

## Visualizations

1. **Bar Chart (Average Ratings)**:
   Displays the average ratings for each product category.

2. **Bar Chart (Total Ratings)**:
   Shows the total number of ratings for each category.

3. **Table**:
   Lists the top 5 rated products for each category, with columns:
   - Product Name
   - Category
   - Rating
   - Number of Ratings
4. **Pie Chart (Ratings Distribution)**:
   Illustrates the proportion of ratings contributed by each category. The highest-rated category is highlighted.
---

## Dependencies

- **Pandas**: Data manipulation and processing.
- **NumPy**: Numerical operations.
- **Plotly**: Interactive visualizations.
- **glob**: File pattern matching for multiple datasets
- **OS**: File and directory management.