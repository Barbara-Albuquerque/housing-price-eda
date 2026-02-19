## Exploratory Data Analysis — Housing Dataset
## Overview

This project performs a structured Exploratory Data Analysis (EDA) on the Housing Dataset.
The goal is to understand the data distribution, detect potential issues, and analyze how different features relate to house prices.

This repository focuses only on data understanding, not machine learning (yet).

# Dataset

Source: Housing.csv [Kaggle - Housing Price Dataset](https://www.kaggle.com/datasets/jenyraja/housing-price).

Target variable: price

Contains both numerical and categorical features related to housing characteristics.

# Steps Performed
### 1. Initial Inspection

* Checked dataset shape
* Displayed sample rows (head)
* Inspected data types (info)
* Summary statistics (describe)
* Verified missing values

This step ensures structural understanding of the dataset.

### 2. Data Type Separation

Variables were separated into:

* Numerical features
* Categorical features

This allows proper visualization and analysis according to variable type.

### 3. Univariate Analysis
#### Numerical Variables

* Histograms with KDE
* Boxplots for outlier detection

_Purpose_:

* Analyze distribution shape
* Detect skewness
* Identify extreme values

#### Categorical Variables

* Countplots (frequency distributions)

_Purpose_:

* Detect imbalance
* Identify rare categories
* Understand data composition

### 4. Correlation Analysis

Correlation matrix for numerical variables with heatmap visualization.

_Purpose_:

* Identify linear relationships
* Detect potential multicollinearity
* Explore features associated with price

### 5. Target-Oriented Analysis
#### Continuous Numerical × Target

Scatterplots (e.g., area vs price)

_Purpose_:

* Identify linear or nonlinear relationships
* Detect heteroscedasticity patterns

#### Discrete Numerical × Target

Boxplots

_Purpose_:

* Compare price distribution across discrete groups (e.g., number of bedrooms)

#### Categorical × Target

Boxplots

_Purpose_:

* Analyze price differences across categories

### 6. Outputs

All visualizations are automatically saved into structured folders:
```
eda_output/
│
├── 01_histograms/
├── 02_correlation/
├── 03_boxplots/
├── 04_countplots/
├── 05_scatter_target/
└── 06_boxplot_target/
```

This keeps the analysis organized and reproducible.

## Key Goals of This EDA

* Understand data distribution
* Detect potential data quality issues
* Identify relationships with the target variable
* Prepare insights for future machine learning modeling

## Next Steps

*Possible next steps include:
* Feature transformation (e.g., log transformation of price)
* Train/test split
* Baseline regression model
* Model evaluation (R², RMSE)
