# Data Dictionary: Marketing Campaign Dataset (marketing_roi_campaign.csv)

This dataset simulates a marketing campaign over 1,000 days. It is specifically designed to illustrate the concept of **Omitted Variable Bias (OVB)** and **Endogeneity** in Causal Inference.

| Column | Type | Description |
|---|---|---|
| Day_ID | Integer | Unique identifier for each day |
| Seasonality_Index | Float | A normalized index (0 to 1) representing the natural demand season (1 = Peak Holiday). This is the **Confounder (Biến nhiễu)**. |
| Ad_Spend | Float | Daily advertising budget (in thousands of dollars). The company historically spends more during peak seasons. |
| Revenue | Float | Daily total revenue (in thousands of dollars). Driven by BOTH Ad Spend and the natural Seasonality. |

## The Data Generating Process (DGP)
If a Data Scientist attempts to run a simple Linear Regression of `Revenue` on `Ad_Spend` without including `Seasonality_Index`, the model will suffer from **Endogeneity**. The coefficient for `Ad_Spend` will be artificially inflated because the model incorrectly attributes the revenue spike of the holiday season entirely to the advertising budget.
