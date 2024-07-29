# Mobile Price Predictor

Welcome to the Mobile Price Predictor project! This is my first end-to-end project, so the organization and code structure might not be ideal, and comments are sparse. However, it provides a comprehensive overview of how to build a model to predict mobile phone prices based on various features.

## Overview

In this project, I performed several tasks to predict mobile phone prices using machine learning techniques. The steps include data collection, data preprocessing, exploratory data analysis (EDA), and model building.

## Table of Contents

- [Data Collection](#data-collection)
- [Data Preprocessing](#data-preprocessing)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
- [Model Building](#model-building)
- [Results](#results)
- [Notes](#notes)

## Data Collection

- **Source:** Data was taken from CampusX Youtube channel (Nitish sir). <a src = "https://docs.google.com/spreadsheets/d/1oBG0ZtYiWzehWa1K6pV8huMtVEJxCY4C9vPaGCt1_gU/edit?gid=1238335059#gid=1238335059" > click here for actual dataset given by campusx </a>

## Data Preprocessing

1. **Data Assessment:**
   - Extracted the `brand` column from the `model` column.
   - Cleaned the `price` column by removing unwanted symbols (rupees symbol and comma).
   - Filled missing values in the `rating` column with the mean of that column.
   - Renamed "Wi-Fi" to "no sim" in the `sim` column.
   - Extracted the SIM type from the `sim` column.
   - Created a new `is_5g` column from the `sim` column.
   - Extracted processor name and number of cores from the `processor` column.
   - Extracted RAM and ROM from the `ram` column.
   - Extracted battery capacity (mAh), charger watt, and fast charging status from the `battery` column.
   - Extracted display size in inches, resolution, Hz, and notch type from the `display` column.
   - Extracted rear camera count, rear primary camera pixels, and front primary camera pixels from the `camera` column.
   - Removed `card` and `os` columns due to excessive missing values.

2. **Feature Engineering:**
   - Converted features into usable formats and created new features for model input.

## Exploratory Data Analysis (EDA)

- Conducted univariate and bivariate analysis.
- Plotted various charts to visualize data distributions and relationships.

## Model Building

Several models were built and evaluated:

- **Linear Multiple Regression:** 69.25% R² Score
- **Ridge Regression:** 69.24% R² Score
- **Decision Tree Regression:** 72.13% R² Score
- **Random Forest Regressor:** 79.33% R² Score
- **XGBoost Regressor:** 81.57% R² Score

## Results

The XGBoost Regressor performed the best, achieving an R² score of 81.57%. This indicates that the model explains approximately 81.57% of the variance in mobile phone prices based on the provided features.

## Tools Used

- **NumPy**: For numerical operations and handling arrays.
- **Pandas**: For data manipulation and analysis.
- **Matplotlib**: For creating static, animated, and interactive visualizations.
- **Seaborn**: For statistical data visualization.
- **Scikit-Learn (sklearn)**: For implementing machine learning algorithms and model evaluation.
- **XGBoost**: For gradient boosting machine learning models.

## Notes

- This project is my first end-to-end attempt, so the code organization may not be optimal, and there are limited comments throughout the code.
- Future improvements could include better code organization, more thorough comments, and additional feature engineering.

Feel free to explore the code and provide feedback or suggestions for improvements!
