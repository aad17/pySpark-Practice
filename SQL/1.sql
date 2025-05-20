"""
transactions
------------
transaction_id: INT
customer_id: INT
transaction_date: DATE
amount: FLOAT

Write a SQL query to identify the first transaction date for each customer and their total 
transaction amount within 30 days of their first purchase.
"""

WITH transaction_cte AS (
    SELECT
        customer_id,
        transaction_date,
        amount,
        ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY transaction_date DESC) AS rank_transaction
    FROM transactions
),

first_transactions_cte AS (
    SELECT 
        customer_id,
        transaction_date,
        amount
    FROM transaction_cte
    WHERE rank_transaction = 1
)

SELECT 
    ftc.customer_id,
    SUM(tc.amount) AS total_amount
FROM transaction_cte tc
JOIN first_transactions_cte ftc
WHERE transaction_date BETWEEN transaction_date AND DATE_ADD(transaction_date, INTERVAL 30 DAY)
GROUP BY customer_id