# Rossmann Pharmaceuticals Sales Forecasting

Welcome to Rossmann Pharmaceuticals Sales Forecasting project! The finance team requires accurate sales forecasts for all stores across multiple cities, six weeks in advance. Currently, store managers rely on their experience and judgment, but the data team has identified key factors—such as promotions, competition, holidays, seasonality, and locality—that are crucial for improving the forecasting process.

## Project Overview

The objective is to build and serve an end-to-end product that delivers accurate sales predictions to the finance team, enabling better planning and decision-making. Each task is organized into separate branches for clarity and better management of changes.

## Branches Overview

- **[Task 1 Exploratory Data Analysis (EDA)](https://github.com/AschalewMathewosDamtew/rossmann-sales-forecast/tree/task-1-eda-customer-behavior)**
  - This branch focuses on exploring customer purchasing behavior through various analyses. It includes:
    - Data cleaning and preprocessing
    - Visualizations to understand sales patterns, promotions, and other influencing factors

### Upcoming Branches
1. **Task 2 - Prediction of Store Sales**
   - **Goal**: To predict daily sales across various stores up to six weeks in advance.
   - **Key Steps**:
     - Data preprocessing (feature extraction, scaling)
     - Model building using scikit-learn pipelines
     - Post-prediction analysis and model serialization
     - Implementation of deep learning techniques (LSTM)

2. **Task 3 - Model Serving API Call**
   - **Goal**: To create a REST API for real-time predictions using the trained models.
   - **Key Steps**:
     - Selection of a framework (e.g., Flask, FastAPI)
     - Loading serialized models and defining API endpoints
     - Deployment to a web server or cloud platform

## How to Navigate
To explore the current exploratory analysis, switch to the EDA branch:
```bash
git checkout eda-branch-name