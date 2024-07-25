# Car Price Prediction Model

## Libraries Used
- `numpy` For numerical operations and array manipulation.
- `pandas` For data manipulation and analysis.
- `sklearn.model_selection` for `train_test_split`
- `sklearn.preprocessing` for `LabelEncoder`
- `sklearn.linear_model` for `LinearRegression`
- `sklearn.metrics` for `r2_score`

## Task
The goal of this project is to predict car prices based on the given dataset.

## Data Collection
The dataset was downloaded from Quikr.

## Data Assessment
Performed a high-level understanding of the data to identify key features and potential issues.

## Data Cleaning
Performed data cleaning on different columns, including actions such as:
- Replacing and removing incorrect data
- Handling missing data (NaN)

## Model Building
1. **Train-Test Split**: The data was split into training and testing sets with an 80:20 ratio.
2. **Label Encoding**: Applied to the 'name', 'company', and 'fuel_type' columns.

### Initial Model
- Used Multiple Linear Regression.
- Achieved an R2 score of only 0.11.

### Further Improvements
- Experimented with different `random_states` in `train_test_split`.
- Improved the R2 score from 0.11 to 0.325, but it is still quite low.

## Suggestions for Improvement
I am seeking advice on how to further improve the accuracy of this model or to identify potential mistakes in the current approach. 

## How to Run the Project
1. Clone the repository.
2. Install the required libraries:
   ```bash
   pip install numpy pandas scikit-learn
   ```
3. Run the model:
    - run on jupyter notebook

Feel free to contribute by opening issues or pull requests for suggestions and improvements.
