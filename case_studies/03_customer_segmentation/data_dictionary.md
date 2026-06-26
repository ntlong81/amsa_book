# Data Dictionary: Customer Segmentation Dataset

This dataset contains 1,000 customer records designed to validate multidimensional clustering algorithms (Hierarchical, K-Means, and GMM).

| Column | Type | Description |
|---|---|---|
| CustomerID | Integer | Unique identifier |
| Age | Integer | Customer's age in years |
| Income | Float | Annual income in millions VND |
| CreditScore | Integer | Credit score |
| Factor_Service | Float | Factor score for Service Satisfaction (from Chapter 4) |
| Factor_Product | Float | Factor score for Product Quality Satisfaction (from Chapter 4) |
| Factor_Price | Float | Factor score for Price Value Satisfaction (from Chapter 4, positive means sensitive) |
| TrueSegment | String | Underlying true segment used for generation |
