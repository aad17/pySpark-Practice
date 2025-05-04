# PySpark Mini Project: Retail Sales Analysis (Easy)

This project uses the dataset `retail_sales_data_easy.csv`. Load it using PySpark and perform the following tasks using **DataFrame API** and **SQL API** where appropriate.

## 🧰 Setup
- Load the CSV file into a PySpark DataFrame.
- Register the DataFrame as a temporary SQL view named `sales`.

## 🔍 Data Exploration & Cleaning
1. Print the schema and show the first 5 rows of the DataFrame.
2. Count the number of distinct customers.
3. Find the number of nulls (if any) in each column.
4. Get the count of transactions per product category.
5. What is the range of purchase dates?

## 📊 Aggregations & Grouping
6. What is the total revenue generated from all transactions?
7. Show the total quantity of products sold per category.
8. Which payment method was used most frequently?
9. What is the average purchase amount for each product category?
10. List the top 5 highest value transactions.

## 🧠 Insights
11. Which customer made the highest total purchase amount?
12. What is the average purchase amount by payment method?
13. For each year, how many transactions took place?
14. Add a new column called `total_amount` = `purchase_amount * quantity`. Show the updated DataFrame.
15. What is the average `total_amount` per product category?

## ✅ Bonus
16. Which day of the week has the highest number of purchases?
17. Create a temporary view and write a SQL query to find the most popular product category for each payment method.
18. Filter and display all purchases made using PayPal over $200.

---

💡 Tip: Practice both DataFrame and SQL approaches side by side for better understanding!