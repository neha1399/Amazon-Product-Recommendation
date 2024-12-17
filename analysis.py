import pandas as pd
import numpy as np
import glob

# Function to process a single dataset
def process_dataset(file_path, name_max_length=30):
    data = pd.read_csv(file_path)
    
    # Normalize column names for consistency (lowercase, remove spaces)
    data.columns = data.columns.str.lower().str.strip()
    
    # Check if the necessary columns exist
    if 'name' not in data.columns or 'ratings' not in data.columns or 'main_category' not in data.columns:
        return None
    
    # Shorten the product name to the specified maximum length
    data['name'] = data['name'].apply(lambda x: x[:name_max_length] if isinstance(x, str) else x)

    # Drop rows with missing values in relevant columns
    data = data.dropna(subset=['name', 'ratings', 'main_category'])
    
    # Convert ratings to numeric, handling errors
    data['ratings'] = pd.to_numeric(data['ratings'], errors='coerce')
    data = data.dropna(subset=['ratings'])

    # Extract only the product name, ratings, and category columns
    product_ratings = data[['name', 'ratings', 'main_category', 'no_of_ratings']]
    
    return product_ratings

# Process multiple datasets
file_paths = glob.glob("data/*.csv")  # Replace with your datasets folder path
all_product_ratings = []

for file_path in file_paths:
    result = process_dataset(file_path)
    if result is not None:
        all_product_ratings.append(result)

# Combine results across datasets
if all_product_ratings:
    combined_product_ratings = pd.concat(all_product_ratings, ignore_index=True)
    
    # Calculate average ratings by category and format to 2 decimals
    # Calculate average ratings by category and format to 2 decimals
    avg_ratings_by_category = combined_product_ratings.groupby('main_category')['ratings'].agg('mean').round(2)

    
    # Calculate most rated category based on the sum of ratings count
    combined_product_ratings['no_of_ratings'] = pd.to_numeric(combined_product_ratings['no_of_ratings'], errors='coerce')
    most_rated_category = combined_product_ratings.groupby('main_category')['no_of_ratings'].sum().idxmax()
    
    # Get top 5 products for each category and format the ratings to 2 decimals
    top_5_by_category = combined_product_ratings.sort_values(by=['main_category', 'ratings'], ascending=[True, False]) \
                                                 .groupby('main_category').head(5)
    top_5_by_category['ratings'] = top_5_by_category['ratings'].round(2)
    
    # Save results
    avg_ratings_by_category.to_csv('average_ratings_by_category.csv')
    top_5_by_category.to_csv('top_5_by_category.csv', index=False)
    
    print(f"Data saved to CSV files: average_ratings_by_category.csv, top_5_by_category.csv")
else:
    print("No data to save.")