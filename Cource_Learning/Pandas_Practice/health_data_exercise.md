
1. Basic Exploration
    1. Shape & Structure Check — Find the number of rows, columns, and data types for each column.
    2. Summary Statistics — Get mean, median, min, max, and standard deviation for all numerical columns.

2. Data Cleaning
    1. Missing Data Analysis — Find percentage of missing values per column and decide handling strategies.
    2. Duplicate Check — Identify and remove duplicate rows based on the ID or combination of key columns.
    3. Data Type Conversion — Convert ID to integer, ensure BMI is float, categorical columns to category type.

3. Data Transformation
    1. BMI Calculation Validation — Recalculate BMI using Weight_kg and Height_cm and compare with given BMI column.
    2. Categorize Age Groups — Create a new column Age_Group like:
            Youth (18–25), Adult (26–40), Middle-aged (41–60), Senior (60+).
            Blood Pressure Category — Based on Blood_Pressure, classify into Low, Normal, Pre-Hypertension, Hypertension.

4. Exploratory Data Analysis (EDA)
    1. Gender Distribution — Count and visualize the proportion of males, females, and others.
    2. State-wise Average BMI — Find and plot the average BMI for each state.
    3. Relationship Check — Plot the relationship between Age and Cholesterol_mgdl.

5. Health Risk Insights
    1. Smoking & Blood Pressure — Compare average blood pressure between smokers and non-smokers.
    2. Exercise & BMI — Find if regular exercise lowers BMI on average.
    3. Diabetes Correlation — Check if diabetic patients have higher cholesterol levels.

6. Data Aggregation
    1. Top 5 Cities with Hypertension — Based on average blood pressure values.
    2. Medical Condition Counts — Frequency count of each Medical_Conditions type.

7. Feature Engineering
    1. Risk Score Creation — Combine BMI, Blood Pressure, and Cholesterol into a new Health_Risk_Score column.
    2. Obesity Flag — Add a binary column if BMI ≥ 30.

8. Predictive Modeling Ideas
    1. Predict Diabetes — Build a logistic regression model using numerical & categorical features.
    2. BMI Prediction — Build a regression model to predict BMI using height, weight, and other features.