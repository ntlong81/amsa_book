# Data Dictionary: Customer Experience Survey Dataset

This dataset simulates 1,000 customers answering a 15-question satisfaction survey using a 5-point Likert scale (1 = Strongly Disagree, 5 = Strongly Agree).

The Data Generating Process (DGP) for this dataset inherently assumes that the answers to these 15 questions are driven by 3 unobserved **Latent Variables (Factors)**.

## Survey Questions:
| Column | Description | True Underlying Factor |
|---|---|---|
| Q1_Friendly | "Staff was friendly" | Service Quality |
| Q2_Fast_Resolve | "Issues were resolved quickly" | Service Quality |
| Q3_Knowledgeable | "Staff was knowledgeable" | Service Quality |
| Q4_Polite | "Staff was polite" | Service Quality |
| Q5_Accessible | "Support was easy to access" | Service Quality |
| Q6_Durable | "The product is durable" | Product Quality |
| Q7_Reliable | "The product is reliable" | Product Quality |
| Q8_Feature_Rich | "The product has great features" | Product Quality |
| Q9_Easy_Use | "The product is easy to use" | Product Quality |
| Q10_Design | "The product has a good design" | Product Quality |
| Q11_Affordable | "The product is affordable" | Pricing Value |
| Q12_Worth_Money | "The product is worth the money" | Pricing Value |
| Q13_Cheap_Maintenance | "Maintenance is cheap" | Pricing Value |
| Q14_Good_Promotions | "Promotions are attractive" | Pricing Value |
| Q15_Competitive_Price | "Price is competitive" | Pricing Value |
