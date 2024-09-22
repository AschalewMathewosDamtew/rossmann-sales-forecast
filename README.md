# Customer Purchasing Behavior Exploration

## Overview
This branch contains an exploratory data analysis (EDA) of customer purchasing behavior at Rossmann Pharmaceuticals. The primary goal is to analyze various factors affecting sales, including promotions, holidays, seasonal trends, and competition. 

## Objectives
- Explore the distribution of promotions in training and test sets.
- Analyze sales behavior before, during, and after holidays.
- Investigate seasonal purchasing behaviors around key holidays.
- Examine the correlation between sales and customer numbers.
- Assess the impact of promotions on sales and customer counts.
- Identify effective promotional strategies for different stores.
- Study customer behavior concerning store opening and closing times.
- Analyze the effect of store assortment types on sales.
- Investigate how competitor distance influences sales.
- Evaluate the impact of new competitors on existing stores.

## Files Included
- `customer_behavior_eda.ipynb`: Jupyter Notebook containing the EDA, visualizations, and insights derived from the data.

## Data Sources
- `train.csv`: Training dataset containing historical sales data.
- `test.csv`: Test dataset for future sales predictions.
- `store.csv`: Store information including features relevant to analysis.

## Installation and Requirements
To run this notebook, you will need the following Python packages:
- pandas
- numpy
- seaborn
- matplotlib

You can install these packages using pip:
    ```bash
   pip install pandas numpy seaborn matplotlib

## How to Use
1. **Clone the repository:**
   ```bash
   git clone https://github.com/AschalewMathewosDamtew/rossmann-sales-forecast.git
   cd rossman-sales-forecast
2. **Switch to this branch:**
   ```bash
   git checkout task-1-eda-customer-behavior
3. **Open the Jupyter Notebook:**
   ```bash
   jupyter notebook customer_behavior_eda.ipynb
4. Run the cells to view the exploratory analysis and visualizations.

#### Insights
The insights derived from this analysis will inform strategies for sales forecasting and promotional effectiveness. It will also guide the finance team in making data-driven decisions to enhance overall performance across stores.

#### License
This project is licensed under the MIT License - see the LICENSE file for details.

### Acknowledgments
- Thanks to the data team for providing the necessary datasets.
- Special thanks to the Rossmann Pharmaceuticals management team for their support and insights.