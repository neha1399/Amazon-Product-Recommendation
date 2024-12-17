# Amazon Product Ratings Analysis

This project analyzes Amazon product ratings data from CSV files and generates a Word document with the results. The analysis includes calculating average ratings for each category, identifying top 5 rated products in each category, and determining the highest rated category.

## Requirements

- Python 3.x
- pandas
- numpy
- glob

## Dataset

The dataset used in this project is a collection of CSV files containing Amazon product ratings data. The dataset was obtained from the [Amazon Product Reviews Dataset on Kaggle](https://www.kaggle.com/snap/amazon-product-reviews-dataset).

## Usage

1. Place Amazon product ratings CSV files in the "data" directory.
2. Run the script using Python.
3. A Word document will be generated with the analysis results, including:
   - Average ratings for each category
   - Top 5 rated products in each category
   - Highest rated category

## Code Structure

The code is organized in the following files:

- `analysis.py`: This is the main file that performs the analysis on the data.
- `requirements.txt`: This file contains the list of Python packages required to run the code.

## Analysis Steps

The analysis process involves the following steps:

1. Load Data from All CSV Files in the Folder: The code reads all CSV files from the "data" directory and concatenates them into one DataFrame.
2. Clean the Data: The code cleans the data by replacing 'Get' with NaN and converting the 'ratings' column to numeric. It also drops rows with missing ratings or product names.
3. Get the Top 5 Rated Products in Each Category: The code groups the cleaned DataFrame by 'main_category' and selects the top 5 rated products in each category.
4. Find the Highest Rated Category: The code calculates the average rating for each category and identifies the highest rated category.
5. Create a Word Document with the Results: The code creates a Word document using the `docx` library. It adds headings and paragraphs with the analysis results.

## Acknowledgments

- [pandas](https://pandas.pydata.org/): A powerful data manipulation library.
- [numpy](https://numpy.org/): A library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.
- [docx](https://python-docx.readthedocs.io/en/latest/): A library for creating and manipulating Word documents.
- [glob](https://docs.python.org/3/library/glob.html): A module that provides a function for matching file names with Unix shell-style wildcards.
- [os](https://docs.python.org/3/library/os.html): A module that provides a portable way of using operating system-dependent functionality.