# Data Dictionary: Sales Forecasting Dataset

This dataset contains 1,000 daily sales records designed to validate multiple linear regression (OLS), ANOVA, and Regularization models.

| Column | Type | Description |
|---|---|---|
| Day_ID | Integer | Unique identifier for each day |
| Region | String | Region of operations (Mien_Bac, Mien_Nam, Mien_Trung) |
| Ad_Spend | Float | Daily advertising expenditure in millions VND |
| Price_Index | Float | Price index of the company's products (relative to baseline 100) |
| Competitor_Price | Float | Average competitor's price index |
| Store_Size | Float | Average retail store size in square meters |
| Online_Traffic | Integer | Daily number of visitors to the website |
| Promotion_Active | Integer | Binary indicator if a campaign promotion was active (1 = Active, 0 = Inactive) |
| Sales | Float | Daily total sales revenue in millions VND (metric target variable) |
