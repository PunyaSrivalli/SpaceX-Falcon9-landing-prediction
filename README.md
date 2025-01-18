# SpaceX Falcon 9 Landing Prediction

## Overview
This project aims to predict the successful landing of the first stage of SpaceX's Falcon 9 rocket using machine learning. Accurate predictions can significantly impact cost estimation and competitiveness in the aerospace industry.

The repository contains analyses and models that explore factors influencing landing success, visualize trends, and predict outcomes using classification techniques.

---

## Table of Contents
- [Project Motivation](#project-motivation)
- [Methodology](#methodology)
- [Data Sources](#data-sources)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Interactive Visualizations](#interactive-visualizations)
- [Machine Learning Models](#machine-learning-models)
- [Results](#results)
- [Tools and Libraries](#tools-and-libraries)


---

## Project Motivation
SpaceX advertises competitive costs for Falcon 9 rocket launches due to reusable first stages. Predicting the landing success of these stages allows for better planning and competitiveness for companies seeking to compete with SpaceX.

Key questions addressed:
1. What factors influence a successful rocket landing?
2. How do features interact to predict success?
3. What operational conditions are necessary for a successful landing?

---

## Methodology
### Data Acquisition
- **SpaceX API**: Retrieved launch records and details via GET requests, processed into pandas DataFrames.
- **Web Scraping**: Used BeautifulSoup to extract additional launch data from Wikipedia.

### Data Wrangling
- Transformed and cleaned data for analysis.
- Created categorical variables using one-hot encoding.
- Labeled outcomes as `Success` (1) or `Failure` (0).

### Data Analysis
- Conducted SQL queries to explore payload trends, launch sites, and success rates.
- Generated visualizations to identify trends and patterns.

### Machine Learning
- Trained and evaluated classification models:
  - Logistic Regression
  - Support Vector Machines (SVM)
  - Decision Tree Classifier
- Tuned hyperparameters using GridSearchCV.

---

## Data Sources
- **SpaceX API**: Historical launch data.
- **Wikipedia**: Supplementary data on launch outcomes.

---

## Exploratory Data Analysis
Key insights include:
- Higher success rates for light payloads.
- Launch sites near coastlines had distinct success patterns.
- Specific orbits like LEO and GEO exhibited better outcomes.

### Key Visualizations
- Payload vs. Launch Site
- Success Rate per Orbit
- Launch Success Yearly Trends

---

## Interactive Visualizations
- **Folium Maps**: Marked launch sites with success/failure rates.
- **Plotly Dash Dashboard**:
  - Pie charts for site-specific success ratios.
  - Scatter plots for payload vs. outcome.

---

## Machine Learning Models
- Built LogisticRegression, SVM, DecisionTree Classifier models, tuned the hyperparameters using GridSearchCV.
- Observed the accuracy of each model, improved the model performance using feature engineering and algorithm tuning.
- Identified the best performing model.
- **Best Model**: Decision Tree Classifier (87% accuracy).
  - Performance metrics of the best model:
    - Sensitivity: 1.00
    - Specificity = 0.50
    - Precision = 0.80
    - Accuracy = 0.83
    - F1 score = 0.89

---

## Results
- Launch sites like `KSC LC-39A` have the highest success rates.
- Payload range and orbit significantly influence landing success.
- Decision Tree Classifier outperformed other models in prediction accuracy.

---

## Tools and Libraries
- Tools & Libraries: Python, Pandas, NumPy, Matplotlib, Seaborn, Folium, Plotly, Scikit-learn.
