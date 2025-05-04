# PySpark Mini Project (Medium Difficulty): E-Commerce Joins Challenge

This project uses 3 datasets: `customers.csv`, `products.csv`, `orders.csv`. Load them using PySpark DataFrames.

## 🧰 Setup
- Load the CSVs into PySpark DataFrames: `customers_df`, `products_df`, `orders_df`.
- Register them as SQL Views: `customers`, `products`, `orders`.

## 🔍 Data Exploration
1. **Print the schemas and show the first 5 records from each DataFrame.**
   - **Expected Output:** Basic structure of each dataset.

2. **How many unique customers have placed at least one order?**
   - **Expected Output:** Single number like 28.

3. **Find how many orders each customer has placed.**
   - **Expected Output:** customer_id | customer_name | order_count

4. **List all customers who haven't placed any orders.**
   - **Expected Output:** customer_id | customer_name

## 🔗 Joins Focus
5. **Perform an inner join between orders and customers. Show order_id, customer_name, and order_date.**
   - **Expected Output:** Merged table.

6. **Perform a left join between customers and orders to find customers without orders.**
   - **Expected Output:** customer_id | customer_name | order_id (NULL for those with no orders).

7. **Join orders, customers, and products to create a full order summary showing:**
   - customer_name, product_name, quantity, order_date, price
   - **Expected Output:** Full flattened table.

8. **Find the total amount spent per order (quantity * price).**
   - **Expected Output:** order_id | total_amount

9. **Find the top 5 customers who spent the most money overall.**
   - **Expected Output:** customer_name | total_spent

10. **List all orders for products costing more than $1000.**
    - **Expected Output:** order_id | product_name | price | customer_name

11. **Perform a full outer join between customers and orders. What are the results?**
    - **Expected Output:** All customers and orders even if not matching (NULLs in some columns).

12. **Find the number of different products each customer has ordered.**
    - **Expected Output:** customer_name | product_count

13. **Using SQL, calculate the total revenue generated for each product.**
    - **Expected Output:** product_name | total_revenue

14. **Which country has the highest number of customers who made orders?**
    - **Expected Output:** country | customer_count

15. **Create a ranking of customers based on total amount spent using ROW_NUMBER() window function.**
    - **Expected Output:** rank | customer_name | total_spent

---

💡 Tip: Try to solve each problem using both DataFrame API and SQL API.