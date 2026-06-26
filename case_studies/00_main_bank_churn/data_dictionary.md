# Data Dictionary: Bank Churn Dataset

| Column | Type | Description |
|---|---|---|
| CustomerID | Integer | Unique identifier for each customer |
| Age | Integer | Customer's age in years |
| Income | Float | Annual income. Contains MAR (Missing at Random) depending on Age. |
| CreditScore | Integer | Credit bureau score. Contains MNAR (Missing Not at Random) depending on score. |
| NumOfProducts | Integer | Number of bank products the customer uses |
| HasCrCard | Integer | 1 if customer has a credit card, 0 otherwise |
| IsActiveMember | Integer | 1 if active member, 0 otherwise |
| EstimatedSalary | Float | Estimated annual salary. Contains MCAR (Missing Completely at Random). |
| Exited | Integer | Target variable: 1 if customer churned (left the bank), 0 otherwise |
