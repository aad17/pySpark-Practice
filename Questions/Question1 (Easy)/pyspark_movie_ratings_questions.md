# PySpark Mini Project: Movie Ratings Analysis

This project uses the dataset `movie_ratings_project.csv`. Load it using PySpark and perform the following tasks using **DataFrame API** and **SQL API**.

## 🧰 Setup
- Load the CSV file into a PySpark DataFrame.
- Register the DataFrame as a temporary SQL view named `ratings`.

## 🔍 Data Exploration & Cleaning
1. **Print the schema and display the first 5 records.**
   - **Expected Output:** Schema with 5 columns; 5 rows showing user_id, movie_title, genre, rating, review_date.

2. **Find the number of unique users.**
   - **Expected Output:** A single number like 65.

3. **List all distinct genres available.**
   - **Expected Output:** List of genres like ['Action', 'Comedy', 'Drama', ...].

4. **Count how many reviews exist for each genre.**
   - **Expected Output:** Table with genres and their review counts.

5. **Find if there are any null values in the dataset.**
   - **Expected Output:** 0/null counts per column.

## 📊 Aggregations & Grouping
6. **Calculate the average rating for each genre.**
   - **Expected Output:** Genre | Average Rating (e.g., Comedy | 3.8).

7. **Identify the top 5 highest-rated movies (average rating).**
   - **Expected Output:** Movie Title | Average Rating, sorted descending.

8. **Find the total number of reviews each year.**
   - **Expected Output:** Year | Review Count.

9. **Which movie received the most reviews?**
   - **Expected Output:** Movie title and review count.

10. **Show the distribution (count) of ratings (1-5 stars).**
    - **Expected Output:** Rating | Count (bar-chart-like table).

## 🧠 Insights
11. **Find the average rating given by each user.**
    - **Expected Output:** User ID | Average Rating.

12. **Which genre has the highest average rating?**
    - **Expected Output:** Genre | Average Rating (single highest).

13. **Add a new column called `rating_category` where:**
    - Rating 4 or 5 = 'Positive'
    - Rating 3 = 'Neutral'
    - Rating 1 or 2 = 'Negative'
    - **Expected Output:** Updated DataFrame with new column.

14. **Display the number of Positive, Neutral, and Negative reviews.**
    - **Expected Output:** Rating Category | Count.

15. **Find the month with the highest number of reviews.**
    - **Expected Output:** Month (e.g., July) | Number of Reviews.

## ✅ Bonus
16. **Using SQL, find the top 3 genres with the most Positive reviews.**
    - **Expected Output:** Genre | Positive Review Count.

17. **Using SQL, show the number of reviews per year for each genre.**
    - **Expected Output:** Year | Genre | Count.

18. **Filter and show all Sci-Fi movies that received a 5-star rating.**
    - **Expected Output:** Movie titles, genre, and rating = 5.

---

💡 Tip: Try solving each using both DataFrame and SQL API to strengthen your skills!