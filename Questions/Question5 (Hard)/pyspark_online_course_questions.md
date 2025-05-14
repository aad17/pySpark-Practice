# PySpark Mini Project (Hard Difficulty): Online Course Platform Analytics

This project involves five datasets: `students.csv`, `courses.csv`, `instructors.csv`, `enrollments.csv`, `reviews.csv`.

## 📦 Data Setup
- Load the CSVs into PySpark DataFrames.
- Register them as SQL Views.

## 🧠 Questions

1. **Which students have enrolled in more than 3 courses?**
   - Expected Output: student_id | student_name | num_courses

2. **Which instructor has the highest average rating across all their courses?**
   - Expected Output: instructor_id | instructor_name | avg_rating

3. **What is the average rating for each course category? (Tech, Business, Design)**
   - Expected Output: category | avg_rating

4. **Find the top 5 most popular courses (by number of enrollments).**
   - Expected Output: course_id | course_title | enrollments

5. **Which students have completed more than 80% in all the courses they enrolled in?**
   - Expected Output: student_id | student_name

6. **List all instructors and the number of unique students they’ve taught.**
   - Expected Output: instructor_id | instructor_name | student_count

7. **For each country, find the average student progress across all courses.**
   - Expected Output: country | avg_progress

8. **Rank courses within each category by average rating using window functions.**
   - Expected Output: course_id | course_title | category | avg_rating | rank

9. **Get the latest review per student per course using ROW_NUMBER.**
   - Expected Output: student_id | course_id | rating | review_date

10. **Find students who have given a 5-star rating to more than one course.**
    - Expected Output: student_id | student_name | five_star_count

11. **Calculate the rolling average rating over the last 3 reviews for each course.**
    - Expected Output: course_id | review_date | rating | rolling_avg

12. **Find the most reviewed course and list all students who reviewed it.**
    - Expected Output: course_id | course_title | student_id | student_name

13. **For each instructor, calculate the average progress of students across all their courses.**
    - Expected Output: instructor_id | instructor_name | avg_student_progress

14. **For each course, compare the number of enrolled students vs number of reviewers.**
    - Expected Output: course_id | enrollments | reviewers | difference

15. **List all students who enrolled but never left a review for any course.**
    - Expected Output: student_id | student_name

---

💡 Tip: You are expected to use both DataFrame and SQL APIs. Many questions will require multiple joins and window functions.