-- Total customers
SELECT COUNT(*) AS total_customers
FROM customer;

--Customer by Nationality
SELECT Nationality, COUNT(*) AS total_customers
FROM customer
GROUP BY Nationality;

-- Average Income of Customer
SELECT Nationality, COUNT(*) AS total_customers
FROM customer
GROUP BY Nationality;

-- Total Bank Deposits
SELECT AVG(`Estimated Income`) AS avg_income
FROM customer;

--Loan Distribution
SELECT AVG(`Bank Loans`) AS avg_loans,
       MAX(`Bank Loans`) AS max_loans,
       MIN(`Bank Loans`) AS min_loans
FROM customer;

-- Customer Segmentation(Based on Income)
SELECT 
  CASE 
    WHEN `Estimated Income` < 50000 THEN 'Low Income'
    WHEN `Estimated Income` BETWEEN 50000 AND 100000 THEN 'Medium Income'
    ELSE 'High Income'
  END AS income_group,
  COUNT(*) AS customers
FROM customer
GROUP BY income_group;

-- Gender-Wise Analysis
SELECT GenderId, COUNT(*) AS total_customers
FROM customer
GROUP BY GenderId;

-- Total Credit Card Balance
SELECT SUM(`Credit Card Balance`) AS total_cc_balance
FROM customer;

-- Properties Owned Analysis
SELECT AVG(`Properties Owned`) AS avg_properties
FROM customer;

-- Risk Analysis
SELECT `Risk Weighting`, COUNT(*) AS customers
FROM customer
GROUP BY `Risk Weighting`
ORDER BY customers DESC;