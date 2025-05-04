# PySpark Mini Project (Medium Difficulty): Employee Performance (Window Functions)

This project uses 2 datasets: `employees.csv`, `performance_reviews.csv`. Load them using PySpark DataFrames.

## 🧰 Setup
- Load the CSVs into PySpark DataFrames: `employees_df`, `reviews_df`.
- Register them as SQL Views: `employees`, `performance_reviews`.

## 🔍 Data Exploration
1. **Show the schema and 5 sample records from each DataFrame.**
   - **Expected Output:** Table previews.

2. **How many performance reviews does each employee have?**
   - **Expected Output:** employee_id | review_count

## 🪟 Window Functions Practice

3. **Assign a rank to each review based on the review_date within each employee.**
   - **Expected Output:** employee_id | review_date | score | rank

4. **Assign a row number to each review ordered by review_date per employee.**
   - **Expected Output:** employee_id | review_date | score | row_number

5. **Use a window function to calculate the average score for each employee across all reviews.**
   - **Expected Output:** employee_id | review_date | score | avg_score

6. **Find the difference between each review's score and the employee’s average score using window functions.**
   - **Expected Output:** employee_id | review_date | score | avg_score | score_diff

7. **Use LAG to get the previous review's score per employee and calculate the change in score.**
   - **Expected Output:** employee_id | review_date | score | previous_score | score_change

8. **Use LEAD to compare each review's score to the next one per employee.**
   - **Expected Output:** employee_id | review_date | score | next_score

9. **Get the most recent review per employee using ROW_NUMBER.**
   - **Expected Output:** employee_id | employee_name | latest_review_date | latest_score

10. **Calculate a rolling average score over the last 3 reviews per employee.**
    - **Expected Output:** employee_id | review_date | score | rolling_avg_3

11. **For each department, rank employees based on their latest review score (highest to lowest).**
    - **Expected Output:** department | employee_id | score | rank

12. **Use a window function to get cumulative review score per employee.**
    - **Expected Output:** employee_id | review_date | score | cumulative_score

13. **For each employee, calculate the number of days between each review and the previous one.**
    - **Expected Output:** employee_id | review_date | previous_date | days_between

---

💡 Tip: Solve every question using both the DataFrame API and SQL Window Functions.