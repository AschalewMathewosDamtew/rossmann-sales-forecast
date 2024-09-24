# Sales Prediction Model with RandomForestRegressor

## Project Overview

This project aims to predict sales for various stores using historical data and store-specific features. The dataset is preprocessed to handle missing values, extract features from datetime columns, and convert categorical variables. The model pipeline uses `RandomForestRegressor` for prediction, with feature scaling and encoding as part of the preprocessing step.

## Data Files

- `train.csv`: Contains historical sales data for training the model.
- `test.csv`: Contains test data for predicting sales.
- `store.csv`: Provides additional information about each store, such as competition distance, promotion details, etc.

## Data Preprocessing

- **Missing Values Handling**: Missing values in `CompetitionDistance` are filled with the median. Missing values in `Promo2SinceYear`, `Promo2SinceWeek`, and `PromoInterval` are filled with 0, indicating no promotion.
  
- **Feature Extraction**: Date features such as year, month, day, week of the year, day of the week, and whether it's a weekend are extracted from the `Date` column.

- **Categorical Encoding**: Categorical features like `StateHoliday`, `StoreType`, and `Assortment` are encoded to numeric form using label encoding and one-hot encoding.

- **Feature Scaling**: Numerical features are scaled using `StandardScaler` for better model performance.

## Model Pipeline

The machine learning pipeline includes:
1. **Preprocessing**:
   - Scaling of numerical features.
   - One-hot encoding of categorical features.
2. **Modeling**:
   - RandomForestRegressor with 100 estimators is used to predict sales.

The pipeline ensures that the data is correctly transformed before being fed into the model.

## Model Evaluation

The model performance is evaluated using the **Mean Squared Error (MSE)**. Feature importance is analyzed to understand which features contribute most to sales prediction.

## Feature Importance

After training the Random Forest model, feature importance analysis shows which features are the most influential in predicting sales. This is visualized using a bar chart.

## Model Saving

The trained model, along with its preprocessing pipeline, is saved using the `joblib` library with a unique timestamp to ensure easy identification of different models.

## How to Use

1. Clone the repository.
2. Load the datasets `train.csv`, `test.csv`, and `store.csv`.
3. Preprocess the data by handling missing values, encoding categorical columns, and scaling numerical features.
4. Train the RandomForestRegressor model using the provided pipeline.
5. Evaluate the model's performance using MSE.
6. Analyze feature importance for insights into the model's decision-making.
7. Save the model with a timestamped filename using the provided code.

## Libraries Used

- `pandas`
- `numpy`
- `scikit-learn`
- `matplotlib`
- `joblib`

## Future Improvements

- Experiment with other regression models (e.g., XGBoost, LightGBM) for better performance.
- Optimize hyperparameters of the RandomForest model using GridSearchCV or RandomizedSearchCV.
- Incorporate additional features such as external economic factors for more robust predictions.